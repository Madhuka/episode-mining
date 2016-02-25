"""
readdding access_log with skiping line and formatting access_log

"""
import re
import timeit
from collections import Counter
import os
import csv

#regex = '(.*? nic.lk) (.*?)"(.*?)(.*?)"(.*?)"(.*?)"(.*?)"'
regex = '(.*? nic.lk )(.*?)'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)\s/ (.*?)" (\d+) - "(.*?)" "(.*?)"'
#regex = '.*'
path = os.path.dirname(os.path.realpath(__file__))
#buidlding string

count = 0
PageNo = 0
SEPS = ','

print 'starting to read accesslog file....'
log_list = ""
with open(path+"/access_log","r") as f:

	for line in f :
	       
		#print line;
		match = re.match(regex, line)
		
		if match:
		    
		 # print "0 "+match.group(0)  
		 # print "1 "+match.group(1) 
		 # print "1 "+match.group(2) 
		 # print re.split(match.group(1), line)[1]
		  count +=1  
		  out = re.split(match.group(1), line)[1]
		  #print out+"iii"
		  log_list += str(out)
		  '''
		  print "2 "+match.group(2)
		  print "3 "+match.group(3)
		  print "4 "+match.group(4)
		  print "5 "+match.group(5)
		  print "6 "+match.group(6)
		  out = match.group(2)
		 # out += '"'
		  out += match.group(4)
		 # out += '"'
		  record = [""+match.group(2)+"\""+match.group(4)+"\""+match.group(5)+''+match.group(6)+''+match.group(7)+""]
                  count +=1
                  out = [out]
                  #record = 'www"'
                  log_list.append(out)
                  print count
                  '''
print "Total session count: " + str(count)
#print log_list

#writting to file 
fd = open(path+"/log", "w+") 
fd.write(log_list)
fd.close()

        #for row in log_list:
          #  print row
            
           # print row
           # row += count
            #count += 1
           # print row
