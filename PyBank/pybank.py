#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Dependecies
import os
import csv


# In[20]:


#paths for input and output files

file_input = os.path.join(".", "Resources", "budget_data.csv")
file_output = os.path.join(".", "Analysis", "budget_analysis.txt")


# In[21]:



# Setting count to ZERO to begin with    
total_months = 0
total_net = 0


net_change_list = []
   


#Use this list to calculate the max and min and compare with IF statements    
greatest = ["",0]
smallest = ["", 999999999999999999]
 
#Read CSV file    
with open(file_input) as budget_data:

    reader = csv.reader(budget_data)
    
    #Reading/skipping over header, stored as variable.
    header = next(reader)
   
    first_row = next(reader)
    
    
    #First row plus net to calculate NEXT
    total_net += int(first_row[1])

    #Keeping track of previous to eventually find MAX or MIN
    previous_net = int(first_row[1])

    
    
    #loop through csv
    for row in reader:
        
        #Finding total months
        total_months = total_months +1
       
        #Finding total net
        total_net += int(row[1])
        
        #tracking change month to month
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        
        
        #Greatest Montly Change Calculation
        #For Greatest and Smallest I reference list created above
        #Greatest: to start, is net_change bigger than ZERO? YES.
        #Is next net change bigger previous 'greatest'? if so, its greatest
        #Loops done for all rows for both greatest and smallest
        if(net_change > greatest[1]): 
            greatest[0] = row[0]
            greatest[1] = net_change
        #smallest Montly Change Calculation    
        if(net_change < smallest[1]):
            smallest[0] = row[0]
            smallest[1] = net_change
        
        #Calculate of month average, SUM of the list /Number in the list
    net_monthly_average = sum(net_change_list)/(len(net_change_list)) 
output =  (
    #Summary Analysis Prints
    f"Financial Analysis\n"
    f"--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_net}\n"
    f"Average Change: {net_monthly_average: .2f}\n" #Cool trick: '.2f' formats two decimals
    f"Greatest Increase in profits: {greatest[0]} $({greatest[1]})\n"
    f"Greatest Decrease in profits: {smallest[0]} $({smallest[1]})"
)
#Write the results to output file as a text file in the Analysis Folder pointed to at top of code
with open(file_output, "w") as text_file:
    text_file.write(output)
print(output)






