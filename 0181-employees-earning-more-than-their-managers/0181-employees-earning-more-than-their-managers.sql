# Write your MySQL query statement below
select e1.Name as Employee
FROM Employee as e1, Employee as e2
WHERE e1.managerId = e2.id and e1.salary > e2.salary