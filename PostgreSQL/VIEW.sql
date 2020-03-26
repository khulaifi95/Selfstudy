CREATE TABLE martian_confidential (
    martian_id int,
    first_name varchar,
    last_name varchar,
    base_id int,
    super_id int,
    salary int,
    dna_id varchar
);

--Security
CREATE VIEW martian_public AS
SELECT martian_id, first_name, last_name, base_id, super_id 
FROM martian_confidential;
SELECT * FROM martian_public;

--Simplicity
CREATE VIEW people_on_mars AS
SELECT concat('m', martian_id) AS id, first_name, last_name, 'Martian' AS status
FROM martian_public
    UNION
SELECT concat('v', visitor_id) AS id, first_name, last_name, 'Visitor' AS status 
FROM visitor;

--Multiple tables
CREATE VIEW base_storage AS
SELECT b.base_id, s.supply_id, s.name,
       COALESCE(
       (SELECT quantity FROM inventory
       WHERE base_id = b.base_id AND supply_id = s.supply_id ), 0)
       AS quantity
FROM base AS b
CROSS JOIN supply AS s;


