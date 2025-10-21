import tkinter as tk

# Variável global para armazenar a expressão matemática
expression = ""

# Função para adicionar um número ou operador à expressão
def press(num):
    """
    Esta função é chamada quando um botão de número ou operador é pressionado.
    Ela concatena o valor do botão à expressão global.
    """
    global expression
    expression = expression + str(num)
    # Atualiza o texto na caixa de entrada (display)
    equation.set(expression)

# Função para avaliar a expressão final
def equalpress():
    """
    Esta função é chamada quando o botão '=' é pressionado.
    Ela tenta avaliar a expressão usando a função eval() do Python.
    Em caso de erro (ex: divisão por zero), exibe uma mensagem de erro.
    """
    try:
        global expression
        # eval() avalia a string como uma expressão matemática
        total = str(eval(expression))
        equation.set(total)
        # O resultado se torna o novo início da expressão para cálculos contínuos
        expression = total
    except:
        equation.set(" erro ")
        expression = ""

# Função para limpar o display
def clear():
    """
    Esta função é chamada quando o botão 'C' é pressionado.
    Ela limpa a expressão e o display.
    """
    global expression
    expression = ""
    equation.set("")

# --- Configuração da Interface Gráfica ---
if __name__ == "__main__":
    # Cria a janela principal da aplicação
    window = tk.Tk()

    # Define o título da janela
    window.title("Calculadora")

    # Define o tamanho da janela (largura x altura)
    window.geometry("320x400")
    
    # Impede que a janela seja redimensionada
    window.resizable(False, False)

    # Define a cor de fundo da janela
    window.configure(bg="#f0f0f0")

    # StringVar é uma variável especial do tkinter para o display
    equation = tk.StringVar()

    # Cria o display (campo de entrada de texto)
    display = tk.Entry(window, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
    # Posiciona o display na grade, ocupando 4 colunas
    display.grid(columnspan=4, padx=10, pady=20)

    # --- Criação dos Botões ---
    # Usamos 'lambda' para passar o valor do botão para a função press()
    
    # Estilos comuns para os botões
    btn_style = {'font': ('arial', 12, 'bold'), 'height': 2, 'width': 5, 'bd': 2, 'relief': 'raised'}
    op_style = {'font': ('arial', 12, 'bold'), 'height': 2, 'width': 5, 'bd': 2, 'relief': 'raised', 'bg': '#ff9f0a'}

    # Fila 1
    button_7 = tk.Button(window, text='7', **btn_style, command=lambda: press(7))
    button_7.grid(row=2, column=0, pady=5)

    button_8 = tk.Button(window, text='8', **btn_style, command=lambda: press(8))
    button_8.grid(row=2, column=1, pady=5)

    button_9 = tk.Button(window, text='9', **btn_style, command=lambda: press(9))
    button_9.grid(row=2, column=2, pady=5)

    divide = tk.Button(window, text='/', **op_style, command=lambda: press("/"))
    divide.grid(row=2, column=3, pady=5)

    # Fila 2
    button_4 = tk.Button(window, text='4', **btn_style, command=lambda: press(4))
    button_4.grid(row=3, column=0, pady=5)

    button_5 = tk.Button(window, text='5', **btn_style, command=lambda: press(5))
    button_5.grid(row=3, column=1, pady=5)

    button_6 = tk.Button(window, text='6', **btn_style, command=lambda: press(6))
    button_6.grid(row=3, column=2, pady=5)

    multiply = tk.Button(window, text='*', **op_style, command=lambda: press("*"))
    multiply.grid(row=3, column=3, pady=5)

    # Fila 3
    button_1 = tk.Button(window, text='1', **btn_style, command=lambda: press(1))
    button_1.grid(row=4, column=0, pady=5)

    button_2 = tk.Button(window, text='2', **btn_style, command=lambda: press(2))
    button_2.grid(row=4, column=1, pady=5)

    button_3 = tk.Button(window, text='3', **btn_style, command=lambda: press(3))
    button_3.grid(row=4, column=2, pady=5)

    minus = tk.Button(window, text='-', **op_style, command=lambda: press("-"))
    minus.grid(row=4, column=3, pady=5)

    # Fila 4
    button_0 = tk.Button(window, text='0', **btn_style, command=lambda: press(0))
    button_0.grid(row=5, column=0, pady=5)

    decimal = tk.Button(window, text='.', **btn_style, command=lambda: press('.'))
    decimal.grid(row=5, column=1, pady=5)

    plus = tk.Button(window, text='+', **op_style, command=lambda: press("+"))
    plus.grid(row=5, column=2, pady=5)

    equal = tk.Button(window, text='=', **op_style, command=equalpress)
    equal.grid(row=5, column=3, pady=5)
    
    # Fila 5 - Botão de Limpar
    clear_button = tk.Button(window, text='C', font=('arial', 12, 'bold'), height=2, width=24, bd=2, relief='raised', bg='#d4d4d2', command=clear)
    clear_button.grid(row=6, column=0, columnspan=4, pady=10)

    # Inicia o loop principal da aplicação, que a mantém em execução
    window.mainloop()