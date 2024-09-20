SELECT "first_name", "last_name", "debut"
FROM "players"
WHERE "birth_country" = 'USA' AND "birth_state" = 'PA' AND "birth_city" = 'Pittsburgh'
ORDER BY "debut" DESC, "first_name", "last_name"
