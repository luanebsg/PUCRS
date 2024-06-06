-- Primeiro, drop as tabelas em ordem inversa à de criação devido às constraints
DROP TABLE Alocacao_Equipamento CASCADE CONSTRAINTS;
DROP TABLE Funcionario CASCADE CONSTRAINTS;
DROP TABLE Obra CASCADE CONSTRAINTS;
DROP TABLE Equipamento CASCADE CONSTRAINTS;
DROP TABLE Construtora CASCADE CONSTRAINTS;

-- Criar a tabela Construtora
CREATE TABLE Construtora (
    id_construtora NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL
);

-- Criar a tabela Obra
CREATE TABLE Obra (
    id_obra NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    fk_construtora NUMBER NOT NULL,
    CONSTRAINT fk_construtora FOREIGN KEY (fk_construtora) REFERENCES Construtora(id_construtora)
);

-- Criar a tabela Funcionario
CREATE TABLE Funcionario (
    id_funcionario NUMBER PRIMARY KEY,
    cpf VARCHAR2(11) NOT NULL UNIQUE,
    nome VARCHAR2(100) NOT NULL,
    salario NUMBER(10, 2) NOT NULL,
    fk_obra NUMBER NOT NULL,
    CONSTRAINT fk_obra FOREIGN KEY (fk_obra) REFERENCES Obra(id_obra)
);

-- Criar a tabela Equipamento
CREATE TABLE Equipamento (
    id_equipamento NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    categoria VARCHAR2(50) NOT NULL
);

-- Criar a tabela Alocacao_Equipamento
CREATE TABLE Alocacao_Equipamento (
    id_alocacao NUMBER PRIMARY KEY,
    fk_equipamento NUMBER NOT NULL,
    fk_obra NUMBER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_diaria NUMBER(10, 2) NOT NULL,
    CONSTRAINT fk_equipamento FOREIGN KEY (fk_equipamento) REFERENCES Equipamento(id_equipamento),
    CONSTRAINT fk_obra_alocacao FOREIGN KEY (fk_obra) REFERENCES Obra(id_obra)
);


-- 2) Criar os dados de uma construtora que tenha o seu nome (nome do aluno) e inserir os dados na tabela correspondente;

INSERT INTO Construtora (id_construtora, nome) VALUES (1, 'Luane Barcellos de Souza Gordo');

-- 3) Criar 2 obras e 5 funcionários para cada uma dessas obras (i.e. 10 funcionários no total);  

-- Criar duas obras
INSERT INTO Obra (id_obra, nome, fk_construtora) VALUES (1, 'Obra A', 1);
INSERT INTO Obra (id_obra, nome, fk_construtora) VALUES (2, 'Obra B', 1);

-- Criar funcionários para a Obra A
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (1, '11111111111', 'Carlos', 3100, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (2, '11111111112', 'Marcelo', 2530, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (3, '11111111113', 'Rodrigo', 2480, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (4, '11111111114', 'Fernando', 2700, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (5, '11111111115', 'Matheus', 2895, 1);

-- Criar funcionários para a Obra B
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (6, '22222222221', 'Gabriel', 1000, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (7, '22222222222', 'Júnior', 1500, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (8, '22222222223', 'Hyago', 2656, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (9, '22222222224', 'Pedro', 2420, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (10, '22222222225', 'João', 1910, 2);

-- 4) Alocar pelo menos 4 equipamentos (de categorias diferentes) à primeira obra que você criou;

-- Criar equipamentos
INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (1, 'Escavadeira', 'Terraplanagem');
INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (2, 'Betoneira', 'Concretagem');
INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (3, 'Guindaste', 'Içamento');
INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (4, 'Compactador', 'Compactação');

-- Alocar equipamentos à primeira obra
INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (1, 1, 1, TO_DATE('2024-06-01', 'YYYY-MM-DD'), TO_DATE('2024-06-15', 'YYYY-MM-DD'), 1000);
INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (2, 2, 1, TO_DATE('2024-06-01', 'YYYY-MM-DD'), TO_DATE('2024-06-10', 'YYYY-MM-DD'), 500);
INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (3, 3, 1, TO_DATE('2024-06-05', 'YYYY-MM-DD'), TO_DATE('2024-06-20', 'YYYY-MM-DD'), 1500);
INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (4, 4, 1, TO_DATE('2024-06-10', 'YYYY-MM-DD'), TO_DATE('2024-06-25', 'YYYY-MM-DD'), 800);

--5) Gerar um script SQL compatível com o SBGB Oracle para popular as tabelas;

-- Script completo

DROP TABLE Alocacao_Equipamento CASCADE CONSTRAINTS;
DROP TABLE Funcionario CASCADE CONSTRAINTS;
DROP TABLE Obra CASCADE CONSTRAINTS;
DROP TABLE Equipamento CASCADE CONSTRAINTS;
DROP TABLE Construtora CASCADE CONSTRAINTS;


CREATE TABLE Construtora (
    id_construtora NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL
);


CREATE TABLE Obra (
    id_obra NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    fk_construtora NUMBER NOT NULL,
    CONSTRAINT fk_construtora FOREIGN KEY (fk_construtora) REFERENCES Construtora(id_construtora)
);


CREATE TABLE Funcionario (
    id_funcionario NUMBER PRIMARY KEY,
    cpf VARCHAR2(11) NOT NULL UNIQUE,
    nome VARCHAR2(100) NOT NULL,
    salario NUMBER(10, 2) NOT NULL,
    fk_obra NUMBER NOT NULL,
    CONSTRAINT fk_obra FOREIGN KEY (fk_obra) REFERENCES Obra(id_obra)
);


CREATE TABLE Equipamento (
    id_equipamento NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    categoria VARCHAR2(50) NOT NULL
);


CREATE TABLE Alocacao_Equipamento (
    id_alocacao NUMBER PRIMARY KEY,
    fk_equipamento NUMBER NOT NULL,
    fk_obra NUMBER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_diaria NUMBER(10, 2) NOT NULL,
    CONSTRAINT fk_equipamento FOREIGN KEY (fk_equipamento) REFERENCES Equipamento(id_equipamento),
    CONSTRAINT fk_obra_alocacao FOREIGN KEY (fk_obra) REFERENCES Obra(id_obra)
);


INSERT INTO Construtora (id_construtora, nome) VALUES (1, 'Luane Barcellos de Souza Gordo');


INSERT INTO Obra (id_obra, nome, fk_construtora) VALUES (1, 'Obra A', 1);
INSERT INTO Obra (id_obra, nome, fk_construtora) VALUES (2, 'Obra B', 1);


INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (1, '11111111111', 'Carlos', 3100, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (2, '11111111112', 'Marcelo', 2530, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (3, '11111111113', 'Rodrigo', 2480, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (4, '11111111114', 'Fernando', 2700, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (5, '11111111115', 'Matheus', 2895, 1);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (6, '22222222221', 'Gabriel', 1000, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (7, '22222222222', 'Júnior', 1500, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (8, '22222222223', 'Hyago', 2656, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (9, '22222222224', 'Pedro', 2420, 2);
INSERT INTO Funcionario (id_funcionario, cpf, nome, salario, fk_obra) VALUES (10, '22222222225', 'João', 1910, 2);


INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (1, 'Escavadeira', 'Terraplanagem');
INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (2, 'Betoneira', 'Concretagem');
INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (3, 'Guindaste', 'Içamento');
INSERT INTO Equipamento (id_equipamento, nome, categoria) VALUES (4, 'Compactador', 'Compactação');


INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (1, 1, 1, TO_DATE('2024-06-01', 'YYYY-MM-DD'), TO_DATE('2024-06-15', 'YYYY-MM-DD'), 1000);
INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (2, 2, 1, TO_DATE('2024-06-01', 'YYYY-MM-DD'), TO_DATE('2024-06-10', 'YYYY-MM-DD'), 500);
INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (3, 3, 1, TO_DATE('2024-06-05', 'YYYY-MM-DD'), TO_DATE('2024-06-20', 'YYYY-MM-DD'), 1500);
INSERT INTO Alocacao_Equipamento (id_alocacao, fk_equipamento, fk_obra, data_inicio, data_fim, valor_diaria) 
VALUES (4, 4, 1, TO_DATE('2024-06-10', 'YYYY-MM-DD'), TO_DATE('2024-06-25', 'YYYY-MM-DD'), 800);



-- 6) Codificar em SQL quatro das seguintes consultas (escolha apenas 4 das 6 consultas abaixo; se você responder mais de 4, apenas as 4 primeiras serão consideradas):


--a) Selecionar CPFs e nomes dos trabalhadores que ganham mais do que 2.500,00;

SELECT cpf, nome
FROM Funcionario
WHERE salario > 2500;

--  b) Selecionar nomes e salários dos trabalhadores da empresa ALFA, ordenados em ordem alfabética crescente;

SELECT f.nome, f.salario
FROM Funcionario f
JOIN Obra o ON f.fk_obra = o.id_obra
JOIN Construtora c ON o.fk_construtora = c.id_construtora
WHERE c.nome = 'Luane Barcellos de Souza Gordo'
ORDER BY f.nome ASC;

-- d) Calcular e exibir a folha de pagamento de cada obra. Uma folha de pagamento é determinada pela soma dos salários dos seus trabalhadores.

SELECT o.nome AS obra, SUM(f.salario) AS folha_pagamento
FROM Funcionario f
JOIN Obra o ON f.fk_obra = o.id_obra
GROUP BY o.nome;

--  e) Selecionar os equipamentos que nunca foram utilizados em nenhuma obra.

SELECT e.nome
FROM Equipamento e
LEFT JOIN Alocacao_Equipamento ae ON e.id_equipamento = ae.fk_equipamento
WHERE ae.id_alocacao IS NULL;


