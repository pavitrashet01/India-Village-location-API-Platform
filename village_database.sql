CREATE DATABASE village_db;
USE village_db;

/* Get all data */
SELECT * FROM villages;

/* Count all rows */
SELECT COUNT(*) FROM villages;

/*  Limit data */
SELECT * FROM villages LIMIT 10;


/*  Filter by state */
SELECT * 
FROM villages 
WHERE state_name = 'karnataka';

/*  Filter by district */
SELECT * 
FROM villages 
WHERE district_name = 'bangalore';

/*  Search village (VERY IMPORTANT ) */
SELECT * 
FROM villages 
WHERE area_name LIKE '%nagar%';


/* . Get unique states */
SELECT DISTINCT state_name 
FROM villages;

/*  Get districts of a state */
SELECT DISTINCT district_name 
FROM villages
WHERE state_name = 'karnataka';


/*  Get villages of a district */
SELECT area_name 
FROM villages
WHERE district_name = 'bangalore';

/*  Count villages per state */
SELECT state_name, COUNT(*) AS total_villages
FROM villages
GROUP BY state_name;


/*  Count districts per state */
SELECT state_name, COUNT(DISTINCT district_name) AS total_districts
FROM villages
GROUP BY state_name;


/* . Multi-filter  */
SELECT * 
FROM villages
WHERE state_name = 'karnataka'
AND district_name = 'bangalore';


/*  Pagination */
SELECT * 
FROM villages
LIMIT 10 OFFSET 20;