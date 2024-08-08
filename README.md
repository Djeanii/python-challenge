1. **Overview Section:**
   - This project contains two Python scripts, PyBank and PyPoll, that perform data analysis on financial and election datasets respectively. Each script reads data from a CSV file, performs the necessary calculations, and outputs the results to both the terminal and a text file.
2. **Directory Structure:**
   - python-challenge/
│
├── PyBank/
│ ├── main.py
│ ├── Resources/
│ │ └── budget_data.csv
│ └── analysis/
│ └── financial_analysis.txt

└── PyPoll/
├── main.py
├── Resources/
│ └── election_data.csv
└── analysis/
└── election_results.txt

3. **PyBank Section:**
- The `PyBank` script analyzes a financial dataset and calculates the following:
  - Total number of months included in the dataset.
  - Net total amount of "Profit/Losses" over the entire period.
  - Changes in "Profit/Losses" over the entire period and the average of those changes.
  - The greatest increase in profits (date and amount) over the entire period.
  - The greatest decrease in losses (date and amount) over the entire period.

  - Navigate to the `PyBank` directory:
   cd python-challenge/PyBank
-run the script

4. **PyPoll Section:**
- The PyPoll script analyzes election data and calculates the following:
  - Total number of votes cast.
  - Complete list of candidates who received votes.
  - Percentage of votes each candidate won.
  - Total number of votes each candidate won.
  - Winner of the election based on popular vote.
  
  -Navigate to the `PyPoll` directory:
  cd python-challenge/Pypoll
- run the script

5. **Setup:**
   - Clone the repository
   - Ensure the directory structure is as described above.
   - Place the provided budget_data.csv in PyBank/Resources/ and election_data.csv in PyPoll/Resources/.
