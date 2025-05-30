-- 코드를 작성해주세요
WITH RECURSIVE GEN AS(
SELECT ID,1 AS GENERATION,PARENT_ID FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
UNION
    SELECT ECOLI_DATA.ID,GENERATION+1,ECOLI_DATA.PARENT_ID FROM ECOLI_DATA JOIN
    GEN ON ECOLI_DATA.PARENT_ID = GEN.ID
)
SELECT COUNT(*) - COUNT(B.ID) AS COUNT, A.GENERATION FROM GEN AS A LEFT JOIN GEN AS B
ON A.GENERATION = B.GENERATION -1 AND A.ID = B.PARENT_ID

GROUP BY A.GENERATION
ORDER BY A.GENERATION
