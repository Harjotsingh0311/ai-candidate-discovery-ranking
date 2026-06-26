PRODUCT = {

    "google",
    "amazon",
    "meta",
    "microsoft",
    "uber",
    "swiggy",
    "zomato",
    "flipkart",
    "atlassian",
    "linkedin",
    "apple",
    "netflix",
    "airbnb"

}

CONSULTING = {

    "tcs",
    "infosys",
    "wipro",
    "capgemini",
    "accenture",
    "cognizant",
    "hcl"

}


def calculate_company_score(history):

    score = 0

    for job in history:

        company = job["company"].lower()

        if any(
            p in company
            for p in PRODUCT
        ):
            score += 1

        if any(
            c in company
            for c in CONSULTING
        ):
            score -= 1

    return score / max(len(history), 1)