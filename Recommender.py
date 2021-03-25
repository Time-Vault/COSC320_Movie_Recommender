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

jsonData= {}
for user in userData:
    jsonData[user] = json.dumps(userData[user])

# Print JSON to file
with open('similarityResults.json', 'w') as fp:
    json.dump(jsonData, fp)