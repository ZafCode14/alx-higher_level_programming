-- Dispalys the average temperature in F by city order
SELECT city, AVG(value) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
