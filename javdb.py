import time
import sys
import pandas as pd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enable UTF-8 for safe console output (Python 3.7+)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except:
    pass

def safe_print(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode('ascii', 'ignore').decode('ascii'))

def setup_driver(locale="en", headless=False):
    options = uc.ChromeOptions()
    if headless:
        options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = uc.Chrome(options=options)

    # Load site to set cookies
    driver.get("https://javdb.com")
    time.sleep(2)

    # Inject cookies
    driver.add_cookie({'name': 'over18', 'value': '1', 'domain': 'javdb.com', 'path': '/'})
    driver.add_cookie({'name': 'locale', 'value': locale, 'domain': 'javdb.com', 'path': '/'})

    return driver

def scrape_actress_list(driver, pages=2):
    base_url = "https://javdb.com/actors?page="
    actress_list = []

    for page in range(1, pages + 1):
        url = f"{base_url}{page}"
        safe_print(f"\n[INFO] Scraping page {page} -> {url}")
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.grid a.box"))
            )
        except Exception as e:
            safe_print(f"[WARNING] Actress cards not found: {e}")
            driver.save_screenshot(f"page{page}_error.png")

        # Save page for debugging
        with open(f"debug_page{page}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.select("div.grid a.box")

        found = 0
        for card in cards:
            href = card.get("href")
            name = card.get("title")
            if href and name and href.startswith("/actors/"):
                full_url = "https://javdb.com" + href
                actress_list.append({"Name": name, "Profile URL": full_url})
                safe_print(f"    - {name} -> {full_url}")
                found += 1
            if len(actress_list) >= 50:
                safe_print("[INFO] Reached 50 actresses. Stopping.")
                return actress_list

        safe_print(f"[INFO] Found {found} actress links on page {page}")
        time.sleep(1)

    return actress_list

def scrape_actress_details(driver, actress):
    safe_print(f"[INFO] Scraping profile: {actress['Name']}")
    try:
        driver.get(actress["Profile URL"])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.panel-block"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")
        tags = [tag.text.strip() for tag in soup.select("a.tag")]

        debut = ""
        movie_count = ""
        info_table = soup.find("div", class_="panel-block")
        if info_table:
            for row in info_table.select("div.columns"):
                label = row.select_one("div.column.is-one-quarter")
                value = row.select_one("div.column:not(.is-one-quarter)")
                if label and value:
                    label_text = label.text.strip().lower()
                    if "debut" in label_text or "出道" in label_text:
                        debut = value.text.strip()
                    elif "作品" in label_text or "movie" in label_text:
                        movie_count = value.text.strip()

        actress["Debut Year"] = debut
        actress["Number of Movies"] = movie_count
        actress["Tags/Genres"] = ", ".join(tags)

    except Exception as e:
        safe_print(f"[WARNING] Failed to scrape profile for {actress['Name']}: {e}")
        actress["Debut Year"] = ""
        actress["Number of Movies"] = ""
        actress["Tags/Genres"] = ""

    time.sleep(0.5)

def main():
    driver = setup_driver(locale="en", headless=False)  # Set to True for silent mode
    actresses = scrape_actress_list(driver, pages=3)

    for actress in actresses:
        scrape_actress_details(driver, actress)

    driver.quit()

    df = pd.DataFrame(actresses)
    output_file = "JAV_Actresses_English_Stealth.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")
    safe_print(f"\n[INFO] Done! Data saved to: {output_file}")

if __name__ == "__main__":
    main()
