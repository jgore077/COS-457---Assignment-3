
select count(id)-1
from Authors
where Authors.id in(SELECT id
FROM Authors 
WHERE Authors.FNAME='Wu' and Authors.LNAME='Wei')

