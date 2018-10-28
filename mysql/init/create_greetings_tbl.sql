use greetingsdb;
CREATE TABLE greetings_tbl( gr_id INT NOT NULL AUTO_INCREMENT, gr_lang VARCHAR(100) NOT 
NULL, greeting  VARCHAR(100) NOT NULL, PRIMARY KEY ( gr_id ) );
INSERT INTO greetings_tbl (gr_id, gr_lang, greeting) VALUES (1, "En", "Hello World");
INSERT INTO greetings_tbl (gr_id, gr_lang, greeting) VALUES (2, "Fr", "Bonjour le monde");
INSERT INTO greetings_tbl (gr_id, gr_lang, greeting) VALUES (3, "Es", "Hola Mundo");
INSERT INTO greetings_tbl (gr_id, gr_lang, greeting) VALUES (4, "It", "Ciao mondo");
select * from greetings_tbl;

