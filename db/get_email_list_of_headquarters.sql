DROP PROCEDURE IF EXISTS get_email_list_of_headquarters;
DELIMITER //
CREATE PROCEDURE get_email_list_of_headquarters (
    IN p_cod_headquarters VARCHAR(50),
    IN p_cod_period       VARCHAR(50)
)
BEGIN
    -- Miembros: Usuarios asociados a la sede
    SELECT DISTINCT s.email AS email, 'MEMBER' AS tipo
    FROM school s
    JOIN school_headquarters_associate sha
      ON sha.cod_school       = s.cod_school
     AND sha.cod_headquarters = p_cod_headquarters
     AND sha.cod_period       = p_cod_period
    WHERE s.email IS NOT NULL AND s.email <> ''

    UNION ALL

    -- Propietarios: Emisores asociados a la sede
    SELECT DISTINCT es.email AS email, 'OWNER' AS tipo
    FROM email_sender es
    JOIN email_sender_headquarters esh
      ON esh.sender_id        = es.id
     AND esh.cod_headquarters = p_cod_headquarters
    WHERE es.is_active = TRUE
      AND es.role = 'OWNER'
      AND es.email IS NOT NULL AND es.email <> ''

    ORDER BY tipo DESC;  -- 'OWNER' primero y 'MEMBER' después
END //
DELIMITER ;
