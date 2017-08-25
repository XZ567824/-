#encoding:utf-8
import jieba
import pickle
from collections import defaultdict
import itertools

path = 'C:/Users/Administrator/Desktop/南京日报数据.txt'
news_all = {}
with open(path, 'r', encoding='utf-8') as f:
    data = defaultdict(list)
    content = f.readlines()
    for con in content:
        sp_con = con.split('#')
        if sp_con[2]>='2017-06-01 00:00:00' and sp_con[2]<'2017-06-02 00:00:00':
            data['1'].append(sp_con[1])
        if sp_con[2]>='2017-06-02 00:00:00' and sp_con[2]<'2017-06-03 00:00:00':
            data['2'].append(sp_con[1])
        if sp_con[2]>='2017-06-03 00:00:00' and sp_con[2]<'2017-06-04 00:00:00':
            data['3'].append(sp_con[1])
        if sp_con[2]>='2017-06-04 00:00:00' and sp_con[2]<'2017-06-05 00:00:00':
            data['4'].append(sp_con[1])
        if sp_con[2]>='2017-06-05 00:00:00' and sp_con[2]<'2017-06-06 00:00:00':
            data['5'].append(sp_con[1])
        if sp_con[2]>='2017-06-06 00:00:00' and sp_con[2]<'2017-06-07 00:00:00':
            data['6'].append(sp_con[1])
        if sp_con[2]>='2017-06-07 00:00:00' and sp_con[2]<'2017-06-08 00:00:00':
            data['7'].append(sp_con[1])
        if sp_con[2]>='2017-06-08 00:00:00' and sp_con[2]<'2017-06-09 00:00:00':
            data['8'].append(sp_con[1])
        if sp_con[2]>='2017-06-09 00:00:00' and sp_con[2]<'2017-06-10 00:00:00':
            data['9'].append(sp_con[1])
        if sp_con[2]>='2017-06-10 00:00:00' and sp_con[2]<'2017-06-11 00:00:00':
            data['10'].append(sp_con[1])
        if sp_con[2]>='2017-06-11 00:00:00' and sp_con[2]<'2017-06-12 00:00:00':
            data['11'].append(sp_con[1])
        if sp_con[2]>='2017-06-12 00:00:00' and sp_con[2]<'2017-06-13 00:00:00':
            data['12'].append(sp_con[1])
        if sp_con[2]>='2017-06-13 00:00:00' and sp_con[2]<'2017-06-14 00:00:00':
            data['13'].append(sp_con[1])
        if sp_con[2]>='2017-06-14 00:00:00' and sp_con[2]<'2017-06-15 00:00:00':
            data['14'].append(sp_con[1])
        if sp_con[2]>='2017-06-15 00:00:00' and sp_con[2]<'2017-06-16 00:00:00':
            data['15'].append(sp_con[1])
        if sp_con[2]>='2017-06-16 00:00:00' and sp_con[2]<'2017-06-17 00:00:00':
            data['16'].append(sp_con[1])
        if sp_con[2]>='2017-06-17 00:00:00' and sp_con[2]<'2017-06-18 00:00:00':
            data['17'].append(sp_con[1])
        if sp_con[2]>='2017-06-18 00:00:00' and sp_con[2]<'2017-06-19 00:00:00':
            data['18'].append(sp_con[1])
        if sp_con[2]>='2017-06-19 00:00:00' and sp_con[2]<'2017-06-20 00:00:00':
            data['19'].append(sp_con[1])
        if sp_con[2]>='2017-06-20 00:00:00' and sp_con[2]<'2017-06-21 00:00:00':
            data['20'].append(sp_con[1])
        if sp_con[2]>='2017-06-21 00:00:00' and sp_con[2]<'2017-06-22 00:00:00':
            data['21'].append(sp_con[1])
        if sp_con[2]>='2017-06-22 00:00:00' and sp_con[2]<'2017-06-23 00:00:00':
            data['22'].append(sp_con[1])
        if sp_con[2]>='2017-06-23 00:00:00' and sp_con[2]<'2017-06-24 00:00:00':
            data['23'].append(sp_con[1])
        if sp_con[2]>='2017-06-24 00:00:00' and sp_con[2]<'2017-06-25 00:00:00':
            data['24'].append(sp_con[1])
        if sp_con[2]>='2017-06-25 00:00:00' and sp_con[2]<'2017-06-26 00:00:00':
            data['25'].append(sp_con[1])
        if sp_con[2]>='2017-06-26 00:00:00' and sp_con[2]<'2017-06-27 00:00:00':
            data['26'].append(sp_con[1])
        if sp_con[2]>='2017-06-27 00:00:00' and sp_con[2]<'2017-06-28 00:00:00':
            data['27'].append(sp_con[1])
        if sp_con[2]>='2017-06-28 00:00:00' and sp_con[2]<'2017-06-29 00:00:00':
            data['28'].append(sp_con[1])
        if sp_con[2]>='2017-06-29 00:00:00' and sp_con[2]<'2017-06-30 00:00:00':
            data['29'].append(sp_con[1])
        if sp_con[2]>='2017-06-30 00:00:00' and sp_con[2]<'2017-07-01 00:00:00':
            data['30'].append(sp_con[1])
    for i in range(1, 31):
        full_data = list(itertools.chain(data[str(1)], data[str(2)],data[str(3)],data[str(4)],data[str(5)],data[str(6)],
                                    data[str(7)],data[str(8)],data[str(9)],data[str(10)],data[str(11)],data[str(12)],
                                    data[str(13)],data[str(14)],data[str(15)],data[str(16)],data[str(17)],data[str(18)],
                                    data[str(19)],data[str(20)],data[str(21)],data[str(22)],data[str(23)],data[str(24)],data[str(25)],
                                    data[str(26)],data[str(27)],data[str(28)],data[str(29)],data[str(30)]))


print(list(full_data))








