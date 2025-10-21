import os
import re
import time
import sys
import random
import pandas as pd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse

# ========== Console-safe printing ==========
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def safe_print(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode('ascii', 'ignore').decode('ascii'))

# ========== Navigation helpers ==========
def safe_get(driver, url, timeout=25):
    try:
        driver.set_page_load_timeout(timeout)
        driver.get(url)
    except TimeoutException:
        try:
            driver.execute_script("window.stop();")
            safe_print(f"[WARN] Timed out loading {url}, stopped page load.")
        except Exception:
            pass

def lazy_scroll(driver, max_rounds=8, pause=0.6):
    last_h = -1
    same = 0
    for _ in range(max_rounds):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        h = driver.execute_script("return document.body.scrollHeight || 0")
        if h == last_h:
            same += 1
            if same >= 2:
                break
        else:
            same = 0
        last_h = h

def handle_popups(driver):
    try:
        for xp in [
            "//button[contains(text(),'I am 18')]",
            "//button[contains(text(),'Enter')]",
            "//button[contains(text(),'Accept')]",
            "//button[contains(text(),'Agree')]",
        ]:
            btns = driver.find_elements(By.XPATH, xp)
            for b in btns:
                if b.is_displayed() and b.is_enabled():
                    b.click()
                    time.sleep(0.8)
    except Exception as e:
        safe_print(f"[DEBUG] No popup or failed to close: {e}")

# ========== Driver setup ==========
def setup_driver(locale="en", headless=False, chrome_major=None):
    options = uc.ChromeOptions()
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    ]
    options.add_argument(f"user-agent={random.choice(ua_list)}")
    if headless:
        options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--lang=en-US,en;q=0.9")
    options.add_argument("--disable-extensions")

    driver = uc.Chrome(options=options, version_main=chrome_major) if chrome_major else uc.Chrome(options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
            Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3]});
        """
    })

    safe_get(driver, "https://javdb.com", timeout=20)
    time.sleep(random.uniform(1.5, 3.0))
    driver.add_cookie({'name': 'over18', 'value': '1', 'domain': 'javdb.com', 'path': '/'})
    driver.add_cookie({'name': 'locale', 'value': locale, 'domain': 'javdb.com', 'path': '/'})
    return driver

# ========== List scraper (with category skip) ==========
def scrape_actress_list(driver, pages=2):
    base_url = "https://javdb.com/actors?page="
    actress_list = []
    skip_slugs = {"censored", "uncensored", "western"}

    for page in range(1, pages + 1):
        url = f"{base_url}{page}"
        safe_print(f"\n[INFO] Scraping page {page} -> {url}")
        page_start = time.monotonic()
        PAGE_BUDGET = 45

        safe_get(driver, url, timeout=20)
        handle_popups(driver)
        time.sleep(random.uniform(1.0, 2.0))
        lazy_scroll(driver, max_rounds=8, pause=0.6)

        selectors = [
            'a.box[href*="/actors/"]',
            'div.grid a[href*="/actors/"]',
            'a[href*="/actors/"]',
        ]

        found_cards = []
        deadline = time.monotonic() + 12
        while time.monotonic() < deadline and not found_cards:
            for sel in selectors:
                found_cards = driver.find_elements(By.CSS_SELECTOR, sel)
                if found_cards:
                    safe_print(f"[INFO] Using selector: {sel}")
                    break
            if not found_cards:
                time.sleep(0.4)

        safe_print(f"[DEBUG] {len(found_cards)} anchors matched on page {page}")

        if not found_cards:
            safe_print(f"[WARNING] Actress cards not found on page {page}, saving debug.")
            with open(f"debug_page{page}.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            driver.save_screenshot(f"debug_page{page}.png")
            continue

        found = 0
        for el in found_cards:
            if time.monotonic() - page_start > PAGE_BUDGET:
                safe_print("[WARN] Page budget exceeded mid-loop; moving on.")
                break

            try:
                href = (el.get_attribute("href") or "").strip()
                if "/actors/" not in href:
                    continue
                slug = href.rstrip("/").split("/")[-1]
                if slug in skip_slugs:
                    continue

                name = (
                    el.get_attribute("title")
                    or el.get_attribute("aria-label")
                    or el.get_attribute("data-original-title")
                    or el.text.strip()
                )
                if not name:
                    try:
                        img = el.find_element(By.CSS_SELECTOR, "img[alt]")
                        name = (img.get_attribute("alt") or "").strip()
                    except Exception:
                        name = ""
                if not name:
                    name = slug

                full_url = href if href.startswith("http") else "https://javdb.com" + href
                actress_list.append({"Name": name, "Profile URL": full_url})
                safe_print(f"    - {name} -> {full_url}")
                found += 1

                if len(actress_list) >= 50:
                    safe_print("[INFO] Reached 50 actresses. Stopping.")
                    return actress_list
            except Exception:
                continue

        safe_print(f"[INFO] Found {found} actress links on page {page}")
        time.sleep(0.6)

    return actress_list

# ========== Detail scraper (improved matching + retry + extra fields) ==========
LABEL_KEYS_DEBUT = [
    "debut", "debut date", "start", "first", "first appearance",
    "出道", "デビュー", "首发", "初登場", "初登场"
]
LABEL_KEYS_MOVIES = [
    "movie", "movies", "works", "titles", "number of works", "appearances",
    "作品", "影片数", "出演本数", "本数"
]
LABEL_KEYS_BIRTHDAY = [
    "birthday", "birth date", "date of birth", "dob", "生年月日", "誕生日", "生日", "出生日期"
]
LABEL_KEYS_HEIGHT = [
    "height", "身長", "身高", "身高", "身長(cm)", "身長（cm）"
]
LABEL_KEYS_CUP = [
    "cup", "bra", "bust size", "罩杯", "カップ"
]

YEAR_RE = re.compile(r"(19|20)\d{2}")
HEIGHT_RE = re.compile(r"(\d{2,3})\s*cm", re.I)
CUP_RE = re.compile(r"\b([A-H])\s*cup\b", re.I)  # simple A–H cup letter

def _match_label(label_text: str, keys) -> bool:
    lt = (label_text or "").strip().lower()
    return any(k in lt for k in keys)

def parse_profile_html(html):
    soup = BeautifulSoup(html, "html.parser")
    tags = [t.text.strip() for t in soup.select("a.tag")]

    debut = movie_count = birthday = height = cup = ""

    # search all label/value rows
    for row in soup.select("div.columns"):
        label = row.select_one("div.column.is-one-quarter")
        value = row.select_one("div.column:not(.is-one-quarter)")
        if not label or not value:
            continue
        lt = label.text.strip()
        vt = value.text.strip()

        if _match_label(lt, LABEL_KEYS_DEBUT):
            debut = vt
        elif _match_label(lt, LABEL_KEYS_MOVIES):
            movie_count = vt
        elif _match_label(lt, LABEL_KEYS_BIRTHDAY):
            birthday = vt
        elif _match_label(lt, LABEL_KEYS_HEIGHT):
            height = vt
        elif _match_label(lt, LABEL_KEYS_CUP):
            cup = vt

    # Fallbacks / normalization
    if not debut:
        text = soup.get_text(" ", strip=True).lower()
        if any(k in text for k in ["debut", "デビュー", "出道", "首发", "初登場", "初登场"]):
            m = YEAR_RE.search(text)
            if m:
                debut = m.group(0)

    if height and "cm" not in height.lower():
        m = HEIGHT_RE.search(height)
        if m:
            height = f"{m.group(1)} cm"
    elif not height:
        # try scanning full text for height
        m = HEIGHT_RE.search(soup.get_text(" ", strip=True))
        if m:
            height = f"{m.group(1)} cm"

    if cup:
        m = CUP_RE.search(cup)
        if m:
            cup = f"{m.group(1).upper()} cup"
    else:
        m = CUP_RE.search(soup.get_text(" ", strip=True))
        if m:
            cup = f"{m.group(1).upper()} cup"

    return debut, movie_count, ", ".join(tags), birthday, height, cup

def scrape_actress_details(driver, actress, retries=2):
    safe_print(f"[INFO] Scraping profile: {actress['Name']}")
    attempt = 0
    while attempt <= retries:
        try:
            safe_get(driver, actress["Profile URL"], timeout=12)
            if "actors/" not in driver.current_url:
                safe_print(f"[SKIP] {actress['Name']} -> Not a profile page")
                for k in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
                    actress[k] = ""
                return

            WebDriverWait(driver, 6).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.tag, div.columns, div.panel-block"))
            )

            debut, movie_count, tags, birthday, height, cup = parse_profile_html(driver.page_source)

            actress["Debut Year"] = debut
            actress["Number of Movies"] = movie_count
            actress["Tags/Genres"] = tags
            actress["Birthday"] = birthday
            actress["Height"] = height
            actress["Cup Size"] = cup
            return
        except Exception as e:
            attempt += 1
            safe_print(f"[WARN] Detail scrape failed ({attempt}/{retries}) for {actress['Name']}: {e}")
            time.sleep(random.uniform(0.6, 1.2))

    # Final default if all retries failed
    for k in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
        actress[k] = actress.get(k, "") or ""

# ========== Orchestrators ==========
CSV_NAME = "JAV_Actresses_English_Stealth.csv"
CSV_OUT  = "JAV_Actresses_English_Stealth_enriched.csv"

def enrich_existing_csv(driver, csv_path=CSV_NAME):
    df = pd.read_csv(csv_path)
    # Ensure all columns exist
    for col in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
        if col not in df.columns:
            df[col] = ""

    records = df.to_dict(orient="records")
    total = len(records)
    safe_print(f"[INFO] Enriching {total} existing records from {csv_path}")

    for i, rec in enumerate(records, 1):
        # Re-scrape if any of the new/old fields are missing
        needs = any(not str(rec.get(c,"")).strip() for c in
                    ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"])
        if not needs:
            continue
        scrape_actress_details(driver, rec, retries=2)
        if i % 10 == 0:
            safe_print(f"[INFO] Progress: {i}/{total}")

    pd.DataFrame(records).to_csv(CSV_OUT, index=False, encoding="utf-8")
    safe_print(f"[INFO] Enriched CSV saved to: {CSV_OUT}")

def scrape_fresh_and_save(driver, pages=3):
    actresses = scrape_actress_list(driver, pages=pages)
    for a in actresses:
        # init new fields so CSV has consistent columns
        for col in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
            a.setdefault(col, "")
        scrape_actress_details(driver, a, retries=2)
    pd.DataFrame(actresses).to_csv(CSV_NAME, index=False, encoding="utf-8")
    safe_print(f"[INFO] Fresh CSV saved to: {CSV_NAME}")

# ========== Main ==========
def main():
    driver = setup_driver(locale="en", headless=False, chrome_major=138)
    try:
        if os.path.exists(CSV_NAME):
            enrich_existing_csv(driver, CSV_NAME)
        else:
            scrape_fresh_and_save(driver, pages=3)
    finally:
        # Silence uc's destructor noise on Windows
        import contextlib
        try:
            uc.Chrome.__del__ = lambda self: None
        except Exception:
            pass
        with contextlib.suppress(Exception, OSError):
            driver.quit()

if __name__ == "__main__":
    main()
