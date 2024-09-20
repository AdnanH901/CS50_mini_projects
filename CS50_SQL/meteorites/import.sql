CREATE TABLE "meteorites_temp" (
    "name" TEXT NOT NULL,
    id INTEGER,
    nametype TEXT NOT NULL,
    class TEXT NOT NULL,
    mass FLOAT,
    discovery TEXT,
    "year" INTEGER CHECK("year" >= 0),
    lat FLOAT,
    long FLOAT,
    PRIMARY KEY(id)
);

CREATE TABLE "meteorites" (
    "name" TEXT NOT NULL,
    id INTEGER,
    class TEXT NOT NULL,
    mass FLOAT,
    discovery TEXT,
    "year" INTEGER CHECK("year" >= 0),
    lat FLOAT,
    long FLOAT,
    PRIMARY KEY(id)
);

.import --csv --skip 1 meteorites.csv meteorites_temp

UPDATE meteorites_temp
SET "name" = NULL
WHERE "name" LIKE '';
UPDATE meteorites_temp
SET "id" = NULL
WHERE "id" LIKE '';
UPDATE meteorites_temp
SET "nametype" = NULL
WHERE "nametype" LIKE '';
UPDATE meteorites_temp
SET "class" = NULL
WHERE "class" LIKE '';
UPDATE meteorites_temp
SET "mass" = NULL
WHERE "mass" LIKE '';
UPDATE meteorites_temp
SET "discovery" = NULL
WHERE "discovery" LIKE '';
UPDATE meteorites_temp
SET "year" = NULL
WHERE "year" LIKE '';
UPDATE meteorites_temp
SET "lat" = NULL
WHERE "lat" LIKE '';
UPDATE meteorites_temp
SET "long" = NULL
WHERE "long" LIKE '';

UPDATE meteorites_temp
SET mass   = ROUND(mass,   2),
    "year" = ROUND("year", 2),
    lat    = ROUND(lat,    2),
    long   = ROUND(long,   2);

DELETE FROM meteorites_temp
WHERE nametype LIKE '%relict%';

INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long" FROM "meteorites_temp"
ORDER BY "year", "name";
