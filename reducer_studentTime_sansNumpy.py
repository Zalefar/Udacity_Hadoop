#!/usr/bin/python   
#Author: Zach 
#Purpose: find each students most active posting hour.   

import sys
import csv 
#import numpy as np

def reducer():
    """
        paramters: sys.stdin from mapper_studentTime 
        
        Output: Author_id followed by the hour were the id was most
        active.   
    """
    reader = csv.reader(sys.stdin, delimiter="\t")   
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar = '"',\
                        quoting=csv.QUOTE_ALL)  
    
    oldKey = None
    hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    for line in reader:
        currentKey = line[0]  
        currentHour = line[1]
        
        if oldKey and oldKey != currentKey:
            
            most_active_hours = [(hour_count,idx) for idx,hour_count in enumerate(hours)]
            most_active_hours.sort(key = lambda x: x[0], reverse=True) 
            
            i = 0 
            while sorted(hours,reverse=True)[0] == most_active_hours[i][0]:
                #print "{0}\t{1}".format(oldKey,most_active_hours[i][1])
                writer.writerow([oldKey,most_active_hours[i][1]])
                i += 1
            oldKey = currentKey
            hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
        oldKey = currentKey
        hours[int(currentHour.replace('"',''))] += 1


    active_hours = [(hour,count) for count,hour in enumerate(hours)]
    active_hours.sort(key = lambda x: x[0], reverse= True)
    i = 0
    while sorted(hours,reverse=True)[0] == active_hours[i][0]:
        #print "{0}\t{1}".format(oldKey,active_hours[i][1])
        writer.writerow([oldKey,active_hours[i][1]])
        i += 1

if __name__ == "__main__":
    reducer() 
              
