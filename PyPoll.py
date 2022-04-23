
# The data we need to retrieve
# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the elction based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. initialze a total vote counter
total_votes = 0 

#candidate options and candidate votes
candidate_options = []

#declare the empty dictionary 
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #read the header row.
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader: 
        #2. Add the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options: 

            # add the candidate name to the candidate list
             candidate_options.append(candidate_name)

             #2a. begin tracking that candidate's vote count. 
             candidate_votes[candidate_name] = 0 

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# determine the percentage of votes for each candidate by looping through the counts. 

# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:

    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #print out each candidiate's name, vote count, and percentage
    # of  votes to the terminal 

      # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    
    

#to do: print out the winning candidate, vote count, and % to terminal

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
