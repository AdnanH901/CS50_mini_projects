SELECT COUNT("first_name") AS "number of players who batted with one hand and threw with the other"
FROM "players"
WHERE ("bats" = 'R' AND "throws" = 'L') OR ("bats" = 'L' AND "throws" = 'R')
