#Udacity Intro to Hadoop and MapReduce Final Project   
###Zach Famer  
**** 
The purpose of this project was to analyze Udacity Forum data in order to explore MapReduce design patterns and structures. Filter, Summarization and Structural patterns were explored and implemented in order to answer a series of questions about the dataset.    


`Hadoop_Final_Project.ipynb` :       
* Contains the project in entirety.      
`forum_data.tar.gz`:     
* Contains the forum data files      
`student_test_posts.csv`:     
* Contains a small test dataset used in construction of mappers and reducers. 
Following .py files are all the mappers and reducers created in the pursuit of this project. These scripts can be exported to a Hadoop distributed file system and run on the datasets contained in the forum_data tar file.  
* `mapper_TopTags.py`     
* `reducer_TopTags.py`     
* `mapper_PostLength.py`      
* `reducer_PostLength.py`      
* `mapper_studentTime.py`    
* `reducer_studentTime_sansNumpy.py`    
* `reducer_studentTime.py`     
* `mapper_studyGroups.py`    
* `reducer_studyGroups.py`     

