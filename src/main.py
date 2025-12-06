import os
from file_manager import processar_textos

if __name__ == "__main__":
    
    PASTA_DATA = "data"
    INPUT_FILE = "input.dat"
    OUTPUT_FILE = "output.dat"
    
    CAMINHO_INPUT = os.path.join(PASTA_DATA, INPUT_FILE)
    CAMINHO_OUTPUT = os.path.join(PASTA_DATA, OUTPUT_FILE)

    #Textos de exemplo para caso o input.dat não seja encontrado
    TEXTOS_PADRAO = [
        "O computador executa instruções em alta velocidade e processa dados com precisão.",
        "A memória armazena informações que são acessadas rapidamente pela CPU.",
        "Os sistemas operacionais controlam os recursos e coordenam as tarefas do processador."
    ]

    #Processa os textos e gera o output.dat
    processar_textos(CAMINHO_INPUT, CAMINHO_OUTPUT, TEXTOS_PADRAO)
    
    print("\nProcesso finalizado.")
    print(f"Lembre-se de que o arquivo '{CAMINHO_INPUT}' deve ser criado na pasta '{PASTA_DATA}' com seus textos.")