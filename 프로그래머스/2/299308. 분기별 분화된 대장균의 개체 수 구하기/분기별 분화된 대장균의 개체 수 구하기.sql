SELECT 
QUARTER, 
COUNT(A.ID) AS ECOLI_COUNT FROM ECOLI_DATA AS A JOIN
(SELECT ID,CONCAT(QUARTER(DIFFERENTIATION_DATE) ,'Q') AS QUARTER FROM ECOLI_DATA) AS B ON A.ID = B.ID
GROUP BY QUARTER
ORDER BY QUARTER