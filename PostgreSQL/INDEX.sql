CREATE TABLE person (
    person_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    birthday date
);


CREATE INDEX person_first_name_idx
ON person (first_name);

SELECT count(*)
FROM person
WHERE first_name = 'Kevin'
    AND last_name = 'Xu';

CREATE INDEX person_first_name_last_name_idx
ON person (last_name, first_name);

SELECT count(*)
FROM person
WHERE last_name = 'Suzy'
    AND first_name = 'Zhou';

