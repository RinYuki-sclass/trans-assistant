import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = uc.ChromeOptions()
driver = uc.Chrome(options=options, version_main=153)

try:
    driver.get('https://www.novelupdates.com/viewlist/149939/')
    
    # Wait up to 30 seconds for Cloudflare to clear
    for i in range(30):
        time.sleep(1)
        title = driver.title
        print(f"[{i}s] Title: {title}")
        if "Just a moment..." not in title and "Checking" not in title and title != "":
            print("Passed Cloudflare!")
            break
        
        # Try to locate Turnstile iframe
        try:
            frames = driver.find_elements(By.CSS_SELECTOR, "iframe[src*='cloudflare'], iframe[src*='turnstile']")
            for f in frames:
                try:
                    driver.switch_to.frame(f)
                    checkbox = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox'], .ctp-checkbox-label, #cf-stage label, span.mark")
                    if checkbox:
                        print("Found checkbox in iframe, clicking...")
                        checkbox[0].click()
                    driver.switch_to.default_content()
                except Exception as fe:
                    driver.switch_to.default_content()
        except Exception:
            pass

    print("Final Title:", driver.title)
    html = driver.page_source
    with open('scratch/nu_list.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Page length:", len(html))
finally:
    driver.quit()
