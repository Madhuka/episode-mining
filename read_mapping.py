import re
import timeit
from collections import Counter
import json
import csv,os
import pandas
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
regex = '(.*?)"(.*?)"'
SEPS = ','

sessionsData = pd.read_csv(path+"/sessionsfile")
mappingData = pd.read_csv(path+"/mapping")

#replace each pageID for new page ID with skiping args in urls
def replacePagesID(newid,cid):
    for index in range(len(sessionsData['0'])):
     	  r = sessionsData['0'][index].split(SEPS)

     	  for num in range(len(r)):
    	       if (r[num]==cid):
    	           print r[num] +"-->"+ newid
    	           r[num] = newid
    	           #print r
                   sessionsData['0'][index] = str(r)[1:-1].strip().replace("'","")
                   #print sessionsData['0'][index]


def removeLinesInMapping(index):
    print 'removing line in mapping index'
   # sindex = mappingData.index[1]
    newMappingData = mappingData.drop( mappingData.index[index])
   # print newMappingData
    newMappingData.to_csv(path+'/mapping_file_1.1',sep = ',', index=False) 
    #print mappingData
    
print 'starting....'
indexList = []
with open(path+"/mapping","r") as f:
        lastline =""
        lastid =0 
	for line in f:
	   newline =  line.split("?",1)[0].split(",",1)[1]
	   id =  line.split("?",1)[0].split(",",1)[0]
           #print lastline 
           #print newline == lastline
           if (newline !=  lastline):
                  lastline =  newline
                  lastid = id
                  #print id + lastline
           else:
                  #print 20*"=" +id
                  indexList.append(int(id));
                  replacePagesID(lastid,id)
                  
print indexList   
removeLinesInMapping(indexList)              
#writting to csv files with making version to file 1.1                 
sessionsData.to_csv(path+'/sessions_file_1.1',sep = ',', index=False) 
