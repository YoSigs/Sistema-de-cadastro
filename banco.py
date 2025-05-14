import sqlite3

def cria_bd():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT,
            nome TEXT,
            descricao TEXT,
            categoria TEXT,
            fornecedor TEXT,
            quantidade INTEGER,
            preco_custo REAL,
            preco_venda REAL,
            unidade TEXT,
            data_cadastro TEXT
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_produto(codigo, nome, descricao, categoria, fornecedor, unidade, preco_custo, preco_venda, quantidade, data_cadastro):
    with sqlite3.connect("estoque.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produtos 
            (codigo, nome, descricao, categoria, fornecedor, unidade, preco_custo, preco_venda, quantidade, data_cadastro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (codigo, nome, descricao, categoria, fornecedor, unidade, preco_custo, preco_venda, quantidade, data_cadastro))
        conn.commit()

