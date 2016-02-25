from __future__ import division
import re
import os
import linecache
import operator
from nltk.tokenize import RegexpTokenizer

path = os.path.dirname(os.path.realpath(__file__))

print '===starting==='
#regex for detect the pages ids 
regex = '(.*?)"(.*?)"'
count = 1
session_count = 0
non_list = 0;
#PageNo = 0
SEPS = ','
lenl = range(2,8)
cluster_list = range(10,11)
all_session = True
avg_length = 100000; 

ngrams_statistics = {}
ngrams_statistics_sorted_length = 100
#count ngrams in sessions (sessions, length for ngram)
def count_ngrams(sessions,length):
    data = sessions
    data = data.replace(',',' ')
    

    tokenizer = RegexpTokenizer("[0-9]+")
    #include only number (pageIDs) for tokens
    token = tokenizer.tokenize(data)
    from nltk.util import ngrams
    #print list(ngrams(token, 2))

    generated_ngrams = list(ngrams(token,length))
    #print generated_ngrams
    try:
        ngrams = ' '.join(generated_ngrams[0])
    except IndexError:
        global non_list 
        non_list += 1
        #print 'Failed generated ngrams as there is no minimum '    
   # print ngrams
 
    for ngram in generated_ngrams:
        if not ngrams_statistics.has_key(ngram):
            ngrams_statistics.update({ngram:1})
        else:
            ngram_occurrences = ngrams_statistics[ngram]
            ngrams_statistics.update({ngram:ngram_occurrences+1})      

def read_sessions(length_ngram,clusterNo):
    global session_count, count
    with open(path+"/sessionsfile","r") as f:
    
            
   	for line in f:
    	       
  		#print 'line';
  		match = re.match(regex, line)
  		if match:
    		  if all_session:
    		          #print length_ngram
        		  data_s=match.group(2)
        		  count_ngrams(data_s,length_ngram)
        		  session_count +=1
    		  else:
    		  #print str(linecache.getline('D:/Research/Data/run03-epd/cluster-group.csv', count).split(",")[100])=="cluster4\n"
    		         
        		 if str(linecache.getline(path+'/cluster-group.csv', count).split(",")[100])=="cluster"+str(clusterNo)+"\n":
        		      #print linecache.getline('D:/Research/Data/run03-epd/cluster-group.csv', count).split(",")[100]
        		      data_s=match.group(2)
        		      #print length_ngram
        		      '''making for specific reason'''
        		      if len(data_s)<avg_length:
        		          print data_s
        		          count_ngrams(data_s,length_ngram)    		      
        		          session_count +=1
        		      '''end making for specific reason
        		      
        		      count_ngrams(data_s,length_ngram)    		      
        		      session_count +=1
        		      '''
        		      
     		     
                  count +=1
    
    #print ngrams_statistics
    ngrams_statistics_sorted = sorted(ngrams_statistics.iteritems(),key=operator.itemgetter(0),reverse=True)
    #print ngrams_statistics_sorted
    #print ngrams_statistics_sorted[:2]

    global non_list
    
    #print str(session_count-non_list)
    
    show_details(length_ngram)
    show_ngrams_statistics(ngrams_statistics_sorted)
    #show_ngrams_statistics(ngrams_statistics)
    write_file(ngrams_statistics_sorted)
    '''
    if(length_ngram == 9):
        show_ngrams_statistics(ngrams_statistics_sorted)
    '''
    #show_precentages()
    session_count = 0
    non_list = 0
    count = 1

def show_precentages():
    a = (((session_count-non_list)/session_count)*100)
    print("%.2f" % a)
    
def show_details(length_ngram):
    print "=== ngram "+str(length_ngram)+"==="
    print "Total Session Count: " +str(session_count)
    print "Found ngrams: " +str(session_count-non_list)
    #print str(length_ngram) +","+str(session_count) + ","+str(session_count-non_list)
    
def show_ngrams_statistics(ngrams_statistics_sortedx):    
    print ngrams_statistics_sortedx[:ngrams_statistics_sorted_length]
    #print ngrams_statistics_sortedx
    
def write_file(data_to_file):
    #with open('D:/Research/Data/run03-epd/mostcommon.csv', 'wb') as f1:
    f = open(path+"/Page Collocation Full (len "+ str(lenl[0])+").csv", "w")
    file_str_out = str(data_to_file[:1000]);
    file_str_out = file_str_out.replace("'),", "') ,")
    file_str_out = file_str_out.replace("),", "\n")
    file_str_out = file_str_out.replace("', '", " , ")
    file_str_out = file_str_out.replace(")]", "")
    file_str_out = file_str_out.replace("[(('", "\"") 
    file_str_out = file_str_out.replace(" (('", "\"")
    file_str_out = file_str_out.replace("') ,", "\",")
    
    f.write(file_str_out)      # str() converts to string
    f.close()
    
def run_nagram_loop(clusterNo):
    for length_ngram in lenl:
        #global ngrams_statistics
        #ngrams_statistics = {}
        read_sessions(length_ngram,clusterNo)

if all_session:  
    print "===All Sessions==="
    #ngrams_statistics = {}
    run_nagram_loop(0)
else:    
    for clusterNo in cluster_list:
        print "===cluster No"+ str(clusterNo)+"==="
        ngrams_statistics = {}
        run_nagram_loop(clusterNo)     
#print linecache.getline('D:/Research/Data/run03-epd/cluster-group.csv', 1)

#reseting count
print "===END==="
