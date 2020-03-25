COPY earthquake FROM '/home/kevinxu95/Selfstudy/PostgreSQL/data/earthquake.csv' 
DELIMITER ',' CSV HEADER;

SELECT * FROM earthquake LIMIT 10;

SELECT count(*) FROM earthquake;

SELECT count(DISTINCT place) FROM earthquake;

SELECT MIN(occurred_on), MAX(occurred_on) FROM earthquake;

SELECT MIN(magnitude), max(magnitude) FROM earthquake;

SELECT DISTINCT cause FROM earthquake;

SELECT count(*) FROM earthquake WHERE cause = 'earthquake';

SELECT * FROM earthquake WHERE cause = 'explosion';

SELECT place, magnitude, occurred_on FROM earthquake 
WHERE cause = 'nuclear explosion' ORDER BY occurred_on DESC LIMIT 10;

SELECT place, magnitude, occurred_on FROM earthquake
ORDER BY magnitude DESC LIMIT 10;

SELECT count(*) FROM earthquake
WHERE place LIKE '%Honshu%Japan%'
AND occurred_on BETWEEN '2011-03-11' AND '2011-03-18';
