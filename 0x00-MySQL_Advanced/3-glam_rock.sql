-- A SQL Script that ranks country origins of bands by fans:
-- Create a table called "users"
SELECT DISTINCT band_name, IFNULL(split, 2023) - IFNULL(formed, 0) as lifespan 
FROM metal_bands 
WHERE FIND_IN_SET('Glam rock', style)
