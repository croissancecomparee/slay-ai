def get_score_color(score):
    if score >= 5:
        return "green"
    elif score >= 4:
        return "yellow"
    elif score >= 3:
        return "orange"
    elif score >= 2:
        return "red"
    elif score >= 1:
        return "darkred"
    elif score < 1:
        return "purple"
    else:
        return "gray"