'''
grouping urls n pageID
for each cluster 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'D:/Research/data/run03/'
elementCount = 20

#methods 
'''
Showing count of page for each cluster and precentage
'''
#defining a function
def pageIdCountInCluster(cNum,dataFrame):
     out  = dataFrame.T
     out.columns = ['ColA']
     ords = out.order(ascending=False).head(elementCount)
     print '\nClusterNo '+ str(cNum)
     print ords
     #myJSON = ords.to_json()
     #print {cNum :myJSON}
    
#counting pages in each cluster and mapping page id to page URL in 'new_mapping.csv'    
def pageCountInCluster(cNum,dataFrame):
     out  = dataFrame.T
     ords = out.order(ascending=False).head(elementCount)
     #print "\n"+45*"="
     print "clusterNo "+ str(cNum)+"\n"
     pids = ords.index.values
     print ords
     for num in range(0,len(pids)):    
        
        x = pids[num]
        #getting index in page count eg: 'p1'
        indexs =  int(x[1:])       
        #print newid_df.loc[indexs-1]['pageID']  
        #print newid_df.loc[indexs-1]['newID'] 
        print urldf.loc[indexs-1]['Request'] + ";"+ str(ords[num])+""
        #print urldf.loc[indexs-1]
#counting session in each cluster      

    #counting pages in each cluster and mapping page id to page URL in 'new_mapping.csv'    
def pageOldIDInCluster(cNum,dataFrame):
     out  = dataFrame.T
     ords = out.order(ascending=False).head(elementCount)
     #print "\n"+45*"="
     #print "clusterNo "+ str(cNum)+"\n"
     pids = ords.index.values
     #print ords
     xout =[]
     for num in range(0,len(pids)):    
        
        x = pids[num]
        #getting index in page count eg: 'p1'
        indexs =  int(x[1:])       
        #print "'"+str (newid_df.loc[indexs-1]['pageID'])+"'"
        xout.append(str (newid_df.loc[indexs-1]['pageID']))
        #print xout
     print "cluster"+ str(cNum)+" = "+ str(xout)   
def clusterCounter(gb):
    gbc = gb.count()
    print gbc['p1'].sort_index()
     
#end of methods

df = pd.read_csv(path+'cluster-group2.csv')
urldf = pd.read_csv(path+'new_mapping.csv')
newid_df = pd.read_csv(path+'new_id.csv')
gb = df.groupby('clusterNo')
clusterCounter(gb)

res = pd.concat([i[1].sum(numeric_only=True) for i in gb], axis=1).T

order = [i[0] for i in gb]

'''
group allpage for each clusters
writting it to csv to file '5-clusters_page_count.csv'
chartting also
'''
#print res
#res.to_csv(path+'5-clusters_page_count.csv',sep = ',', index=True)
#res.T.plot(kind='bar');
#plt.show()   


     
for num in range(0,len(res)-5):    
    pageCountInCluster(num,res.T[num])
    #pageOldIDInCluster(num,res.T[num])
    #print res
    #res.to_csv('pageCountfile',sep = ',', index=False)     
   # pageIdCountInCluster(num,res.T[num])
'''  
charting remove for temp  
out  = res.T[3]
out.columns = ['ColA']
#print out.order().rank(method='min')
ords = out.order(ascending=False).head(20)
myJSON = ords.to_json()
#print myJSON
res.T[2].plot()
#ords.plot(kind='bar');
plt.show()
#f.close();
'''