from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()
driver.get("http://ptc.cointiply.com/games")
driver.implicitly_wait(50)
driver.find_element(By.XPATH, '//button[text()="Start Playing & Earning Coins"]').click()
time.sleep(16)
WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")))
driver.find_element_by_xpath("//a[@title='Wander Words']").click()
time.sleep(8)
driver.switch_to.default_content()
target=driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")
target.location_once_scrolled_into_view
WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")))
driver.find_element(By.XPATH, '//ark-ad-div[@data-type="play-button"]').click()
time.sleep(17)
driver.execute_script("window.history.go(-1)")
time.sleep(4)

for i in range(100):
    print(i)
    try:
        print("Running inside loop")
        driver.find_element_by_xpath("//a[@title='Jewel Shuffle']").click()
        time.sleep(6)
        driver.switch_to.default_content()
        target=driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")
        target.location_once_scrolled_into_view
        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")))
        driver.find_element(By.XPATH, '//ark-ad-div[@data-type="play-button"]').click()
        time.sleep(17)
        driver.switch_to.default_content()
        driver.execute_script("window.history.go(-1)")

    except NoSuchElementException:
        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")))
        driver.find_element_by_xpath("//a[@title='Wander Words']").click()
        time.sleep(6)
        driver.switch_to.default_content()
        target=driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")
        target.location_once_scrolled_into_view
        WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")))
        driver.find_element(By.XPATH, '//ark-ad-div[@data-type="play-button"]').click()
        time.sleep(17)
        driver.switch_to.default_content()
        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        WebDriverWait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@class='responsive-game-frame']")))
 




 


 


 