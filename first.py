from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
from selenium.webdriver.chrome.service import Service
service = Service("./drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.youtube.com")
bashliq=driver.current_url
driver.maximize_window()
if "youtube.com" in bashliq:
   print("duz ishledi: "+bashliq)
   driver.get("http://www.amazon.com")
   bashliq=driver.current_url
   if "amazon.com" in bashliq:
      print("duz ishledi: "+bashliq)
      driver.back()
      
driver.get("http://www.google.com")
     