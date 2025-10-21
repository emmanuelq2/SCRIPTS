# -*- coding: utf-8 -*-
import os
import re
import sys
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# -------- Console-safe print --------
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def safe_print(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode('ascii', 'ignore').decode('ascii'))

# -------- Config --------
CHROME_MAJOR = 141  # <-- change to your installed Chrome major version
CSV_NAME    = "JAV_Actresses_English_Stealth.csv"
CSV_OUT     = "JAV_Actresses_English_Stealth_enriched.csv"

# -------- UC-only driver (auto-download) --------
def setup_driver(locale="en", headless=False):
    """
    UC only. No Selenium Manager. Auto-downloads driver for CHROME_MAJOR.
    """
    opts = uc.ChromeOptions()
    if headless:
        opts.headless = True
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--lang=en-US,en;q=0.9")
    opts.add_argument("--disable-extensions")

    # Optional: pageLoadStrategy=none helps avoid long waits
    caps = DesiredCapabilities.CHROME.copy()
    caps["pageLoadStrategy"] = "none"

    driver = uc.Chrome(options=opts, version_main=CHROME_MAJOR, desired_capabilities=caps)
    driver.set_page_load_timeout(12)

    # Mild stealth
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator,'webdriver',{get:()=>undefined});
            Object.defineProperty(navigator,'languages',{get:()=>['en-US','en']});
            Object.defineProperty(navigator,'plugins',{get:()=>[1,2,3]});
        """
    })

    # Warm-up & cookies
    safe_get(driver, "https://javdb.com", hard_cap_seconds=8)
    driver.add_cookie({'name': 'over18', 'value': '1', 'domain': 'javdb.com', 'path': '/'})
    driver.add_cookie({'name': 'locale', 'value': locale, 'domain': 'javdb.com', 'path': '/'})
    return driver

# -------- Non-blocking navigation --------
def safe_get(driver, url, hard_cap_seconds=8):
    """Navigate without hanging: hard-stops load after hard_cap_seconds."""
    try:
        driver.execute_script("window.stop();")
    except Exception:
        pass
    driver.get("about:blank")
    # Kill any previous timer
    try:
        driver.execute_script("window._kill && clearTimeout(window._kill);")
    except Exception:
        pass
    # Set a new kill timer and go
    try:
        driver.execute_script(f"window._kill = setTimeout(() => window.stop(), {int(hard_cap_seconds*1000)});")
    except Exception:
        pass
    driver.get(url)

def handle_popups(driver):
    """Click age-gate / cookie consent if visible."""
    xpaths = [
        "//button[contains(text(),'I am 18')]",
        "//button[contains(text(),'Enter')]",
        "//button[contains(text(),'Accept')]",
        "//button[contains(text(),'Agree')]",
    ]
    try:
        for xp in xpaths:
            for b in driver.find_elements(By.XPATH, xp):
                if b.is_displayed() and b.is_enabled():
                    b.click()
                    time.sleep(0.6)
    except Exception:
        pass

# -------- Actress list scraper --------
def scrape_actress_list(driver, pages=3):
    base_url = "https://javdb.com/actors?page="
    actress_list = []
    skip_slugs = {"censored", "uncensored", "western"}  # category pages

    for page in range(1, pages + 1):
        url = f"{base_url}{page}"
        safe_print(f"\n[INFO] Scraping page {page} -> {url}")
        safe_get(driver, url, hard_cap_seconds=10)
        handle_popups(driver)

        # Give the DOM a breath, but don't block forever
        try:
            WebDriverWait(driver, 6).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="/actors/"]'))
            )
        except Exception:
            pass

        soup = BeautifulSoup(driver.page_source, "html.parser")
        anchors = soup.select('a[href*="/actors/"]')
        safe_print(f"[DEBUG] {len(anchors)} anchors matched on page {page}")

        found = 0
        for a in anchors:
            href = a.get("href") or ""
            name = a.get("title") or a.text.strip()
            if not href.startswith("/actors/"):
                continue
            slug = href.rstrip("/").split("/")[-1]
            if slug in skip_slugs:
                continue

            full_url = "https://javdb.com" + href
            actress_list.append({"Name": name or slug, "Profile URL": full_url})
            safe_print(f"    - {name or slug} -> {full_url}")
            found += 1

            if len(actress_list) >= 50:
                safe_print("[INFO] Reached 50 actresses. Stopping.")
                return actress_list

        safe_print(f"[INFO] Found {found} actress links on page {page}")
        time.sleep(random.uniform(0.8, 1.4))

    return actress_list

# -------- Profile details (multilingual) --------
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
LABEL_KEYS_HEIGHT = ["height", "身長", "身高", "身長(cm)", "身長（cm）"]
LABEL_KEYS_CUP = ["cup", "bra", "bust size", "罩杯", "カップ"]

YEAR_RE   = re.compile(r"(19|20)\d{2}")
HEIGHT_RE = re.compile(r"(\d{2,3})\s*cm", re.I)
CUP_RE    = re.compile(r"\b([A-H])\s*cup\b", re.I)

def _label_is(label_text, keys):
    lt = (label_text or "").strip().lower()
    return any(k in lt for k in keys)

def parse_profile_html(html):
    soup = BeautifulSoup(html, "html.parser")
    tags = [t.text.strip() for t in soup.select("a.tag")]

    debut = movie_count = birthday = height = cup = ""

    for row in soup.select("div.columns"):
        label = row.select_one("div.column.is-one-quarter")
        value = row.select_one("div.column:not(.is-one-quarter)")
        if not label or not value:
            continue
        lt = label.text.strip()
        vt = value.text.strip()

        if _label_is(lt, LABEL_KEYS_DEBUT):
            debut = vt
        elif _label_is(lt, LABEL_KEYS_MOVIES):
            movie_count = vt
        elif _label_is(lt, LABEL_KEYS_BIRTHDAY):
            birthday = vt
        elif _label_is(lt, LABEL_KEYS_HEIGHT):
            height = vt
        elif _label_is(lt, LABEL_KEYS_CUP):
            cup = vt

    # Fallbacks
    full_text = soup.get_text(" ", strip=True)
    if not debut and any(k in full_text for k in ["Debut", "デビュー", "出道", "首发", "初登場", "初登场"]):
        m = YEAR_RE.search(full_text)
        if m:
            debut = m.group(0)

    if height and "cm" not in height.lower():
        m = HEIGHT_RE.search(height)
        if m:
            height = f"{m.group(1)} cm"
    elif not height:
        m = HEIGHT_RE.search(full_text)
        if m:
            height = f"{m.group(1)} cm"

    if cup:
        m = CUP_RE.search(cup)
        if m:
            cup = f"{m.group(1).upper()} cup"
    else:
        m = CUP_RE.search(full_text)
        if m:
            cup = f"{m.group(1).upper()} cup"

    return debut, movie_count, ", ".join(tags), birthday, height, cup

def scrape_actress_details(driver, actress, retries=2):
    safe_print(f"[INFO] Scraping profile: {actress['Name']}")
    attempt = 0
    while attempt <= retries:
        try:
            safe_get(driver, actress["Profile URL"], hard_cap_seconds=12)

            # quick guard
            if "actors/" not in driver.current_url:
                safe_print(f"[SKIP] {actress['Name']} -> Not a profile page")
                for k in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
                    actress[k] = ""
                return

            WebDriverWait(driver, 6).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.tag, div.columns, div.panel-block"))
            )

            debut, movie_count, tags, birthday, height, cup = parse_profile_html(driver.page_source)
            actress["Debut Year"]      = debut
            actress["Number of Movies"] = movie_count
            actress["Tags/Genres"]     = tags
            actress["Birthday"]        = birthday
            actress["Height"]          = height
            actress["Cup Size"]        = cup
            return
        except Exception as e:
            attempt += 1
            safe_print(f"[WARN] Detail scrape failed ({attempt}/{retries}) for {actress['Name']}: {e}")
            time.sleep(random.uniform(0.6, 1.2))

    # Final defaults if retries failed
    for k in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
        actress[k] = actress.get(k, "") or ""

# -------- Orchestrators --------
def enrich_existing_csv(driver, csv_path=CSV_NAME):
    df = pd.read_csv(csv_path)
    for col in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
        if col not in df.columns:
            df[col] = ""
    records = df.to_dict(orient="records")
    total = len(records)
    safe_print(f"[INFO] Enriching {total} existing records from {csv_path}")

    for i, rec in enumerate(records, 1):
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
    # initialize columns so CSV has consistent header even if fields are blank
    for a in actresses:
        for col in ["Debut Year","Number of Movies","Tags/Genres","Birthday","Height","Cup Size"]:
            a.setdefault(col, "")
        scrape_actress_details(driver, a, retries=2)
    pd.DataFrame(actresses).to_csv(CSV_NAME, index=False, encoding="utf-8")
    safe_print(f"[INFO] Fresh CSV saved to: {CSV_NAME}")

# -------- Main --------
def main():
    driver = setup_driver(locale="en", headless=False)
    try:
        if os.path.exists(CSV_NAME):
            enrich_existing_csv(driver, CSV_NAME)
        else:
            scrape_fresh_and_save(driver, pages=3)
    finally:
        # Silence uc's destructor noise on Windows
        try:
            uc.Chrome.__del__ = lambda self: None
        except Exception:
            pass
        try:
            driver.quit()
        except Exception:
            pass

if __name__ == "__main__":
    main()

 


