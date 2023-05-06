-- A SQL Script that creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE w_avrg_score FLOAT;
    SET w_avrg_score = (SELECT SUM(score * weight) / SUM(weight)
        FROM users AS U
        JOIN corrections AS C ON U.id=C.user_id
        JOIN projects AS P on C.project_id=P.id
        WHERE U.id=user_id);
    UPDATE users SET average_score = w_avrg_score WHERE id=user_id;
END $$
