SELECT student.firstname, gender.name  as gender from student 
INNER JOIN  gender
ON gender.id=student.gender_id;


SELECT teacher.firstname, gender.name as gender  , department.name as department , position.name as position from teacher 
INNER JOIN  gender
ON gender.id=teacher.gender_id
INNER JOIN  department
ON department.id=teacher.department_id
INNER JOIN  position
ON position.id=teacher.position_id;;