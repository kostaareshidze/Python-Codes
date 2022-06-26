class Song:
    def __init__(self, title, releaseYear, duration = 60, likes = 0):
        self.__title = title
        self.__releaseYear = releaseYear 
        self.__duration = duration
        self.__likes = likes
    def getTitle(self):
        return self.__title
    def getReleaseYear(self):
        return self.__releaseYear
    def getDuration(self):
        return self.__duration
    def getLikes(self):
        return self.__likes
    def setDuration(self, newValue):
        if newValue < 0 or newValue > 720 or newValue == self.__duration:
            return False
        else:
            self.__duration == newValue
            return True
    def like(self):
         self.__likes += 1
    def unlike(self):
        self.__likes -= 1

    def __str__(self):
        newDuration = self.__duration / 60
        return f'Title:{self.__title},Duration:{newDuration} minutes,Release year:{self.__releaseYear},Likes:{self.__likes}'
