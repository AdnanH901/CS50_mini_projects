SELECT COUNT("english_title")AS "number of titles containing ""Eastern Capital"""
FROM "views"
WHERE "artist" = 'Hiroshige' AND "english_title" LIKE '%Eastern Capital%';
