CREATE VIEW june_vacancies AS
SELECT listing_id, property_type, host_name, COUNT(available) AS "days_vacant"
FROM listings
JOIN availabilities ON availabilities.listing_id = listings.id
WHERE "date" LIKE '2023-06-%'
AND available = "TRUE"
GROUP BY host_name
limit 15;

