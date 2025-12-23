import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

class StealthScraper:
    def __init__(self):
        print(">> Initialisation du navigateur (Edge Natif)...")
        options = webdriver.EdgeOptions()
        options.add_argument("--guest")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Edge(options=options)

    def human_sleep(self, min_time=2, max_time=5):
        time.sleep(random.uniform(min_time, max_time))

    def get_jobs(self, url):
        print(f"Navigation vers {url}...")
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"ERREUR CRITIQUE DE CONNEXION : Impossible d'accéder au site. Vérifie ton internet.\nDétail: {e}")
            return []

        self.human_sleep(3, 5) 
        
        jobs = []
        try:
            print("   (Simulation de scroll...)")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            self.human_sleep(1, 2)
            
            job_elements = self.driver.find_elements(By.TAG_NAME, "a")
            
            count = 0
            for el in job_elements:
                if count >= 5: break
                try:
                    text = el.text
                    href = el.get_attribute("href")
                    
                    if text and len(text) > 5 and href and "http" in href: 
                        jobs.append({"title": text, "url": href})
                        count += 1
                except:
                    continue
                    
        except Exception as e:
            print(f"Erreur scraping: {e}")
            
        return jobs

    def close(self):
        print("Fermeture du navigateur.")
        try:
            self.driver.quit()
        except:
            pass