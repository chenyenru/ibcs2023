3 classes:
    student
    assignment
    subject

A subject has multiple students and assignments

1. student
   - ID
   - given name
   - family name
   - enrolled subjects
2. subject
   - subject name
   - students
   - student assignments

get_assignments_for_student(student_id) -> list of assignments
get_student_grade(student_id) -> float
show_grades() -> list of gardes for each subject
 - get_assignments_for_student(student_id)
3. assignment
   - assignment name
   - max marks
   - student marks
   - student ID
get_mean() -> float
get_student_grade(student_id) -> float
get_below(percent) -> list of student ids and marks
get_above(percent) -> list of student ids and marks

