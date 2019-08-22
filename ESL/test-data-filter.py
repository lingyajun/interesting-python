# test-job-lead-china : title,company,com_type,area,exp,edu,salary,link,time
# test-英语老师-local  : time,title,school,area,exp,salary,link

import pandas
import re
import numpy

def test():
#    data = pandas.read_csv('test-job-lead-china-4.csv')
    data = pandas.read_csv('test-英语老师-local-3.csv')
#    print(data)
    print(data.info())
    print(type(data))
    print('-----------------')
    print(data.sample(5))
    print('-----------------')
    data['type'] = '英语老师'
 #   print(data['type'])
    print('-------area----------')
    r= data['area'].sample(6)
    print(r)
    r= data['area'].str.split('-', expand = True)
    print(r)

    data['province'] = r[0]
    data['city'] = r[1]
    p = data['province'].sample(16)
    c = data['city'].sample(16)
    print(p)
    print(c)
    
    data.loc[data['province']=='北京', 'city'] = '北京'
    data.loc[data['province']=='上海', 'city'] = '上海'
    data.loc[data['province']=='天津', 'city'] = '天津'
    data.loc[data['province']=='重庆', 'city'] = '重庆'
    c = data['city'].sample(16)
    print(c)
    print('-------exp--degree--------')
    r= data['exp'].sample(6)
    print(r)
    r= data['exp'].str.split('/', expand = True)
    t = r[1]
    print(t.sample(6))
    e= r[0]
    print(e.sample(6))
    print(e.unique())

    exp_map = {'不限':'经验不限', '一年以上':'一到三年', '三年以上':'三到五年', '两年以上':'一到三年',
           '五年以上':'五到十年', '应届毕业生':'经验不限', '六年以上':'五到十年', '四年以上':'三到五年',
           '九年以上':'五到十年', '七年以上':'五到十年', '十年以上':'十年以上', '在读学生':'经验不限', 
           '八年以上':'五到十年'}
    data['experience'] = e.map(exp_map)
    print(data['experience'].sample(10))

    print(t.unique())
    degree_map = {'大专':'大专', '不限':'学历不限', '大学本科以上':'本科', '大学本科':'本科', 
              '大专以上':'大专', '不限以上':'学历不限', '中专以上':'中专', '硕士以上':'硕士', 
              '硕士':'硕士', '高中以上':'高中', '中专':'中专'}
    data['degree'] = t.map(degree_map)
    print(data['degree'].sample(6))
    print(data.sample(6))
    print('-------salary--------')
    s = data['salary'].unique()
    print(s)
    
    return data

def getSalary(salary):
    # 面议  15W-30W/年  5.5K-7.5K/月  800-1200/月
    if '面议' in salary:
        return numpy.nan
    if 'K' in salary and '月' in salary:
        pK = r'(.*)K-(.*)K'
        low, high = re.findall(pK, salary)[0]
        return (float(low)+ float(high))/2
    if 'W' in salary and '年' in salary:
        pW = r'(.*)W-(.*)W'
        low, high = re.findall(pW, salary)[0]
        return (float(low)+ float(high))/2 *10/12
    if 'K' not in salary and '月' in salary:
        p = r'(.*)-(.*)/'
        low, high = re.findall(p, salary)[0]
        return (float(low)+float(high))/2 /1000
    
'''    
#test()

salary = '5.5K-7.5K/月'
print(getSalary(salary))
salary = '15W-30W/年'
print(getSalary(salary))
salary = '800-1200/月'
print(getSalary(salary))
'''

def testLocal():
    data = test()
    print('-------salary--------')
    data['salary_clean'] = data['salary'].apply(getSalary)
    data['salary_clean'] = numpy.round(data['salary_clean'], 1)
    ss = data.sample(5)
    print(ss)
    data.to_csv('test-英语老师-local-clean.csv', index = False, mode='a', header= True  )
    return data


def testJobleadChina():
    data = pandas.read_csv('test-job-lead-china-4.csv')
    print(data.info())
    print(data.sample(5))

    exp = data['exp']
    print(exp.unique())
    exp_clean = exp.str.split(': ', expand=True)[1]
    print(exp_clean.sample(5))
    data['exp_clean'] = exp_clean
    
    salary = data['salary']
    print(salary.unique())
    salary_clean = salary.apply(getSalaryJobleadChina)
    data['salary_clean'] = salary_clean
    print(salary_clean.sample(5))
    
    print(data.info())
    print(data.sample(5))
    data.to_csv('test-job-lead-china-clean.csv', index = False, mode='a', header= True  )
    return data


def getSalaryJobleadChina(salary):
    # 20000K/MTH - 25000K/MTH , 25K/MTH - 26K/MTH
    pattern = r'(.*)K/MTH - (.*)K/MTH'
    result = re.findall(pattern, salary)
    #print('result: ', result)
    #print('result: ', result[0][0])
    low, high = result[0]
    s = (float(low) + float(high))/2
    if '00' in salary:
        return s/1000
    else:
        return s

    
#testJobleadChina()
#testLocal()

'''
salary = '20000K/MTH - 25000K/MTH'
r = getSalaryJobleadChina(salary)
print(r)
'''
