from __future__ import division
import os
import numpy as np
import operator
from nltk.tokenize import RegexpTokenizer

path = os.path.dirname(os.path.realpath(__file__))

print '===starting reading skip_pages ==='

regex=[];
 

def grouping_sessions(session,count):
    out_line = ''
    count = 1
    array = []
    count_array = []
    page_ids = []
    #print session
    for index, page in enumerate(session):
        
        if(index < len(session)-1):
            next  = session[index+1]
        if(page == next):
            count +=1
        else:
            #print count
            array.append(page+'['+str(count)+']')
            page_ids.append(page)
            count_array.append(count)
            count = 1
        if(index == len(session)-1):
            #print count-1
            array.append(page+'['+str(count-1)+']')
            page_ids.append(page)
            count_array.append(count-1)
            
    #print array
    #print page_ids
    #print count_array
    out_line = str(page_ids)+','+str(count_array)+','+str(count)+'\n'
    out_line = out_line.replace("[", '"').replace(']', '"')
    
    print out_line
    regex.append(out_line)
    
def page_sequences(file_name):
    global session_count, count
    with open(path+'/page_sequences/'+file_name+'.csv','r') as f:
                
   	for line in f:
   	    current_session = line.split('"')[1].replace(" ", "").split(',');
   	    current_session_count = line.split('"')[2].replace(", ", "");   	    
   	    #current_session = line.split('"')[1].replace(" ", "").split(',');
            grouping_sessions(current_session,current_session_count);
            
                    
def getKey(item):
   #print item.split('"')[1]
   return item.split('"')[1]        

def write_file(data_to_file,file_name):
    #print data_to_file
    data_to_file = sorted(data_to_file, key=getKey)
    str1 = ''.join(data_to_file)
    directory = path+"/page_sequences"
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory+"/"+file_name+".csv", "w")    
    f.write(str1)      # str() converts to string
    f.close()
    
def make_regex_level1(file_name,file_out):
    page_sequences(file_name)
    write_file(regex,file_out)

#main processing calling
make_regex_level1('skip_pages','skip_pages_regex_level_1');
make_regex_level1('without_skip_pages','without_skip_pages_regex_level_1');

print "===END==="
