import re
import timeit
from collections import Counter
import os
import csv

regex = '(.*?)"(.*?)"'
regex_any = '(.*?)'
session_regex_start = regex_any
session_regex_middle = '0,72,72' 
page_seperater = ','
session_regex_end = regex_any
session_regex = session_regex_start + session_regex_middle + session_regex_end


count = 0
SEPS = ','
path = os.path.dirname(os.path.realpath(__file__))

print 'starting reading sessions_file_1.1....'
input = []

def display(session_regex,session_count,session_list):
    print ('session count : ' + str(session_count))
    print ('regex : ' + str(session_regex))
    print ('session_list : ' + str(session_list))

def loop_sessions_file(session_regex_start,new_session_regex_middle,session_regex_end):
    session_regex = session_regex_start + new_session_regex_middle + session_regex_end    
    with open(path+"/sessions_file_1.1","r") as f:
        session_list = []
        session_count = 0
        for line in f:
    	       
  		#print line;
  		match = re.match(regex, line)
  		if match and int(count) < 10000:
    		  current_session = match.group(2).replace(" ", "")
    		  session_no = match.group(1)
    		  session_match = re.match(session_regex, current_session)
    		  if session_match:
    		      session_count +=1
    		      session_list.append(session_no[:-1])
    		      #print session_count

        display(session_regex,session_count,session_list)
        
def loop_collocation_file():
    ngram_regex = '"(.*?)",(.*?)'     
    with open(path+"/Page Collocation Full (len 2).csv","r") as f:
        for line in f:            
            match = re.match(ngram_regex, line)
            if match:
                #print('found n-grams')
                ngram = match.group(1).strip().replace(" ", "")
                print (ngram)
                loop_sessions_file(regex_any,ngram,'')
                
loop_collocation_file()            
