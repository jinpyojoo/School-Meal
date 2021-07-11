import requests, re
from bs4 import BeautifulSoup
import datetime
class School:
    def __init__(self, region, code):
        if region is None or code is None:
            raise Exception("지역 또는 학교코드가 비어있습니다.")
        self.region = region
        self.code = code
    
    today = datetime.datetime.today()
    def getMeal(self, year=today.year, month=today.month, day=today.day, code=2):
        weekday = datetime.date(year=year, month=month, day=day).weekday()
        schMmealScCode = code
        month = str(month).zfill(2)
        year = str(year).zfill(2)
        day = str(day).zfill(2)
        if self.region in ["sen", "pen", "dge", "ice", "gen", "dje", "use", "sje", "goe", "kwe", "cbe", "cne", "jbe", "jne", "gbe", "gne", "jje"]:
            num = weekday + 1
            URL = (
                    "http://stu."+self.region+".go.kr/sts_sci_md01_001.do?"
                    f"schulCode={self.code}"
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
            raise Exception("지역 코드가 맞지 않습니다.")
        return element