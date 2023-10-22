
WITH tmp AS( SELECT Count(ID) as count,ID,FNAME,LNAME
FROM Authors
GROUP BY FNAME,LNAME)

SELECT tmp.FNAME,tmp.LNAME
FROM tmp
WHERE tmp.count=1
