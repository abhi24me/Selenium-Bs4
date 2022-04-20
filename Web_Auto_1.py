import time
import emoji
import pyautogui as py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl as op
import psycopg2 as ps


# Connecting driver to the code
path = Service(r"S:\Web_Automation\chromedriver.exe")
driver = webdriver.Chrome(service=path)
try:
    # Connecting the url
    driver.get("https://www.phptravels.net/")

    # Maximizing the window for better performance
    driver.maximize_window()

    # Accepting the cookies
    cookie = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="cookie_stop"]'''))).click()
    # Getting the title of the page just to be informed about the website.
    print(driver.title)


    # Authenticating to the Website
    login = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/header/div[1]/div/div/div[2]/div/div/a[2]'''))).click()
    # time.sleep(3)
    email = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input''')))
    email.send_keys("user@phptravels.com")
    # time.sleep(3)
    pwd = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input''')))
    pwd.send_keys("demouser")
    py.typewrite(["Enter"])


    # Booking hotel
    hotels = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a'''))).click()
    time.sleep(3)

    # Entering desired city
    city_name = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="select2-hotels_city-container"]'''))).click()
    py.typewrite("Dubai")
    time.sleep(6)  # Must have sleep to load the search
    py.typewrite(["Enter"])
    time.sleep(2)
    search = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="submit"]/span[1]'''))).click()
    time.sleep(3)

    # Selecting the Hotel
    hotel = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="oasis beach tower"]/div/div[2]/div/div[2]/div/a/span[1]'''))).click()

    # Selecting the room
    xpath3 = '''//*[@id="availability"]/div[2]/div[1]/div[2]/div/div[2]/form/div/div[4]/div/div/button'''
    room = driver.find_element(by=By.XPATH, value=xpath3)
    driver.execute_script("arguments[0].click();", room)
    time.sleep(3)
#**********************************************************************************************************************#
    # Entering USER details

    # traveller1
    first_name = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/div[2]/form/section/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/input''')))
    first_name.send_keys("Salman")
    last_name = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/div[2]/form/section/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/input''')))
    last_name.send_keys("Khan")

    # traveller2
    first_name = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/div[2]/form/section/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/input''')))
    first_name.send_keys("Amitabh")
    last_name = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="fadein"]/div[2]/form/section/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/input''')))
    last_name.send_keys("Bacchan")
    time.sleep(3)

    # payment options
    xpath4 = '''//*[@id="myTab"]/div[3]/div/label/div/img'''
    pay = driver.find_element(by=By.XPATH, value=xpath4)
    driver.execute_script("arguments[0].click();", pay)

    # Agree to the T&C
    xpath5 = '''//*[@id="fadein"]/div[2]/form/section/div/div/div[1]/div[4]/div/div/div/label'''
    agree = driver.find_element(by=By.XPATH, value=xpath5)
    driver.execute_script("arguments[0].click();", agree)

    # Confirming the booking
    xpath6 = '''//*[@id="booking"]'''
    confirm = driver.find_element(by=By.XPATH, value=xpath6)
    driver.execute_script("arguments[0].click();", confirm)

    # Proceeding to payment and Done.
    proceed = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'''//*[@id="form"]'''))).click()
    pay_now = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="form"]/button'''))).click()
    time.sleep(3)

    #Screenshot of booking
    screenshot = py.screenshot()
    screenshot.save("booking.png")
    print("Screenshot taken for EXTRA surety \U0001F600")

    # just to see and verify the booking
    time.sleep(2)
    driver.quit()
    print(emoji.emojize("Your booking status is ( Confirmed ):thumbs_up:"))

except:
    driver.close()
    driver.quit()





