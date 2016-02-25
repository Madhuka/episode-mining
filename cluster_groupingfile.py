'''
Page IDs for cluster 13 (old IDs)
6686,/form.php
6711,/form_mail.php
8302,/index.php/2013-09-08-16-33-46
13571,/infopayments.php
14043,/lksearch.php
'''
'''
using file open for mapping new id to older page ids (urls)
'''

import re

currentCluster = ['1028','18763']

cluster0 = ['1', '14043', '6686', '8302', '12681']
cluster1 = ['13571', '1', '17511', '14043', '8318']
cluster2 = ['1', '14043', '8298', '8302', '10447']
#cluster3 = ['17182', '1', '8522', '7826', '10402']
cluster3 = ['17182', '1','8522']
cluster4 = ['1', '14043', '8298', '8302', '8318']
cluster5 = ['14043', '6686', '1', '6711', '8298']
cluster6 = ['1', '18607', '6605', '17182', '9218']
cluster7 = ['1', '14043', '6686', '8298', '8302']
cluster8 = ['1', '14043', '8318', '8302', '13571']
#cluster9 = ['1', '10407', '12796', '12346', '12794']
cluster9 = ['1', '10407']
#cluster10 = ['17182', '1', '8013', '10376', '10341']
cluster10 = ['17182', '1', '8013']
#cluster11 = ['1', '7826', '14043', '6686', '6711']
cluster11 = ['1', '7826', '14043', '6686']
#cluster12 = ['8013', '14043', '1', '10343', '17511']
cluster12 = ['8013', '14043', '1', '10343']
cluster13 = ['1', '14043', '6686', '6711', '8013']
#cluster14 = ['1028', '18763', '9382', '12794', '9383']
cluster14 = ['1028', '18763']



currentCluster = cluster1


#weka arff header buidling 
def headerBuilder():
    print "% session clustering\n% Madhuka Udantha \n% t1,t2,t3,t4,t5\n%\n\n@relation log-monitoring "
    labels = str(currentCluster)[1:-1]
    print "@attribute t1 {"+labels+"}"
    print "@attribute t2 {"+labels+"}"
    print "@attribute t3 {"+labels+"}"
    print "@attribute t4 {"+labels+"}"
    print "@attribute t5 {"+labels+"}"
    print "@data"
Clen = len(currentCluster)
headerBuilder()
#currentCluster = ['1', '14043', '6686', '3745']
out = []
regex = '(.*?)"(.*?)"'
with open("D:/Research/Data/run03/sessionsfile","r") as f:

	for line in f :
	       
		#print line;
		match = re.match(regex, line)
		
		if match:
		    
		    out = match.group(2).split(',')
		    #print out
		    b3 = set(out).intersection(currentCluster)
		    #print b3
                    if len(b3)>int (Clen-1) :
                        #print str(b3)  +" -->"+ match.group(1)
                        d = {}
                        #print full page seques 
                        for num in range(0,len(currentCluster)):
                            #print out.index(currentCluster[num])
                            d[currentCluster[num]] = out.index(currentCluster[num])
                            #print out
                        #print d
                        #print sorted(d.values())
                        print str(sorted(d, key=d.get))[1:-1]
                        #place page is ocured
                        #print sorted(d.items(), key=lambda x:x[1])

