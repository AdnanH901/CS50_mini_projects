SELECT "english_title" AS 'Print Title'
FROM "views"
WHERE "brightness" >= 0.5
ORDER BY "contast" DESC
LIMIT 5;
