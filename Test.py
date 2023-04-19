from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import webdriver
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    search_x = browser.find_element(By.ID, "input_value")
    x = search_x.text
    x_value = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(x_value)

    button1 = browser.find_element(By.ID, "solve")
    button1.click()
    
finally:
    print(browser.switch_to.alert.text)
    browser.quit()

            

