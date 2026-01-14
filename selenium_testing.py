from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd
from datetime import date

# ===============================
# SETUP
# ===============================
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# ===============================
# PRODUCT LIST
# ===============================
crm_products = [
    {"name": "Salesforce Sales Cloud", "url": "https://www.capterra.com/p/61368/Salesforce/#reviews"},
    {"name": "HubSpot CRM", "url": "https://www.capterra.com/p/152373/HubSpot-CRM/"},
    {"name": "Zoho CRM", "url": "https://www.capterra.com/p/155928/Zoho-CRM/"},
    {"name": "Pipedrive", "url": "https://www.capterra.com/p/132666/Pipedrive/"},
    {"name": "Monday CRM", "url": "https://www.capterra.com/p/245800/Monday-CRM/"},
    {"name": "Microsoft Dynamics 365 Sales", "url": "https://www.capterra.com/p/157279/Dynamics-365/"},
{"name": "Kylas Sales CRM", "url": "https://www.capterra.com/p/210630/Kylas/"},

]

rows = []

# ===============================
# SCRAPING LOOP
# ===============================
for product in crm_products:
    print(f"Scraping: {product['name']}")

    try:
        driver.get(product["url"])
        time.sleep(5)

        # PRODUCT NAME
        product_name = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//main//*[normalize-space(text())='CRM Software']/following::*[normalize-space(text())][1]"
            ))
        ).text

        # RATING
        rating = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//main//*[normalize-space(text())='Overall rating']/following::*[contains(text(), '.')][1]"
            ))
        ).text

        # MAIN TEXT
        main_text = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        ).text

        # REVIEW COUNT (largest number = total reviews)
        numbers = re.findall(r"\b\d{1,3}(?:,\d{3})+\b", main_text)
        review_count = max(int(n.replace(",", "")) for n in numbers)

        # PRICING TEXT
        pricing_lines = [
            line for line in main_text.split("\n")
            if "$" in line and ("month" in line.lower() or "user" in line.lower())
        ]
        pricing_text = pricing_lines[0] if pricing_lines else "Pricing not found"

        rows.append({
            "product_name": product_name,
            "category": "CRM",
            "rating": float(rating),
            "review_count": review_count,
            "pricing_text": pricing_text,
            "source": "Capterra",
            "scrape_date": date.today().isoformat()
        })

        print(f"✔ Success: {product_name}")

    except Exception as e:
        print(f"✖ Failed on {product['name']} — skipped")
        continue

# ===============================
# SAVE OUTPUT
# ===============================
df = pd.DataFrame(rows)
df.to_csv("crm_products_raw.csv", index=False)
print("\nFINAL DATASET:")
print(df)

driver.quit()








