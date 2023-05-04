
-- A SQL Script that ranks country origins of bands by fans:
-- Create a table called "users"

SELECT band_name, IFNULL(split, NOW()) - formed as lifespan 
FROM metal_bands WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC

--  IFNULL(`split`, 2020) - `formed`
-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Requirements:


-- Column names must be: band_name and lifespan (in years)
-- You should use attributes formed and split for computing the lifespan
-- Your script can be executed on any database