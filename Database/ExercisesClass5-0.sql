--- CRIAÇÃO DO BANCO
DROP TABLE cidades CASCADE CONSTRAINTS;
DROP TABLE estados CASCADE CONSTRAINTS;

CREATE TABLE estados 
(
    uf CHAR ( 2 ) NOT NULL,
    nome VARCHAR2 ( 40 ) NOT NULL,
    regiao CHAR ( 2 ) NOT NULL,
    CONSTRAINT PK_ESTADOS PRIMARY KEY (uf)
);

CREATE TABLE cidades 
(
    cod_cidade NUMBER ( 4 ) NOT NULL,
    nome VARCHAR2 ( 60 ) NOT NULL,
    uf CHAR ( 2 ),
    CONSTRAINT PK_CIDADES PRIMARY KEY (cod_cidade)
);

ALTER TABLE cidades ADD ( CONSTRAINT FK_EST_CID FOREIGN KEY (uf) REFERENCES estados (uf));

---------- Estados----------
insert into estados values ('AC','Acre','N');
insert into estados values ('AL','Alagoas','NE');
insert into estados values ('AP','Amapá','N');
insert into estados values ('AM','Amazonas','N');
insert into estados values ('BA','Bahia','NE');
insert into estados values ('CE','Ceará','NE');
insert into estados values ('DF','Distrito Federal','CO');
insert into estados values ('ES','Espírito Santo','SE');
insert into estados values ('GO','Goiás','CO');
insert into estados values ('MA','Maranhão','NE');
insert into estados values ('MT','Mato Grosso','CO');
insert into estados values ('MS','Mato Grosso do Sul','CO');
insert into estados values ('MG','Minas Gerais','SE');
insert into estados values ('PA','Pará','N');
insert into estados values ('PB','Paraíba','NE');
insert into estados values ('PR','Paraná','S');
insert into estados values ('PE','Pernambuco','NE');
insert into estados values ('PI','Piauí','NE');
insert into estados values ('RJ','Rio de Janeiro','SE');
insert into estados values ('RN','Rio Grande do Norte','NE');
insert into estados values ('RS','Rio Grande do Sul','S');
insert into estados values ('RO','Rondônia','N');
insert into estados values ('RR','Roraima','N');
insert into estados values ('SC','Santa Catarina','S');
insert into estados values ('SP','São Paulo','SE');
insert into estados values ('SE','Sergipe','NE');
insert into estados values ('TO','Tocantins','N');

---------- Cidades-----------
insert into cidades values (1,'Abadia de Goiás','GO');
insert into cidades values (2,'Abadia dos Dourados','MG');
insert into cidades values (3,'Abadiânia','GO');
insert into cidades values (4,'Abaeté','MG');
insert into cidades values (27,'Acrelândia','AC');
insert into cidades values (186,'Amapá','AP');
insert into cidades values (295,'Aracaju','SE');
insert into cidades values (451,'Bagé','RS');
insert into cidades values (581,'Belém','PA');
insert into cidades values (647,'Boa Vista','RR');
insert into cidades values (749,'Brasília','DF');
insert into cidades values (902,'Caldas Novas','GO');
insert into cidades values (947,'Campinas','SP');
insert into cidades values (968,'Campo Grande','MS');
insert into cidades values (977,'Campo Novo de Rondônia','RO');
insert into cidades values (1031,'Canoas','RS');
insert into cidades values (1486,'Cuiabá','MT');
insert into cidades values (1504,'Curitiba','PR');
insert into cidades values (1807,'Florianópolis','SC');
insert into cidades values (1826,'Fortaleza','CE');
insert into cidades values (1922,'Goiânia','GO');
insert into cidades values (2588,'João Pessoa','PB');
insert into cidades values (2823,'Macapá','AP');
insert into cidades values (2831,'Maceió','AL');
insert into cidades values (2877,'Manaus','AM');
insert into cidades values (7777,'Nova', null);

--O nome e a região das cidades cadastradas no estado de Goiás.
SELECT c.nome AS nome_cidade, e.regiao
FROM cidades c
JOIN estados e ON c.uf = e.uf
WHERE c.uf = 'GO';

--O código, o nome e a região de cada cidade dos estados do Rio Grande do Sul, São Paulo e Paraná cujo nome inicia por “C”. Ordenar pelo nome da cidade de forma decrescente.
SELECT c.nome AS nome_cidade, e.regiao, cod_cidade
FROM cidades c
JOIN estados e ON c.uf = e.uf
WHERE c.uf = 'RS';

--O nome do estado e de suas respectivas cidades incluindo as cidades que não pertencem a nenhum estado;
SELECT estados.nome AS estado_nome, cidades.nome AS cidade_nome
FROM estados right join cidades
	on estados.uf = cidades.uf
ORDER BY estados.nome;