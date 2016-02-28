#!/usr/bin/python 
#Author: Zach Farmer
#Purpose: determine if correlation btw. post length and answers length.   

import sys
import csv 

def mapper():
    """
        paramters: sys.stdin from forum_node.tsv or small test dataset 
        
        Output: Either node_id if node_type question or abs_parent_id if
        node_type answer as keys and the length of the body for values.
    """
    
    reader = csv.reader(sys.stdin, delimiter="\t")   
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar = '"',\
                        quoting=csv.QUOTE_ALL)  
    
    for line in reader:
        
        node_type = line[5] 
        body_len = len(line[4]) 
        
        if node_type == "question":
            writer.writerow([line[0],"Q-"+str(body_len)])
        elif node_type == "answer":
            writer.writerow([line[7],"A-"+str(body_len)])
    
        
if __name__=="__main__":
    mapper()