from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VeeamSelenium:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_webpage_and_maximize(self, url):
        """Open a webpage specified by the URL."""
        self.driver.get(url)
        self.driver.maximize_window()
    
    def select_dropdown_option(self, dropdown_xpath, option_xpath):
        self.driver.find_element(By.XPATH, dropdown_xpath).click()
        option = self.driver.find_element(By.XPATH, option_xpath)
        option.click()
    
    
    def count_text_occurrences(self, text,expected_occurences):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        
        elements = self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}')]")
        print(f"The are {len(elements)} jobs on the page")
        if len(elements) == expected_occurences:
            print("The number of jobs is the expected")
        else:
            print("The number of jobs in not the expected")


    def close_browser(self):
        self.driver.quit()

bot=VeeamSelenium()
bot.open_webpage_and_maximize('https://cz.careers.veeam.com/vacancies')
xpath = '//*[@id="sl"]' 
option_text = '//*[@id="root"]/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/a[2]'
bot.select_dropdown_option(xpath, option_text)
occurrences = bot.count_text_occurrences("Learn more",14)
bot.close_browser()