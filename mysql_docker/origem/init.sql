CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO clientes (nome, email) VALUES
('João', 'joao@email.com'),
('Maria', 'maria@email.com'),
('Pedro', 'pedro@email.com');

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    preco DECIMAL(10,2)
);

INSERT INTO produtos (nome, preco) VALUES
('Teclado', 150.00),
('Mouse', 80.00),
('Monitor', 800.00);

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    data_pedido DATE
);

INSERT INTO pedidos (cliente_id, data_pedido) VALUES
(1, '2025-01-01'),
(2, '2025-02-01'),
(3, '2025-03-01');

CREATE TABLE estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    quantidade INT
);

INSERT INTO estoque (produto_id, quantidade) VALUES
(1, 10),
(2, 20),
(3, 15);

CREATE TABLE fornecedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    contato VARCHAR(50)
);

INSERT INTO fornecedores (nome, contato) VALUES
('Fornecedor A', 'contatoA@email.com'),
('Fornecedor B', 'contatoB@email.com');
