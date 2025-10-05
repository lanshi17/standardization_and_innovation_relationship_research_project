import json
import pandas as pd
import matplotlib.pyplot as plt

#读取json文件,共有12个文件,每个文件对应一个城市,依次为南京市无锡市徐州市常州市苏州市南通市连云港市淮安市盐城市扬州市镇江市泰州市宿迁市
#循环读取12个文件,将数据转换为DataFrame,列名称依次是城市名称,年份,标准研制贡献指数,起草单位数量,研制标准数量,主导研制数量,主持研制数量,参与研制数量
#将12个DataFrame合并成一个DataFrame
#文件路径为"E:\Administrator\Documents\大三下\标准化优秀毕业论文\期刊\数据\标准研制贡献指数\chart_data (1).json"
#json文件没有城市名称,需要新增一列城市名称,将城市名称填充到该列
data = pd.DataFrame()
#创建一个城市名称列表
city = ['南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市', '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市']
for i in range(1, 14):
    with open(f'E:\\Administrator\\Documents\\大三下\\标准化优秀毕业论文\\期刊\\数据\\标准研制贡献指数\\chart_data ({i}).json', 'r', encoding='utf-8') as f:
        data1 = json.load(f)
        #转换数据,'xAxisData'为年份,'seriesData'为标准研制贡献指数,起草单位数量,研制标准数量,主导研制数量,主持研制数量,参与研制数量的二维数组
        data1 = {'城市名称': city[i-1],
                 '年份': data1['xAxisData'],
                 '标准研制贡献指数': data1['seriesData'][0],
                 '起草单位数量': data1['seriesData'][1],
                 '研制标准数量': data1['seriesData'][2],
                 '主导研制数量': data1['seriesData'][3],
                 '主持研制数量': data1['seriesData'][4],
                 '参与研制数量': data1['seriesData'][5]}
        data1 = pd.DataFrame(data1)
        data = pd.concat([data, data1], axis=0)
data = data.reset_index(drop=True)
#只保留06-22年的数据
data = data[data['年份'] >= 2006]
data = data[data['年份'] <= 2022]
data = data.reset_index(drop=True)
#将数据保存为csv文件,unicode编码
data.to_csv('E:\\Administrator\\Documents\\大三下\\标准化优秀毕业论文\\期刊\\数据\\标准研制贡献指数.csv', encoding='utf_8_sig', index=True)
print(data)




