USE estudos_sql;
CREATE TABLE funcionarios(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
cargo VARCHAR(100) NOT NULL,
departamento VARCHAR(100) NOT NULL,
salario DECIMAL(10, 2) NOT NULL,
cidade VARCHAR(100) NOT NULL,
ativo TINYINT(1) DEFAULT 1
);

INSERT INTO funcionarios (id, nome, departamento, cargo, salario, cidade, ativo) VALUES
(1, 'Ana', 'TI', 'Desenvolvedora', 5200.00, 'Ribeirão Preto', 1),
(2, 'Bruno', 'Financeiro', 'Analista', 4100.00, 'Franca', 1),
(3, 'Carla', 'TI', 'Analista de Dados', 4800.00, 'Ribeirão Preto', 1),
(4, 'Diego', 'RH', 'Assistente', 2800.00, 'Sertãozinho', 0),
(5, 'Elisa', 'Financeiro', 'Coordenadora', 6500.00, 'Ribeirão Preto', 1),
(6, 'Fernando', 'TI', 'Desenvolvedor', 5500.00, 'Franca', 1),
(7, 'Gabriela', 'RH', 'Analista', 3900.00, 'Ribeirão Preto', 1),
(8, 'Henrique', 'TI', 'Estagiário', 1800.00, 'Sertãozinho', 0);

-- Retorne todos os dados de todos os funcionários
SELECT *
FROM funcionarios;

-- Retorne nome, cargo, salario
SELECT nome, cargo, salario
FROM funcionarios;

-- Mostre quais departamentos existem na empresa sem repetir valores
SELECT DISTINCT departamento
FROM funcionarios; 

-- Retrone nome e salario, mas faça a coluna salario aparecer no resultado com o nome salario_mensal
SELECT nome, salario AS salario_mensal
FROM funcionarios;

-- Retorne nome, salaráio mensal e crie uma coluna calculada chamada salario_anual, considerando 12 salários
SELECT nome, salario AS salario_mensal, (salario * 12) AS salario_anual
FROM funcionarios;

-- Retorne todos os funcionários cujo salário seja maior que 4000
SELECT *
FROM funcionarios
WHERE salario > 4000;

-- Retorne somente os funcionários de TI que ganham mais de 5000
SELECT *
FROM funcionarios
WHERE departamento = 'TI' AND  salario > 5000;

-- Retorne os funcionários que moram em Ribeirão Preto ou Franca
SELECT *
FROM funcionarios
WHERE cidade = 'Ribeirão Preto' OR cidade = 'Franca';

-- Retorne funcionários que estejam ativos (ativo = 1) e que ganhem entre 3000 e 5000, incluindo os limites
SELECT *
FROM funcionarios
WHERE ativo = 1 AND salario >=3000 AND salario <= 5000;