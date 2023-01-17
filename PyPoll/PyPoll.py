#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os

#data input and output, source and destination 
file_input = os.path.join(".", "Resources", "election_data.csv")
file_output = os.path.join(".", "Analysis", "data_analysis.txt")



# In[2]:


#Declared variables set to ZERO, empty string, empty list and empty dictionary - to start
total_votes = 0
winner_votes = 0
winner_name = ""
candidate_list = []
candidate_dictionary = {}


# In[3]:


#Open data file
with open(file_input) as election_data:
#Read the data which is in csv file
    csvreader = csv.reader(election_data)
    #Pull out the header, Also skips the header row. Rest of rows are data
    header = next(csvreader)
    
    #Since remaining rows are each votes, total rows = total number of votes
    for row in csvreader:
        total_votes += 1
        
        #In the CSV, candidate names are located in Index 2, third column 
        #This line of code will extract a candidate name for each row
        candidate_name = row[2]
        
        #Logic to collect unique candidate name and add to list of candidates
        #Also building a dictionary where candidate is key, value is votes starting at ZERO
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_dictionary[candidate_name] = 0
        
        #If candidate name is already in the dictionary, this tallys the votes per candidate
        candidate_dictionary[candidate_name] += 1
    


# In[4]:



#Output data to text file
with open(file_output, "w") as election_analysis:
    #This is the output of the first part of desired results
    election_part1 = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    #Print part 1 of 3 of analysis/results.
    print(election_part1)
    
    #Writes part 1 of analysis to text output file
    election_analysis.write(election_part1)
    
    #Using dictionary, this code finds candidate as key and associated total votes
    for candidate,votes in candidate_dictionary.items():
        #Simple percentage calculation
        percentage_votes = votes/total_votes * 100
        
        #Assembling part 2 of 3 of election results: Candidates, percentage votes, votes
        election_part2 = (
        f"{candidate}: {round(percentage_votes, ndigits=3)}% ({votes})\n"
        ) #Rounding function used to round percentage to 3 decimals
        
        #Prints out results Part 2
        print(election_part2)
        #Outputs analysis to text file
        election_analysis.write(election_part2)
        
        #Finds the candidate with most votes in the dictionary and declares winner
        if (votes > winner_votes):
            winner_votes = votes
            winner_name = candidate
    
    #Part 3 of 3 of election results declares the winner
    election_part3 = (   
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")
    #Print Winner
    print(election_part3)
    
    #Write/Output part 3 of results, the winner, to the text file
    election_analysis.write(election_part3)
            
        
     


# In[ ]:




