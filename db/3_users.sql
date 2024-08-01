INSERT INTO users (id, first_name, middle_name, last_name, username, email, password) VALUES 
	(1, 'Евгений', 'Олегович', 'Иванов', 'test', 'admin@internal.portal', encode(sha256('test'::bytea), 'hex')),
	(2, 'Григорий', 'Евгеньевич', 'Тротиллов', 'tost', 'analitic@internal.portal', encode(sha256('tost'::bytea), 'hex')),
	(3, 'Леонид', 'Ролеплеевич', 'Пахомов', 'tist', 'tech_support@internal.portal', encode(sha256('tist'::bytea), 'hex')),
	(4, 'Даниил', 'Николаевич', 'Иванов', 'tast', 'ml_sotr1@internal.portal', encode(sha256('tast'::bytea), 'hex')),
	(5, 'Леонид', 'Нуборпшевич', 'Ленниферстов', 'tyst', 'guest@internal.portal', encode(sha256('tyst'::bytea), 'hex'));