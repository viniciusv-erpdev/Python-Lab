student_scores = [88, 73]
student_names = ['Paul', 'Ernest']

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    list_names_scores = []
    i = 0
    j = 0

    for i in range(len(student_scores)):
        j += 1
        score = str(student_scores[i])
        name = student_names[i]
        list_names_scores.append(str(j) + "." + " " + name + ":" + " " + score)
        i += 1

    return list_names_scores


#list_names_scores.append(str(i) + "." + " " + name + ":" + " " + str(score))
print(student_ranking(student_scores, student_names))
