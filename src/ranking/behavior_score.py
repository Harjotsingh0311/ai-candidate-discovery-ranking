def normalize(value, maximum):

    if value <= 0:
        return 0

    return min(value / maximum, 1)


def calculate_behavior_score(signals):

    github = normalize(
        max(signals.get("github_activity_score", 0), 0),
        100
    )

    recruiter_response = signals.get(
        "recruiter_response_rate",
        0
    )

    interview_completion = signals.get(
        "interview_completion_rate",
        0
    )

    profile_complete = normalize(
        signals.get(
            "profile_completeness_score",
            0
        ),
        100
    )

    open_to_work = float(
        signals.get(
            "open_to_work_flag",
            False
        )
    )

    recruiter_saved = normalize(
        signals.get(
            "saved_by_recruiters_30d",
            0
        ),
        30
    )

    search_count = normalize(
        signals.get(
            "search_appearance_30d",
            0
        ),
        100
    )

    profile_views = normalize(
        signals.get(
            "profile_views_received_30d",
            0
        ),
        100
    )

    offer_acceptance = max(
        signals.get(
            "offer_acceptance_rate",
            0
        ),
        0
    )

    score = (

        0.20 * github +

        0.15 * recruiter_response +

        0.15 * interview_completion +

        0.10 * profile_complete +

        0.10 * open_to_work +

        0.10 * recruiter_saved +

        0.10 * search_count +

        0.05 * profile_views +

        0.05 * offer_acceptance

    )

    return score