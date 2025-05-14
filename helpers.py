import sqlite3
import customtkinter as ctk

def gerar_proximo_codigo():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo FROM produtos ORDER BY id DESC LIMIT 1")
    ultimo = cursor.fetchone()
    conn.close()

    if ultimo:
        ultimo_codigo = int(ultimo[0])
        proximo_codigo = str(ultimo_codigo + 1).zfill(3)
    else:
        proximo_codigo = "001"

    return proximo_codigo


def exibir_erro(msg, parent=None):
    janela = ctk.CTkToplevel(parent)
    janela.title("Erro")
    janela.geometry('300x150')
    janela.resizable(False,False)
    janela.grab_set()

    label = ctk.CTkLabel(janela, text=msg, wraplength=250)
    label.pack(pady=20)

    botao = ctk.CTkButton(janela, text="OK", command=janela.destroy)
    botao.pack(pady=1)


def validar_campos_vazio(lista_campos, parent):
    for entry, campo in lista_campos.items():
        if entry.get().strip() == "":
            exibir_erro(f"O campo '{campo}' não pode estar vazio", parent)
            return False
    return True


def validar_campos_numericos(lista_campos,  parent):
    for entry, campo in lista_campos.items():
        try:
            float(entry.get())
        except ValueError:
            exibir_erro(f"Digite somente numeros no campo '{campo}'", parent)
            return False
    return True


def validar_campos(lista_vazios, lista_numericos, parent):
    if not validar_campos_vazio(lista_vazios, parent):
        return False
    if not validar_campos_numericos(lista_numericos, parent):
        return False
    return True
