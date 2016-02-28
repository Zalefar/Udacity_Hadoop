#!/usr/bin/python  
#Author: Zach Farmer
#Purpose: Return Top 10 tags found in questions 

import sys
import csv    

def mapper():   
    """
        Parameter: sys.stdin from forum_node.tsv or test file.
        
        Output: tab deliniated csv lines for input to reducer_TopTags.py
    """
    
    reader = csv.reader(sys.stdin, delimiter="\t")   
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar = '"',\
                        quoting=csv.QUOTE_ALL)  
    
    for line in reader:
        
        node_id = line[0]
        node_type = line[5]     
        tags = line[2].split(" ")      
        
        if node_type == "question":
            for tag in tags:
                #print "{0}\t{1}".format(line[0],tag)
                writer.writerow([tag,line[0]])
            
        
if __name__ == "__main__":
    mapper() 
    