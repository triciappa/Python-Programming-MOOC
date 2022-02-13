# Write your solution here
import math

# Function to call user to enter the exam point and the exercises completed until
# the yser enter a empty line.
# The data is stored in a list.
def input_from_user():
    input_list = []
    while True:
        user_input = input ("Exam points and exercises completed: ")
        if user_input == "":
            break
        input_list.append(user_input)
    return input_list

def split_and_convert_int (my_list : list):
    str_grades = []
    # Separate de string of exam and exercises into two strings
    for string in my_list:
        for char in string.split(): 
            str_grades.append(char)
    
    num_grades=[]
    # Convert each string in the list to an integer
    for i in str_grades:
        num_grades.append(int(i))
    return num_grades

def grades_course (my_list : list):
    exam_index = 0
    exercise_index = 1
    grade_list = []
    total_points = []
    while exam_index < len (my_list):
        # The exercise poinst are based on 100 and 10% = 1pt, 20% = 2 pts... rounded down
        exercise_points = (my_list[exercise_index]*10)/100
        sum = my_list[exam_index] + math.trunc(exercise_points)
        total_points.append(sum)
        if sum <= 14 or my_list[exam_index] < 10:
            grade_list.append(0)
        elif sum >= 15 and sum <= 17 :
            grade_list.append(1)
        elif sum >= 18 and sum <= 20 :
            grade_list.append(2)
        elif sum >= 21 and sum <= 23 :
            grade_list.append(3)
        elif sum >= 24 and sum <= 27 :
            grade_list.append(4)
        elif sum >= 28 and sum <= 30 :
            grade_list.append(5)
        exam_index += 2
        exercise_index += 2

    return grade_list, total_points

def course_statistics (grades_list : list, points_list : list):
    points_average = sum (points_list) / len(points_list)
    count = len ([i for i in grades_list if i > 0])
    pass_percentage = (count / len (grades_list))*100 
    print ("Statistics:")
    print (f"Points average: {points_average:.1f}") 
    print (f"Pass percentage: {pass_percentage:.1f}")
    print ("Grade distribution:")
    index = 5
    while index >= 0:
        count_grade = len ([i for i in grades_list if i == index])
        aux = count_grade * "*"
        print (f"{index}: {aux}")
        index -= 1

def main ():
    user_results = input_from_user()
    grades_list = split_and_convert_int (user_results)
    grades, points = grades_course (grades_list)
    course_statistics (grades, points)

main ()
