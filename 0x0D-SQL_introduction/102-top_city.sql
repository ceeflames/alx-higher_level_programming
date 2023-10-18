-- This displays the 3 cities with the highest avg
-- temp between July and August.
SELECT city, AVG(value) AS avg_temp
FROM temperatures WHERE month = 7 OR month = 8
GROUP By city ORDER BY avg_temp DESC LIMIT 3;
