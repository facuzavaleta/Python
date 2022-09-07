def grade(score):
    if score == 10:
        return "A+"
    elif score >= 9:
        return "A"
    elif score >= 8:
        return "B+"
    elif score >= 7:
        return "B"
    elif score >= 6:
        return "C+"
    else:
        return "No aprobado"

def passedSubject(subject):
    return (subject[1] >= 6)

def applyGrade(scores):
    passed = dict(filter(passedSubject, scores.items()))
    subjects = map(str.upper, passed.keys())
    grades = map(grade, passed.values())
    return dict(zip(subjects, grades))

print(applyGrade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))