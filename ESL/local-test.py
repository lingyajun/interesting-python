# www.job910.com/search.aspx?funtype=&sortField=1&sort=1&pageSize=20&pageIndex=2&salary=&maxSalary=&minSalary=&workMethod=&education=&experience=&uptime=0&keyword=英语老师&area=

import requests
from lxml import etree
import pandas

class Job910(object):
    # __base_url = 'http://www.job910.com/search.aspx?sortField=1&sort=1&pageSize=20&pageIndex={}&keyword=英语老师'

    def __init__(self, base_url, pages):
        self.__pages = pages
        self.__base_url = base_url

    def getData(self):
        for p in range(1, self.__pages +1):
            url = self.__base_url.format(p)
            res = requests.get(url)
            self.parseAndSaveData(res, p)

    @staticmethod
    def parseAndSaveData(res, page):
        if res.status_code != 200:
            print(f'get data failed -- {p}, {res.status_code}') 
        else :
            print(f'get data success -- {page}')
            with open('local-result-text.html', 'w') as f:
                f.write(res.text)
            pass

    def parseTest(self):
        with open('local-result-text.html', 'r') as f:
            ss = f.read()
            parsed = etree.HTML(ss)
           # print(f'parseTest read data  -- {ss[:120]}')
            print()
            
            '''
<div class="info-col-1st"><div class="position title"><a title="彭泽私立新星学校 诚聘 初中英语教师（骨干教师）" href="/jobs_view_287922.html" target="_blank" class="extend" rel="287922">初中英语教师（骨干教师）</a></div><div class="area title2">江西-九江-彭泽县</div></>
<div class="info-col-2nd"><div class="salary title">8W-12W/年</div><div class="time title2">2019/08/11</div></div>
<div class="info-col-3rd"><a class="com title adclick" data-click="{cid:13544}" title="彭泽私立新星学校的最新招聘信息" href="/school_view_13544.html" target="_blank">彭泽私立新星学校</a><div class="exp title2">不限/大学本科</div></div><div class="recommend-bar">推荐</div></li><li><div class="check-col"><div class="check-button" data-id="180498"><i class="icon-font">&#xe618;</i></div></div>

<div class="info-col-1st"><div class="position title"><a title="毕节市七星关区佟家榜实验学校 诚聘 初中英语教师" href="/jobs_view_180498.html" target="_blank" class="extend" rel="180498">初中英语教师</a></div><div class="area title2">贵州-毕节-七星关区</div></div><div class="info-col-2nd"><div class="salary title">9W-13W/年</div><div class="time title2">2019/08/11</div></div>
            '''
        # htmlTag = '//*[@class="position title"]/a/text()'
       # htmlTag = '//*[@class="search-result-list"]/ul/text()'
        htmlTag = 'ul[contains(@class, "search-result-list")]/text()'
        result = parsed.xpath(htmlTag)
        print(f'parseTest data  -- \n{result}')
        htmlTag2 = '//*[contains(@class, "position title")]/a/text()'
        title = parsed.xpath(htmlTag2)
        print(f'parseTest data  -- \n{title}\n --{len(title)}--')
        tag = '//*[@class="area title2"]/text()'
        area = parsed.xpath(tag)
        print(f'parseTest area data  -- \n{area}\n --{len(area)}--')
        
        tag = '//*[@class="salary title"]/text()'
        salary = parsed.xpath(tag)
        print(f'parseTest salary data  -- \n{salary}\n --{len(salary)}--')
        
        tag = '//*[@class="time title2"]/text()'
        time = parsed.xpath(tag)
        print(f'parseTest time data  -- \n{time}\n --{len(time)}--')
        
        tag = '//*[@class="com title adclick"]/@href'
        href = parsed.xpath(tag)
        print(f'parseTest href data  -- \n{href}\n --{len(href)}--')
        
        tag = '//*[@class="com title adclick"]/text()'
        school = parsed.xpath(tag)
        print(f'parseTest school data  -- \n{school}\n --{len(school)}--')
        
        tag = '//*[@class="exp title2"]/text()'
        exp = parsed.xpath(tag)
        print(f'parseTest exp data  -- \n{exp}\n --{len(exp)}--')
        
        result = pandas.DataFrame({'time': time ,'school': school ,'area': area ,'exp': exp ,'salary': salary ,'link': href })
       # result.to_csv('test-英语老师-local.csv', index = False, mode='a', header=True  )
       # result.to_csv('test-英语老师-local.csv', index = False, mode='a', header=True  )
        result.to_csv('test-英语老师-local.csv', index = True, mode='a', header=True  )

            
if __name__ == '__main__':
    base_url = 'http://www.job910.com/search.aspx?sortField=1&sort=1&pageSize=20&pageIndex={}&keyword=英语老师'
    pages = 1
    job = Job910(base_url, pages)
#    job.getData()
    job.parseTest()



