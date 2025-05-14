from telas.cadastro import JanelaCadastro
from telas.entrada import JanelaEntrada
import customtkinter as ctk
from banco import cria_bd



def Cria_janela():
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.title('Controle de estoque')
    root.geometry('900x800')
    root.resizable(width=False, height=False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    ctk.CTkButton(root, text="Cadastrar",
        command=lambda: JanelaCadastro(root),
        fg_color='#FF8C00',
        corner_radius=50,
        hover_color='#D2691E'
    ).place(relwidth=0.2, relheight=0.05, relx=0.1, rely=0.2)

    ctk.CTkButton(root, text="Entrada",
        command=lambda: JanelaEntrada(root),
        fg_color='#FF8C00',
        corner_radius=50,
        hover_color='#D2691E'
        ).place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.2)

    ctk.CTkButton(root, text="Editar",
        fg_color='#FF8C00',
        corner_radius=50,
        hover_color='#D2691E'
        ).place(relwidth=0.2, relheight=0.05, relx=0.7, rely=0.2)

    root.mainloop()

cria_bd()

Cria_janela()


