from selenium import webdriver
# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
driver = webdriver.Chrome(executable_path=r'/root/MapProject/AnalyzeMapTopic/pythonCode/chromedriver', chrome_options=chrome_options)

driver.get('https://business.591.com.tw/?type=1&kind=5&businessSort=1') 
print(driver.title)
