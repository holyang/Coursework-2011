# Filename: y.py
# Name: Yang Shen
# Center No / Index No: 3024 /
# Description: Supporting classes for music library

# Super class Resource
class Resource():

    ''' Resource class constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    ''' Resource number accessor '''
    def getResourceNo(self):
        return self.__ResourceNo

    ''' Title accessor '''
    def getTitle(self):
        return self.__Title

    ''' DateAcquired accesor '''
    def getDateAcquired(self):
        return self.__DateAcquired

    ''' REsource type accessor '''
    def getResourceType(self):
        return self.__ResourceType

    ''' Title modifier '''
    def setTitle(self, newTitle):
        self.__Title = newTitle

    ''' Date acquired modifier '''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    ''' Resource type modifier '''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    ''' Helper function to display all date '''
    def display(self):
        return("{0:5s}{1:30s}{2:6s}{3:1s}".format \
               (self.__ResourceNo, self.__Title, self.__DateAcquired, self.__ResourceType))

# Subclass MusicCD
class MusicCD(Resource):

    ''' MusicCD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Artist = Artist
        self.__NoOfTracks == NoOfTracks

    ''' Artist accessor '''
    def getArtist(self):
        return self.__Artist

    ''' Number of tracks accessor '''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    ''' Artist modifier '''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    ''' Number of tracks modifier '''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks
    
    ''' Helper function to display all data'''
    def display(self):
        return("{0:42s}{1:50s}{2}".format(super().display(), self.__Artist, self.__NoOfTracks))

# Subclass FilmDVD
# class FilmDVD(Resource):

r1 = Resource("00001", "Best of Super Junior", "090911", "C")
r2 = Resource("00002", "Shaolin Temple", "121210", "D")

print(r1.getResourceNo())
print(r1.display())
print(r1.setTitle("Hello SJ!"))
print(r1.display())

r3 = Resource("00003","","","")

print(r3.display())
r3.setTitle("Good morning Shinee")
r3.setDateAcquired("080810")
r3.setResourceType("C")
print(r3.display())
