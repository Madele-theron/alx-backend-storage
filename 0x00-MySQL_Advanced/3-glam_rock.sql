-- A SQL Script that ranks country origins of bands by fans:
-- Create a table called "users"

SELECT DISTINCT band_name, DATEDIFF(IFNULL(split, NOW()), formed) as lifespan 
FROM metal_bands WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC
