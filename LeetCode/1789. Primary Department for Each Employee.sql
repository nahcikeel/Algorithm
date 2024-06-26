SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING count(department_id) = 1
UNION
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
ORDER BY employee_id
