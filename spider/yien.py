from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable gpu')
driver = webdriver.Chrome()

url = 'https://www.endata.com.cn/BoxOffice/BO/Year/index.html'
driver.get(url)
sleep(1)
f = open('./movies333.csv', mode='a',encoding='utf-8')
f.write("name,type,value,avgtval,avgman,country,time,core")
f.write('\n')
select_el = driver.find_element_by_id('OptionDate')
# 找到切换年份对应的element
select = Select(select_el)
for i in range(len(select.options)):
    select.select_by_index(i)
    # 用索引的方式进行切换页面
    sleep(2)
    tr_list = driver.find_elements_by_xpath('//table[@class="bo-table img-table"]//tr')[1:]
    for tr in tr_list:
        for td in tr.find_elements_by_xpath('./td'):
            f.write(td.text.strip())
            f.write('，')
        f.write('\n')
    f.write('\n\n')
    print('第%d页打印完毕' % i)
    if(i==7):
        print("OK!")
        break
driver.close()



