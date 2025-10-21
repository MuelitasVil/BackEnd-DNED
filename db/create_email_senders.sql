-- ==========================
-- CARGA DE CORREOS (sin nombre)
-- ==========================
INSERT IGNORE INTO email_sender (email, name) VALUES
('boletin_un@unal.edu.co',               NULL),
('comdninfoa_nal@unal.edu.co',           NULL),
('enviosvri_nal@unal.edu.co',            NULL),
('rectorinforma@unal.edu.co',            NULL),
('comunicado_csu_bog@unal.edu.co',       NULL),
('reconsejobu_nal@unal.edu.co',          NULL),
('dninfoacad_nal@unal.edu.co',           NULL),
('dgt_dned@unal.edu.co',                 NULL),
('gruposeguridad_nal@unal.edu.co',       NULL),
('sisii_nal@unal.edu.co',                NULL),
('postmaster_unal@unal.edu.co',          NULL),
('postmasterdnia_nal@unal.edu.co',       NULL),
('protecdatos_na@unal.edu.co',           NULL),
('infraestructurati_dned@unal.edu.co',   NULL),
('dre@unal.edu.co',                      NULL),
('dned@unal.edu.co',                     NULL),
('estudiantilcsu@unal.edu.co',           NULL),
('estudiantilca@unal.edu.co',            NULL),

-- Medellín
('alertas_med@unal.edu.co',                              NULL),
('informa_biblioteca@unal.edu.co',                       NULL),
('informa_comunicaciones@unal.edu.co',                   NULL),
('informa_direccion_administrativa@unal.edu.co',         NULL),
('informa_direccion_laboratorios@unal.edu.co',           NULL),
('informa_fac_ciencias_humanas_y_economicas@unal.edu.co',NULL),
('informa_juridica@unal.edu.co',                         NULL),
('inf_aplicaciones_med@unal.edu.co',                     NULL),
('informa_vicerrectoria@unal.edu.co',                    NULL),
('informa_bienestar_universitario@unal.edu.co',          NULL),
('infservcomp_med@unal.edu.co',                          NULL),
('inflogistica_med@unal.edu.co',                         NULL),
('informa_fac_ciencias@unal.edu.co',                     NULL),
('informa_fac_minas@unal.edu.co',                        NULL),
('informa_fac_ciencias_agrarias@unal.edu.co',            NULL),
('info_aplica_med@unal.edu.co',                          NULL),
('informa_secretaria_sede@unal.edu.co',                  NULL),
('innovaacad_med@unal.edu.co',                           NULL),
('unalternativac_nal@unal.edu.co',                       NULL),
('pcm@unal.edu.co',                                      NULL),
('postmaster_med@unal.edu.co',                           NULL),
('infeducontinua@unal.edu.co',                           NULL),
('informa_direccion_academica@unal.edu.co',              NULL),
('informa_direccion_de_investigacion_y_extension@unal.edu.co', NULL),
('informa_direccion_ordenamiento_y_desarrollo_fisico@unal.edu.co', NULL),
('informa_fac_arquitectura@unal.edu.co',                 NULL),
('informa_registro_y_matricula@unal.edu.co',             NULL),
('informa_unimedios@unal.edu.co',                        NULL),
('infpersonal_med@unal.edu.co',                          NULL),
('reestudia_med@unal.edu.co',                            NULL),

-- Manizales
('ventanilla_man@unal.edu.co',   NULL),
('bienestar_man@unal.edu.co',    NULL),
('planea_man@unal.edu.co',       NULL),
('postmaster_man@unal.edu.co',   NULL),
('vicsede_man@unal.edu.co',      NULL),
('estudiantilcs_man@unal.edu.co',NULL),

-- Palmira
('unnoticias_pal@unal.edu.co',   NULL),
('postmaster_pal@unal.edu.co',   NULL),
('estudiantilcs_pal@unal.edu.co',NULL),

-- Orinoquía
('divcultural_ori@unal.edu.co',  NULL),

-- La Paz
('secsedelapaz@unal.edu.co',     NULL),
('sedelapaz@unal.edu.co',        NULL),
('tics_paz@unal.edu.co',         NULL),
('vicesedelapaz@unal.edu.co',    NULL),

-- Bogotá
('divulgaciondrm_bog@unal.edu.co', NULL),
('reprecarrera_bog@unal.edu.co',   NULL),
('comunicaciones_bog@unal.edu.co', NULL),
('diracasede_bog@unal.edu.co',     NULL),
('dircultural_bog@unal.edu.co',    NULL),
('notificass_bog@unal.edu.co',     NULL),
('postmaster_bog@unal.edu.co',     NULL);

-- ==========================
-- CARGA DE CORREOS CON NOMBRE (Facultades Bogotá)
-- Si ya existe el correo, actualiza el 'name'
-- ==========================
INSERT INTO email_sender (email, name) VALUES
('correo_fchbog@unal.edu.co', 'Facultad de Ciencias Humanas - Bogotá'),
('correo_fibog@unal.edu.co',  'Facultad de Ingeniería - Bogotá'),
('correo_fcbog@unal.edu.co',  'Facultad de Ciencias - Bogotá'),
('correo_farbog@unal.edu.co', 'Facultad de Artes - Bogotá'),
('correo_fcebog@unal.edu.co', 'Facultad de Ciencias Económicas - Bogotá'),
('correo_fmbog@unal.edu.co',  'Facultad de Medicina - Bogotá'),
('correo_fdbog@unal.edu.co',  'Facultad de Derecho, Ciencias Políticas y Sociales - Bogotá'),
('correo_fmvbog@unal.edu.co', 'Facultad de Medicina Veterinaria y de Zootecnia - Bogotá'),
('correo_fcabog@unal.edu.co', 'Facultad de Ciencias Agrarias - Bogotá'),
('correo_febog@unal.edu.co',  'Facultad de Enfermería - Bogotá'),
('correo_fobog@unal.edu.co',  'Facultad de Odontología - Bogotá')
ON DUPLICATE KEY UPDATE
  name = VALUES(name);
