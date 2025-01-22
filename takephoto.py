from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"

# Chrome driver setup
browser_driver = Service('/usr/bin/chromedriver')

# Start the browser
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Step 1: Navigate to the page
    page_to_scrape.get("https://www.sakamotodayschapters.com/")

    responseT = page_to_scrape.find_element(By.XPATH, '//*[@id="ceo_latest_comics_widget-3"]/ul')

    height = responseT.size['height']
    width = responseT.size['width']

    
    desired_width = max(width, 600)  

    desired_height = min(height, 500)

    page_to_scrape.set_window_size(desired_width, desired_height)  

   
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseT)

    responseT.screenshot('kaiju.png')

finally:
    # Close the browser
    page_to_scrape.quit()
