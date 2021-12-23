3 classes:
    student
    assignment
    subject


A subject has multiple students and multiple assignments
A student can be in multiple subject
Each student in a subject will have one of every assignment

So the _Student_ object will be in charge of those data, and other objects will only be accessing it


student
    ID
    given name
    family name
    enrolled subkects

    get_assignments_for_student(student_id) -> list of assignments
    get_student_grader(student_id) -> float

subject
    subject name
    students
    student assignments

    get_assignments_for_student(student_id)

assignment
    assignment name
    max marks
    student marks {
        student id : student mark
    }

    get_mean() -> float
    get_student_grade(student_id) -> float
    get_below(percent) -> list of student ids and marks
    get_above(percent) -> list fo student ids and marks


    CSV - Comma separated values
    JSON - 
      {
         "students" :[
             {
                 "id": "my_id",
                 "family name":
             }
         ]
       }