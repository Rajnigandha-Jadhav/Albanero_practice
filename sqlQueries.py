# To fetch all columns from employees table of "my_first_database" database...
# SELECT * FROM my_first_database.employees;

# To fetch all columns from employees table having the maximum salary...
# SELECT * FROM my_first_database.employees where employee_salary =(select max(employee_salary) from my_first_database.employees);


# To fetch all columns from employees table having name that starts with alphabet R...
# select * from employees where employee_name like "R%";


# To fetch only 2 columns from employees table having the second maximum salary...
# SELECT EMPLOYEE_id, employee_salary from employees order by 2 desc limit 1,1;

# To fetch all columns from employees table having the second maximum salary...
# SELECT *
# FROM employees
# ORDER BY employee_salary DESC
# LIMIT 1 OFFSET 0;


# To fetch all columns from employees table having the salary in range...
# select * from employees where employee_salary in (8000,12000);


# select * from employees;


# create table copy_table as select * from employees;


# select * from copy_table;


# select * from employees where employee_salary between 8000 and 12000;


# delete from employees where employee_id in(1,2);


# select * from employees;