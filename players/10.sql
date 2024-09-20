/*
Write an SQL query that selects  the first  name,  last name,
and debut date of players who were born in the United States,
bat with  their right hand,  and weigh more than  200 pounds.
Rename the  column  for debut date to  "start_date" and order
the   results   by   the   debut  date  in  ascending  order.
*/

SELECT "first_name", "last_name", "debut" AS "start_date"
FROM "players"
WHERE "birth_country" = "USA" AND "bats" = "R" AND "weight" > 200
ORDER BY "debut";
