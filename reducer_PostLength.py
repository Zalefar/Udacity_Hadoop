#!/usr/bin/python  
#Author: Zach Farmer
#Purpose: Determine if correlation btw. post length and answers length.   

import sys
import csv 

def reducer(): 
    """
        paramters: sys.stdin from mapper_PostLength 
        
        Output: Post length of question and average post lenght of answers
        
    """
    
    reader = csv.reader(sys.stdin, delimiter="\t")   
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar = '"',\
                        quoting=csv.QUOTE_ALL)  
    
    oldKey = None
    q_post_len = 0.0
    answ_len = 0.0 
    count = 0
    
    for line in reader: 
        
        currentKey = line[0]
        node_type,post_length = line[1].split("-") 
        
        if oldKey and oldKey != currentKey:
            if count != 0:
                avg_answ_len = answ_len/float(count)
            else:
                avg_answ_len = 0
            writer.writerow([oldKey, q_post_len, avg_answ_len])
            oldKey = currentKey
            answ_len = 0.0
            count = 0
        
        oldKey = currentKey
        
        if node_type == "Q":
            q_post_len = int(post_length.replace('"',''))
        elif node_type == "A":
            answ_len += int(post_length.replace('"',''))
            count += 1
    
    if count != 0:
        avg_answ_len = answ_len/float(count)
    else:
        avg_answ_len = 0
    writer.writerow([oldKey,q_post_len, avg_answ_len])
        
if __name__ == "__main__":
    reducer()   
    