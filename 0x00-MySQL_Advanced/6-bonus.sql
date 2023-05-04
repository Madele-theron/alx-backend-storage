-- SQL script that creates a stored procedure AddBonus 
-- that adds a new correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)

BEGIN
    DECLARE project_id INT;

    -- Check if project name exists:
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- If the project name does not exist, insert it and get it's id:
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Add correction to user
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$

DELIMITER ;
