#!/usr/bin/python  
#Author: Zach Farmer  
#Purpose: Find potential study groups by measuring frequency of students post per question.  

import sys 
import csv  

def reducer(): 
    """
        parameter: sys.stdin from mapper_studyGroups.py
        
        output: sys.stdout .tsv lines containing the post node_id for the top level
        question and all the author_ids associated with post related to the question.
    """
    
    reader = csv.reader(sys.stdin, delimiter="\t")
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar='"',\
                        )   
    
    oldKey = None
    author_ids = []
    for line in reader:
        
        currentKey = line[0] 
        
        if oldKey and oldKey != currentKey: 
            writer.writerow([oldKey,author_ids])
            oldKey = currentKey
            author_ids = []
            
        oldKey = currentKey 
        author_ids.append(int(line[1]))
            
    writer.writerow([oldKey,author_ids])

if __name__ == "__main__": 
    reducer()  
        
    