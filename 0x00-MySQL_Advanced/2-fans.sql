-- A SQL Script that ranks country origins of bands by fans:
-- Create a table called "users"

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC

-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

-- Requirements:

-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans



-- SELECT origin AS origin, SUM(fans) AS nb_fans 
-- FROM metal_bands 
-- GROUP BY origin 
-- ORDER BY nb_fans DESC;

-- SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
-- GROUP BY `origin`
-- ORDER BY `nb_fans` DESC;