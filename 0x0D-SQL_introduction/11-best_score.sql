-- lists all records wit a score >= 10 from the "second_table"
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
