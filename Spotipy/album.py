
from song import Song
class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []
    def getTitle(self):
        return self.__title
    def getReleaseyYear(self):
        return self.__releaseYear
    def getSongs(self):
        return self.__songs
    def __findSame(self, song):
        isInSong = False
        for x in self.__songs:
            if x.getTitle() == song.getTitle() and x.getDuration() == song.getDuration() and x.getReleaseYear() == song.getReleaseYear():
                isInSong = True
                return isInSong
        return isInSong
    def addSong(self, *songs):
        counter = 0
        for x in songs:
            findsName = self.__findSame(x)
            if findsName == False:
                self.__songs.append(x)
                counter += 1
        return counter     
    def sortBy(self, byKey, reverse):
        if reverse == True:
            sortedList = sorted(self.__songs, key = byKey)
        else:
            sortedList = sorted(self.__songs, key = byKey, reverse = True)
        return sortedList 
    def sortByName(self, reverse):    
        return sorted(self.__songs, key = lambda x: x.getTitle(), reverse = not reverse)
    def sortByPopularity(self, reverse):
        return sorted(self.__songs, key = lambda x: x.getLikes(), reverse = not reverse)
    def sortByDuration(self, reverse):
        return sorted(self.__songs, key = lambda x: x.getDuration(), reverse = not reverse)
    def sortByReleaseYear(self, reverse):
        return sorted(self.__songs, key = lambda x: x.getReleaseYear(), reverse = not reverse)
    def __str__(self):
        return f'Title:{self.__title},Release year:{self.__releaseYear},songs:{{{"|".join(str(item) for item in self.__songs)}}}'
