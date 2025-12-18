import tkinter as tk
from tkinter import messagebox

# calculadora
def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0: return "erro"
    return a / b

# funçoes da calculadora
def executar_calculo():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        operacao = lista_operacoes.get()

        if operacao == "Soma": res = somar(n1, n2)
        elif operacao == "Subtração": res = subtrair(n1, n2)
        elif operacao == "Multiplicação": res = multiplicar(n1, n2)
        elif operacao == "Divisão":
            res = dividir(n1, n2)
            if res == "erro":
                messagebox.showerror("Erro", "Divisão por zero não é permitida!")
                return
        
        label_resultado.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showwarning("Atenção", "Por favor, digite apenas números!")

# limpar numeros inseridos
def limpar_campos():
    entry_n1.delete(0, 'end')
    entry_n2.delete(0, 'end')
    label_resultado.config(text="Resultado: ")
    lista_operacoes.set("Soma")

# front end
janela = tk.Tk()
janela.title("Calculadora Pro")
janela.geometry("350x450")
janela.configure(bg="#2c3e50")

# entradas
tk.Label(janela, text="Primeiro Número:", bg="#2c3e50", fg="white").pack(pady=5)
entry_n1 = tk.Entry(janela, font=("Arial", 12))
entry_n1.pack()

tk.Label(janela, text="Segundo Número:", bg="#2c3e50", fg="white").pack(pady=5)
entry_n2 = tk.Entry(janela, font=("Arial", 12))
entry_n2.pack()

# menu
lista_operacoes = tk.StringVar(janela)
lista_operacoes.set("Soma")
opcoes = tk.OptionMenu(janela, lista_operacoes, "Soma", "Subtração", "Multiplicação", "Divisão")
opcoes.configure(bg="#34495e", fg="white", highlightthickness=0)
opcoes.pack(pady=15)

# botão calcular
botao_calc = tk.Button(janela, text="CALCULAR", command=executar_calculo, 
                       bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=15)
botao_calc.pack(pady=5)

# botão limpar (cor)
botao_limpar = tk.Button(janela, text="LIMPAR", command=limpar_campos, 
                        bg="#e67e22", fg="white", font=("Arial", 10, "bold"), width=15)
botao_limpar.pack(pady=5)

# resultado
label_resultado = tk.Label(janela, text="Resultado: ", bg="#2c3e50", fg="#ebebeb", font=("Arial", 14, "bold"))
label_resultado.pack(pady=20)

janela.mainloop()
