USE estudos_sql;

CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT NOT NULL,
    em_promocao BOOLEAN NOT NULL
);

INSERT INTO produtos (nome, categoria, preco, estoque, em_promocao) VALUES
('Smartphone X', 'Eletrônicos', 2500.00, 15, TRUE),
('Notebook Pro', 'Eletrônicos', 4500.00, 5, FALSE),
('Mouse Sem Fio', 'Acessórios', 80.00, 50, TRUE),
('Teclado Mecânico', 'Acessórios', 250.00, 0, FALSE),
('Monitor 27"', 'Eletrônicos', 1200.00, 8, TRUE),
('Cadeira Gamer', 'Móveis', 950.00, 12, FALSE),
('Mesa para Escritório', 'Móveis', 600.00, 3, TRUE),
('Fone de Ouvido Bluetooth', 'Acessórios', 150.00, 25, TRUE);

-- Retorne o nome e o preço de todos os produtos que pertencem à categoaria 'Eletrônicos'.
SELECT nome, preco
FROM produtos
WHERE categoria = 'Eletrônicos';

-- Listar todos os dados dos produtos que possuem preço maior ou igual a R$ 1.000,00.
SELECT *
FROM produtos
WHERE preco >= 1000;

-- Encontre o nome, a categoria e o preco de todos os produtos que estão em promoção e possuem preço menor que R$ 500,00
SELECT nome, categoria, preco
FROM produtos
WHERE em_promocao = TRUE AND preco < 500;

-- Listar o nome e o estoque de todos os produtos da categoria 'Acessórios' que não estão com estoque zerado
SELECT nome, estoque
FROM produtos
WHERE estoque != 0;

-- Exiba o nome e o preco dos produtos cujo preço esteja na faixa entre R$ 100,00 e R$ 1.000,00
SELECT nome, preco
FROM produtos
WHERE preco BETWEEN 100 AND 1000;

-- Selecione todos os produtos que pertençam às categorias 'Acessórios' ou 'Móveis'
SELECT *
FROM produtos
WHERE categoria IN ('Acessórios', 'Móveis');