import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_prizepicks():
    # 1. Initialize Stealth Driver
    options = uc.ChromeOptions()
    # options.add_argument('--headless') # Uncomment to run in background
    driver = uc.Chrome(options=options)
    
    try:
        driver.get("https://app.prizepicks.com/")
        
        # 2. Close Initial Popups
        wait = WebDriverWait(driver, 15)
        close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close")))
        close_btn.click()
        
        # 3. Select NBA Category
        nba_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='name'][normalize-space()='NBA']")))
        nba_tab.click()
        time.sleep(2) # Give board time to load

        # 4. Target All Player Cards
        # This XPath finds every player tile on the board
        player_cards = driver.find_elements(By.XPATH, "//div[@id='projections']//div[contains(@class, 'projection-card')]")
        
        all_props = []
        for index, card in enumerate(player_cards):
            name = card.find_element(By.XPATH, ".//div[@class='name']").text
            line = card.find_element(By.XPATH, ".//div[@class='presale-score']").text
            stat = card.find_element(By.XPATH, ".//div[@class='text']").text
            
            # Hit Rate Formula Logic (Example: Over 54.25% required)
            # You would integrate your formula engine here
            
            all_props.append({"rank": index + 1, "name": name, "line": line, "stat": stat})

        # 🎯 SPECIFIC FOCUS: LINE 10
        line_10 = all_props[9] if len(all_props) >= 10 else None
        return all_props, line_10

    finally:
        driver.quit()

# Run the scrape
props, target = scrape_prizepicks()
print(f"Scanned {len(props)} props. Target Line 10: {target}")
