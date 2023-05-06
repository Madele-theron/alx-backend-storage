-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser ( 
    IN user_id INT
)
BEGIN
    DECLARE avrg_score FLOAT;
    SET avrg_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);
    UPDATE users SET average_score = avrg_score WHERE id=user_id;
END $$
DELIMITER ;
