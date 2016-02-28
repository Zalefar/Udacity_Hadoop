#!/usr/bin/python 
#Author: Zach Farmer
#Purpose: find each students most active posting hour.  

import sys
import csv 
from datetime import datetime  

def mapper():
    
    reader = csv.reader(sys.stdin, delimiter="\t") 
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar = '"',\
                        quoting=csv.QUOTE_ALL)  
    
    for line in reader: 
        
        
        author_id = line[3]
        #                     %Y   %m     %d   %H     %M     %S          %f            %z                  
        #data[0] Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
        #print line[8].split("+")[0]
        if line[8] != "added_at":
            time = line[8].split("+")[0]
            hour = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f").hour
            writer.writerow([author_id,hour])
        
if __name__ == "__main__":
    mapper()