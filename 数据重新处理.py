#!/usr/bin/env python
# -*- coding: utf-8-sig -*-
#
#  �������´���.py
#  
#  Copyright 2021 �˼��������� <�˼���������@LAPTOP-541EAAFT>
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


#����csv�⴦��csv����
import scv

filename1 = "my_file1.csv"
filename2 = 'my_file2.csv'
#1Ϊ�����ļ���2Ϊд���ļ�
members = []
QQ = []
xb =[]
total_list=[]

with open(filename1, "rt") as csvfile1:
    reader = csv.DictReader(csvfile1)
    #��csv��������keyֵ�ķ�ʽ���뵽�б���
    column = [row['��Ա'] for row in reader]
    members=column[:]
    #��column�б��ƣ��ظ�
    column = column = [row['QQ��'] for row in reader]
	QQ     = column [:]
	column = [row['�Ա�'] for row in reader]
	xb     = column[:]

#�ó���Ա������
num=len(menbers)
#���õ����������б�ϲ�
for i in range(0,num+1):
	total.append=members.pop()
	total.append=QQ.pop()
	total.append=xb.pop()
	
#ʹ�����б�д��	
with open(filename2,'wt') as csvfile2:
   cw = csv.writer(csvfile2)
   #����writerow()����
   for item in total:
      cw.writerow(item) #���б��ÿ��Ԫ��д��csv�ļ���һ��
   #�����writerows()����
   #cw.writerows(l) #��Ƕ���б�����д��csv�ļ���ÿ�����Ԫ��Ϊһ�У�ÿ���ڲ�Ԫ��Ϊһ������










