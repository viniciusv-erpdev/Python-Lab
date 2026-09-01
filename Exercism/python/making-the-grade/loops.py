"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """

    scores_rounded = []

    for score in student_scores:
        scores_rounded.append(round(score))

    return scores_rounded


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    failed_students_counter = 0

    for score in student_scores:
        if score <= 40:
            failed_students_counter += 1

    return failed_students_counter


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    above_threshold = []

    for score in student_scores:
        if score >= threshold:
            above_threshold.append(score)

    return above_threshold


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    increment = round(((highest - 40)/4))
    min = 41 + increment
    letter_grades_list = []
    i = 0

    while i < 4:

        if i == 0:
            letter_grades_list.append(41)
            i += 1
        else:
            letter_grades_list.append(min)
            min += increment
            i += 1

    return letter_grades_list

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


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """

    perfect_studant_data = []
    i = 0

    for info in student_info:

        if i <= (len(student_info) - 1):

            if info[1] == 100:
                perfect_studant_data = info
                break

        i += 1  

    return perfect_studant_data
