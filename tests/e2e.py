import sys

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service(url):
    driver = webdriver.Chrome()
    driver.get(url)
    score = driver.find_element(By.ID, 'score').text
    return 1 <= int(score) <= 1000

def test_driver():
    url = input('please enter the site url\n')
    if test_scores_service(url):
       sys.exit()
    sys.exit(-1)

test_driver()