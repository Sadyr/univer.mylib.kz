

def get_total_mark_by_semester(courses, course_gpa_dict):
    mult_sum = 1
    sum_credits = 0
    for course in courses:
        sum_course = 0
        sum_course = course.gpa + course.credit
        mult_sum = mult_sum * sum_course
        sum_credits = sum_credits + course.credit
    total_mark_by_semester = mult_sum / sum_credits
    return total_mark_by_semester



    
