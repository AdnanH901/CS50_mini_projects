SELECT COUNT("english_title") AS "number of titles containing ""Fuji"""FROM "views"
WHERE "artist" = 'Hokusai' AND "english_title" LIKE '%fuji%';
