# election_analysis

## Overview of Election Audit

*Purpose*

An employee, Tom, of the Colorado Board of Elections needs some help with an election audit of the tabulated results of a Colorado precinct. Factors such as: total number of votes cast, total number of votes for each candidate, percentage of votes for each candidate, and the winner of the election will need to be produced from the provided election data. The products of the elections analysis will certify this US Congressional race. 

*Resources* 

1. Data Source: election_results.csv
2. Software: Python 3.7.6; Visual Studio Code 1.50.0 

## Election-Audit Results: 

**- How many votes were cast in this congressional election?**

This congressional election had a total number of 369,711 votes cast. 

[Total Votes Cast](https://user-images.githubusercontent.com/102566199/164950630-c2ba12c5-b76d-4cc4-ada5-0234bed11619.png)

**- County Breakdown: number of votes and percentage of total votes**

    - Jefferson: 38,855 votes cast (10.5% of the total votes)
    
    - Denver: 306,055 votes cast (82.8& of the total votes)
    
    - Arapahoe: 24,801 votes cast (6.7% of the total votes)
    
[Votes by County](https://user-images.githubusercontent.com/102566199/164950769-5e97c7b1-1a2a-42a9-8f8e-7c54ed554aa7.png)

**- Which county had the largest number of votes?**

Denver had the highest number of votes with 306,055 votes cast, which was 83% of the total votes amount.

[Denver's Votes](https://user-images.githubusercontent.com/102566199/164950805-dde2bcf7-8500-4ae0-ad15-29e9ebf2420c.png)

**- Candidate Breakdown: number of votes received and percentage of total votes**

       *Charles Casper Stockham*: recevied 23% of the total votes, earning 85,213 votes.
       
       *Diana DeGette*: received 73.8% of the total votes, earning 272,892 votes
       
       *Raymon Anthony Doane* received 3.1% of the total votes, earning only 11,606 votes.
       
[Pencentage of Votes Received](https://user-images.githubusercontent.com/102566199/164950692-de586a14-66f8-42ab-bbc7-2857d6d3e8e0.png)

**- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**

Diana DeGette won the election! They earned 272,892 votes, which was 73.8% of the total vote amount. 

## Election-Audit Summary: 

*Business Proposal*

The script that was written for the election audit can easily be modified to make it versatile. The script has enough the potential to be used for any election. There are simple tweaks to the code that would allow for this. Assuming that we use a similar format of receiving election data in a csv file, some changes that could be made to the Python script are to change the values that specify the region that the votes are being collected from. Changing the following code to instead be for states would allow it to be used for other areas. County could be changed to state, depending on the election location. 

`county_options = []
county_votes = {}`

Additional code could also be added to the script to pull into different voter parties. This could help in the presidential elections because the party system is an important way that many votes are differentiated. This could be done by creating more values to assign information to. Similar to the following code, a dictionary could store a candidate's part affiliation; instead of just the votes associated with the candidate. 

`candidate_options = []
candidate_votes = {}`

This script could bring in multiple classes of candidates as well, if the data was provided, to be able to determine the winning candidates for multiple positions. The reason it is so flexible is the use of assigned variables. Changing these allows it to be morphed to be used in many ways. 
