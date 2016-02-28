#!/usr/bin/python   
#Author: Zach 
#Purpose: find each students most active posting hour.   

import sys
import csv 
import numpy as np

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
    hours = np.zeros(24)
    
    for line in reader:
        currentKey = line[0]  
        currentHour = line[1]
        
        if oldKey and oldKey != currentKey:
            #Method to select all max values found from jabaldonedo post at:
            #http://stackoverflow.com/questions/17568612/how-to-make-numpy-argmax-return-all-occurences-of-the-maximum
            #most_active = np.argwhere(hours == np.argmax(hours)).flatten().tolist()
            #print most_active
            #if len(most_active) > 1:
            #    for hour in most_active:
            #        writer.writerow([oldKey, hour])
                
            #else:
                #writer.writerow([oldKey,most_active[0]])
            most_active_hours = np.argsort(-hours)
            #print hours
            #print most_active_hours
            i = 0 
            while hours[np.argmax(hours)] == hours[most_active_hours[i]]:
                #print "{0}\t{1}".format(oldKey, most_active_hours[i])
                writer.writerow([oldKey,most_active_hours[i]])
                i += 1
            oldKey = currentKey
            hours = np.zeros(24)
    
        oldKey = currentKey
        hours[int(currentHour.replace('"',''))] += 1


    most_active_hours = np.argsort(-hours)
    i = 0 
    while hours[np.argmax(hours)] == hours[most_active_hours[i]]:
        #print "{0}\t{1}".format(oldKey, most_active_hours[i])
        writer.writerow([oldKey,most_active_hours[i]])
        i += 1
    #print "{0}\t{1}".format(oldKey, np.argmax(hours))
    #writer.writerow([oldKey,np.argmax(hours)])

if __name__ == "__main__":
    reducer() 
              