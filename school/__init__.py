import requests, re
from bs4 import BeautifulSoup
import datetime
class School:
    def __init__(self, *, region, id):
        self.region = region
        self.id = id
    def getMeal(self, year, month, day, code):
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