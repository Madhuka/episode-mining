from __future__ import division
import os
import numpy as np
import operator
from nltk.tokenize import RegexpTokenizer

path = os.path.dirname(os.path.realpath(__file__))

print '===starting reading page_sequences file==='
#add skip pages ids
skip_pages = ['0','145']

array_with_skip_pages=[];
array_without_skip_pages=[]; 

def read_sessions():
    global session_count, count
    with open(path+"/page_sequences.csv","r") as f:
    
            
   	for line in f:
   	        line_added = False;
    	        current_session = line.split('"')[1].replace(" ", "").split(',');
    	        current_session_count = line.split('",')[1].split('\n')[0].replace(" ", "")
  		#print current_session;  
  		#print current_session_count
  		tmp_array = np.in1d(current_session,skip_pages)
  		for item in tmp_array:
  		    if ((item == False) & (current_session_count != '1')):
  		        array_without_skip_pages.append(line)
  		        line_added = True
  		        break
  		if( (line_added == False) & (current_session_count != '1')):      
                    array_with_skip_pages.append(line)
                
def write_file(data_to_file,file_name):
    str1 = ''.join(data_to_file)
    #with open('D:/Research/Data/run03-epd/mostcommon.csv', 'wb') as f1:
    directory = path+"/page_sequences"
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory+"/"+file_name+".csv", "w")    
    f.write(str1)      # str() converts to string
    f.close()
    
read_sessions()


#used in sorting the list 
def getKey(item):
   print item.split('"')[1]
   return item.split('"')[1]

#sorting the lists   
sorted_array_without_skip_pages = sorted(array_without_skip_pages, key=getKey)
sorted_array_with_skip_pages = sorted(array_with_skip_pages, key=getKey)

write_file(sorted_array_with_skip_pages,'skip_pages')
write_file(sorted_array_without_skip_pages,'without_skip_pages')
#reseting count
print "===END==="
