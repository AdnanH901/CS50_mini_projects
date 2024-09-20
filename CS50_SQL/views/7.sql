SELECT "english_title" AS 'Brightest prints'
FROM "views"
WHERE "artist" = 'Hiroshige'
ORDER BY "brightness" DESC
LIMIT 5;
