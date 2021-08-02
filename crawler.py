#!/usr/bin/env python
#-*-coding:utf-8 -*-
#
#  爬取.py
#  
#  Copyright 2021 此间兮若流年 <此间兮若流年@LAPTOP-541EAAFT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import os
import pandas as pd

def save_data(driver):
    res = driver.page_source        # 获取源码
    driver.quit()                   # 关闭浏览器
    soup = BeautifulSoup(res,"lxml")
    html = soup.select("td")
    
    # 先用第2、3 个成员判断一下有无 <群标签>字段
    age_2 = html[ 2 * 10 + 6].text.replace("t", "").replace("n", "")             # Q龄
    age_3 = html[ 2 * 10 + 6].text.replace("t", "").replace("n", "")             # Q龄
    
    data = []
    if "年" in age_2 and "年" in age_3:  # 说明无<群标签>
        for i in range(5000):     # 每个群最大5000人
            try:
                item = []
                for j in range(2,9):
                    lineArr = html[ i*10 + j].text.replace("t", "").replace("n", "")
                    item.append(lineArr)  ## 添加每个成员的信息，
                data.append(item)
            except:
                break
                
        cols = ['群成员', '群名片', 'QQ号', '性别', 'Q龄', '入群时间',  '最后发言时间']
        df = pd.DataFrame(data = data,  columns = cols,encoding='utf-8')
                
    if "年" not in age_2 or "年" not in age_3:  ## 说明有<群标签>
        for i in range(5000):     ## 每个群最大5000人
            try:
                item = []
                for j in range(2,10):
                    lineArr = html[ i*11 + j].text.replace("t", "").replace("n", "")
                    item.append(lineArr)  ## 添加每个成员的信息，
                data.append(item)
            except:
                break
            
        cols = ['群成员', '群名片', 'QQ号', '性别', 'Q龄', '入群时间', '等级积分', '最后发言时间']
        df = pd.DataFrame(data = data,  columns = cols)
     
    # 文件命令方式：路径path：./dataset_yyyymmdd/ 
    #             文件名name：群号 + .csv
    df.to_csv("./dataset_" + now[:8] + "/"  +  group_id + '.csv', 
         encoding = 'utf_8_sig', 
         index = None)
    
    return df

def scroll_foot(driver):
    '''
    下拉界面
    '''
    js="var q=document.documentElement.scrollTop=100000"
    return driver.execute_script(js)
    
now = datetime.datetime.today().strftime("%Y%m%d")
try:  # 创建一个文件夹，用于存放数据集。文件夹命令方式：dataset + yyyymmdd（本日日期）
    file = os.mkdir("dataset_" + now)
except: # 如果文件夹已存在，则放弃创建
    pass

group_id = '657924698'   # 需要爬取的群号
url = 'https://qun.qq.com/member.html#gid={}'.format(group_id)

driver = webdriver.Firefox()#使用Firefox运行selenium
driver.get(url=url)

# 允许完上面代码后请确认登陆了再运行下面程序
# 可以利用time.sleep 给自己x秒内登陆完成后再自动执行下面程序
time.sleep(10)

max_n = 0
while max_n < len(driver.page_source):
    max_n = len(driver.page_source)
    scroll_foot(driver)
    time.sleep(2.5) ## 每2.5秒下拉一次刷新名单，直至刷新不到新名单位置
    
df = save_data(driver) ## 保存本地数据
df.head()
