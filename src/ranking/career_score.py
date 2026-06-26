LEVELS = {

    "intern":0,
    "associate":1,
    "junior":2,
    "engineer":3,
    "senior":4,
    "lead":5,
    "staff":6,
    "principal":7,
    "manager":8,
    "director":9

}


def calculate_career_score(history):

    score = 0

    previous = -1

    promotions = 0

    for job in reversed(history):

        title = job["title"].lower()

        current = previous

        for key,value in LEVELS.items():

            if key in title:

                current = value

                break

        if current > previous:

            promotions += 1

        previous = current

    return promotions / max(len(history),1)