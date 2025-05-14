import customtkinter as ctk
from banco import cadastrar_produto
from helpers import *
from datetime import datetime

class JanelaCadastro(ctk.CTkToplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.iconify()  # Minimiza a janela principal
        self.title("Cadastrar Produto")
        self.geometry("900x800")

        self.criar_widgets()


    def criar_widgets(self):
        # Nome
        ctk.CTkLabel(self, text='Nome').place(relx=0.1, rely=0.07)
        self.entry_nome = ctk.CTkEntry(self, placeholder_text='Nome do Produto', border_color='#FF8C00', border_width=1)
        self.entry_nome.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.05)

        # Descrição
        ctk.CTkLabel(self, text='Descrição').place(relx=0.1, rely=0.17)
        self.entry_desc = ctk.CTkEntry(self, placeholder_text='Descrição do produto', border_color='#FF8C00', border_width=1)
        self.entry_desc.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)

        # Categoria
        ctk.CTkLabel(self, text='Categoria').place(relx=0.55, rely=0.07)
        self.entry_categoria = ctk.CTkEntry(self, placeholder_text='Categoria do produto', border_color='#FF8C00', border_width=1)
        self.entry_categoria.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.05)

        # Fornecedor
        ctk.CTkLabel(self, text='Fornecedor').place(relx=0.1, rely=0.41)
        self.entry_fornecedor = ctk.CTkEntry(self, placeholder_text='Fornecedor', border_color='#FF8C00', border_width=1)
        self.entry_fornecedor.place(relx=0.1, rely=0.45, relwidth=0.35, relheight=0.05)

        # Unidade de Medida
        ctk.CTkLabel(self, text='Unidade de medida').place(relx=0.55, rely=0.41)
        self.entry_medida = ctk.CTkComboBox(self, values=["Kg","Unidade","Dezena","Duzia","Cento","Caixa"],button_color='#FF8C00',button_hover_color='#D2691E',
                                            border_color='#FF8C00', dropdown_hover_color='#D2691E', border_width=1)
        self.entry_medida.place(relx=0.55, rely=0.45, relwidth=0.35, relheight=0.05)
        self.entry_medida.set("Unidade")


        # Preço de compra
        ctk.CTkLabel(self, text='Preço de compra').place(relx=0.1, rely=0.52)
        self.entry_preco_compra = ctk.CTkEntry(self, placeholder_text='Preço de compra R$', border_color='#FF8C00', border_width=1)
        self.entry_preco_compra.place(relx=0.1, rely=0.56, relwidth=0.35, relheight=0.05)

        # Preço de venda
        ctk.CTkLabel(self, text='Preço de venda').place(relx=0.55, rely=0.52)
        self.entry_preco_venda = ctk.CTkEntry(self, placeholder_text='Preço de venda R$', border_color='#FF8C00', border_width=1)
        self.entry_preco_venda.place(relx=0.55, rely=0.56, relwidth=0.35, relheight=0.05)

        # Quantidade
        ctk.CTkLabel(self, text='Quantidade').place(relx=0.1, rely=0.63)
        self.entry_quantidade = ctk.CTkEntry(self, placeholder_text='Quantidade', border_color='#FF8C00', border_width=1)
        self.entry_quantidade.place(relx=0.1, rely=0.67, relwidth=0.35, relheight=0.05)

        # Botão salvar
        ctk.CTkButton(self, text="Salvar", command=self.salvar, fg_color="#FF8C00", hover_color="#D2691E").place(
            relx=0.4, rely=0.8, relwidth=0.2, relheight=0.06)

        #Deixa a entry do nome selecionada ao abrir a janela
        self.after(100,lambda :self.entry_nome.focus())

        self.bind("<Return>", self.salvar)


    def salvar(self, event=None):

        print("testando")
        campos = {
            self.entry_nome: "Nome",
            self.entry_categoria: "Categoria",
            self.entry_fornecedor: "Fornecedor",
            self.entry_preco_compra: "Preço de Compra",
            self.entry_preco_venda: "Preço de Venda",
            self.entry_quantidade: "Quantidade"
        }

        campos_numericos = {
            self.entry_preco_compra: "Preço de Compra",
            self.entry_preco_venda: "Preço de Venda",
            self.entry_quantidade: "Quantidade"
        }

        if not validar_campos(campos, campos_numericos, self):
            return

        #código do produto
        codigo = gerar_proximo_codigo()

        #Nome do produto
        nome = self.entry_nome.get()
        #Descrição
        descricao = self.entry_desc.get()
        #Categoria
        categoria = self.entry_categoria.get()
        #Fornecedor
        fornecedor = self.entry_fornecedor.get()
        #unidade
        unidade = self.entry_medida.get()
        #Preço de compra
        preco_compra = self.entry_preco_compra.get()
        #preço de venda
        preco_venda = (self.entry_preco_venda.get())
        #quantidade
        quantidade = self.entry_quantidade.get()
        #Data de cadastro
        data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Chama função do banco
        cadastrar_produto(
            codigo, nome, descricao, categoria, fornecedor,
            unidade, preco_compra, preco_venda, quantidade, data_cadastro
        )

        self.destroy()
        self.root.deiconify()  # Reexibe a janela principal