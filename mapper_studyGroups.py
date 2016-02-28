#!/usr/bin/python  
#Author: Zach Farmer  
#Purpose: Find potential study groups by measuring frequency of students post per question.  

import sys 
import csv   

def mapper():
    """
        parameter: sys.stdin from fourm_node.tsv or the sample test file student_tests_post.tsv
        
        output: sys.stdout .tsv lines containing the post node_id and the author_ids 
        of the question node and each child answer and comment post. Will include duplicate 
        author_id's if author posted more then once.
    """
    
    reader = csv.reader(sys.stdin, delimiter="\t")
    writer = csv.writer(sys.stdout, delimiter="\t", quotechar='"',\
                        quoting = csv.QUOTE_ALL)   
    
    for line in reader:
        
        node_id = line[0]
        node_type = line[5]  
        author_id = line[3] 
        abs_parent_id = line[7]
        
        
        if node_type == "question":
            writer.writerow([node_id,author_id])
        elif node_type == "answer" or node_type == "comment":
            writer.writerow([abs_parent_id, author_id])

if __name__ == "__main__":
    mapper()   