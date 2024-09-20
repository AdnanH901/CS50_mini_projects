CREATE TABLE IF NOT EXISTS "passengers" (
    "id"         INTEGER,
	"first_name" TEXT,
	"last_name"  TEXT,
	"age"        TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "check-ins" (
	"date"      NUMERIC,
	"flight_id" INTEGER,
    FOREIGN KEY 
	FOREIGN KEY ("flight_id") REFERENCES "flights"("id")
);

CREATE TABLE IF NOT EXISTS "airlines" (
	"id"      INTEGER,
	"name"    TEXT,
	"section" TEXT,
	PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS "flights" (
    "id"             INTEGER,
	"flight_no"      INTEGER,
	"airline_id"     INTEGER,
	"code_from"      TEXT,
	"code_to"        TEXT,
	"date"           NUMERIC,
	"departure_date" NUMERIC,
    "arrival_date"   NUMERIC,
    PRIMARY KEY("id"),
	FOREIGN KEY ("airline_id") REFERENCES "airlines"("id")
);
