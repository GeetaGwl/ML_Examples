import numpy as np
import pandas as pd 
#from pandas_profiling import ProfileReport

data=pd.read_csv("./Marks.csv")
print(data)
data2=pd.isnull(data).sum().sum()
print("null is ",data2)

data3=data.dropna()
print(data3)
#print(data)
#print(data.groupby('Sections')["Class"].count())
data=data.fillna({
    'Total_Marks':0,'Per':'0%','Attn':'-'
})
print(data)

print()

print(data.groupby('Sections')["Class"].count())
g_data=data.groupby('Sections')
for section,data_list in g_data :
    print("Sections ",section)
    print(data_list)

'''print("Sect A Students")

print(g_data.get_group('A')) 
a=data.stack(level=0)  
print(a)
print(data)

profile=ProfileReport(data,title="data report",html={'style':{'full_width':True,'backgroundColor':'pink'}})
profile.to_file('profile_report.html')'''
