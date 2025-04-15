from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import requests

EMAIL = 'dodox777@proton.me'
PASSWORD = '13579@Ad'
CHANNEL_URL = 'https://discord.com/channels/1322328218279088128/1349108144898310174'
WEBHOOK_URL = 'https://discord.com/api/webhooks/1361594365503471837/hoHfLa_AvmJ-NYlvBDpN7HEvx6kkh6lNjC5YkeNuUw_Cmn4VO0u0_WuDVmcPwyz0QIZZ'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=Service(), options=options)
driver.get('https://discord.com/login')

time.sleep(5)
driver.find_element(By.NAME, 'email').send_keys(EMAIL)
driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
driver.find_element(By.NAME, 'password').submit()

time.sleep(10)
driver.get(CHANNEL_URL)
time.sleep(8)

last_message = ""

try:
    while True:
        driver.refresh()
        time.sleep(8)

        messages = driver.find_elements(By.CSS_SELECTOR, '[class^="messageContent-"]')
        if messages:
            latest_message = messages[-1].text
            if latest_message != last_message:
                print("New message:", latest_message)
                last_message = latest_message
                requests.post(WEBHOOK_URL, json={"content": latest_message})
                print("Sent to webhook")
            else:
                print("No new message.")
        else:
            print("No messages found.")

        time.sleep(960)  # 16 minutes

except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    driver.quit()
