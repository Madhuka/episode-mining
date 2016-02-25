import re
import os
from collections import Counter
import json
import csv

regex = '(.*?)"(.*?)"(.*?)"(.*?)"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)\s/ (.*?)" (\d+) - "(.*?)" "(.*?)"'
#regex = '.*'

#buidlding string

count = 0
PageNo = 0
SEPS = ','
MAX_COUNT = 1000000;
SITE_NAME= 'nic';

print 'starting....'
input = []
output = ''
path = os.path.dirname(os.path.realpath(__file__))
new_path = path +'\\'+SITE_NAME

def create_drectory(directory):
    print directory
    if not os.path.exists(directory):
        os.makedirs(directory)

create_drectory(new_path+'\\')       
with open(path+"/log","r") as f:

	for line in f:
	       
		print line;
		match = re.match(regex, line)
		if match and int(count) < MAX_COUNT:
		  #print match.group(3).strip().split(' ')[0]=='200'
		  if (match.group(3).strip().split(' ')[0]=='200'):
		      print match.group(1)
		      output += line
		  r = match.group(2).split(SEPS)
		  v = Counter(r)
		  input +=[v]
                 # print str(match.group(1)) + str(v)
                  print len(r)
                  count +=1
                  '''
                  for rl in r:
                        
                        if PageNo == int(rl):
                            print 'x'
		  '''
print "Total session count: " + str(count)
print output
text_file = open(path+"/clean_log", "w")

text_file.write(output)
text_file.close()