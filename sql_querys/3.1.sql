
SELECT Title
from Paper
where Paper.ID in(
SELECT ID 
from Authors
where Authors.FNAME='Minoru' and Authors.LNAME='Eto')
ORDER by Paper.LastUpdate ASC;

