CREATE TABLE secret_user(
    user_id int,
    first_name varchar,
    last_name varchar,
    code_name varchar,
    country varchar,
    organisation varchar,
    salary varchar,
    knows_kung_fu bool
)

INSERT INTO secret_user VALUES
(1, 'Jimmy', 'Bond', '007', 'United Kingdom', 'MI6', 97200, 'false')

UPDATE secret_user 
SET first_name = 'James'
WHERE user_id = 1;

INSERT INTO secret_user 
(user_id , first_name ,last_name ,country , organisation , salary , knows_kung_fu )
VALUES (4, 'Jack', 'Ryan', 'United States', 'CIA', 85000, false);

UPDATE secret_user 
SET code_name = 'Neo 2.0', salary = 115000
WHERE first_name = 'Jack' AND last_name = 'Ryan';

UPDATE secret_user 
SET knows_kung_fu = TRUE 
WHERE user_id IN (1);

UPDATE secret_user 
SET salary = 1.1*salary;

SELECT sum(salary)
FROM secret_user;