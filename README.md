# mail-merger

# Author: Erik Kizior

## Edit History
- Rachel Sang, 2/07/2025: Created hours.py to send end of semester tutor emails containing total volunteer hours.
- Erik Kizior, 9/19/2024: Integrating gmail API into script to directly create drafts
- Alyssa Fu, 9/16/2023: Editing README
- Erik Kizior, 9/16/2023: Creating original script

## generatePlacementEmails.py

Running the script will output an Excel file containing three columns:

- Tutor email
- Number of students placed with that tutor
- Placement email text

The text should follow the template on the next page of this document.

The line `df = pd.read_excel(placementsPath, sheet_name=0)` describes the spreadsheet from which data will be drawn. Supply `placementsPath` with the appropriate path to the excel file that contains placement data.

If run with the `--draft` flag, it will automatically draft emails in `tmcberkeley@gmail.com`.

Command-line arguments are accepted as follows: `python3 generateEmails.py path/to/placements`

Optional `--draft` flag to draft emails in Gmail: `python3 generateEmails.py path/to/placements --draft`


### Directions for use:

1. Create a file containing all placement pairings. In FA23, we made these pairings in the file called “TMC [SEMESTER YEAR] PLACEMENT INFO” generated from responses to the new student application.  We added three columns: instrument, tutor name, and tutor email
2. Edit the python script to match your desired output. In particular, make sure to change the date string to reflect the scheduled date of symposium, and change the subject line of the email
3. Download the file containing the placement pairings and the python script into the same location. CD into that directory in the terminal and run the python script with the command `python3 generatePlacementEmails.py /path/to/placements` Errors may arise from columns not matching the expected input. Feel free to modify the lines within the `for index in df.index:` section to match the column names in your spreadsheet.
4. Upload the output excel file to the drive for legacy documentation

## Deltas
Import run configurations from a config file such that manual edits to individual lines of code are not necessary.

## Sample Output

Thank you for applying to be a private tutor for The Music Connection! Below are the details of your placement:

Instrument: 

Student name: 

Grade: 

Parent email: 

Parent phone: 


REMINDER: Our Tutor Symposium is on [Symposium Date] from [Time] in [Room]! This meeting is mandatory for all new tutors. Returning tutors are only required to stay from [Time] pm. We will be going over how to send your first email to your student’s parents. Please send the first email after the Tutor Symposium and before [Deadline Date] at 11:59 pm, and make sure to CC tmcberkeley@gmail.com on the first communication. 

Thank you and we look forward to working with you! Please email back if you have any questions!

Best,
The Music Connection

## hours.py
Divas and baddies. Ladies and gentlemen. I, Rachel Soobin Sang, have usurped my own limitations and provided a delightful little Python file to automate end-of-the-semester emails to all of our tutors at the request of Aaron Lee. Holy moly guys, I feel accomplished. I HOPE MY PREDECESSORS ARE PROUD, and I hope that this program is helpful. 

1. Create an Excel file containing tutor emails, tutor names, and their total number of volunteer hours. If you do not have this file, the Chief Operations Officer should have a Google Spreadsheet of every tutor's logged volunteer hours, including workshops. Export this file as a .xlsx file. In FA24, this spreadsheet was named hours.xlsx with three columns: EMAIL, TUTOR NAME, and TOTAL. 
2. Edit the provided Python script to match your needs. For instance, adjust the statistics and semester and year to reflect the semester that you are currently working in. 
3. Download the Python script and the Excel file into the same directory. See Erik's instructions for generateEmails.py for more details if you are unsure of how to do this. Run the program with the command `python3 hours.py path/to/placements --draft`

