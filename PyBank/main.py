import csv
import os

# Define file path
file_path = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
changes = []
dates = []
previous_profit = None

# Read CSV file
try:
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader, None)  # Use None as the default to avoid StopIteration

        if header is None:
            print("Error: The CSV file is empty.")
        else:
            for row in reader:
                date = row[0]
                profit = int(row[1])
                total_months += 1
                net_total += profit

                if previous_profit is not None:
                    change = profit - previous_profit
                    changes.append(change)
                    dates.append(date)

                previous_profit = profit

            # Calculate average change, greatest increase, and greatest decrease
            if changes:
                average_change = sum(changes) / len(changes)
                greatest_increase = max(changes)
                greatest_decrease = min(changes)
                greatest_increase_date = dates[changes.index(greatest_increase)]
                greatest_decrease_date = dates[changes.index(greatest_decrease)]

                # Print results to terminal
                print("Financial Analysis")
                print("----------------------------")
                print(f"Total Months: {total_months}")
                print(f"Total: ${net_total}")
                print(f"Average Change: ${average_change:.2f}")
                print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
                print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

                # Write results to text file
                output_path = os.path.join("analysis", "financial_analysis.txt")
                with open(output_path, mode='w') as file:
                    file.write("Financial Analysis\n")
                    file.write("----------------------------\n")
                    file.write(f"Total Months: {total_months}\n")
                    file.write(f"Total: ${net_total}\n")
                    file.write(f"Average Change: ${average_change:.2f}\n")
                    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
                    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
            else:
                print("No data to analyze.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
