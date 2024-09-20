SELECT "english_title" AS 'Lowest contrast'
FROM "views"
WHERE "artist" = 'Hokusai'
ORDER BY "contrast" ASC
LIMIT 5;

