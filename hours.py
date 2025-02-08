"""
Extract data in the form:

Hi [TUTOR NAME],

On behalf of the TMC community, we want to thank you for a successful fall semester. Overall, we had a total of 600+ hours volunteered
across 77 tutors and 112 private students. We have included your total number of hours volunteered during the Fall 2024 semester below. 
Tutor Name: [TUTOR NAME]
Total Hours: [TOTAL HOURS]

Thank you again for all your hard work during the Fall 2024 semester. We hope to see you continue on this semester!

Sincerely,
The Music Connection

"""

import sys
import pandas as pd
import draftEmails


def generateMessage(tutorName, numHours):
    return (f"Hi {tutorName},\n\n"
            "On behalf of the TMC community, we want to thank you for a successful fall semester. Overall, we had a total of 600+ hours volunteered "
            "across 77 tutors and 112 private students. We have included your total number of hours volunteered during the Fall 2024 semester below.\n\n"
            f"Tutor Name: {tutorName} \n"
            f"Total Hours: {numHours} hours \n\n"
            "Thank you again for all your hard work during the Fall 2024 semester. We hope to see you continue this semester!\n\n"
            "Sincerely,\n"
            "The Music Connection")



def generateEmails(hoursPath='hours.xlsx'):

    print("Interpreting data from " + hoursPath + "...")

    df = pd.read_excel(hoursPath, sheet_name=0)

    outputData = []

    print("Generating emails...")

    for index, row in df.iterrows():
        tutor = {
            'Email': row['EMAIL'],
            'Tutor Name': row['TUTOR NAME'],
            'Total Hours': row['TOTAL'],
            'Text': generateMessage(row['TUTOR NAME'], row['TOTAL'])
        }
        outputData.append(tutor)

    print("Dumping data to output.xlsx...")

    outputDF = pd.DataFrame(outputData)
    outputDF.to_excel("output.xlsx")

    print("Done!")

    return outputDF

if __name__ == "__main__":

    outputDF = None

    if len(sys.argv) == 2 or len(sys.argv) == 3:
        outputDF = generateEmails(sys.argv[1])
    else:
        outputDF = generateEmails()
    

    if len(sys.argv) == 3 and sys.argv[2] == '--draft':

        print("Drafting emails on gmail...")

        sender_email = 'tmcberkeley@gmail.com'
        subject = "[IMPORTANT] TMC FA24 Total Volunteer Hours"

        draftEmails.create_drafts_from_df(outputDF, sender_email, subject)
