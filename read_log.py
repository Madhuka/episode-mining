#111.223.135.118 - [28/May/2013:23:54:59 +0530] "GET /SVRClientWeb/main/styles/theme-orange/appui/elements/elements.fieldset.css HTTP/1.1" 200 307 "https://www.sampathvishwa.com/SVRClientWeb/main/ui/common/index.jsp" "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Ubuntu Chromium/25.0.1364.160 Chrome/25.0.1364.160 Safari/537.22" GET /SVRClientWeb/main/styles/theme-orange/appui/elements/elements.fieldset.css - HTTP/1.1 www.sampathvishwa.com

import re
import apachelog
import pandas
import pandas as pd
import numpy as np
import string
import subprocess
import os
import io
#from
from pandas import read_csv
from datetime import datetime
from datetime import timedelta

path = os.path.dirname(os.path.realpath(__file__))

fformat = r'%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"'
print 'starting'
p = apachelog.parser(fformat)
log = open(path+'/clean_log').readlines()
xnr_of_lines = sum(1 for line in log)
print '\nTotal Number of Lines in Converted Log File: ' + str(xnr_of_lines)
print '\n'
log_list = []
for line in log:
           try:
              print line
              data = p.parse(line)
              print data
           except:
               pass
               print "Unable to parse " + line
           data['%t'] = data['%t'][1:12]+' '+data['%t'][13:21]+' '+data['%t'][22:27]
          
           log_list.append(data)
           
df = pd.DataFrame(log_list)

df = df.rename(columns={'%>s': 'Status', '%b':'Bytes', 
                            '%h':'IP','%l':'UserName' ,'%r':'Request', '%t': 'Time', '%u':'UserID','%{Referer}i' : 'Referer', '%{User-Agent}i' : 'Agent'})     
    
              
#date time

def strptime_with_offset(string, format='%d/%b/%Y %H:%M:%S'):
        try:
            print string
            base_dt = datetime.strptime(string[:-6], format)
            offset = int(string[-6:])
            delta = timedelta(hours=offset/100, minutes=offset%100)
            return base_dt + delta 
        except:
            pass
    
df['Time'] = df['Time'].apply(strptime_with_offset)
print df.dtypes  
print len(df)
    
df = df[~df['Request'].str.contains('jpg|jpeg|png|js|min.js|ico|bmp|gif|css|JPG|JPEG|PNG|JS|MIN.JS|ICO|BMP|GIF|CSS', na=False)]

    
df['Time'] = pandas.to_datetime(df['Time'])
    
#checking log date time period
df9 = df[(df['Time'] > '2013-12-08 00:00') & (df['Time'] < '2015-12-19 23:59')]
print len(df9)    
                 
                    
#genrate session 
#g = df9.groupby(['IP'])  
g = df9.groupby(['IP', 'Agent']) 
df9['session_number'] = g['Time'].apply(lambda s: (s - s.shift(1) > pd.offsets.Minute(30).nanos).fillna(0).cumsum(skipna=False))
df1 = df9.set_index(['IP', 'Agent', 'session_number'])
g1 = df9.groupby(['IP', 'Agent', 'session_number'])
df1['session'] = g1.apply(lambda x: 1).cumsum()
NoOfSessions = len(df1.groupby('session'))
print '\n\nTotal No of Sessions : ' + str(NoOfSessions)
print '\n\n'    

#output 
df2 = pd.DataFrame(df1.reset_index())
df2.to_csv(path+'/sessionsfile',sep = ',')
mapSessionwithIP = df2[['session','IP','Agent']]   

def gmet(x):
    x = x.split(' ')
    return x[1]
    
df2['Request'] = df2['Request'].apply(gmet)
    
print  df2['Request'][0:5]   

                              
#mapping
from sklearn import preprocessing
requestlist = df2.Request.tolist()

le = preprocessing.LabelEncoder()
le.fit(requestlist)
l = le.transform(requestlist)
print '\n\n\n'
df2['mapping'] = np.array(l)
dfx = df2[['mapping','Request']].drop_duplicates(cols='mapping', take_last=False)
dfx.sort_index(by=['mapping'], ascending=True).to_csv(path+'/mapping', index=False)
    
    

df2['mapping'] = df2['mapping'].apply(str)  
print df2[0:5]  
df6 = pd.DataFrame(df2.groupby('session').apply(lambda x: ','.join(x.mapping))).reset_index()
df6.to_csv(path+'/sessionsfile',sep = ',', index=False)                               
