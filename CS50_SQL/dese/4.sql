SELECT COUNT("name") AS "number of schools", "city" FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
ORDER BY COUNT("name") DESC, "city"
LIMIT 10;


