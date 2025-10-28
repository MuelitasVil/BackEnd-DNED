DROP PROCEDURE IF EXISTS get_email_list_of_school;
DELIMITER //
CREATE PROCEDURE get_email_list_of_school (
    IN p_cod_school VARCHAR(50),
    IN p_cod_period VARCHAR(50)
)
BEGIN
    SELECT DISTINCT u.email AS email, 'MEMBER' AS tipo
    FROM unit_unal u
    JOIN unit_school_associate usa
      ON usa.cod_unit   = u.cod_unit
     AND usa.cod_school = p_cod_school
     AND usa.cod_period = p_cod_period
    WHERE u.email IS NOT NULL AND u.email <> ''

    UNION

    SELECT DISTINCT es.email AS email, 'OWNER' AS tipo
    FROM email_sender es
    JOIN email_sender_school ess
      ON ess.sender_id  = es.id
     AND ess.cod_school = p_cod_school
    WHERE es.is_active = TRUE
      AND es.role = 'OWNER'
      AND es.email IS NOT NULL AND es.email <> '';
END //
DELIMITER ;
