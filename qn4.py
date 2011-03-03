# Filename: qn4.py
# Author: Yang Shen 6C22

from collections import OrderedDict

def PRINTRECORD():

    try:
        uresource_file = open("URESOURCE.DAT", "r")
        loan_file = open("LOAN.DAT", "r")
        
        loan_dict = {}
        
        loan_list = []
        dates = []
        end_list = []
        end_end_list = []

        loan_details = loan_file.readlines()
        resource_details = uresource_file.readlines()

        for record_line in loan_details:
            
            record_line = record_line.rstrip("\n")
            resource_no = record_line[:5]
            student_id = record_line[5:10]
            student_name = record_line[10:40]
            Day = record_line[40:42]
            Month = record_line[42:44]
            Year = record_line[44:46]
            DateDueBack = Year + Month + Day
            
            if DateDueBack not in dates:
                dates.append(DateDueBack)

            for record_line_two in resource_details:
                record_line_two = record_line_two.rstrip("\n")

                if resource_no == record_line_two[:5]:
                    resource_title = record_line_two[5:35]
                    resource_type = record_line[41:]

                    if resource_type == "C":
                        resource_type = "CD"
                    else:
                        resource_type = "DVD"
                    break
                else:
                    continue

            loan_list = [DateDueBack, resource_no, resource_title, resource_type, student_id, student_name]
            
            end_list.append(loan_list)
            
            loan_list = list()
            
        for date in dates:
            for loan in end_list:
                if date == loan[0]:
                    del loan[0]
                    end_end_list.append(loan)
                        
            loan_dict[date] = end_end_list

            end_end_list = list()
        sorted_loan_dict = OrderedDict(sorted(loan_dict.items(), key=lambda t: t[0]))
        for k, v in sorted_loan_dict.items():
            print("Date: " + k[4:6] + "-" + k[2:4] + "-" + "20" + k[:2])
            print("-" * 75)
            print()
            for i in range(len(v)):
                for j in range(len(v[i])):
                    print(v[i][j], end = " ")
                print()
            print("Number of Resources: ",len(v))
            print()
        
        ## close files
        uresource_file.close()
        loan_file.close()

    except IOError:

        print("Error! Input file does not exist.")

if __name__ == "__main__":
    PRINTRECORD()

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
