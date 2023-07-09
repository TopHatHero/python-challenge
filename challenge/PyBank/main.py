import csv



file_path = "C:/Users/alexu/Desktop/challenge/PyBank/Resources/budget_data.csv"

total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        total_months += 1

        total_profit_losses += int(row[1])

        change = int(row[1]) - previous_profit_loss
        changes.append(change)
        previous_profit_loss = int(row[1])

        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change

        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

average_change = sum(changes) / len(changes)

analysis_results = [
    "Financial Analysis",
    "------------------",
    f"Total Months: {total_months}",
    f"Total: ${total_profit_losses}",
    f"Average Change: ${round(average_change, 2)}",
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
]

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

output_file = r"C:\Users\alexu\Desktop\challenge\PyBank\analysis\financial_analysis.txt"
with open(output_file, "w") as txtfile:
    for result in analysis_results:
        txtfile.write(result + "\n")

print(f"\nAnalysis results have been exported to '{output_file}'.")


