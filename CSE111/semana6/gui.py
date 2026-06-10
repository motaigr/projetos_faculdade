import tkinter as tk
from tkinter import Frame, Label, Button
from entrada_numero import IntEntry
import random

def main():
    raiz = tk.Tk()
    janela_principal = Frame(raiz)
    janela_principal.master.title("Lançamento de dados")
    janela_principal.pack(padx=8, pady=8, fill=tk.BOTH, expand=1)

    configurar_janela(janela_principal)

    janela_principal.mainloop()

def configurar_janela(janela):
    rotulo_lados = Label(janela, text="Por favor, digite o número de lados do seus dados:(2-20)")
    rotulo_lados.grid(row=0, column=0)
    entrada_lados = IntEntry(janela, lower_bound=2, upper_bound=20, width=4)
    entrada_lados.grid(row=0, column=1)

    rotulo_dados = Label(janela, text="Por favor, digite a quantidade de dados que quer lançar (1-10)")
    rotulo_dados.grid(row=1, column=0)
    entrada_dados = IntEntry(janela, lower_bound=1, upper_bound=10, width=4)
    entrada_dados.grid(row=1, column=1)

    botao_lancamento = Button(janela, text="Lance os dados!")
    botao_lancamento.grid(row=2, column=0)
    botao_limpar = Button(janela, text="Limpar")
    botao_limpar.grid(row=2, column=1)


    rotulo_resultado = Label(janela, text="")
    rotulo_resultado.grid(row=3, column=0)


    def lancamento(num_lados, qtd_dados):
        soma = 0
        texto_resultado = ""
        for lance in range(qtd_dados):
            aleatorio = random.randint(1, num_lados)
            soma = soma + aleatorio
            texto_resultado = texto_resultado + f'{aleatorio} '
        texto_resultado = texto_resultado + f'| total: {soma}'
        return texto_resultado

    def acao_limpar():
        entrada_lados.clear()
        entrada_dados.clear()
        rotulo_resultado.config(text="Limpar")

    botao_limpar.config(command=acao_limpar)

    def acao_botao():
        try:
            num_lados = entrada_lados.get()
        except:
            rotulo_resultado.config(text="Por favor, digite um número de lados valido")
            return
        try:
            qtd_dados = entrada_dados.get()
        except:
            rotulo_resultado.config(text="Por favor, digite um número de dados valido")
            return
        texto_resultado = lancamento(num_lados, qtd_dados)
        rotulo_resultado.config(text=texto_resultado)

    botao_lancamento.config(command=acao_botao)

if __name__ == "__main__":
    main()