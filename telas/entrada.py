import sqlite3

import customtkinter as ctk

class JanelaEntrada(ctk.CTkToplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.iconify()
        self.title("Entrada de produtos")
        self.geometry("900x800")

        self.cria_widgets()

    def cria_widgets(self):
        ctk.CTkLabel(self, text='Nome'). place(relx=0.05, rely=0.05)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text='Nome do Produto', border_color='#FF8C00', border_width=1)
        self.entry_nome.place(relx=0.05, rely = 0.1, relwidth=0.35, relheight = 0.05)

        ctk.CTkLabel(self, text='Código').place(relx=0.6, rely=0.05)
        self.entry_codigo = ctk.CTkEntry(self, placeholder_text='Código do Produto', border_color='#FF8C00', border_width=1)
        self.entry_codigo.place(relx=0.6,rely=0.1, relwidth=0.35, relheight = 0.05)

        self.btn_enter = ctk.CTkButton(self, text='Enter', command=self.Buscar). place(relx= 0.4, rely=0.9)

    def Buscar(self):
        nome_digitado = self.entry_nome.get()
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE nome = ?",(nome_digitado,))
        produto = cursor.fetchone()
        cursor.close()

        if produto:
            print('Produto encontrado')
        else:
            print('Produto nao encontrado')
