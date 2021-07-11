import requests, json
def getSchool(region, name, beautify=False):
    if region in ["sen", "pen", "dge", "ice", "gen", "dje", "use", "sje", "goe", "kwe", "cbe", "cne", "jbe", "jne", "gbe", "gne", "jje"]:
        url = (
            "http://par."+region+".go.kr/spr_ccm_cm01_100.do?"
            "kraOrgNm="+name
        )
        temp = json.loads(requests.get(url).text)
        if not beautify:
            return temp['resultSVO']['orgDVOList']
        else:
            temp = list(temp['resultSVO']['orgDVOList'])
            _schoolList = []
            for n in range(len(temp)):
                temp[n]['data'].pop('sqlAction')
                temp[n]['data'].pop('atptOfcdcOrgCode')
                temp[n]['data'].pop('schulKndScCode')
                temp[n]['data'].pop('schulCrseScCodeNm')
                temp[n]['data']['office'] = temp[n]['data']['atptOfcdcNm']
                temp[n]['data'].pop('atptOfcdcNm')
                temp[n]['data']['code'] = temp[n]['data']['orgCode']
                temp[n]['data'].pop('orgCode')
                temp[n]['data']['name'] = temp[n]['data']['kraOrgNm']
                temp[n]['data'].pop('kraOrgNm')
                temp[n]['data']['zip'] = temp[n]['data']['zipAdres']
                temp[n]['data'].pop('zipAdres')
                temp[n]['data']['type'] = temp[n]['data']['schulCrseScCode']
                temp[n]['data'].pop('schulCrseScCode')
                _schoolList.append(temp[n]['data'])
            return _schoolList