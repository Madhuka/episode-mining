from __future__ import division
import os
import numpy as np
import operator
import string
from itertools import chain
from nltk.tokenize import RegexpTokenizer

path = os.path.dirname(os.path.realpath(__file__))

print '===starting regex level two ==='

regex=[];
s_array = []
c_array = []
final_c_array = []
cx_array = []
 
def fetch_data(*args):    
    out  = map(list, zip(*args))
    #print out
    out_list =[]
    for pagecount in out:
        c = list(set(pagecount))
        out_list.append(c)
    return out_list
    
def make_stringline_regex(page, list_count):  
    out_str = ''
    if (len(list_count)==1):
        
        if (list_count[0]!=1):
         out_str += page+str(list_count)
        if (list_count[0]==1):
         out_str += page
    else:
        str_count = ''
       # for index, count in enumerate(list_count):  
        out_str += page + str([list_count[0],list_count[len(list_count)-1]])
    #print out_str
    return out_str.replace(",",":")
    
def make_string_regex(list_s, list_count):  
    for index, session in enumerate(list_s):     
        out_str = ''
        for sec_index, pageId in enumerate(session): 
            #print pageId
            count_list = list_count[index][sec_index]
            out_str = out_str + make_stringline_regex(pageId,count_list)+', '
        print out_str[:-2]
    
def page_regex_1(file_name):    
    with open(path+'/page_sequences/'+file_name+'.csv','r') as f:

   	for index, line in enumerate(f):
   	    #print index
   	    current_line = line
            trans = string.maketrans("\"' \n","    ")
            #removing unwanted characters and getting session
            s_line = line.split('","')[0].translate(trans) 
            c_line = line.split('","')[1].translate(trans)              
   	    current_session = s_line.replace(" ", "").split(',')
   	    current_session_count = c_line.replace(" ", "").split(',')
   	    #convert string list for number
   	    current_session_count = map(int, current_session_count)
   	    #checking is there any element in session list
   	    if len(s_array)>0:
   	        #is the same session 
           	if (current_session == s_array[-1]):
           	    #print 'same...'
           	    #print c_array[-1]
           	    #print current_session_count
           	    cx_array.append(current_session_count)
           	    #make_count_list (c_array[-1],current_session_count)
           	    #c_array[-1] = make_count_list (c_array[-1],current_session_count)
           	else:
           	    s_array.append(current_session)
           	    c_array.append(current_session_count)
           	    #print cx_array
           	    #print fetch_data(*cx_array)
           	    final_c_array.append(fetch_data(*cx_array))
           	    del cx_array[:]
           	    cx_array.append(current_session_count)
            else:
                s_array.append(current_session)
                c_array.append(current_session_count)
                cx_array.append(current_session_count)

    final_c_array.append(fetch_data(*cx_array))
    #print s_array
    #print c_array
    #print final_c_array
   	    
            
                    
def getKey(item):
   print item.split('"')[1]
   return item.split('"')[1]        


    
def make_regex_level1(file_name,file_out):
    page_regex_1(file_name)
    #write_file(regex,file_out)

#main processing calling
#make_regex_level1('skip_pages_regex_level_1','x');
make_regex_level1('without_skip_pages_regex_level_1','x');

make_string_regex(s_array,final_c_array)

#print s_array
#print final_c_array
print "===END==="
