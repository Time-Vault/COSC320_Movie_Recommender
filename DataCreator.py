import random

data = {}


class Genres(enumerate):
    horror = "HORROR"
    comedy = "COMEDY"


class genre_data_keys(enumerate):
    likedList = "LIKED_LIST"
    notRatedList = "NOT_RATED_LIST"
    dislikedList = "DISLIKED_LIST"
    likeRatio = "LIKE_RATIO"
    dislikeRatio = "DISLIKE_RATIO"


class UserData (object):

    def __init__(self):
        self.genres = {}
        self.similarityList = {}
        self.recommendations = {}

    def add_genre_data(self, likedList, notRatedList, dislikedList, genre):
        self.genres[genre] = {}
        self.genres[genre][
            genre_data_keys.likedList] = likedList
        self.genres[genre][
            genre_data_keys.notRatedList] = notRatedList
        self.genres[genre][
            genre_data_keys.dislikedList] = dislikedList
        self.genres[genre][
            genre_data_keys.likeRatio] = len(likedList) / (len(likedList)+len(dislikedList))
        self.genres[genre][
            genre_data_keys.dislikeRatio] = len(dislikedList) / (len(likedList)+len(dislikedList))

    def genre_data_to_string(self, genre):
        string = "---------------------- \n"
        string += "Liked List: " + str(self.genres[genre][
            genre_data_keys.likedList]) + ", \n"
        string += "Disliked List: " + str(self.genres[genre][
            genre_data_keys.dislikedList]) + ", \n"
        string += "Not Rated List: " + str(self.genres[genre][
            genre_data_keys.notRatedList]) + ", \n"
        string += "Like Ratio: " + str(self.genres[genre][
            genre_data_keys.likeRatio]) + ", \n"
        string += "Dislike Ratio: " + str(self.genres[genre][
            genre_data_keys.dislikeRatio]) + ", \n"
        string += "---------------------- \n"
        return string


names = [
    "terry",
    "calham",
    "mack",
    "marieke",
    "alex",
]

movies = [
    "friday the 13th",
    "texas chainsaw massacre",
    "Nightmare on Elm Street",
    "Scream",
    "Childs Play",
    "Jaws",
]

calham = UserData()
calham.add_genre_data(["F13"], ["carrie"], [
                      "Cabin IN The Woods"], Genres.horror)

print(calham.genre_data_to_string(Genres.horror))

for name in names:
    likedList = []
    dislikedList = []
    notRated = []

    for movie in movies:
        testNum = random.uniform(0, 1)
        if testNum > 0.5:
            likedList.append(movie)
        elif testNum <= 0.2:
            notRated.append(movie)
        else:
            dislikedList.append(movie)

    data[name] = UserData()
    data[name].add_genre_data(likedList, notRated, dislikedList, Genres.horror)
    print(name + "'s DATA\n")
    print(data[name].genre_data_to_string(Genres.horror))

data = {}


class Genres(enumerate):
    horror = "HORROR"
    comedy = "COMEDY"


class genre_data_keys(enumerate):
    likedList = "LIKED_LIST"
    notRatedList = "NOT_RATED_LIST"
    dislikedList = "DISLIKED_LIST"
    likeRatio = "LIKE_RATIO"
    dislikeRatio = "DISLIKE_RATIO"


class UserData (object):

    def __init__(self):
        self.genres = {}
        self.similarityList = {}
        self.recommendations = {}

    def add_genre_data(self, likedList, notRatedList, dislikedList, genre):
        self.genres[genre] = {}
        self.genres[genre][
            genre_data_keys.likedList] = likedList
        self.genres[genre][
            genre_data_keys.notRatedList] = notRatedList
        self.genres[genre][
            genre_data_keys.dislikedList] = dislikedList
        self.genres[genre][
            genre_data_keys.likeRatio] = len(likedList) / (len(likedList)+len(dislikedList))
        self.genres[genre][
            genre_data_keys.dislikeRatio] = len(dislikedList) / (len(likedList)+len(dislikedList))

    def genre_data_to_string(self, genre):
        string = "---------------------- \n"
        string += "Liked List: " + str(self.genres[genre][
            genre_data_keys.likedList]) + ", \n"
        string += "Disliked List: " + str(self.genres[genre][
            genre_data_keys.dislikedList]) + ", \n"
        string += "Not Rated List: " + str(self.genres[genre][
            genre_data_keys.notRatedList]) + ", \n"
        string += "Like Ratio: " + str(self.genres[genre][
            genre_data_keys.likeRatio]) + ", \n"
        string += "Dislike Ratio: " + str(self.genres[genre][
            genre_data_keys.dislikeRatio]) + ", \n"
        string += "---------------------- \n"
        return string


names = [
    "terry",
    "calham",
    "mack",
    "marieke",
    "alex",
]

movies = [
    "friday the 13th",
    "texas chainsaw massacre",
    "Nightmare on Elm Street",
    "Scream",
    "Childs Play",
    "Jaws",
]

calham = UserData()
calham.add_genre_data(["F13"], ["carrie"], [
                      "Cabin IN The Woods"], Genres.horror)

print(calham.genre_data_to_string(Genres.horror))

for name in names:
    likedList = []
    dislikedList = []
    notRated = []

    for movie in movies:
        testNum = random.uniform(0, 1)
        if testNum > 0.5:
            likedList.append(movie)
        elif testNum <= 0.2:
            notRated.append(movie)
        else:
            dislikedList.append(movie)

    data[name] = UserData()
    data[name].add_genre_data(likedList, notRated, dislikedList, Genres.horror)
    print(name + "'s DATA\n")
    print(data[name].genre_data_to_string(Genres.horror))
