#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
f = open('year_charge.csv')
data = csv.reader(f)
next(data)
area = []
charge = []
year = [2016,2017,2018,2019,2020]
years = []
colors = ['red','orangered','gold','yellow','olive','lightgreen','green','aquamarine','deepskyblue','royalblue','navy','blue','bludviolet','violet','purple','deeppink','pink']
for row in data:
    row[1:] = map(int,row[1:])
    area.append(row[0])
    charge.append(row[1:])
    
#print(area)
#print(charge)
#print(year)
color = range(17)

import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.figure(dpi=300)
for i in range(len(area)):
    plt.bar(year,charge[i],label=area[i])

#print(charge)
plt.title('전국 전기차 충전소 현황 (2016~2020)')
plt.xlabel('연도',labelpad=10)
plt.ylabel('충전소 개수',labelpad=10)
plt.legend(bbox_to_anchor=(1,1.1))
plt.show()


# In[8]:


import csv
f = open('install.csv')
data = csv.reader(f)
next(data)
next(data)
next(data)
count = [0]*17
area = ['경기도','서울특별시','경상남도','경상북도','대구광역시','제주특별자치도','전라남도','강원도','충청북도','전라북도','인청광역시',
       '충청남도','부산광역시','대전광역시','광주광역시','세종특별자치시','울산광역시']

for row in data:
        for i in range(len(area)):
            if area[i] in row[2]:
                 count[i] += 1

#print(count)
#print(sum(count))
count.sort(reverse=True)


import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic',size=5)
plt.figure(dpi=300)
wedgeprops={'width': 0.7, 'edgecolor': 'w','linewidth': 2}
plt.pie(count, startangle = 90, autopct='%.1f%%', wedgeprops = wedgeprops, labels=area, counterclock=False)
#plt.title('전국 전기차 충전소 비중')
plt.axis('equal')
plt.legend(bbox_to_anchor=(1.1,1))
plt.show()


# In[7]:


import csv
f = open('year_charge.csv')
data = csv.reader(f)
next(data)
area = []
charge = []
year = [2016,2017,2018,2019,2020]
years = []
colors = ['red','orangered','gold','yellow','olive','lightgreen','green','aquamarine','deepskyblue','royalblue','navy','blue','bludviolet','violet','purple','deeppink','pink']
for row in data:
    row[1:] = map(int,row[1:])
    area.append(row[0])
    charge.append(row[1:])
    
#print(area)
#print(charge)
#for i in charge:
    #sum += sum(i)
#print(year)
#color = range(17)

import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.figure(dpi=300)
for i in range(len(area)):
    plt.plot(year,charge[i],'-o',label=area[i])

#print(charge)
plt.title('전국 전기차 충전소 현황 (2016~2020)')
plt.xlabel('연도',labelpad=10)
plt.ylabel('충전소 개수',labelpad=10)
plt.legend(bbox_to_anchor=(1,1.1))
plt.show()


# In[6]:


import csv
f = open('install.csv')
data = csv.reader(f)
next(data)
next(data)
next(data)
count = [0]*14
area = ['진안군','정읍시','전주시','장수군','임실군','익산시','완주군','순창군','부안군','무주군','남원시','김제시','군산시','고창군']

for row in data:
    if row[2].split(' ')[0] == '전라북도':
        #if row[2].split(' ')[1] == '전주시':
        for i in range(len(area)):
            if area[i] in row[2]:
                count[i] += 1

count[-2] += 1
#print(count[2])
#print(count)
#print(sum(count))

import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.figure(dpi=300)
plt.barh(area,count,color='#18caca',label='충전소 수')
plt.title('전라북도 내 충전소 현황')
plt.xlabel('충전소 수',labelpad=10)
plt.ylabel('지역명',labelpad=10)
plt.legend()
plt.show()


# In[5]:


import csv
f = open('rest.csv')
data = csv.reader(f)
next(data)
number = ['02','031','032','033','041','042','043','051','052','053','054','055','061','063']
area = ['서울','경기','인천','강원','충남','대전','충북','부산','울산','대구','경북','경남','전남','전북']
count = [0] * 14
count2 = [0] * 14
for row in data:
    if row[2] == 'O':
        for i in range(len(number)):
            if row[1].split('-')[0] == number[i]:
                count[i] += 1

#print('전국 휴게소 전기차 충전소 총 개수 :',sum(count))
#print('전국 휴게소 전기차 충전소 최대 개수 :',max(count))
count[1] += 4
count[9] += 2
count[-2] += 2
count[6] += 1

import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.figure(dpi=300)
plt.title('전국 휴게소 별 전기차 충전소 현황')
plt.barh(area,count,label='충전소 수',color='#18caca')
plt.xlabel('충전소 수',labelpad=10)
plt.ylabel('지역명',labelpad=10)
plt.legend()
plt.show()


# In[4]:


import csv
import matplotlib.pyplot as plt

f = open("city_ev.csv")
data = csv.reader(f)
next(data)

city = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
city_ev = [0] * 17

for row in data:
    if '전기' in row[4]:
        for i in range(len(city)):
            if row[i+5] != '  ':
                city_ev[i] += int(row[i+5])
    
#print(city)
#print(city_ev)


f = open("charger.csv")
data = csv.reader(f)
next(data)

cg_city = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
cg_count = [0] * 17

for row in data:
    for i in range(len(cg_city)):
        if row[2].split(' ')[0] in cg_city[i]:
            if row[3] != '':
                cg_count[i] += int(row[3])
    
#print(cg_city)
#print(cg_count)

plt.rc('font', family='Malgun Gothic')
plt.figure(dpi=300)
plt.barh(city, city_ev, label = '시/도별 전기차 수',color='#d4eae8')
plt.barh(city, cg_count, label = '시/도별 충전소 수',color='#18caca')
plt.title('전국 시/도별 전기차 수에 따른 충전소 비율')
plt.xlabel('개수',labelpad=10)
plt.ylabel('지역명',labelpad=10)
plt.legend()
plt.show()


# In[3]:


import csv
import matplotlib.pyplot as plt

f = open("jb_ev.csv")
data = csv.reader(f)
next(data)

city = ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군', '장수군', '전주시', '정읍시', '진안군']
city_ev = [0] * 14

for row in data:
    for i in range(len(city)):
        if row[1] in city[i]:
            city_ev[i] += int(row[4])
    
#print(city)
#print(city_ev)

plt.rc('font', family='Malgun Gothic')
plt.figure(dpi=300)
plt.barh(city, city_ev, label = '전기차 수',color='#18caca')
plt.title('전라북도 내 전기차 등록 현황')
plt.xlabel('전기차 수',labelpad=10)
plt.ylabel('지역명',labelpad=10)
plt.legend()
plt.show()


# In[2]:


import csv
import matplotlib.pyplot as plt

result = []
labels = ['2016', '2017', '2018', '2019', '2020', '2021']

for i in range(16,22):
    f = open("20%d_11.csv" %i)
    data = csv.reader(f)

    for row in data:
        if '합계' in row:
            sum = (int(row[7]) + int(row[8]))
            result.append(sum)
    #print("20%d년 11월 기준 전기차 등록 대수 : "%i, sum)
    
plt.rc('font', family='Malgun Gothic')
plt.figure(dpi=300)
plt.bar(labels, result, label = '전기차 수',color='#18caca')
plt.title('2016~2021년 전기차 등록 현황')
plt.legend()
plt.xlabel('연도',labelpad=10)
plt.ylabel('전기차 수',labelpad=10)
plt.show()
#plt.hist(result, bins = 20)
#plt.xlabel(labels)

