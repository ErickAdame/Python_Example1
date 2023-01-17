#!/usr/bin/env python
# coding: utf-8

# In[70]:


import csv
import os

file_input = os.path.join(".", "Resources", "election_data.csv")
file_output = os.path.join(".", "Analysis", "data_analysis.txt")



# In[71]:


total_votes = 0
winner_votes = 0
winner_name = ""
candidate_list = []
candidate_dictionary = {}


# In[72]:


with open(file_input) as election_data:

    csvreader = csv.reader(election_data)
    
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_dictionary[candidate_name] = 0
        
        candidate_dictionary[candidate_name] += 1
    


# In[78]:


with open(file_output, "w") as election_analysis:
    election_part1 = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_part1)
    
    election_analysis.write(election_part1)
    
    for candidate,votes in candidate_dictionary.items():
        percentage_votes = votes/total_votes * 100
        
        
        election_part2 = (
        f"{candidate}: {round(percentage_votes, ndigits=3)}% ({votes})\n"
        )
        print(election_part2)
        election_analysis.write(election_part2)
        
    
        if (votes > winner_votes):
            winner_votes = votes
            winner_name = candidate
            
    election_part3 = (   
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")
    print(election_part3)
    
    election_analysis.write(election_part3)
            
        
        #election_analysis.write(f"{candidate}: {percentage_votes}% ({votes})")
        
     


# In[ ]:





# In[ ]:





# In[68]:





# In[69]:





# In[ ]:




