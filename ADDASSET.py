# Filename: ADDASSET.py
# Author: Yang Shen & Yap Zi Xuan
# Class/Register No.: 5C22/12 & 5C23/15
# Description:

import re
import os
import datetime
import time

def ADDASSET():
    try:
        exist = os.path.exists("ASSET.DAT")

        # set pattern
        AssetID_APattern = re.compile("[Aa]")
        AssetID_TPattern = re.compile("[Tt]")

        a_count = 0
        t_count = 0

        if exist:
            asset_file = open("ASSET.DAT", "r+")

            asset_file.readline() # start from second line

            CurrentFile = asset_file.readlines()


            
            asset_file.seek(0) # seek from beginning
            
            for line in asset_file:
               if AssetID_APattern.match(asset_file.read(1)):
                    a_count+=1
               else:
                    t_count+=1
            if t_count != 0:
                t_count -=1
                
            asset_file.close()
            
        else:
            CurrentFile = []

        asset_file = open("ASSET.DAT", "w+")
        UpdateDate = datetime.date.today()
        asset_file.write(UpdateDate.strftime("%d-%m-%Y"))
        MaxAdd = 19998 - len(CurrentFile)
        valid_NumberOfAssets = False

        while not valid_NumberOfAssets:
            NumberOfAssets = input("Enter number of Assets: ")
            if len(NumberOfAssets) == 0:
                print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                      "Field cannot be empty.")
            elif not NumberOfAssets.isdigit():
                print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                      "Number of Assets must contain only integers. Try again.")
            elif not 0<int(NumberOfAssets)<=MaxAdd:
                print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                      "Maximum Number of Assets can be added is " + MaxAdd + ".")
            else:
                valid_NumberOfAssets = True
        TotalAssets = int(NumberOfAssets) + len(CurrentFile)
        asset_file.write(str(TotalAssets) + "\n")

        if exist:
            for each in CurrentFile:
                asset_file.write(each)
        else:
            pass

        for entry in range(int(NumberOfAssets)):

            print("\n" + "Entry number: " + str(entry+1) + "\n")
            print("Next ID for 'A': " + str(a_count+1).zfill(4))
            print("Next ID for 'T': " + str(t_count+1).zfill(4))
            
            # get and validate AssetID
            valid_AssetID = False

            while not valid_AssetID:
                AssetID = input("\n" + "Enter Asset ID: ")
                
                if len(AssetID) != 5: # presence and length check
                    print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Length of AssetID must be 5. Try again.")
                    
                elif not AssetID[1:6].isdigit(): # data type check
                    print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Last 4 characters of Asset ID must be in integers. Try again.")
                    
                else:
                    if AssetID_APattern.match(AssetID): # pattern check
                        if not AssetID[1:6] == str(a_count+1).zfill(4):
                            print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                                  "Asset ID not in order. Try again.")
                        else:
                            valid_AssetID = True
                            AssetID = AssetID.upper()
                            a_count+=1
                            
                    elif AssetID_TPattern.match(AssetID): # pattern check
                        if not AssetID[1:6] == str(t_count+1).zfill(4):
                            print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                                  "Asset ID not in order. Try again.")
                        else:
                            valid_AssetID = True
                            AssetID = AssetID.upper()
                            t_count+=1
                    else:
                        print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                              "First character of Asset ID must be A or T only. Try again.")
                        
            # get and validate Description        
            valid_Description = False

            while not valid_Description:
                Description = input("Enter Description: ")
                
                if not 0 < len(Description) <= 30: # length and presence check
                    print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Length of Description must be within 1 to 30. Try again.")
                else:
                    valid_Description = True

            # get and validate DatePurchased
            valid_DatePurchased = False

            Date_Pattern = re.compile("^[0-9]{4}[-][0-9]{2}[-][0-9]{2}$")
            
            while not valid_DatePurchased:
                DatePurchased = input("Enter Date of Purchased (YYYY-MM-DD): ")
                
                if len(DatePurchased) != 10: # length and presence check
                    print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Date of Purchased is either empty or of invalid length. Try again.")
                    
                elif not Date_Pattern.match(DatePurchased): # pattern check
                    print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Date of Purchased must be in the form of YYYY-MM-DD. Try again. ")                
                else:
                    try: # valid date check
                            time.strptime(DatePurchased, "%Y-%m-%d")  
                            if not datetime.datetime.strptime(DatePurchased, "%Y-%m-%d") < datetime.datetime.today(): # future date check
                                print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                                      "Invalid Date. Try again.")
                            else:
                                valid_DatePurchased = True
                    except ValueError:
                        print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                              "Invalid Date. Try again.")
                        
            # get and validate Status
            valid_Status = False
            
            Status_Pattern = re.compile("[AaCcLlFf]")
            
            while not valid_Status:
                Status = input("Enter Status of Asset: ")
                
                if len(Status) != 1: # length and presence check
                    print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Field is either empty or contains more than 1 character. Try again.")
                    
                elif not Status_Pattern.match(Status): # pattern check
                    print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Status must be either 'A' for Available; 'C' for Condemned; 'F' for Faulty; 'L' for On-Loan. Try again,")
                else:
                    valid_Status = True
                    Status = Status.upper()

            asset_file.write("%5s%-30s%10s%1s" % (AssetID, Description, DatePurchased, Status + "\n"))

            # telling user if there is next entry.
            if not str(entry+1) == str(NumberOfAssets):
                print("Data saved. Proceeding to Next Entry." + "\n")
            else:
                print("Data saved." + "\n")

        asset_file.close()

        # confirm all data is saved.
        print("All data saved.")
                         

    except IOError:
        print("*WARNING*"+ "\n" + "AN ERROR OCCURED:" + "\n" +
              "Unable to create or write the file.")

# main program
if __name__ == "__main__":
    ADDASSET();
