
SELECT count(Title)
FROM Paper
WHERE Paper.ID in (
SELECT C.ID
from Citations as C, Authors as A
where A.ID =C.CITE_ID and A.FNAME='Lei' and A.LNAME='Yin' )


