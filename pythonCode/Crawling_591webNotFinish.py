#################try linux code


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import smtplib
import pymongo


def mailTo(title,mailAdds,message,whoSend='Crawler591Web'):
    msg = MIMEMultipart()
    sender = whoSend
    subject = title
    body = message
    msg['From'] = sender
    msg['To'] = ','.join(mailAdds)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text=msg.as_string()
    #print text
    # Send the message via our SMTP server
    s = smtplib.SMTP('192.168.2.1',25)
    s.sendmail(sender,mailAdds, text)
    s.quit()

mailTo("Crawler591WebBegin",["andy.yuan@wowprime.com"],"go")

try:
    b=time.time()
    ##############linux系列用
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=options, executable_path=r'/root/MapProject/AnalyzeMapTopic/pythonCode/chromedriver')
    ##############linux系列用

    # browser = webdriver.Chrome(executable_path=r'/root/MapProject/AnalyzeMapTopic/pythonCode/chromedriver')
    time.sleep(2)

    browser.get('https://business.591.com.tw/?type=1&kind=5&businessSort=1')

    time.sleep(5)

    # x = browser.find_element_by_class_name("accreditPop").find_element_by_css_selector("a").click()

    browser.find_element_by_class_name("fa-angle-down").click()

    CityList = browser.find_element_by_id("optionBox").find_elements_by_class_name("city-li")
    url591List = set()

    cityN = 0
    for i in range(len(CityList)):
        cityN += 1
        browser.find_element_by_id("optionBox").find_elements_by_class_name("city-li")[i].click()
        time.sleep(3)
        soup = bs(browser.page_source, "lxml")
        try:
            allpage = int(soup.select('.pageBar > a')[1]['data-total']) // 30 + 1
        except:
            allpage = 1
        pageNo = 1
        while pageNo <= allpage:
            soup = bs(browser.page_source, "lxml")
            url591List.update(
                ["https:" + i['href'].strip() for i in soup.select("#content")[0].select(".infoContent > h3 > a")])
            # print("已抓取第{}個城市第{}頁網頁".format(cityN, pageNo))
            pageNo += 1
            time.sleep(0.5)
            x = 0
            s = 0
            while x == 0 and s < 10:
                try:
                    browser.find_element_by_link_text('下一頁').click()
                    x = 1
                except:
                    s += 0.5
                    time.sleep(0.5)

            time.sleep(4)
        browser.find_element_by_class_name("fa-angle-down").click()
        time.sleep(2)

    browser.close()
    client = pymongo.mongo_client.MongoClient("localhost", 27017, username='j122085', password='850605')
    # collection = client.rawData.wowprimeipeen
    collection = client.rawData.websites591
    collection.drop()
    collection.insert_one({"urls": list(url591List)})
    client.close()
    e = time.time()
    print(int(e - b))
    mailTo("Crawler591WebReport", ["andy.yuan@wowprime.com"], "完成{}筆，耗時{}秒".format(len(url591List), int(e - b)))
except Exception as er:
    errorstr = "出錯" + str(er) + "出錯位置:" + str(sys.exc_info()[2].tb_lineno)
    mailTo("Crawler591Web_error", ["andy.yuan@wowprime.com"], errorstr)
