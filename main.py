import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from urllib.parse import urlparse

if __name__ == '__main__':
    link1="https://duckduckgo.com/?q="
    # You can change the word Large in the second part of link to change wanted size
    link2="&t=ffab&iar=images&iaf=size%3ALarge&iax=images&ia=images"
    # Number of images
    iterations = 50

    # Searched queries
    list_queries = []
    # add Github token to make webdriver_manager working
    os.environ[
        'GH_TOKEN'] = ""
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    for query in list_queries:
        if not os.path.exists(query):
            os.mkdir(query)
        path = link1+query+link2
        driver.get(path)
        # You can change the time to 1
        # 15 used to have time to change other parameters at webpage
        time.sleep(15)
        first_image = driver.find_element(By.XPATH, value="/html/body/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/div[1]")
        first_image.click()
        for i in range(iterations):
            time.sleep(1)
            button = driver.find_element(By.XPATH, value="/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/a")
            link=button.get_attribute('href')
            filename = urlparse(link)
            filename = os.path.basename(filename.path)
            file_path = os.path.join(os.getcwd(), query, filename)
            try:
                time.sleep(1)
                r=requests.get(link)
                with open(file_path, 'wb') as f:
                    f.write(r.content)
            except Exception as e:
                print("file not found")
                print(link)
            next_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/div/div[2]/i[2]")
            next_button.click()
    driver.quit()

