--Properly tested on LiveSQL.Oracle

DROP TABLE PESSOAS CASCADE CONSTRAINTS;

CREATE TABLE PESSOAS
(
    cpf VARCHAR(20) NOT NULL,
    nome VARCHAR(150) NOT NULL,
    idade NUMBER(3),
    endereco VARCHAR(150)
);

INSERT INTO PESSOAS (cpf, nome, idade, endereco)
VALUES ('32809', 'Maria', 25, 'Rua A, 20');

INSERT INTO PESSOAS (idade, endereco, cpf, nome)
VALUES (25, 'Rua A, 20', '30599', 'Pedro');

INSERT INTO PESSOAS (cpf, nome, idade, endereco)
VALUES ('29385', 'Carlos', NULL, NULL);

INSERT INTO PESSOAS (cpf, nome, idade, endereco)
VALUES ('39582', 'Alice', 80, NULL);

INSERT INTO PESSOAS (cpf, nome, idade, endereco)
VALUES ('78838', 'Antonio', NULL, 'Rua B, 80');

INSERT INTO PESSOAS (cpf, nome)
VALUES ('90038', 'Ana Paula');

INSERT INTO PESSOAS (cpf, nome, idade)
VALUES ('23487', 'Roberto Carlos', 18);

INSERT INTO PESSOAS (cpf, nome, endereco)
VALUES ('4363', 'Mario da Silva', 'Rua C, 50');

INSERT INTO PESSOAS (cpf, nome, endereco)
VALUES ('43639', 'Maria da Silva', 'Rua D, 52');

SELECT * FROM PESSOAS;

-- Names that start with the letter 'A':
SELECT *
FROM PESSOAS
WHERE nome LIKE 'A%';

-- Names that start with 'Ana':
SELECT *
FROM PESSOAS
WHERE nome LIKE 'Ana%';

-- Names that end with 'Silva':
SELECT *
FROM PESSOAS
WHERE nome LIKE '%Silva';

-- Names that contain 'Carlos':
SELECT *
FROM PESSOAS
WHERE nome LIKE '%Carlos%';

-- It can correspond to 'Maria' or 'Carlos':
SELECT *
FROM PESSOAS
WHERE nome LIKE 'Mari_ da Silva';

-- People with 25, 30 or 40 years old:
SELECT *
FROM PESSOAS
WHERE idade IN (25, 30, 40);

ALTER TABLE PESSOAS
DROP COLUMN idade;

SELECT * FROM PESSOAS;

ALTER TABLE PESSOAS
ADD sexo CHAR(1);

SELECT * FROM PESSOAS;

ALTER TABLE PESSOAS
MODIFY endereco VARCHAR(200);

DESC PESSOAS;

ALTER TABLE PESSOAS
ADD salario NUMBER(8,2) DEFAULT 1305.56 NOT NULL;

SELECT * FROM PESSOAS;