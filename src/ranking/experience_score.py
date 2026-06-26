def calculate_experience_score(years):

    if 5 <= years <= 9:
        return 1.0

    if 4 <= years < 5:
        return 0.8

    if 9 < years <= 10:
        return 0.8

    if 3 <= years < 4:
        return 0.5

    if 10 < years <= 12:
        return 0.5

    return 0.2