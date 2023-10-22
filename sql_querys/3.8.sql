
WITH tmp AS(
SELECT ID,Count(ID) as Count
FROM   Authors
GROUP BY ID)

SELECT  Title
FROM Paper,tmp
WHERE tmp.Count=1 and tmp.ID=Paper.ID


