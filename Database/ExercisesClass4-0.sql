-- Remover a tabela FILMES se ela existir
DROP TABLE Filmes;

-- Criar a tabela FILMES
CREATE TABLE Filmes
(
    cod_filme NUMBER(5),
    titulo    VARCHAR(250),
    ano       NUMBER(4),
    diretor   VARCHAR(100),
    genero    VARCHAR(80),
    atoresPrincipais VARCHAR(1000),
    duracao   NUMBER(4), -- em minutos
    valorIngresso    NUMBER(5,2)
);

-- Inserir valores na tabela FILMES
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(1, 'Cosmopolis', 2012, 'David Cronenberg', 'Drama', 'Robert Pattinson, Juliette Binoche, Sarah Gadon, Mathieu Amalric', 108, 22.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(2, 'The Awakening', 2012, 'Nick Murphy', 'Horror', 'Rebecca Hall, Dominic West, Imelda Staunton, Lucy Cohu', 107, 29.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(3, 'The Shawshank Redemption', 1994, 'Frank Darabont', 'Drama,Crime', 'Tim Robbins, Morgan Freeman and Bob Gunton', 142, 25.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(4, 'Pulp Fiction', 1994, 'Quentin Tarantino', 'Crime,Thriller', 'John Travolta, Uma Thurman and Samuel L. Jackson', 154, 29.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(5, 'One Flew Over the Cuckoos Nest', 1975, 'Milos Forman', 'Drama', 'Jack Nicholson, Louise Fletcher and Michael Berryman', 133, 55.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(6, 'Inception', 2010, 'Christopher Nolan', 'Action', 'Leonardo DiCaprio, Joseph Gordon-Levitt and Ellen Page', 148, 79.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(7, 'Fight Club', 1999, 'David Fincher', 'Drama', 'Brad Pitt, Edward Norton and Helena Bonham Carter', 139, 75.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(8, 'Casablanca', 1942, 'Michael Curtiz', 'Drama', 'Humphrey Bogart, Ingrid Bergman and Paul Henreid', 102, 62.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(9, 'The Matrix', 1999, 'Andy Wachowski, Lana Wachowski', 'Action', 'Keanu Reeves, Laurence Fishburne and Carrie-Anne Moss', 136, 28.99);
INSERT INTO Filmes (cod_filme, titulo, ano, diretor, genero, atoresPrincipais, duracao, valorIngresso) VALUES
(10, 'Se7en', 1995, 'David Fincher', 'Crime', 'Morgan Freeman, Brad Pitt and Kevin Spacey', 127, 42.99);

-- Selecionar todos os registros da tabela FILMES
SELECT * FROM Filmes;

-- Selecionar o título, o ano e o diretor de todos os filmes
SELECT titulo, ano, diretor FROM Filmes;

-- Selecionar os filmes de horror de 2012
SELECT * FROM Filmes WHERE ano = 2012 AND genero = 'Horror';

--O título e o ano dos filmes com duração maior do que 2 horas
SELECT titulo, ano FROM FIlmes WHERE duracao > 120;

--o título e a duração dos dramas lançados na década de 1990 com pelo menos 1 hora e 20 minutos de duração, dos diretores cujos nomes começam pela letra ‘D’
SELECT titulo, duracao FROM Filmes WHERE ano BETWEEN 1990 AND 1999 AND duracao >= 80 AND genero LIKE '%Drama%' AND diretor LIKE 'D%';

--o título, o gênero e o valor do ingresso dos filmes a partir de 2006, mostrando os valores inflacionados em 8,63%.
SELECT titulo, genero, valorIngresso, valorIngresso * 1.0863 AS valorInflacionado FROM Filmes WHERE ano >= 2006;

--a quantidade de filmes de ação com ingressos que custam mais do que R$ 20,00.
SELECT COUNT(*) AS quantidade_filmes FROM Filmes WHERE genero LIKE '%Action%' AND valorIngresso > 20.00;

--os nomes de todos os diretores cadastrados, sem repetir, e em ordem alfabética.
SELECT DISTINCT diretor FROM Filmes ORDER BY diretor;

--aumentar em 10 minutos a duração dos filmes em que participa o ator Morgan Freeman.
UPDATE Filmes SET duracao = duracao + 10 WHERE atoresPrincipais LIKE '%Morgan Freeman%';

--Dar um desconto de 10% para os filmes de drama do ano 2012
UPDATE Filmes SET valorIngresso = valorIngresso * 0.9 WHERE genero LIKE '%Drama%' AND ano = 2012;

--Acrescentar um asterisco (*) no final dos títulos dos filmes com duração menor ou igual a 120 minutos
UPDATE Filmes SET titulo = titulo || '*' WHERE duracao <= 120;

--Excluir os filmes com valor de ingresso superior a R$ 60,00
DELETE FROM Filmes WHERE valorIngresso > 60.00;

--Excluir os filmes em cujo título aparece a palavra “assombrado” ou cujo sobrenome do diretor é “David Fincher”
DELETE FROM Filmes WHERE titulo LIKE '%assombrado%' OR diretor LIKE '%David Fincher%';

SELECT * FROM Filmes



