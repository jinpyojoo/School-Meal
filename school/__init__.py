from bs4 import BeautifulSoup
import datetime, json, time, requests, re
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
class School:
    def __init__(self, *, region, id):
        self.region = region
        self.id = id
    
    def getSchool(region, name):
        if region in ["sen", "pen", "dge", "ice", "gen", "dje", "use", "sje", "goe", "kwe", "cbe", "cne", "jbe", "jne", "gbe", "gne", "jje"]:
            driver = webdriver.Chrome("./chromedriver.exe", options=options)
            URL = "http://stu."+region+".go.kr/spr_ccm_cm01_001.do"
            driver.get(URL)
            driver.find_element_by_xpath(
                '//*[@id="infoNam"]'
            ).send_keys(name)
            driver.find_element_by_xpath(
                '//*[@id="schLocation"]'
            ).click()
            time.sleep(0.1)
            return json.loads(driver.execute_script('return JSON.stringify(schoolList[0]["data"])'))

        else:
            raise Exception("지역 코드가 맞지 않습니다")

    def getMeal(self, year, month, day, code=2):
        weekday = datetime.date(year=year, month=month, day=day).weekday()
        schMmealScCode = code
        month = str(month).zfill(2)
        year = str(year).zfill(2)
        day = str(day).zfill(2)
        if self.region in ["sen", "pen", "dge", "ice", "gen", "dje", "use", "sje", "goe", "kwe", "cbe", "cne", "jbe", "jne", "gbe", "gne", "jje"]:
            num = weekday + 1
            URL = (
                    "http://stu."+self.region+".go.kr/sts_sci_md01_001.do?"
                    f"schulCode={self.id}"
                    "&schulCrseScCode=4"
                    "&schulKndScCode=04"
                    "&schMmealScCode=%d&schYmd=%s" % (schMmealScCode, str(year)+str(month)+str(day))
                )
            html = ""
            resp = requests.get(URL)
            if resp.status_code == 200 :
                html = resp.text
            soup = BeautifulSoup(html, 'html.parser')
            element_data = soup.find_all("tr")
            element_data = element_data[2].find_all('td')
            try:
                element = str(element_data[num])
                element_filter = ['[', ']', '<td class="textC last">', '<td class="textC">', '</td>', '&amp;', '(h)', '.']
                for element_string in element_filter :
                    element = element.replace(element_string, '')
                element = re.sub(r"\d", "", element)
                element = element.split('<br/>')
                element = list(filter(None, element))
            except Exception as ex:
                element = []
        else:
            raise Exception("지역 코드가 맞지 않습니다")
        return element