-- A SQL Script that creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    UPDATE users AS U,
        (SELECT U.id, SUM(score * weight) / SUM|(weight) as w_avrg
        FROM users AS U
        JOIN corrections AS C ON U.id=C.user_id
        JOIN projects AS P ON C.project_id=P.id
        GROUP BY U.id
    AS WA
    SET U.average_score = WA.w_avrg
    WHERE U.id=WA.id
END $$
DELIMITER ;
