# mail-merger

## Edit History
Erik Kizior, 9/19/2024: Parameterizing details that change in a semester
Alyssa Fu, 9/16/2023: Editing README
Erik Kizior, 9/16/2023: Authoring original script

## generatePlacementEmails.py

Running the script will output an excel file containing three columns:
tutor email
number of students placed with that tutor
placement email text
The text should look like the template on the next page of this document
The line ”df = pd.read_excel('placements.xlsx', sheet_name=0)” describes the spreadsheet that data will be drawn from. Replace ‘placements.xlsx’ with the appropriate spreadsheet file that contains placement data


### Directions for use:

1. Create a file containing all placement pairings. In FA23, we made these pairings in the file called “TMC [SEMESTER YEAR] PLACEMENT INFO” generated from responses to the new student application.  We added three columns: instrument, tutor name, and tutor email
2. Edit the python script to match your desired output. In particular, make sure to change the date string to reflect the scheduled date of symposium
3. Download the file containing the placement pairings and the python script into the same location. CD into that directory in the terminal and run the python script with the command “python3 generatePlacementEmails.py” Errors may arise from columns not matching the expected input. Feel free to modify the lines within the “for index in df.index:” section to match the column names in your spreadsheet.
4. Upload the output excel file to the drive for legacy documentation

## Deltas
Improve the UI such that manual edits to individual lines of code are not necessary. Ex: should be able to pass dates/excel filename as parameters
Hi [TUTOR NAME],

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



