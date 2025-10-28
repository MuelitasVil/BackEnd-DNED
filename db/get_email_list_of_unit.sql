DROP PROCEDURE IF EXISTS get_email_list_of_unit;
DELIMITER //
CREATE PROCEDURE get_email_list_of_unit (
    IN p_cod_unit   VARCHAR(50),
    IN p_cod_period VARCHAR(50)
)
BEGIN
    SELECT DISTINCT uu.email_unal AS email, 'MEMBER' AS tipo
    FROM user_unal uu
    JOIN user_unit_associate uua
      ON uua.email_unal = uu.email_unal
     AND uua.cod_unit   = p_cod_unit
     AND uua.cod_period = p_cod_period
    WHERE uu.email_unal IS NOT NULL AND uu.email_unal <> ''

    UNION

    SELECT DISTINCT es.email AS email, 'OWNER' AS tipo
    FROM email_sender es
    JOIN email_sender_unit esu
      ON esu.sender_id = es.id
     AND esu.cod_unit  = p_cod_unit
    WHERE es.is_active = TRUE
      AND es.role = 'OWNER'
      AND es.email IS NOT NULL AND es.email <> '';
END //
DELIMITER ;
