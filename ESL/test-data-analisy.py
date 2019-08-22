import pandas
import re
import numpy
import matplotlib.pyplot as plot
import seaborn


plot.style.use('ggplot')
from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决seaborn中文字体显示问题
plot.rc('figure', figsize=(10, 10))  #把plt默认的图片size调大一点
#plot.rcParams["figure.dpi"] =mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#mpl.rcParams["savefig.dpi"]= 2000
#%matplotlib inline

'''
    洋外教的工资真的高吗？
    市场对于洋外教的经验和学历要求如何？
    哪些地区对洋外教的需求多？
    什么机构在招聘洋外教？
'''

def compaileSalary():
    # 'test-英语老师-local-clean.csv' , 'test-job-lead-china-clean.csv'
    dataLocal = pandas.read_csv('test-英语老师-local-clean.csv')
    dataJobLead = pandas.read_csv('test-job-lead-china-clean.csv')
    print(dataLocal.info())
    print(dataJobLead.info())

    dataLocal['teacher_type'] = 'chinese'# '中教'
    dataJobLead['teacher_type'] = 'fornginer' #'外教'
    
    local = dataLocal[['salary_clean', 'teacher_type']]
    joblead = dataJobLead[['salary_clean', 'teacher_type']]
    dataSalary = pandas.concat([local, joblead])
    print(dataSalary.info())
    print(dataSalary.sample(5))

    '''
    cols = {'salary_clean':'薪资', 'teacher_type':'教师类型'}
    dataSalary.rename(columns=cols, inplace = True)
    print(dataSalary.info())
    print(dataSalary.sample(5))
    '''
    print('-------seaborn-------')
    '''
    1. /home/hosea/anaconda3/lib/python3.7/site-packages/seaborn/axisgrid.py:230: 
    UserWarning: The `size` paramter has been renamed to `height`; please update your code.
    
    2. ValueError: dpi must be positive
    
    g = seaborn.FacetGrid(dataSalary, row='教师类型', size=4, aspect=2, xlim=(0,30))
    '''
    '''
    indexs =dataSalary[ dataSalary['薪资'] <=0].index
    dataSalary.drop(indexs, inplace=True)
    print(dataSalary.info())
    print(dataSalary.sample(5))
    '''
    #seaborn.set(font_scale=1.5)
    #plot.dpi = 1
   # g = seaborn.FacetGrid(dataSalary, row='教师类型', height=4, aspect=2, xlim=(0,30))
   # g.map(seaborn.distplot, '薪资', rug=False)
    g = seaborn.FacetGrid(dataSalary, row='teacher_type', height=4, aspect=2, xlim=(0,30))
    g.map(seaborn.distplot, 'salary_clean', rug=False)
    print(g)
    print('-------seaborn-end------')
    plot.show()
    
compaileSalary()


