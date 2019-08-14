
import requests
from lxml import etree
import pandas

class JobleadChina(object):
    # http://www.jobleadchina.com/job?job_industry=Teaching&company_name=&page=2
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
            '''
            with open('job-lead-china-result-text.html', 'w') as f:
                f.write(res.text)
            pass
            '''
            parsed = etree.HTML(res.text)
            tag = '//*[contains(@class, "positionTitle")]/a/text()'
            title =[t.replace('\n', ' ').replace('\t', ' ') for t in parsed.xpath(tag)]
            print(f'parse data -- {title} -- {len(title)} --')
            
            tag = '//*[@class="positionTitle"]/a/@href'
            href = parsed.xpath(tag)
            
            tag = '//*[@class="salaryRange"]/text()'
            salary =[s.strip()  for s in parsed.xpath(tag)]
            print(f'parse data -- {salary} -- {len(salary)} --')
            
            tag = '//*[@class="companyName"]/a/text()'
            company = parsed.xpath(tag)
            print(f'parse data -- {company} -- {len(company)} --')
            
            tag = '//*[@class="post-time"]/text()'
            time = parsed.xpath(tag)
            print(f'parse data -- {time} -- {len(time)} --')
            
            tag = '//*[@class="jobThumbnailCompanyIndustry"]/span[3]/text()'
            area = parsed.xpath(tag)
            print(f'parse data -- {area} -- {len(area)} --')
            
            tag = '//*[@class="jobThumbnailPositionRequire"]/span[1]/text()'
            edu = parsed.xpath(tag)
            print(f'parse data -- {edu} -- {len(edu)} --')
            
            tag = '//*[@class="jobThumbnailPositionRequire"]/span[3]/text()'
            exp = parsed.xpath(tag)
            print(f'parse data -- {exp} -- {len(exp)} --')

            tag = '//*[@class="jobThumbnailCompanyIndustry"]/span[1]/text()'
            com_type = parsed.xpath(tag)
            print(f'parse data -- {com_type} -- {len(com_type)} --')
            
            result = pandas.DataFrame({'title': title, 'company': company, 'com_type': com_type, 'area': area, 'exp': exp, 'edu': edu,  'salary': salary, 'link': href,  'time': time  })
            result.to_csv('test-job-lead-china-4.csv', index = False, mode='a', header= page ==1  )
            print(f'parse and save data success -- {page}')

            
    def parseTest(self):
        with open('job-lead-china-result-text.html', 'r') as f:
            ss = f.read()
            
            '''
            				<div class="jobThumbnail">
					<div class="jobThumbnailCompanyLogo">
						<figure class="jobThumbnailCompanyLogo_figure">
							<img class="jobThumbnailCompanyLogoImg" src="/uploads/companies/1448/company_logo_avatar.jpg" alt="English house">
						</figure>
					</div>
					<div class="jobThumbnailPosition">
						<div class="jobThumbnailPositionName">
							<h3 class="positionTitle">
								<a href="http://www.jobleadchina.com/job/4387">ESL Teacher for a public school</a>
							</h3>
						</div>
						<div class="jobThumbnailSalaryRange">
							<h3 class="salaryRange">
								20K/MTH - 25K/MTH
							</h3>
						</div>
						<div class="jobThumbnailPositionRequire">
							<span>Bachelor</span>
							<span class="seperate-line"></span>
							<span>Experience: Internship</span>
							<span class="seperate-line"></span>
							<span>Full-time</span>
						</div>
													<div class="jobThumbnailPositionPoint"></div>
											</div>
					<div class="jobThumbnailCompany">
						<div class="jobThumbnailCompanyName">
							<h3 class="companyName">
								<a href="http://www.jobleadchina.com/job/4387">English house</a>
							</h3>
						</div>
						<div class="jobThumbnailCompanyIndustry">
							<span>Others</span>
							<span class="seperate-line"></span>
							<span>Shenzhen</span>
						</div>
						<div class="jobThumbnailWalfareTag">
																											</div>
						<div class="timestamp">
							<i class="glyphicon glyphicon-time post-time"></i>
							<span class="post-time">Post time: August 14, 2019</span>
						</div>
					</div>
				</div>

            '''
            parsed = etree.HTML(ss)
            tag = '//*[contains(@class, "positionTitle")]/a/text()'
            title = parsed.xpath(tag)
            print(f'parse data -- {title} -- {len(title)} --')
            
            tag = '//*[@class="positionTitle"]/a/@href'
            href = parsed.xpath(tag)
            print(f'parse data -- {href} -- {len(href)} --')
        

        
if __name__ == '__main__':
    base_url = 'http://www.jobleadchina.com/job?job_industry=Teaching&company_name=&page={}'
    pages = 31
    job = JobleadChina(base_url, pages)
    job.getData()
#    job.parseTest()
    
    