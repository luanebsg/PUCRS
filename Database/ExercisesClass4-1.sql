-- Remover a tabela ALUNOS se ela existir
DROP TABLE ALUNOS CASCADE CONSTRAINTS;

-- Remover a tabela ESTADOS se ela existir
DROP TABLE ESTADOS CASCADE CONSTRAINTS;

-- Remover a tabela CIDADES se ela existir
DROP TABLE CIDADES CASCADE CONSTRAINTS;

-- Criar a tabela ALUNOS
CREATE TABLE ALUNOS
(
    nroMatricula VARCHAR(10) NOT NULL,
    cpf VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    nome VARCHAR(150) NOT NULL,
    anoIngresso NUMBER(4) NOT NULL,
    endereco VARCHAR(150) NULL,
    sexo CHAR(1) NOT NULL,
    CONSTRAINT PK_ALUNOS PRIMARY KEY (nroMatricula),
    CONSTRAINT AK1_ALUNOS UNIQUE (cpf),
    CONSTRAINT AK2_ALUNOS UNIQUE (email)
);

-- Inserir valores na tabela ALUNOS
INSERT INTO ALUNOS (nroMatricula, cpf, email, nome, anoIngresso, endereco, sexo) VALUES ('10085', '5091', 'exemplo@gmail.com', 'João', 2022, 'Rua A', 'M');
INSERT INTO ALUNOS (nroMatricula, cpf, email, nome, anoIngresso, endereco, sexo) VALUES ('10086', '5092', 'exemplo1@gmail.com', 'Maria', 2022, 'Rua A', 'F');

-- Selecionar todos os registros da tabela ALUNOS
SELECT * FROM ALUNOS;

-- Adicionar restrições de verificação (CHECK)
ALTER TABLE ALUNOS
ADD CONSTRAINT CK_AnoIngr CHECK (anoIngresso > 2000);

ALTER TABLE ALUNOS
ADD CONSTRAINT CK_sexo CHECK (sexo IN ('M', 'F'));

-- Criar a tabela ESTADOS
CREATE TABLE ESTADOS
(
    uf CHAR(2) NOT NULL,
    nome1 VARCHAR(40) NOT NULL,
    regiao CHAR(2) NOT NULL,
    CONSTRAINT PK_ESTADOS PRIMARY KEY (uf)
);

-- Inserir valores na tabela ESTADOS
INSERT INTO ESTADOS VALUES ('RS', 'Rio Grande do Sul', 'S');

-- Selecionar todos os registros da tabela ESTADOS
SELECT * FROM ESTADOS;

-- Criar a tabela CIDADES
CREATE TABLE CIDADES
(
    cod_cidade NUMBER(4) NOT NULL,
    nome1 VARCHAR(60) NOT NULL,
    uf CHAR(2) NULL,
    CONSTRAINT PK_CIDADES PRIMARY KEY (cod_cidade)
);

-- Adicionar a restrição de chave estrangeira (FOREIGN KEY)
ALTER TABLE CIDADES
ADD CONSTRAINT FK_EST_CID
    FOREIGN KEY (uf)
    REFERENCES ESTADOS (uf);

-- Selecionar todos os registros da tabela CIDADES
SELECT * FROM CIDADES;
