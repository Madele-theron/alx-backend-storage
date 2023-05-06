-- A SQL Script that shows all bands that has Glam Rock as style:
-- in order of lifespan
SELECT band_name, DATEDIFF(IFNULL(split, 2023), formed) AS lifespan 
FROM metal_bands 
WHERE style LIKE '%Glam rock%';