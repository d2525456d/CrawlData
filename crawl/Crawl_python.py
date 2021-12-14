#import các thư viện
from selenium import webdriver
import pandas as pd
import random

#Nhập dữ liệu vào
league = input("Nhập giải đấu muốn crawl(EPL,La liga, Bundesliga, Serie A, Ligue 1, RFPL:")
Year = input("Nhập mùa giải:2020/2021,2019/2020,2018/2019,2017/2018,2016/2017,2015/2016,2014/2015")

#Dùng selenium để click đến nơi có dữ liệu muốn crawl
if league == "EPL":
    n = 380
    driver = webdriver.Chrome(executable_path=".\Driver\chromedriver.exe")
    driver.get('https://understat.com/')
    driver.find_element_by_xpath('/html/body/div[1]/header/div/nav[1]/ul/li[1]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div').click()


if league == "La liga":
    n = 380
    driver = webdriver.Chrome(executable_path=".\Driver\chromedriver.exe")
    driver.get('https://understat.com/')
    driver.find_element_by_xpath('/html/body/div[1]/header/div/nav[1]/ul/li[2]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div').click()


if league == "Bundesliga":
    n = 340
    driver = webdriver.Chrome(executable_path=".\Driver\chromedriver.exe")
    driver.get('https://understat.com/')
    driver.find_element_by_xpath('/html/body/div[1]/header/div/nav[1]/ul/li[3]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div').click()


if league == "Serie A":
    n = 380
    driver = webdriver.Chrome(executable_path=".\Driver\chromedriver.exe")
    driver.get('https://understat.com/')
    driver.find_element_by_xpath('/html/body/div[1]/header/div/nav[1]/ul/li[4]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div').click()


if league == "Ligue 1":
    n = 380
    driver = webdriver.Chrome(executable_path=".\Driver\chromedriver.exe")
    driver.get('https://understat.com/')
    driver.find_element_by_xpath('/html/body/div[1]/header/div/nav[1]/ul/li[5]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div').click()


if league == "RFPL":
    n = 300
    driver = webdriver.Chrome(executable_path=".\Driver\chromedriver.exe")
    driver.get('https://understat.com/')
    driver.find_element_by_xpath('/html/body/div[1]/header/div/nav[1]/ul/li[6]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div').click()


if Year == "2020/2021":
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/ul/li[2]').click()
if Year == "2019/2020":
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/ul/li[3]').click()
if Year == "2018/2019":
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/ul/li[4]').click()
if Year == "2017/2018":
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/ul/li[5]').click()
if Year == "2016/2017":
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/ul/li[6]').click()
if Year == "2015/2016":
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/ul/li[7]').click()
if Year == "2014/2015":
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/ul/li[8]').click()


#tạo dict để đưa dữ liệu vào dict rồi tạo thành DataFrame
dt = {'Home_team': [],'Home_score':[],'Away_score':[],'Away_team':[],'Home_xG':[],'Away_xG':[]}
match = 0
Home_team = []
Home_score = []
Away_score = []
Away_team = []
Home_xG = []
Away_xG = []
#n là tổng số trận của giải mình muốn crawl
#hàm để crawl
while match < n:

    # print(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/a').text)
    # print(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/a').text)
    # print(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/a').text)
    b = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div'))

    team = []
    for i in range(b):
        a = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div'))
        for j in range(a):
            if a == 0:
                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div/div[1]/div/a').text
                Home_team.append(team)
                match += 1
            else:

                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div['+str(j+1)+']/div[1]/div/a').text
                Home_team.append(team)
                match += 1


    team = []
    for i in range(b):
        a = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div'))
        for j in range(a):
            if a == 0:
                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div/a/div[1]/span[1]').text
                Home_score.append(team)
            else:

                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div['+str(j+1)+']/a/div[1]/span[1]').text
                Home_score.append(team)


    team = []
    for i in range(b):
        a = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div'))
        for j in range(a):
            if a == 0:
                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div/a/div[1]/span[2]').text
                Away_score.append(team)
            else:

                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div['+str(j+1)+']/a/div[1]/span[2]').text
                Away_score.append(team)


    team = []
    for i in range(b):
        a = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div'))
        for j in range(a):
            if a == 0:
                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div/div[2]/div/a').text
                Away_team.append(team)
            else:

                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div['+str(j+1)+']/div[2]/div/a').text
                Away_team.append(team)



    team = []
    for i in range(b):
        a = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div'))
        for j in range(a):
            if a ==0:
                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div/a/div[2]/span[1]').text
                Home_xG.append(team)
            else:
                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div['+str(j+1)+']/a/div[2]/span[1]').text
                Home_xG.append(team)



    team = []
    for i in range(b):
        a = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div'))
        for j in range(a):
            if a == 0:
                team  =driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div/a/div[2]/span[2]').text
                Away_xG.append(team)
            else:
                team = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div['+str(i+1)+']/div[2]/div['+str(j+1)+']/a/div[2]/span[2]').text
                Away_xG.append(team)




    #ấn vào prev week
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/button[1]').click()
#Đưa các data crawl được vào dict
dt['Home_team'] = Home_team
dt['Home_score'] = Home_score
dt['Away_score'] = Away_score
dt['Away_team'] = Away_team
dt['Home_xG'] = Home_xG
dt['Away_xG'] = Away_xG
#đóng web
driver.close()
#đưa dict thành DataFrame
dt = pd.DataFrame(dt)
#random để tạo file không bị trùng
t = random.randint(0,10000)
#print t ra để biết file vừa crawl là file nào
print(t)
#chuyển thành file csv
dt.to_csv('File_craw'+str(t)+'.csv',header=True)
