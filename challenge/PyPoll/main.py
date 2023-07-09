import csv


file_path = "C:/Users/alexu/Desktop/challenge/PyPoll/Resources/election_data.csv"


total_votes = 0
candidates = {}
winner = ""


with open(file_path , newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

    for row in csvreader:
        
        total_votes += 1

        
        candidate_name = row[2]

        
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        
        else:
            candidates[candidate_name] += 1

max_votes = max(candidates.values())
for candidate, votes in candidates.items():
    if votes == max_votes:
        winner = candidate

percentages = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percentages[candidate] = round(percentage, 3)


analysis_results = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
]

for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    analysis_results.append(f"{candidate}: {percentage}% ({votes})")

analysis_results.extend([
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------",
])


for result in analysis_results:
    print(result)


output_file = r"C:\Users\alexu\Desktop\challenge\PyPoll\analysis\election_analysis.txt"
with open(output_file, "w") as txtfile:
    for result in analysis_results:
        txtfile.write(result + "\n")

print(f"\nAnalysis results have been exported to '{output_file}'.")