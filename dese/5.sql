SELECT "city", COUNT("name") AS "number of schools" FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
HAVING COUNT("name") < 4
ORDER BY "number of schools" DESC, "city";

