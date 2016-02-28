#!/usr/bin/python  
#Author: Zach Farmer
#Purpose: Return Top 10 tags found in questions   

import sys
import csv 
#from collections import defaultdict 

def reducer(): 
    """
        paramters: sys.stdin from mapper_TopTags.py
        
        Output: Top ten tags from question nodes 
    """
    
    reader = csv.reader(sys.stdin, delimiter="\t")   
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar = '"',\
                        quoting=csv.QUOTE_ALL)  
    
    oldKey = None 
    count = 0 
    
    #tag_dict = defaultdict(int)
    topTen_tagDict = {}
    for line in reader:
    
        currentKey = line[0]   
        
        if oldKey and oldKey != currentKey:
            if len(topTen_tagDict.keys()) < 10:
                topTen_tagDict[oldKey] = count
                oldKey = currentKey
                count = 0 
            elif len(topTen_tagDict.keys()) >= 10:
                if count > min(topTen_tagDict.values()):
                    del topTen_tagDict[[k for k, v in topTen_tagDict.iteritems()\
                                         if v == min(topTen_tagDict.values())][0]]
                    topTen_tagDict[oldKey] = count 
                    oldKey = currentKey 
                    count = 0 
                else:
                    oldKey = currentKey
                    count = 0 
            #print "{0}\t{1}".format(count,oldKey)
            #count = 0
        
        oldKey = currentKey 
        count += 1
        
    if count > min(topTen_tagDict.values()):
        del topTen_tagDict[[k for k, v in topTen_tagDict.iteritems()\
                            if v == min(topTen_tagDict.values())][0]]
        topTen_tagDict[oldKey] = count   
        
    for key,count in sorted(topTen_tagDict.items(), key = lambda x: x[1], reverse=True):
        writer.writerow([key,count]) 
        
    #print "{0}\t{1}".format(count,oldKey)
        #tag_dict[currentKey] += 1
        
    #for key,count in sorted(tag_dict.items(), key = lambda x: x[1],reverse=True)[0:10]:
        #print "{0}\t{1}".format(key,count)
        #writer.writerow([count,key]) 
            
if __name__ == "__main__": 
    reducer()  
    
            
    