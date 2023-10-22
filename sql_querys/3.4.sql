
SELECT Title
FROM Paper
WHERE Paper.id not in (
SELECT id
from Citations)

