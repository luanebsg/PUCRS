-- Criação do banco de dados
CREATE DATABASE escola_jiu_jitsu;

-- Selecionar o banco de dados
\c escola_jiu_jitsu;

-- Drop tables se existirem
DROP TABLE IF EXISTS planejamento_treinos;
DROP TABLE IF EXISTS treinos;
DROP TABLE IF EXISTS presencas;
DROP TABLE IF EXISTS pagamentos;
DROP TABLE IF EXISTS alunos;

-- Criação da tabela de Alunos
CREATE TABLE alunos (
    aluno_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    email VARCHAR(100),
    data_matricula DATE NOT NULL
);

-- Criação da tabela de Pagamentos
CREATE TABLE pagamentos (
    pagamento_id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES alunos(aluno_id),
    data_pagamento DATE NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    metodo_pagamento VARCHAR(50) NOT NULL
);

-- Criação da tabela de Presenças
CREATE TABLE presencas (
    presenca_id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES alunos(aluno_id),
    data_presenca DATE NOT NULL
);

-- Criação da tabela de Treinos
CREATE TABLE treinos (
    treino_id SERIAL PRIMARY KEY,
    data_treino DATE NOT NULL,
    horario TIME NOT NULL,
    tipo_treino VARCHAR(100) NOT NULL,
    instrutor VARCHAR(100) NOT NULL
);

-- Criação da tabela de Planejamento de Treinos
CREATE TABLE planejamento_treinos (
    planejamento_id SERIAL PRIMARY KEY,
    treino_id INT REFERENCES treinos(treino_id),
    aluno_id INT REFERENCES alunos(aluno_id)
);
-- Inserção de alunos
INSERT INTO alunos (nome, data_nascimento, endereco, email, data_matricula) VALUES 
('João Pedro Gonçalves', '1983-04-11', 'Setor Souza, 2', 'dda-mata@gmail.com', '2012-02-26'),
('Esther Moraes', '1989-01-27', 'Avenida Pietra Farias, 3', 'marcos-vinicius87@gmail.com', '2016-06-08'),
('Mirella Jesus', '1992-03-28', 'Rua de Vieira, 839', 'cecilia64@gmail.com', '2012-10-28'),
('Rebeca da Rosa', '2010-05-01', 'Lagoa Rocha, 3', 'cda-luz@gmail.com', '2018-09-17'),
('Dra. Maria Julia Fernandes', '2019-06-12', 'Recanto Pinto, 84', 'zporto@gmail.com', '2022-07-22'),
('João Vitor da Rocha', '1988-10-10', 'Avenida Nascimento, 6', 'michelleferreira@gmail.com', '2019-11-05'),
('Dr. Samuel Batista', '1988-06-29', 'Residencial Caroline, 46', 'juliamoura@gmail.com', '2015-12-28'),
('Nicolas Pires', '2010-01-29', 'Praça da Conceição, 14', 'valentim23@gmail.com', '2022-01-06'),
('Dr. Joaquim Martins', '1998-02-05', 'Vale Monteiro, 9', 'melisapatricia@gmail.com', '2021-07-06'),
('Julia Monteiro', '1981-09-06', 'Ladeira Barbosa, 63', 'mauricioaraujo@gmail.com', '2012-02-11'),
('Dr. César Oliveira', '1997-10-04', 'Conjunto Sueli, 77', 'vinicius95@gmail.com', '2016-08-04'),
('Fábio Cavalcanti', '2014-03-19', 'Rua de Santiago, 733', 'beth-lisboa@gmail.com', '2014-02-05'),
('Cauã Jesus', '2001-10-19', 'Travessa Jardim, 92', 'fernando-carvalho@gmail.com', '2014-10-17'),
('Sofia Fernandes', '1979-05-26', 'Rua Sônia, 55', 'gabriella87@gmail.com', '2014-11-24'),
('Laura da Luz', '1988-12-22', 'Travessa Vitório, 308', 'susana06@gmail.com', '2015-02-05'),
('Beatriz Souza', '1988-11-06', 'Vila Barros, 9', 'esteves61@gmail.com', '2015-07-15'),
('Carlos Pinto', '2010-02-28', 'Vila Carmem, 289', 'emanuel-pinheiro@gmail.com', '2019-01-22'),
('Sr. Alex Costa', '2012-12-18', 'Jardim Ana, 2', 'ayla-monteiro@gmail.com', '2016-04-28'),
('Dra. Esther Oliveira', '2015-12-06', 'Recanto Barbosa, 20', 'regina74@gmail.com', '2015-08-26'),
('Larissa Almeida', '1988-12-16', 'Rua Eufrásio, 36', 'gabriella15@gmail.com', '2011-07-06'),
('Tereza Ferreira', '1979-01-22', 'Residencial Campos, 32', 'fernanda30@gmail.com', '2012-11-06'),
('Breno da Conceição', '2012-08-13', 'Parque Ricardo, 2', 'cleber-leal@gmail.com', '2010-09-01'),
('Breno da Mota', '1980-05-20', 'Praça Bianchi, 764', 'lbueno@gmail.com', '2010-04-09'),
('Cauã Cavalcanti', '1987-06-23', 'Residencial Geraldo, 93', 'andreina-figueiredo@gmail.com', '2021-06-22'),
('Bárbara Santos', '2018-05-05', 'Vila Norma, 554', 'pamela-ribeiro@gmail.com', '2020-07-12'),
('Renato Rocha', '1981-09-29', 'Residencial Raquel, 181', 'freitascarla@gmail.com', '2015-05-04'),
('Larissa da Mata', '1980-08-11', 'Rua Souza, 836', 'kparanhos@gmail.com', '2017-12-27'),
('Sofia Oliveira', '2018-08-15', 'Travessa Nova, 39', 'emanoel73@gmail.com', '2021-07-24'),
('Enzo Cavalcanti', '1987-07-20', 'Jardim Sueli, 10', 'mariannalmeida@gmail.com', '2014-02-05'),
('Manuela Farias', '2015-10-01', 'Rua Ana, 80', 'joaquim78@gmail.com', '2018-10-28'),
('Evelyn Oliveira', '2004-12-19', 'Setor Prado, 240', 'sabrina-figueiredo@gmail.com', '2015-11-08'),
('Letícia da Paz', '1996-12-23', 'Vila Pinto, 220', 'inesferreira@gmail.com', '2011-12-18'),
('João Pereira', '2004-02-27', 'Parque Daniel, 334', 'alcantarastephany@gmail.com', '2014-02-28'),
('Sr. Raul Carvalho', '1997-12-16', 'Praça Fernandes, 663', 'ddelgado@gmail.com', '2010-02-11'),
('Cauã Lima', '1991-04-05', 'Lagoa Elisa, 617', 'enrique72@gmail.com', '2022-12-15'),
('Matheus Ferreira', '1984-01-11', 'Rua do Prado, 6', 'mirian87@gmail.com', '2011-01-20'),
('Davi Moraes', '1996-06-04', 'Travessa Almeida, 320', 'elias29@gmail.com', '2017-05-15'),
('Yasmin Correia', '2006-01-29', 'Vila Eduardo, 647', 'thais-araujo@gmail.com', '2011-09-25'),
('Enrico da Paz', '2006-01-19', 'Avenida Mário, 2', 'damaris-costa@gmail.com', '2010-08-15'),
('Alice da Mata', '1988-10-05', 'Praça Eduardo, 56', 'helenacarvalho@gmail.com', '2021-08-23'),
('Isabella Castro', '1985-10-05', 'Recanto Nogueira, 60', 'ribeirobruna@gmail.com', '2014-04-01'),
('Rodrigo Pires', '2011-01-01', 'Jardim Cecília, 66', 'emanuel-pinheiro@gmail.com', '2011-05-21'),
('Matheus Rodrigues', '2004-10-23', 'Vale Stela, 77', 'franciscacorreia@gmail.com', '2018-04-17'),
('Sarah Ferreira', '1998-12-17', 'Rua Severino, 20', 'smota@gmail.com', '2017-06-01'),
('Miguel Almeida', '1983-08-04', 'Rua Luiza, 6', 'daniel07@gmail.com', '2020-02-05'),
('Theo da Rocha', '1991-05-06', 'Rua Matos, 73', 'jose-araujo@gmail.com', '2018-06-22'),
('Rafael Cunha', '2015-02-23', 'Praça Monteiro, 992', 'amaria32@gmail.com', '2017-06-02'),
('Leonardo Barros', '2014-11-16', 'Travessa Pietra, 39', 'ebatista@gmail.com', '2011-02-25'),
('Helena da Rosa', '2001-11-27', 'Conjunto Tatiane, 598', 'damarispires@gmail.com', '2012-06-07'),
('Matheus Rocha', '1992-04-11', 'Travessa Novo, 33', 'bnoel@gmail.com', '2010-09-19'),
('Gabriel Cavalcanti', '1994-07-09', 'Travessa da Mata, 90', 'caldeira86@gmail.com', '2011-10-09');

-- Inserção de pagamentos
INSERT INTO pagamentos (aluno_id, data_pagamento, valor, metodo_pagamento) VALUES 
(1, '2024-07-29', 150.00, 'PIX'),
(2, '2024-07-29', 150.00, 'PIX'),
(3, '2024-07-29', 150.00, 'PIX'),
(4, '2024-07-29', 150.00, 'PIX'),
(5, '2024-07-29', 150.00, 'Boleto Bancário'),
(6, '2024-07-29', 150.00, 'PIX'),
(7, '2024-07-29', 150.00, 'PIX'),
(8, '2024-07-29', 150.00, 'Cartão de Crédito'),
(9, '2024-07-29', 150.00, 'PIX'),
(10, '2024-07-29', 150.00, 'PIX'),
(11, '2024-07-29', 150.00, 'Boleto Bancário'),
(12, '2024-07-29', 150.00, 'PIX'),
(13, '2024-07-29', 150.00, 'PIX'),
(14, '2024-07-29', 150.00, 'Cartão de Crédito'),
(15, '2024-07-29', 150.00, 'PIX'),
(16, '2024-07-29', 150.00, 'PIX'),
(17, '2024-07-29', 150.00, 'Boleto Bancário'),
(18, '2024-07-29', 150.00, 'PIX'),
(19, '2024-07-29', 150.00, 'PIX'),
(20, '2024-07-29', 150.00, 'PIX'),
(21, '2024-07-29', 150.00, 'Cartão de Crédito'),
(22, '2024-07-29', 150.00, 'PIX'),
(23, '2024-07-29', 150.00, 'PIX'),
(24, '2024-07-29', 150.00, 'Boleto Bancário'),
(25, '2024-07-29', 150.00, 'PIX'),
(26, '2024-07-29', 150.00, 'PIX'),
(27, '2024-07-29', 150.00, 'Cartão de Crédito'),
(28, '2024-07-29', 150.00, 'PIX'),
(29, '2024-07-29', 150.00, 'PIX'),
(30, '2024-07-29', 150.00, 'Boleto Bancário'),
(31, '2024-07-29', 150.00, 'PIX'),
(32, '2024-07-29', 150.00, 'PIX'),
(33, '2024-07-29', 150.00, 'Cartão de Crédito'),
(34, '2024-07-29', 150.00, 'PIX'),
(35, '2024-07-29', 150.00, 'PIX'),
(36, '2024-07-29', 150.00, 'Boleto Bancário'),
(37, '2024-07-29', 150.00, 'PIX'),
(38, '2024-07-29', 150.00, 'PIX'),
(39, '2024-07-29', 150.00, 'Cartão de Crédito'),
(40, '2024-07-29', 150.00, 'PIX'),
(41, '2024-07-29', 150.00, 'PIX'),
(42, '2024-07-29', 150.00, 'Boleto Bancário'),
(43, '2024-07-29', 150.00, 'PIX'),
(44, '2024-07-29', 150.00, 'PIX'),
(45, '2024-07-29', 150.00, 'Cartão de Crédito'),
(46, '2024-07-29', 150.00, 'PIX'),
(47, '2024-07-29', 150.00, 'PIX'),
(48, '2024-07-29', 150.00, 'Boleto Bancário'),
(49, '2024-07-29', 150.00, 'PIX'),
(50, '2024-07-29', 150.00, 'PIX');

-- Inserção de presenças
INSERT INTO presencas (aluno_id, data_presenca) VALUES 
(1, '2024-07-29'),
(2, '2024-07-29'),
(3, '2024-07-29'),
(4, '2024-07-29'),
(5, '2024-07-29'),
(6, '2024-07-29'),
(7, '2024-07-29'),
(8, '2024-07-29'),
(9, '2024-07-29'),
(10, '2024-07-29'),
(11, '2024-07-29'),
(12, '2024-07-29'),
(13, '2024-07-29'),
(14, '2024-07-29'),
(15, '2024-07-29'),
(16, '2024-07-29'),
(17, '2024-07-29'),
(18, '2024-07-29'),
(19, '2024-07-29'),
(20, '2024-07-29'),
(21, '2024-07-29'),
(22, '2024-07-29'),
(23, '2024-07-29'),
(24, '2024-07-29'),
(25, '2024-07-29'),
(26, '2024-07-29'),
(27, '2024-07-29'),
(28, '2024-07-29'),
(29, '2024-07-29'),
(30, '2024-07-29'),
(31, '2024-07-29'),
(32, '2024-07-29'),
(33, '2024-07-29'),
(34, '2024-07-29'),
(35, '2024-07-29'),
(36, '2024-07-29'),
(37, '2024-07-29'),
(38, '2024-07-29'),
(39, '2024-07-29'),
(40, '2024-07-29'),
(41, '2024-07-29'),
(42, '2024-07-29'),
(43, '2024-07-29'),
(44, '2024-07-29'),
(45, '2024-07-29'),
(46, '2024-07-29'),
(47, '2024-07-29'),
(48, '2024-07-29'),
(49, '2024-07-29'),
(50, '2024-07-29');

-- Inserção de treinos
INSERT INTO treinos (data_treino, horario, tipo_treino, instrutor) VALUES 
('2024-07-01', '20:00:00', 'Treino de Resistência', 'Carlos Pereira'),
('2024-07-03', '20:00:00', 'Treino de Técnica', 'Maria Santos'),
('2024-07-05', '20:00:00', 'Treino de Resistência', 'Carlos Pereira'),
('2024-07-08', '20:00:00', 'Treino de Técnica', 'Maria Santos'),
('2024-07-10', '20:00:00', 'Treino de Resistência', 'Carlos Pereira'),
('2024-07-12', '20:00:00', 'Treino de Técnica', 'Maria Santos'),
('2024-07-15', '20:00:00', 'Treino de Resistência', 'Carlos Pereira'),
('2024-07-17', '20:00:00', 'Treino de Técnica', 'Maria Santos'),
('2024-07-19', '20:00:00', 'Treino de Resistência', 'Carlos Pereira'),
('2024-07-22', '20:00:00', 'Treino de Técnica', 'Maria Santos'),
('2024-07-24', '20:00:00', 'Treino de Resistência', 'Carlos Pereira'),
('2024-07-26', '20:00:00', 'Treino de Técnica', 'Maria Santos');

-- Inserção de planejamento de treinos
INSERT INTO planejamento_treinos (treino_id, aluno_id) VALUES 
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 6),
(2, 7),
(2, 8),
(2, 9),
(2, 10),
(3, 11),
(3, 12),
(3, 13),
(3, 14),
(3, 15),
(4, 16),
(4, 17),
(4, 18),
(4, 19),
(4, 20),
(5, 21),
(5, 22),
(5, 23),
(5, 24),
(5, 25),
(6, 26),
(6, 27),
(6, 28),
(6, 29),
(6, 30),
(7, 31),
(7, 32),
(7, 33),
(7, 34),
(7, 35),
(8, 36),
(8, 37),
(8, 38),
(8, 39),
(8, 40),
(9, 41),
(9, 42),
(9, 43),
(9, 44),
(9, 45),
(10, 46),
(10, 47),
(10, 48),
(10, 49),
(10, 50);
-- Consulta para verificar todas as informações dos alunos
SELECT * FROM alunos;

-- Consulta para verificar pagamentos de um aluno específico
SELECT * FROM pagamentos WHERE aluno_id = 1;

-- Consulta para verificar a presença de um aluno específico
SELECT * FROM presencas WHERE aluno_id = 2;

-- Consulta para verificar o planejamento de treinos de um aluno específico
SELECT * FROM planejamento_treinos WHERE aluno_id = 1;

-- Consulta para verificar treinos agendados
SELECT * FROM treinos WHERE data_treino >= CURRENT_DATE;

-- Relatório de todos os pagamentos realizados
SELECT alunos.nome, pagamentos.data_pagamento, pagamentos.valor, pagamentos.metodo_pagamento
FROM pagamentos
JOIN alunos ON pagamentos.aluno_id = alunos.aluno_id;

-- Relatório de presença dos alunos
SELECT alunos.nome, presencas.data_presenca
FROM presencas
JOIN alunos ON presencas.aluno_id = alunos.aluno_id;

-- Relatório de planejamento de treinos
SELECT alunos.nome, treinos.data_treino, treinos.horario, treinos.tipo_treino, treinos.instrutor
FROM planejamento_treinos
JOIN alunos ON planejamento_treinos.aluno_id = alunos.aluno_id
JOIN treinos ON planejamento_treinos.treino_id = treinos.treino_id;
