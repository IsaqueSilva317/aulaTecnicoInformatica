import tkinter as tk
from tkinter import messagebox

# Dicionário com os atalhos (10 por categoria)
atalhos = {
    'CPL': {
        'appwiz.cpl': 'Programas e Recursos',
        'desk.cpl': 'Configurações de Vídeo e Tela',
        'inetcpl.cpl': 'Propriedades da Internet',
        'main.cpl': 'Configurações do Mouse',
        'mmsys.cpl': 'Configurações de Som',
        'ncpa.cpl': 'Conexões de Rede',
        'powercfg.cpl': 'Opções de Energia',
        'sysdm.cpl': 'Propriedades do Sistema',
        'timedate.cpl': 'Data e Hora',
        'firewall.cpl': 'Configurações do Firewall do Windows'
    },
    'EXCEL': {
        'Ctrl + N': 'Nova planilha',
        'Ctrl + O': 'Abrir documento existente',
        'Ctrl + S': 'Salvar planilha',
        'Ctrl + P': 'Imprimir',
        'Ctrl + Shift + L': 'Ativar/Desativar Filtros',
        'Ctrl + "+"': 'Inserir nova linha ou coluna',
        'Ctrl + Shift + "$"': 'Aplicar formato de moeda',
        'Alt + Enter': 'Quebrar linha dentro da célula',
        'Ctrl + ;': 'Inserir data atual',
        'F4': 'Repetir última ação'
    },
    'MSC': {
        'services.msc': 'Painel de Serviços do Windows',
        'eventvwr.msc': 'Visualizador de Eventos',
        'compmgmt.msc': 'Gerenciamento do Computador',
        'devmgmt.msc': 'Gerenciador de Dispositivos',
        'diskmgmt.msc': 'Gerenciamento de Disco',
        'gpedit.msc': 'Editor de Diretivas de Grupo',
        'secpol.msc': 'Políticas de Segurança Local',
        'perfmon.msc': 'Monitor de Desempenho',
        'lusrmgr.msc': 'Gerenciador de Usuários Locais',
        'taskschd.msc': 'Agendador de Tarefas'
    },
    'WINDOWS': {
        'Win + D': 'Mostrar área de trabalho',
        'Win + E': 'Abrir Explorador de Arquivos',
        'Win + L': 'Bloquear o computador',
        'Alt + Tab': 'Alternar entre janelas abertas',
        'Win + Shift + S': 'Captura de tela',
        'Win + R': 'Abrir janela Executar',
        'Win + I': 'Abrir Configurações',
        'Win + Ctrl + D': 'Criar nova área de trabalho virtual',
        'Win + Ctrl + F4': 'Fechar área de trabalho virtual atual',
        'Win + M': 'Minimizar todas as janelas'
    }
}

# Função que exibe os atalhos do botão clicado
def mostrar_atalhos(nome_programa):
    lista = atalhos[nome_programa]
    texto = f"Atalhos de {nome_programa}:\n\n"
    for comando, descricao in lista.items():
        texto += f"{comando} → {descricao}\n"
    messagebox.showinfo(f"{nome_programa}", texto)

# Criar a janela principal
janela = tk.Tk()
janela.title("SpeedWork Professional")
janela.geometry("450x400")
janela.config(bg="#f0f0f0")

# Título
titulo = tk.Label(janela, text="SpeedWork PRO", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#007ACC")
titulo.pack(pady=15)

subtitulo = tk.Label(janela, text="Escolha um programa para ver os atalhos:", font=("Arial", 11), bg="#f0f0f0")
subtitulo.pack(pady=5)

# Criar os botões dinamicamente
for nome in atalhos.keys():
    botao = tk.Button(
        janela,
        text=nome,
        font=("Arial", 12, "bold"),
        width=15,
        bg="#007ACC",
        fg="white",
        activebackground="#005999",
        command=lambda n=nome: mostrar_atalhos(n)
    )
    botao.pack(pady=6)

# Botão para sair
botao_sair = tk.Button(
    janela,
    text="Sair",
    font=("Arial", 11),
    bg="gray",
    fg="white",
    width=10,
    command=janela.destroy
)
botao_sair.pack(pady=15)

# Rodar o programa
janela.mainloop()