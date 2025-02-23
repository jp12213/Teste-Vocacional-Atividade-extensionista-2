import tkinter as tk
from tkinter import messagebox


def processar_respostas():
    respostas = [var.get() for var in variaveis]

    # Verifica se todas as perguntas foram respondidas
    if all(resposta != 0 for resposta in respostas):
        if respostas[0] == 1 and respostas[6] == 1:
            sugestao = "Psicologia, Recursos Humanos ou Serviço Social"
        elif respostas[0] == 2 and respostas[4] == 1 and respostas[5] == 1:
            sugestao = "Engenharia, Ciências da Computação ou Análise de Sistemas"
        elif respostas[2] == 1 and respostas[7] == 1:
            sugestao = "Biologia, Geologia ou Ciências Ambientais"
        elif respostas[3] == 2 and respostas[1] == 1:
            sugestao = "Artes, Publicidade ou Design Gráfico"
        elif respostas[8] == 1 and respostas[6] == 1:
            sugestao = "Direito, Jornalismo ou Administração"
        elif respostas[9] == 1 and respostas[4] == 1:
            sugestao = "Engenharia de Produção, Gestão de Processos ou Contabilidade"
        else:
            sugestao = "Administração, Economia ou Marketing"

        exibir_resultado(sugestao)
    else:
        # Exibe um alerta caso alguma pergunta não tenha sido respondida
        messagebox.showwarning("Erro", "Por favor, responda a todas as perguntas.")


def exibir_resultado(sugestao):
    # Criar uma nova janela para exibir o resultado
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Resultado do Teste Vocacional")

    # Tornar a janela com fundo claro
    resultado_window.config(bg="#f0f0f0")
    resultado_window.geometry("500x400")

    # Título da janela de resultados
    resultado_title = tk.Label(resultado_window, text="Sugestão de Carreira", font=("Helvetica", 18, "bold"),
                               bg="#4CAF50", fg="white", pady=10)
    resultado_title.pack(fill="x")

    # Exibir sugestão de carreira com destaque
    sugestao_label = tk.Label(resultado_window,
                              text=f"Com base nas suas respostas, sugerimos explorar a área de:\n\n{sugestao}",
                              font=("Helvetica", 14), bg="#f0f0f0", justify="center", wraplength=400)
    sugestao_label.pack(pady=40)

    # Botão para fechar a janela de resultado
    fechar_button = tk.Button(resultado_window, text="Fechar", command=resultado_window.destroy, font=("Helvetica", 12),
                              bg="#FF5722", fg="white", relief="solid", width=20, height=2)
    fechar_button.pack(pady=20)


def sair_fullscreen(event=None):
    root.attributes('-fullscreen', False)


root = tk.Tk()
root.title("Teste Vocacional")

# Tornar a janela em tela cheia
root.attributes('-fullscreen', True)

# Título
titulo = tk.Label(root, text="Bem-vindo ao Teste Vocacional!", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white",
                  pady=10)
titulo.pack(fill="x")

# Descrição
descricao = tk.Label(root, text="Responda às perguntas e descubra uma sugestão de carreira para você.",
                     font=("Helvetica", 12), bg="#f0f0f0")
descricao.pack(pady=10)

# Perguntas e respostas
variaveis = []
for pergunta in [
    "Você prefere trabalhar com 1-pessoas ou com 2-números?",
    "Você gosta mais de atividades 1-criativas ou 2-técnicas?",
    "Você prefere trabalhar ao 1-ar livre ou em um 2-escritório?",
    "Você se considera mais 1-analítico ou 2-emocional?",
    "Você gosta de resolver problemas lógicos? 1 para sim e 2 para não.",
    "Você tem interesse por tecnologia e inovação? 1 para sim e 2 para não.",
    "Você prefere trabalhar em 1-equipe ou 2-sozinho?",
    "Você gosta de aprender sobre ciências naturais? 1 para sim e 2 para não.",
    "Você se sente confortável falando em público? 1 para sim e 2 para não.",
    "Você prefere 1-seguir regras e processos ou 2-criar suas próprias soluções?"
]:
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=10, anchor="w", padx=20)

    label = tk.Label(frame, text=pergunta, font=("Helvetica", 10), bg="#f0f0f0")
    label.pack(side="left", padx=10)

    var = tk.IntVar(value=0)  # Inicializa a variável com valor 0 (nenhuma resposta)
    variaveis.append(var)

    rb1 = tk.Radiobutton(frame, text="1", variable=var, value=1, font=("Helvetica", 10), bg="#f0f0f0", relief="solid",
                         width=5)
    rb1.pack(side="left", padx=5)
    rb2 = tk.Radiobutton(frame, text="2", variable=var, value=2, font=("Helvetica", 10), bg="#f0f0f0", relief="solid",
                         width=5)
    rb2.pack(side="left", padx=5)

# Botão
botao = tk.Button(root, text="Ver Resultado", command=processar_respostas, font=("Helvetica", 12, "bold"), bg="#4CAF50",
                  fg="white", relief="solid", width=20, height=2)
botao.pack(pady=20)

# Botão para sair do modo tela cheia
botao_sair_fullscreen = tk.Button(root, text="Sair da tela cheia", command=sair_fullscreen,
                                  font=("Helvetica", 12, "bold"), bg="#FF5722", fg="white", relief="solid", width=20,
                                  height=2)
botao_sair_fullscreen.pack(pady=10)

# Permite sair do modo tela cheia com a tecla Esc
root.bind("<Escape>", sair_fullscreen)

root.mainloop()
