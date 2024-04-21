# SELECT E.EMP_NO, E.EMP_NAME, CASE WHEN AVG(G.SCORE) >= 96 THEN 'S'
#                                 WHEN AVG(G.SCORE) >= 90 THEN 'A'
#                                 WHEN AVG(G.SCORE) >= 86 THEN 'B'
#                                 ELSE 'C'
#                             END AS GRADE,
                            
#                             E.SAL * CASE WHEN AVG(G.SCORE) >= 96 THEN 0.2
#                                 WHEN AVG(G.SCORE) >= 90 THEN 0.15
#                                 WHEN AVG(G.SCORE) >= 86 THEN 0.1
#                                 ELSE 0
#                             END AS BONUS
                            
# FROM HR_EMPLOYEES E JOIN HR_GRADE G USING(EMP_NO)
#                     JOIN HR_DEPARTMENT D USING(DEPT_ID) 
# GROUP BY E.EMP_NO
# ORDER BY E.EMP_NO


select emp_no, emp_name
,   case 
        when avg(score) >= 96 then 'S'
        when avg(score) >= 90 then 'A'
        when avg(score) >= 80 then 'B'
        else 'C'
    end as grade
,   sal *
    case 
        when avg(score) >= 96 then 0.2
        when avg(score) >= 90 then 0.15
        when avg(score) >= 80 then 0.1
        else 0
    end as bonus
from hr_employees 
join hr_grade using(emp_no)
join hr_department using(dept_id)
group by emp_no
order by emp_no;