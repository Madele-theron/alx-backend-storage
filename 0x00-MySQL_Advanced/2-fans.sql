-- A SQL Script that ranks country origins of bands by fans:
-- Create a table called "users"

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
