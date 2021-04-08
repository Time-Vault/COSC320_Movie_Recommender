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
class genre_data_keys(enumerate):
    likedList = "LIKED_LIST"
    notRatedList = "NOT_RATED_LIST"
    dislikedList = "DISLIKED_LIST"
    likeRatio = "LIKE_RATIO"
    dislikeRatio = "DISLIKE_RATIO"

# IMPORT FROM JSON START
f = open('inputData.json')
importData = json.load(f)
userData = {}
userNames = []

for i in importData:
    count = 0
    user = json.loads(importData[i])
    userNames.append(i)
    userData[i] = user
# END

def similarity(list1, list2):
    lst3 = [value for value in list1 if value in list2]
    return len(lst3)

def compareGenre (user1, user2, genre):
    u1Liked = user1['genres'][genre][genre_data_keys.likedList]
    u2Liked = user2['genres'][genre][genre_data_keys.likedList]
    u1Disliked = user1['genres'][genre][genre_data_keys.dislikedList]
    u2Disliked = user2['genres'][genre][genre_data_keys.dislikedList]
    similarityRatio = similarity(u1Liked,u2Liked) + similarity(u1Disliked,u2Disliked) - similarity(u2Disliked,u1Liked)-similarity(u2Liked,u1Disliked) / (len(u1Liked) + len(u2Liked) + len(u1Disliked) + len(u2Disliked))
    if similarityRatio < 0:
        return 0;
    else:
        return similarityRatio

def computeSimilarity():
    for i in range(len(userNames)):
        user1 = userData[userNames[i]]
        for j in range(len(userNames)):
            if (j+1 < len(userNames)):
                user2 = userData[userNames[j+1]]
                for genre in userData[userNames[i]]['genres']:
                    if genre not in userData[userNames[i]]['similarityList']:
                        userData[userNames[i]]['similarityList'][genre] = {}
                    if genre not in userData[userNames[j+1]]['similarityList']:
                        userData[userNames[j+1]]['similarityList'][genre] = {}

                    maxSimilarity = compareGenre(user1, user1, genre)
                    userSimilarity = compareGenre(user1, user2, genre) / maxSimilarity
                    if userSimilarity > maxSimilarity:
                        maxSimilarity = userSimilarity
                    user1['similarityList'][genre][userNames[j+1]] = userSimilarity
                    user2['similarityList'][genre][userNames[i]] = userSimilarity

def computeReccomendations():
    # Loop from 0 -> n
    for i in range(len(userNames)):
        user1 = userData[userNames[i]]
        # Loop through users 1 -> n
        for j in range(len(userNames)):
            if (j+1 < len(userNames)):
                user2 = userData[userNames[j+1]]

                # Loop through all genres
                for genre in userData[userNames[i]]['genres']:
                    # Declare object for genre if it doesn't exist
                    if (genre not in user1['recommendations']):
                        user1['recommendations'][genre] = {}
                    # Declare not rated List
                    if (user1['similarityList'][genre][userNames[j+1]] >= 0.5):
                        notRatedList = user1['genres'][genre][genre_data_keys.notRatedList]

                        # Loop through all movies in the not rated List
                        for movie in notRatedList:
                            # if movie has not recommendation rating yet set to 0
                            if (movie not in user1['recommendations'][genre]):
                                user1['recommendations'][genre][movie] = 0
                            # If user2 has liked the movie add their similarity to the recommendation else subtract from ratio
                            if (movie in user2['genres'][genre][genre_data_keys.likedList]):
                                user1['recommendations'][genre][movie] += user1['similarityList'][genre][userNames[j+1]]
                            elif (movie in user2['genres'][genre][genre_data_keys.dislikedList]):
                                user1['recommendations'][genre][movie] -= user1['similarityList'][genre][userNames[j + 1]]



computeSimilarity()
computeReccomendations()


jsonData= {}
jsonData = json.dumps(userData)

# Print JSON to file
with open('similarityResults.json', 'w') as fp:
    json.dump(jsonData, fp)