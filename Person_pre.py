#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# 设置支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
rc = {'font.sans-serif': 'SimHei',
      'axes.unicode_minus': False}  # 用来正常显示中文标签
# 设置学术化的图片风格
sns.set_style("whitegrid", rc=rc)  #设置绘图风格
sns.set_palette("hls")  #设置颜色主题
sns.set_context("paper")  #设置绘图元素缩放比例
data_raw = pd.read_csv('data/预调研数据.csv')
#不包括index和最后一列
data_raw.columns = ['index', 'totalseconds', 'totalvalue', 'Industry', 'Nature', 'Year', 'EmployeesNum', 'Income', 'Area', 'SL11', 'SL12', 'SL13', 'SL21', 'SL22', 'SL23', 'KMC11', 'KMC12', 'KMC21', 'KMC22', 'KMC31', 'KMC32', 'OLC11', 'OLC12',  'OLC21', 'OLC22', 'OLC31', 'OLC32','TIC11','TIC12','TIC13','TIC14','TIC21','TIC22','TIC23','Awards1','Awards2','Awards3','Awards4','Awards5','Awards6','Awards7','TIC31','TIC32','TIC33','MCI1','MCI2','MCI3','StrategicFocus1','StrategicFocus2','StrategicFocus3','StrategicFocus4','StrategicFocus5','sugestion']
#删除第一列
data_raw = data_raw.drop(columns=['index'])
#删除最后一列
data_raw = data_raw.drop(columns=['sugestion'])
#保存为csv文件
data_raw.to_csv('exports/预调研数据.csv', index=False)
data_raw
#%%
data = data_raw.copy()
#%%
data_total = pd.DataFrame()
data_total['SL'] = (data['SL11'] + data['SL12'] + data['SL13'] + data['SL21'] + data['SL22'] + data['SL23'])/6
data_total['KMC'] = (data['KMC11'] + data['KMC12']  + data['KMC21'] + data['KMC22'] + data['KMC31'] + data['KMC32'] )/6
data_total['OLC'] = (data['OLC11'] + data['OLC12'] + data['OLC21'] + data['OLC22'] + data['OLC31'] + data['OLC32'] )/6
data_total['TIC'] = (data['TIC11'] + data['TIC12'] + data['TIC13'] + data['TIC14'] + data['TIC21'] + data['TIC22'] + data['TIC23'] + data['TIC31'] + data['TIC32'] + data['TIC33'])/10
data_total['MCI'] = (data['MCI1'] + data['MCI2'] + data['MCI3'])/3
data_total['Scale']= data_raw['EmployeesNum']
data_total['Year']= data_raw['Year']
#数据四舍五入
data_total = data_total.round(0)
data_total.to_csv('exports/预调研量表数据总分.csv', index=False)
data_total.isnull().sum()
#%%
