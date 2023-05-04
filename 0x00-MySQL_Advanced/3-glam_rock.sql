-- A SQL Script that shows all bands that has Glam Rock as style:
-- in order of lifespan
SELECT DISTINCT band_name, DATEDIFF(IFNULL(split, NOW()), formed) as lifespan 
FROM metal_bands 
WHERE style LIKE '%Glam rock%';
