-- https://ru.hexlet.io/challenges/rdb_basics_highest_salary
-- Напишите SQL запрос который найдет самые большие зарплаты для каждого департамента.
-- name 	salary
-- IT 	90000
-- Sales 	80000

SELECT departments.name, MAX(employees.salary) as salary
  FROM departments
  JOIN employees ON employees.department_id = departments.id
  GROUP BY departments.id;