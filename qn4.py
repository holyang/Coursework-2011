import time

def PRINTRECORD():

    try:
        resource_file = open("RESOURCE.DAT", "r")
        uresource_file = open("URESOURCE.DAT", "r")
        loan_file = open("LOAN.DAT", "r")
        report_file = open("REPORT.DAT", "w")

        detail_lines = loan_file.readlines()
        loan_list = []
        dates = []

        for record_line in detail_lines:
            loan_list_data = []
            record_line = record_line.rstrip("\n")
            resource_no = record_line[:5]
            student_id = record_line[5:11]
            DateDueBack = record_line[41:47]
            loan_list_data.append(record_line)
            loan_list_data.append(resource_no)
            loan_list_data.append(student_id)
            loan_list.append(loan_list_data)
            
            if DateDueBack == dates[record_line-1]:
                continue
            else:
                dates.append(DateDueBack)
                
                resource_num = 0
                count = 0
                i = 0
                j = 0
		
                while i <= length.loan_list():
                    loan_file.write("Date: " + loan_list[i][3])
                    while loan_list[i][3] < loan_list[i+1][3]:
                        loan_file.write(loan_list[i][0])
                        loan_file.write(loan_list[i][1])
                        loan_file.write(loan_list[i][2])
                        i = i + 1			
                        i = i + 1
			
        new_lines = resource_file.readlines()
        
        for data_line in new_lines:

            data_line = data_line.rstrip("\n")
            new_resource_no = data_line[:5]
                
        print("-" * 75)
        print(loan_list)
        
        ## close files
        resource_file.close()
        loan_file.close()
        report_file.close()

    except IOError:

        print("Error! Input file does not exist.")

##from collections import OrderedDict
##
##d = ('banana': 3, 'apple':4, 'pear': 1, 'orange': 2)	
##
##e = OrderedDict(sorted(d.items(), key=lambda t: t[0])) # Sort key
##
##f = OrderedDict(sorted(d.items(), key=lambda t: t[1])) # Sort 2nd string
##
##g = OrderedDict(sorted(d.items(), key=lambda t: len(t[0]))) # Sort length of string
##
##import re
##
##$ set up nric test pattern
##pattern = re.compile("^[sStTfGgG][0-9](7)[a-zA-Z]$")
##
##if not pattern.match(nric):
##	print("Invalid NRIC")
##else:
##	print("ok")
