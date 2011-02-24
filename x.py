# Filename: cwb2.py
# Name: Yang Shen
# Centre No / Index No: 3024 /
# Description: Read from RESOURCE.DAT, get extra info based on resource type
#              perform validation and write to URESOURCE.DAT

from classes import *

def UPDATERESOURCE():

    try:
        # open resource file for reading
        resource_file = open("RESOURCE.DAT", "r")

        # open updated resource file for writing
        uresource_file = open("URESOURCE.DAT", "w")
        
        # read heading line from resource file (creation date, number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
        
        # store creation date and number of records
        creation_date = heading_line[0:10]
        num_recs = heading_line[10:]

        # write creation date and number of records to updated resource file
        uresource_file.write(creation_date + num_records)
        
        # read remaining record details
        detail_lines = resource_file.readlines()

        # initialize resource list
        resource_list = []
        
        
        # loop for number of records
        for record_line in detail_lines:
            # clean record line
            record_line = record_line.rstrip("\n")

            # store resource number, title, date acquired, resource type
            resource_no = record_line[0:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]
            
            # print resource info
##            print("Resource no: " + resource_no)
##            print("Title: " + title)
##            print("Date acquired: " + date_acquired)
##            print("Resource type: " + resource_type)
            
            # if resource type is music CD
            if resource_type == "C":
                # get and validate artist
                valid_artist = False
                while not valid_artist:
                    artist = input("Enter artist: ")
                    if len(artist) == 0:
                        print("Invalid! Empty input. Try again.")
                    elif len(artist) > 50:
                        print("Invalid! Exceed 50 characters. Try again.")
                    else:
                        valid_artist = True
                        
            # get and validate number of tracks
                valid_NoOfTracks = False
                while not valid_NoOfTracks:
                    NoOfTracks = input("Enter number of tracks: ")
                    if len(NoOfTracks) == 0:
                        print("Invalid! Empty input. Try again.")
                    elif not NoOfTracks.isdigit():
                        print("Invalid! Must be a number. Try again.")
                    elif not (0 < int(NoOfTracks) <= 20): # range check
                        print("Invalid! Must be between 1 and 20. Try again.")
                    else:
                        valid_NoOfTracks = True
                resource_list.append(MusicCD(resource_no, title, title, date_acquired, resource_type, artist, NoOfTracks))

            elif resource_type == "D":
                # get and validate director
                valid_director = False
                while not valid_director:
                    director = input("Enter director: ")
                    if len(director) == 0:
                        print("Invalid!")
                    elif len(director) > 50:
                        print("Invalid!")
                    else:
                        valid_director = True
    
                valid_running_time = False
                while not valid_running_time:
                    running_time = input("Enter running time: ")
                    if len(running_time) == 0: # presence check
                        print("Invalid! Empty input. Try again.")
                    elif not running_time.isdigit():
                        print("Invalid! Must be a number. Try again.")
                    elif not (30 <= int(running_time) <= 180):
                        print("Invalid!")
                    else:
                        valid_running_time = True
            
                    
        # else resource type is film DVD
            # get and validate director
            # get and validate running time
        # write resource info and exra details to updated resource file
##        for resource in resource_list:
##            if resource.getResourceType() == "C":
##                uresoure_file.write(resource.getResourceNo() + resource.getTitle() + resource.getDateAcquired + \
##                                    resource.getResourceType() + resource.getArtist() + resource.getResourceType() + \
##                                    "NULL (count to 50)    " + " 000" + "\n")
##            else:
##                uresource_file.write(resource.getResourceNo() + resource.getTitle() + resource.getDateAcquired + \
##                                     resource.getResourceType() + resource.getDirector() + resource.getResourceType() + "\n")
##
##        for resource in resource_list:
##            resource_file.write(resource.display())
            
# close files
        resource_file.close()
        uresource_file.close()
    except IOError:
        # display file input/output errors
        print("Error! Cannot read from input file or write to output file.")

if __name__ == "__main__":
    UPDATERESOURCE()
