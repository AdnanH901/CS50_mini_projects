-- *** The Lost Letter *** --
SELECT "address", "type" FROM "addresses"
WHERE "id" = (
    SELECT "address_id" FROM "scans"
    WHERE "action" = 'Drop' AND "package_id" = (
        SELECT "id" FROM "packages"
        WHERE "from_address_id" = (
            SELECT "id" FROM "addresses"
            WHERE "address" = '900 Somerville Avenue'
        )
    )
);

-- *** The Devious Delivery *** --
SELECT "contents" FROM "packages"
WHERE "from_address_id" IS NULL;

SELECT * FROM "addresses"
WHERE "id" IN (
    SELECT "address_id" FROM "scans"
    WHERE "package_id" IN (
        SELECT "id" FROM "packages"
        WHERE "from_address_id" IS NULL
    )
);

SELECT * FROM "scans"
WHERE "package_id" IN (
    SELECT "id" FROM "packages"
    WHERE "from_address_id" IS NULL
);

-- *** The Forgotten Gift *** --
SELECT "contents" FROM "packages"
WHERE "from_address_id" = (
    SELECT "id" FROM "addresses"
    WHERE "address" = "109 Tileston Street"
);

SELECT * FROM "addresses"
WHERE "id" = (
    SELECT "address_id" FROM "scans"
    WHERE "action" = 'Drop' AND "package_id" = (
        SELECT "id" FROM "packages"
        WHERE "from_address_id" = (
            SELECT "id" FROM "addresses"
            WHERE "address" = '109 Tileston Street'
        )
    )
);


select * from "drivers"
where "id" in (
    select distinct "driver_id" from "scans"
    where "action" = "Pick" AND "package_id" = (
        SELECT "id" FROM "packages"
        WHERE "contents" = "Flowers"
    )
);

