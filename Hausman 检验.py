#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import openpyxl

import warnings

# Suppress FutureWarnings from the linearmodels package
warnings.filterwarnings("ignore", category=FutureWarning, module="linearmodels.*")

# Your existing code here
# 设置支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
rc = {'font.sans-serif': 'SimHei',
      'axes.unicode_minus': False}  # 用来正常显示中文标签
# 设置学术化的图片风格
sns.set_style("whitegrid", rc=rc)  #设置绘图风格
sns.set_palette("hls")  #设置颜色主题
sns.set_context("paper")  #设置绘图元素缩放比例
data = pd.read_csv('data/data_diff.csv')
data['City'] = data['City'].astype('category')
data['Year'] = data['Year'].astype('category')
data.head()
#%%
#检查缺失值
data.isnull().sum()

#%%
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr
#%%
# 启用 pandas 和 R 之间的数据框转换
pandas2ri.activate()

# 导入 R 中的相关包
plm = importr('plm')
base = importr('base')
#%%
r_data = pandas2ri.py2ri(data)
robjects.globalenv['r_data'] = r_data
#%%
# 将面板数据转换为时间序列对象
pdata = plm.pdata_frame(r_data, index=robjects.vectors.StrVector(['City', 'Year']))
robjects.globalenv['pdata'] = pdata

# 进行levinlin检验
levinlin_test_result = plm.purtest(pdata.rx2('TIP'), test='levinlin')
print(levinlin_test_result)



#%%
