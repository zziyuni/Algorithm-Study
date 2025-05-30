-- 코드를 입력하세요
WITH RECURSIVE TIME AS(
SELECT 0 AS HOUR
    UNION ALL
SELECT HOUR +1 FROM TIME
    WHERE HOUR <23
)
SELECT HOUR, COUNT(ANIMAL_ID) AS COUNT FROM TIME LEFT JOIN ANIMAL_OUTS
ON TIME.HOUR = HOUR(DATETIME) 
GROUP BY TIME.HOUR
ORDER BY TIME.HOUR