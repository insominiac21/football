from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = 'https://www.sonyliv.com/live-sport/uefa-champions-league-2023-24-1700000773/football-barcelona-vs-psg-qf-2nd-leg-16-apr-2024-1000272095?watch=true&utm_source=Google&utm_medium=Onebox&utm_campaign=football_live_UCL_barcelona-vs-psg'

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.binary_location = 'C:\Program Files\BraveSoftware\Brave-Browser\Application'  

while True:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(300)
    driver.quit()