from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = input("Enter url of youtube playlist: ")
range_start = int(input("rangestart (enter if from first): ") or 1)-1
# Initialize the driver
driver = webdriver.Chrome()

# Open the YouTube playlist
driver.get(url)

try:
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    for i in range(driver.execute_script("return document.documentElement.scrollHeight")//100+1):
        driver.execute_script("window.scrollBy(0, 100);")

    # Collect all elements after scrolling
    times = driver.find_elements(By.CLASS_NAME, 'badge-shape-wiz__text')

    total = 0

    for i in times[range_start:]:
        if i.text.count(":")==2:
            hours,mins,secs = i.text.split(":")
            total += int(hours)*60*60
        else:mins,secs = i.text.split(":")
        total += int(secs)
        total +=int(mins)*60

    print(f"playlist length is {total//60//60}:{total//60%60}:{total%60}")

except Exception as e:
    print("Error:", e)
finally:
    input("Press Enter to close the browser...")
    driver.quit()
