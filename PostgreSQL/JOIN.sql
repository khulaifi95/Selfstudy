CREATE TABLE martian (
    martian_id int,
    first_name varchar,
    last_name varchar,
    base_id int,
    super_id int
);

CREATE TABLE base (
    base_id int,
    base_name varchar,
    founded int
);

INSERT INTO martian VALUES
(1, 'Ray', 'Bradbury', 1, null);

INSERT INTO base VALUES
(1, 'Tharsisland', 2037);

INSERT INTO martian VALUES
(13, 'John', 'Carter', NULL, 8)

INSERT INTO base VALUES
(5, 'Olympus Mons Spa & Casino', null)

SELECT first_name , last_name , base_name FROM martian 
INNER JOIN base
ON martian.base_id = base.base_id;

 inner, left, right and full join

SELECT m.martian_id , b.base_id , b.base_name 
FROM martian AS m
FULL JOIN base AS b
ON m.base_id = b.base_id;

CREATE TABLE visitor (
    visitor_id int,
    host_id int,
    first_name varchar,
    last_name varchar
);

CREATE TABLE inventory (
     base_id int,
     supply_id int,
     quantity int
);

CREATE TABLE supply (
    supply_id int,
    name varchar,
    description varchar,
    quantity int
);

SELECT v.first_name AS visitor_fn, v.last_name AS visitor_ln, 
       m.first_name AS martian_fn, m.last_name AS martian_ln
FROM visitor AS v
LEFT JOIN martian AS m
ON v.host_id = m.martian_id;

SELECT m.first_name AS fn, m.last_name AS ln,
       s.first_name AS super_fn, s.last_name AS super_ln
FROM martian AS m
LEFT JOIN martian AS s
ON m.super_id = s.martian_id 
WHERE super_fn IS NOT NULL
ORDER BY m.martian_id;

SELECT s.supply_id , i.quantity, s.name, s.description 
FROM (SELECT * FROM inventory WHERE base_id = 1) AS i
RIGHT JOIN supply AS s
ON i.supply_id = s.supply_id
ORDER BY s.supply_id;

SELECT ISNULL(i.quantity, 0) FROM 

SELECT v.first_name AS v_fn, v.last_name AS v_ln,
       m.first_name AS m_fn, m.last_name AS m_ln
FROM visitor AS v
FULL JOIN martian AS m
ON v.host_id = m.martian_id 
WHERE m.martian_id IS NULL OR v.visitor_id IS NULL;



