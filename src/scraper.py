import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--disable-logging")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

class StealthScraper:
    def __init__(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--guest")
        self.driver = webdriver.Edge(options=options)

    def get_jobs(self, url):
        self.driver.get(url)
        time.sleep(3)

        jobs = []
        links = self.driver.find_elements(By.CSS_SELECTOR, ".titleline > a")

        for link in links[:8]:
            jobs.append({
                "title": link.text,
                "url": link.get_attribute("href")
            })

        return jobs

    def close(self):
        self.driver.quit()
