from album import Album
from song import Song


class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles
    def getFirstName(self):
        return self.__firstName
    def getSecondName(self):
        return self.__lastName
    def getBirthYear(self):
        return self.__birthYear
    def getAlbums(self):
        return self.__albums
    def getSingles(self):
        return self.__singles
    def mostLikedSong(self):
        mostLiked = self.__singles[0]
        for x in self.__singles:
            if x.getLikes() > mostLiked.getLikes():
                mostLiked = x
        for x in self.__albums:
            for y in x.getSongs():
                if y.getLikes() > mostLiked.getLikes():
                    mostLiked = y
        return mostLiked
    def leastLikedSong(self):
        leastLikes = self.__singles[0]
        for x in self.__singles:
            if x.getLikes() < leastLikes.getLikes():
                leastLikes = x
        for x in self.__albums:
            for y in x.getSongs():
                if y.getLikes() < leastLikes.getLikes():
                    leastLikes = y
        return leastLikes
    def totalLikes(self):
        sumOfSingles = 0
        sumOfAlbums = 0
        for x in self.__singles:
            sumOfSingles += x.getLikes()
        for x in self.__albums:
            for y in x.getSongs():
                sumOfAlbums += y.getLikes()
        sum = sumOfAlbums + sumOfSingles
        return sum
        
    def __str__(self) :
        return f'Name:{self.__firstName} {self.__lastName},Birth year:{self.__birthYear},Total likes:{self.totalLikes()}'


