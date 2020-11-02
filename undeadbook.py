# __author__ = 'sm2743'
# Lab 5
# Sierra Fiacco and Brittany Brandriff

import time
book = {}

# should print the status and parameters


def update(book, status, audience, userid):
    timestamp = time.time()
    likes = []
    postid = str(timestamp) + userid
    post = [status, audience, userid, timestamp, likes]
    book[postid] = post
    print("Post made at", timestamp, "by", userid)
    return postid


# should count the number of likes based on the user id


def like(book, id, userid):
    post = book[id]
    post[4]
    if userid in post[4]:
        pass
    else:
        post[4].append(userid)


# should count the number of unlikes based on the user id


def unlike(book, id, userid):
    post = book[id]
    post[4]
    if userid in post[4]:
        post[4].remove(userid)
    else:
        pass


def display(book, id):
    post = book[id]
    print("Time = ", post[3])
    print("Groups = ", post[1])
    print("Likes = ", len(post[4]))
    print(post[2], " says: ")
    print(post[0])


# test Code
barnabas_one = update(book,
                      "Storming the village at 9.  Anyone interested?",
                      ["Zombies", "Vampires"],
                      "BarnabusCollins")
time.sleep(1)

casper_one = update(book,
                    "Can I come?",
                    ["Vampires"],
                    "Casper")

time.sleep(1)

barnabas_two = update(book,
                      "Forgot to include the ghosts! LOL",
                      ["Ghosts"],
                      "BarnabasCollins")

time.sleep(1)

barnabas_three = update(book,
                        "Lots of villagers with forks here...",
                        ["Vampires", "Zombies", "Ghosts"],
                        "BarnabasCollins")

like(book, barnabas_one, "Edmund")
like(book, barnabas_one, "Grimm")
like(book, barnabas_one, "Edmund")
like(book, casper_one, "Edmund")
like(book, casper_one, "Grimm")
like(book, casper_one, "Harry")
like(book, casper_one, "Cound Chocula")
like(book, barnabas_two, "Casper")
like(book, barnabas_three, "Casper")
like(book, barnabas_three, "Count Chocula")
like(book, barnabas_three, "Boo")

unlike(book, casper_one, "Edmund")
unlike(book, barnabas_three, "Casper")
unlike(book, casper_one, "Edmund")

display(book, barnabas_one)
display(book, barnabas_three)
print("-----")
display(book, casper_one)
