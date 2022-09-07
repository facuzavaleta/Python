def grade(score):
    if score == 10:
        return "A+"
    elif score >= 9.5:
        return "A"
    elif score >= 9:
        return "B+"
    elif score >= 8.5:
        return "B"
    elif score >= 8:
        return "C+"
    elif score >= 7.5:
        return "C"
    else:
        return "D"

def applyGrade(scores):
    return list(map(grade, scores))

print(applyGrade([5, 8.7, 9, 7.8, 10, 9.2]))