import random
from enum import Enum
import json

names = [
    "Calham",
    "Mack",
    "Marieke",
    "Alex",
    "Tom Sawyer",
    "Petricia",
    "Obama",
    "Canadian #1",
    "Putin",
    "Karl Marx",
    "David Bowie",
    "Freddie Mercury",
    "Niel Armstrong",
    "Buzz Aldrin",
    "Terry Crews",
]


class Genres(Enum):
    horror = "HORROR"
    comedy = "COMEDY"
    action = "ACTION"
    scifi = "SCIFI"
    drama = "DRAMA"
    documentary = "DOCUMENTARY"
    romance = "ROMANCE"

movieData = {
    Genres.horror: ["IT: Chapter 1", "IT: Chapter 2"],
    Genres.comedy: ["Tropic Thunder", "Hot Fuzz"],
    Genres.action: ["Die Hard", "Avengers"],
    Genres.scifi: ["Star Wars: A New Hope", "Star Wars: Revenge of the Sith"],
    Genres.drama: ["Parasite", "Citizen Kane"],
    Genres.documentary: ["March of the Penguins", "Tiger King"],
    Genres.romance: ["The Notebook", "Titanic"]
}


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
            genre_data_keys.likeRatio] = self.ratioHelper(likedList, dislikedList)
        self.genres[genre][
            genre_data_keys.dislikeRatio] = self.ratioHelper(dislikedList, likedList)

    def genre_data_to_string(self, genre):
        string = "----------------------" + str(genre).upper() + "----------------------\n"
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
        return string

    def print_user_genre_data(self):
        for genre in Genres:
            print(self.genre_data_to_string(genre.value))

    def ratioHelper(self, n, d):
        totalLen = len(n) + len(d)
        if totalLen != 0:
            return len(n) / totalLen
        else:
            return 0


data = {}
jsonData = {}

for name in names:

    data[name] = UserData()
    for genre in Genres:
        likedList = []
        dislikedList = []
        notRated = []
        for movie in movieData[genre]:
            testNum = random.uniform(0, 1)
            if testNum > 0.5:
                likedList.append(movie)
            elif testNum <= 0.2:
                notRated.append(movie)
            else:
                dislikedList.append(movie)
        data[name].add_genre_data(likedList, notRated, dislikedList, genre.value)

# Convert Classes to JSON
for user in data:
    jsonData[user] = json.dumps(data[user].__dict__)

# Print JSON to file
with open('result.json', 'w') as fp:
    json.dump(jsonData, fp)