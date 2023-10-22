
WITH tmp AS (SELECT  ID,Count(ID) as cnt
FROM Authors
WHERE Authors.ID
IN(SELECT ID
FROM Authors
WHERE Authors.FNAME='Indranath' and Authors.LNAME='Sengupta'
GROUP BY ID)
GROUP BY ID)

SELECT ID,tmp.cnt
FROM tmp
WHERE tmp.cnt<3