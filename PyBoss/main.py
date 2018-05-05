import os
import csv

csv_path =["employee_data1.csv","employee_data2.csv"]
output_path = 'new_employee.csv'

empId = []
first_name = []
last_name = []
DOB = []
SSN = []
State = []

for datafiles in csv_path:

    with open (datafiles, newline="") as csvfile:
        csvreader = csv.reader (csvfile, delimiter=",")

        next (csvreader,None)
        
        for row in csvreader:
            empId.append (row [0])
        
            first_name.append (row[1].split()[0])
            last_name.append (row[1].split()[1])

            DOB_old = row[2].split("-")
            DOB_new = (DOB_old[1] + "-"+ DOB_old[2] +"-"+DOB_old[0])
            DOB.append (DOB_new)
            
            SSN_old = row[3].split("-")
            SSN_new = ("***-**-" + SSN_old[2])
            SSN.append (SSN_new)

            us_state_abbrev = {
                'Alabama': 'AL',
                'Alaska': 'AK',
                'Arizona': 'AZ',
                'Arkansas': 'AR',
                'California': 'CA',
                'Colorado': 'CO',
                'Connecticut': 'CT',
                'Delaware': 'DE',
                'District of Columbia': 'DC',
                'Florida': 'FL',
                'Georgia': 'GA',
                'Hawaii': 'HI',
                'Idaho': 'ID',
                'Illinois': 'IL',
                'Indiana': 'IN',
                'Iowa': 'IA',
                'Kansas': 'KS',
                'Kentucky': 'KY',
                'Louisiana': 'LA',
                'Maine': 'ME',
                'Maryland': 'MD',
                'Massachusetts': 'MA',
                'Michigan': 'MI',
                'Minnesota': 'MN',
                'Mississippi': 'MS',
                'Missouri': 'MO',
                'Montana': 'MT',
                'Nebraska': 'NE',
                'Nevada': 'NV',
                'New Hampshire': 'NH',
                'New Jersey': 'NJ',
                'New Mexico': 'NM',
                'New York': 'NY',
                'North Carolina': 'NC',
                'North Dakota': 'ND',
                'Ohio': 'OH',
                'Oklahoma': 'OK',
                'Oregon': 'OR',
                'Pennsylvania': 'PA',
                'Rhode Island': 'RI',
                'South Carolina': 'SC',
                'South Dakota': 'SD',
                'Tennessee': 'TN',
                'Texas': 'TX',
                'Utah': 'UT',
                'Vermont': 'VT',
                'Virginia': 'VA',
                'Washington': 'WA',
                'West Virginia': 'WV',
                'Wisconsin': 'WI',
                'Wyoming': 'WY',
            }
            State_new = us_state_abbrev.get (row[4])
            State.append (State_new)

new_list = zip (empId,first_name,last_name,DOB,SSN,State)

with open (output_path,"w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow (["Emp Id", "First Name", "Last Name", "DOB", "SSN", "State"])
    csvwriter.writerows (new_list)

