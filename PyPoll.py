# -*- coding: UTF-8 -*-
'PyPoll Program'

# Add our dependencies.
import csv
import os

# Load our data file.
election_results = os.path.join('resources','election_results.csv')

# Write our results.
election_analysis = os.path.join('analysis','election_analysis.txt')

# Track the total votes.
total_votes = 0

# Track votes for each candidate.
candidates = []
candidate_votes = {}

# Track the votes for each county.
counties = []
county_votes = {}

# Track the winning candidate.
winner = ''
winning_count = 0
winning_pct = 0

# Track the county with the greatest voter turnout.
greatest_county = ''
greatest_county_turnout = 0

# Lil space (everyone needs it.)
spacer = '-------------------------'

# Open, read, and analyze our data file.
with open(election_results) as election_data:
    file_reader = csv.reader(election_data)

    # Skip the header.
    header = next(file_reader)

    # Read our data file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Extract the candidate names.
        candidate = row[2]

        # Extract the county names.
        county = row[1]

        # Add each candidate name to our candidate list.
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        # Tally the votes for each candidate.
        candidate_votes[candidate] += 1

        # Add each county name to our county list.
        if county not in counties:
            counties.append(county)
            county_votes[county] = 0
        
        # Tally the votes for each county.
        county_votes[county] += 1

with open(election_analysis,'w') as output:
    
    # Print the total votes cast.
    election_results = (
        f'\nElection Results\n'
        f'{spacer}\n'
        f'There were {total_votes:,} total votes cast in the election.'
        )

    print(election_results)
    output.write(f'{election_results}\n')

    # Lil space (everyone needs it.)
    print(spacer)
    output.write(f'{spacer}\n')

    # The percentage of the total vote & the total votes for each county.
    for county in county_votes:
        votes = county_votes[county]
        vote_pct = votes / total_votes * 100
        county_summary = (f'{county} county accounted for {vote_pct:.1f}% of the total vote and contributed {votes:,} total votes.')

        print(county_summary)
        output.write(f'{county_summary}\n')

        if votes > greatest_county_turnout:
            greatest_county_turnout = votes
            greatest_county = county

    # Lil space (everyone needs it.)
    print(spacer)
    output.write(f'{spacer}\n')

    county_summary = (f'{greatest_county} county had the greatest voter turnout.')
    print(county_summary)
    output.write(f'{county_summary}\n')

    # Lil space (everyone needs it.)
    print(spacer)
    output.write(f'{spacer}\n')

    # List each candidate in this election.
    candidate_count = (f'There are {len(candidates)} candidates in this election.\n')
    print(candidate_count)
    output.write(f'{candidate_count}\n')

    for candidate in candidates:
        print(candidate)
        output.write(f'{candidate}\n')

    # Lil space (everyone needs it.)
    print(spacer)
    output.write(f'{spacer}\n')

    # The percentage of the popular vote & the total votes for each candidate.
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_pct = votes / total_votes * 100
        candidate_summary = (f'{candidate} received {vote_pct:.1f}% of the popular vote and {votes:,} total votes.')

        print(candidate_summary)
        output.write(f'{candidate_summary}\n')

        # Picking a winner.
        if votes > winning_count and vote_pct > winning_pct:
            winner = candidate
            winning_count = votes
            winning_pct = vote_pct

    # And the winner is!
    winner_summary = (
        f'{spacer}\n'
        f'The winner of the election is {winner}.\n'
        f'{winner} got {winning_count:,} total votes.\n'
        f'{winner} got {winning_pct:.1f}% of the popular vote.'
        )

    print(f'{winner_summary}\n')
    output.write(f'{winner_summary}')