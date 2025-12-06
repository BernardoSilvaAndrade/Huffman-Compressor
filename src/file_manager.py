import os
from huffman_compressor import (
    calcular_frequencia_palavras, 
    construir_arvore, 
    gerar_codigos_huffman, 
    serializar_arvore, 
    decodificar_texto
)

def processar_textos(caminho_input, caminho_output, textos_padrao):
    """Lê os textos, aplica Huffman e escreve o resultado no output.dat."""
    
    textos_brutos = []
    
    #Tenta ler o input.dat 
    if os.path.exists(caminho_input):
        print(f"\n✅ Lendo do arquivo: {caminho_input}")
        with open(caminho_input, 'r', encoding='utf-8') as f:
            #Separa os textos por linhas em branco duplas 
            textos_brutos = f.read().strip().split('\n\n')
    else:
        print(f"\n⚠️ O arquivo '{caminho_input}' não foi encontrado.")
        print(f"   Usando textos padrão para demonstração.")
        textos_brutos = textos_padrao
        
    if not textos_brutos:
        print("\n❌ Não há textos para processar. Finalizando.")
        return

    #Garante que a pasta data existe para salvar o output.dat 
    os.makedirs(os.path.dirname(caminho_output), exist_ok=True) 

    with open(caminho_output, 'w', encoding='utf-8') as out_f:
        out_f.write("--- Resultados da Compressão de Huffman ---\n\n")

        for i, texto_bruto in enumerate(textos_brutos):
            if not texto_bruto.strip():
                continue

            #Cálculo de Frequência e Construção da Árvore
            frequencias = calcular_frequencia_palavras(texto_bruto)
            if not frequencias:
                continue

            raiz_arvore = construir_arvore(frequencias)
            codigos_huffman = gerar_codigos_huffman(raiz_arvore, codigos={}) 

            #Compressão
            texto_comprimido_bits = []
            palavras_originais = [
                palavra.strip('.,;:"\'()').replace('\n', '') 
                for palavra in texto_bruto.lower().split() 
                if palavra.strip('.,;:"\'()').replace('\n', '')
            ]
            
            for palavra in palavras_originais:
                texto_comprimido_bits.append(codigos_huffman.get(palavra, ""))
            
            texto_comprimido_str = " ".join(texto_comprimido_bits)

            #Decodificação 
            texto_decodificado = decodificar_texto(raiz_arvore, texto_comprimido_bits)


            #Escrita no arquivo de saída
            out_f.write(f"### TEXTO {i+1} ###\n")
            out_f.write(f"Texto Original: {texto_bruto.strip()}\n") 

            #Estrutura da Árvore de Huffman
            out_f.write("\n1. Estrutura da Árvore (Pré-Ordem - Para Decodificação):\n")
            out_f.write(serializar_arvore(raiz_arvore) + "\n")
            
            #Códigos Gerados
            out_f.write("\n2. Conjunto de Códigos Gerados (Símbolo: Código Binário):\n")
            for palavra, codigo in sorted(codigos_huffman.items()):
                out_f.write(f"   '{palavra}': {codigo}\n")
            
            #Texto Comprimido
            out_f.write("\n3. Texto Comprimido (Sequência de Bits, separados por espaço):\n")
            out_f.write(texto_comprimido_str + "\n\n")
            
            #Informações para Análise 
            tamanho_original = len(texto_bruto.encode('utf-8')) * 8 
            tamanho_comprimido = len(''.join(texto_comprimido_bits))
            
            out_f.write(f"   -> Palavras Únicas (Símbolos): {len(frequencias)}\n")
            out_f.write(f"   -> Bits Comprimidos: {tamanho_comprimido}\n")
            out_f.write(f"   -> Taxa de Compressão (Aprox.): {(1 - tamanho_comprimido / tamanho_original) * 100:.2f}%\n")
            out_f.write(f"   -> Decodificação de Teste: {texto_decodificado}\n")
            out_f.write("---\n\n")

    print(f"Processamento concluído. Resultados escritos em: {caminho_output}")