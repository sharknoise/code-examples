-- https://ru.hexlet.io/challenges/rdb_basics_rich_employees/
-- Напишите SQL запрос который найдет имена всех работников, 
-- которые получают больше чем их менеджеры. 
-- Если у работника нет менеджера, они не должны попадать в выборку.

--mine
SELECT e1.name FROM employees AS e1
  JOIN employees as e2 
  ON e1.manager_id = e2.id
  AND e1.salary > e2.salary;

--teacher
SELECT employees.name
FROM employees JOIN employees AS manager ON (employees.manager_id = manager.id)
WHERE employees.salary > manager.salary;