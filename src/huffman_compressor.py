import heapq
from collections import defaultdict

#Estrutura de Dados (Nó da Árvore de Huffman)
class NoHuffman:
    """Representa um nó na Árvore de Huffman."""
    def __init__(self, palavra, frequencia):
        self.palavra = palavra
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        #Método de comparação para a fila de prioridade
        return self.frequencia < outro.frequencia
    
    def __repr__(self):
        return f"({self.palavra}: {self.frequencia})"

# Funções do Algoritmo de Huffman

def calcular_frequencia_palavras(texto):
    """Calcula a frequência de cada palavra em um texto, separando por espaço."""
    palavras = texto.lower().split()
    frequencias = defaultdict(int)
    for palavra in palavras:
        #Simplificação: Remove pontuação básica
        palavra_limpa = palavra.strip('.,;:"\'()').replace('\n', '')
        if palavra_limpa:
            frequencias[palavra_limpa] += 1
    return dict(frequencias)

def construir_arvore(frequencias):
    """Constrói a Árvore de Huffman a partir das frequências."""
    fila_prioridade = [NoHuffman(palavra, freq) for palavra, freq in frequencias.items()]
    heapq.heapify(fila_prioridade)

    while len(fila_prioridade) > 1:
        no1 = heapq.heappop(fila_prioridade)
        no2 = heapq.heappop(fila_prioridade)
        nova_frequencia = no1.frequencia + no2.frequencia
        novo_no = NoHuffman(None, nova_frequencia) 
        
        #Garante consistência na ordem dos ramos (0 para esquerdo, 1 para direito)
        novo_no.esquerda = no1 if no1.frequencia <= no2.frequencia else no2
        novo_no.direita = no2 if no1.frequencia <= no2.frequencia else no1
        
        heapq.heappush(fila_prioridade, novo_no)

    return fila_prioridade[0]

def gerar_codigos_huffman(raiz, codigo_atual="", codigos=None):
    """Percorre a árvore para gerar os códigos binários (0 para esquerdo, 1 para direito)."""
    if codigos is None:
        codigos = {}
        
    #Condição de parada: Se for um nó folha
    if raiz.palavra is not None:
        codigos[raiz.palavra] = codigo_atual
        return codigos

    #Percorre a esquerda (ramo 0)
    if raiz.esquerda:
        gerar_codigos_huffman(raiz.esquerda, codigo_atual + "0", codigos)
    
    #Percorre a direita (ramo 1)
    if raiz.direita:
        gerar_codigos_huffman(raiz.direita, codigo_atual + "1", codigos)
        
    return codigos

def serializar_arvore(raiz):
    """Gera uma representação serializada da árvore (formato textual simples em pré-ordem)."""
    if raiz is None:
        return "#"
    
    if raiz.palavra is not None:
        return f"[{raiz.palavra}:{raiz.frequencia}]"
    
    return f"(I:{raiz.frequencia}) {serializar_arvore(raiz.esquerda)} {serializar_arvore(raiz.direita)}"

def decodificar_texto(raiz, texto_comprimido_bits):
    """
    Decodifica a sequência de bits de volta para palavras usando a Árvore de Huffman.
    (Funcionalidade extra para demonstrar a decodificação)
    """
    texto_decodificado = []
    no_atual = raiz
    
    #O texto comprimido_bits é uma lista de códigos
    #Juntamos para percorrer bit a bit
    sequencia_bits = "".join(texto_comprimido_bits)
    
    for bit in sequencia_bits:
        if bit == '0':
            no_atual = no_atual.esquerda
        else:
            no_atual = no_atual.direita
        
        #Se atingiu um nó folha, é uma palavra
        if no_atual.palavra is not None:
            texto_decodificado.append(no_atual.palavra)
            no_atual = raiz 
            
    return " ".join(texto_decodificado)