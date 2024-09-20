"""
Extract data in the form:

Hi [TUTOR NAME],

Thank you for applying to be a private tutor for The Music Connection! Below are the details of your placement:

Instrument: 
Student name: 
Grade: 
Parent email: 
Parent phone: 

REMINDER: Our Tutor Symposium is on Sunday, September 17th from 1-3 pm in Social Sciences 104! This meeting is mandatory for all new tutors. Returning tutors are only required to stay from 1-2 pm. We will be going over how to send your first email to your student’s parents. Please send the first email after the Tutor Symposium and before Wednesday, September 20th at 11:59 pm, and make sure to CC tmcberkeley@gmail.com on the first communication. 

Thank you and we look forward to working with you! Please email back if you have any questions!

Best,
The Music Connection
"""

import sys
import pandas as pd
import draftEmails


def generateGreeting(tutorName, numStudents):
    output = ""
    output += 'Hi ' + str(tutorName) + ','
    output += '\n'
    output += '\n'
    if numStudents == 1:
        output += 'Thank you for applying to be a private tutor for The Music Connection! Below are the details of your placement:'
    else:
        output += 'Thank you for applying to be a private tutor for The Music Connection! Below are the details of your placements:'
    output += '\n'
    output += '\n'
    return output


def generateAllPlacements(placements):
    if len(placements) == 1:
        instrument, studentName, grade, parentEmail, parentPhone = placements[0]
        return generatePlacement(instrument, studentName, grade, parentEmail, parentPhone)
    else:
        output = ""
        for i, placement in enumerate(placements):
            instrument, studentName, grade, parentEmail, parentPhone = placement
            output += "Placement " + str(i + 1) + ":"
            output += '\n'
            output += generatePlacement(instrument,
                                        studentName, grade, parentEmail, parentPhone)
        return output


def generatePlacement(instrument, studentName, grade, parentEmail, parentPhone):
    output = ""
    output += 'Instrument: ' + str(instrument)
    output += '\n'
    output += 'Student name: ' + str(studentName)
    output += '\n'
    output += 'Grade: ' + str(grade)
    output += '\n'
    output += 'Parent email: ' + str(parentEmail)
    output += '\n'
    output += 'Parent phone: ' + str(parentPhone)
    output += '\n'
    output += '\n'
    return output


def generateOutro(numStudents):
    output = ""
    if numStudents == 1:
        output += 'REMINDER: Our Tutor Symposium is on Saturday, September 21st from 11:30-1:30 pm in Morrison 120! This meeting is mandatory for all new tutors. We will be going over how to send your first email to your student’s parents. Please send the first email after the Tutor Symposium and before Wednesday, September 20th at 11:59 pm, and make sure to CC tmcberkeley@gmail.com on the first communication. '
    else:
        output += 'REMINDER: Our Tutor Symposium is on Sunday, September 17th from 1-3 pm in Social Sciences 104! This meeting is mandatory for all new tutors. We will be going over how to send your first email to your students’ parents. Please send the first email after the Tutor Symposium and before Wednesday, September 20th at 11:59 pm, and make sure to CC tmcberkeley@gmail.com on the first communication. '
    output += '\n'
    output += '\n'
    output += 'Thank you and we look forward to working with you! Please email back if you have any questions!'
    output += '\n'
    output += '\n'
    output += 'Best,'
    output += '\n'
    output += 'The Music Connection'
    return output


def generateEmails(placementsPath='placements.xlsx'):

    df = pd.read_excel(placementsPath, sheet_name=0)

    tutors = set()
    placementDict = {}
    numStudents = {}
    tutorNames = {}

    for index in df.index:
        tutorName = df['TUTOR NAME'][index]
        studentName = df['Student Name'][index]
        instrument = df['INSTRUMENT'][index]
        tutorEmail = df['TUTOR EMAIL'][index]
        grade = df['Grade Level'][index]
        parentEmail = df['PARENT Email Address'][index]
        parentPhone = df['Phone Number - (111) 111 - 1111'][index]

        tutors.add(tutorEmail)
        placement = (instrument, studentName, grade, parentEmail, parentPhone)
        tutorNames[tutorEmail] = tutorName

        if tutorEmail in placementDict:
            allPlacements = list(placementDict[tutorEmail])
            allPlacements.append(placement)
            placementDict[tutorEmail] = tuple(allPlacements)
            numStudents[tutorEmail] = numStudents[tutorEmail] + 1
        else:
            placementDict[tutorEmail] = tuple([placement])
            numStudents[tutorEmail] = 1


    outputData = []

    for tutor in tutors:
        text = ""
        text += generateGreeting(tutorNames[tutor], numStudents[tutor])
        text += generateAllPlacements(placementDict[tutor])
        text += generateOutro(numStudents[tutor])
        outputData.append([tutor, numStudents[tutor], text])


    outputDF = pd.DataFrame(outputData, columns=['Email', 'Num Students', 'Text'])
    outputDF.to_excel("output.xlsx")

    return outputDF

# Accepts arugments on the command line as follows:
# python3 generateEmails.py path/to/placements
if __name__ == "__main__":

    outputDF = None

    if len(sys.argv) == 2:
        outputDF = generateEmails(sys.argv[1])
    else:
        outputDF = generateEmails()
    
    sender_email = 'tmcberkeley@gmail.com'
    subject = "[IMPORTANT] TMC SP24 Student Placement Info + Tutor Symposium"

    draftEmails.create_drafts_from_df(outputDF)
    