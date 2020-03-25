CREATE TABLE song(
    song_id int,
    title varchar,
    artist varchar,
    album varchar,
    year_released int,
    duration numeric,
    tempo numeric,
    loudness numeric
);

COPY song FROM '/home/kevinxu95/Selfstudy/PostgreSQL/data/songs.csv' DELIMITER ',' CSV HEADER;

SELECT DISTINCT year_released
FROM song ORDER BY year_released;

SELECT count(*) FROM song 
WHERE year_released = 0;

DELETE FROM song
WHERE year_released = 0; 

SELECT min(tempo), max(tempo) FROM song;

DELETE FROM song
WHERE tempo = 0;

SELECT min(loudness), max(loudness) FROM song;

SELECT count(*) FROM song
WHERE loudness > 0;

DELETE FROM song
WHERE loudness > 0;

SELECT year_released, round(AVG(tempo)) FROM song
GROUP BY year_released
ORDER BY year_released;



