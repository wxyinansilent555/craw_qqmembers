#!/usr/bin/env python
# -*- coding: utf-8-sig -*-
#
#  数据重新处理.py
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


#导入csv库处理csv数据
import scv

filename1 = "my_file1.csv"
filename2 = 'my_file2.csv'
#1为输入文件，2为写入文件
members = []
QQ = []
xb =[]
total_list=[]

with open(filename1, "rt") as csvfile1:
    reader = csv.DictReader(csvfile1)
    #打开csv，用搜索key值的方式读入到列表当中
    column = [row['成员'] for row in reader]
    members=column[:]
    #将column列表复制，重复
    column = column = [row['QQ号'] for row in reader]
	QQ     = column [:]
	column = [row['性别'] for row in reader]
	xb     = column[:]

#得出成员的人数
num=len(menbers)
#利用弹出将三个列表合并
for i in range(0,num+1):
	total.append=members.pop()
	total.append=QQ.pop()
	total.append=xb.pop()
	
#使用新列表写入	
with open(filename2,'wt') as csvfile2:
   cw = csv.writer(csvfile2)
   #采用writerow()方法
   for item in total:
      cw.writerow(item) #将列表的每个元素写到csv文件的一行
   #或采用writerows()方法
   #cw.writerows(l) #将嵌套列表内容写入csv文件，每个外层元素为一行，每个内层元素为一个数据










