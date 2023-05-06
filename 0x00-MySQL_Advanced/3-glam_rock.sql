-- A SQL Script that shows all bands that has Glam Rock as style
-- in order of lifespan
SELECT band_name, IFNULL(split, 2023) - IFNULL(formed, 0) AS lifespan 
FROM metal_bands 
WHERE style LIKE '%Glam rock%';
