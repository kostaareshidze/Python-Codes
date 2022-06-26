
from album import Album
from artist import Artist
from song import Song


class SpotiPy:
    def __init__(self, artists = []):
        self.__artists = artists
    def getArtists(self) :
        return self.__artists
    def __findSame(self, artist):
        isInArtists = False
        for x in self.__artists:
                if x.getFirstName() == artist.getFirstName() and x.getSecondName() == artist.getSecondName() and x.getBirthYear() == artist.getBirthYear():
                    isInArtists = True            
                    return isInArtists
        return isInArtists
    def addArtists(self, *artists):
        for x in artists:
            findsName = self.__findSame(x)
            if findsName == False:
                self.__artists.append(x)
        return self.__artists
    def getTopTrendingArtist(self):
        mostLikedArtist = self.__artists[0]
        for x in self.__artists:
            if x.totalLikes() > mostLikedArtist.totalLikes():
                mostLikedArtist = x
        return tuple((mostLikedArtist.getFirstName(), mostLikedArtist.getSecondName()))

        
    def getTopTrendingAlbum(self):
        for artist in self.__artists:
            maximumLikes = 0
            likes = 0
            for album in artist.getAlbums():
                for song in album.getSongs():
                    likes += song.getLikes()
                    if(likes > maximumLikes):
                        maximumLikes = likes
                        trending = album
                        likes = 0
                        maximumLikes = 0
        return trending
    def getTopTrendingSong(self):
        listOfSongs = []
        for artists in self.__artists:
            top = artists.mostLikedSong()
            listOfSongs.append(top)
        bestSong = sorted(listOfSongs, key = lambda x: x.getLikes())[-1]
        return bestSong
 
    @staticmethod
    def loadFromFile():
        file =  open("data3.txt", 'r') 
            

