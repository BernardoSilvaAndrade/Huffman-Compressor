# 📚 Implementação do Código de Huffman para Compressão de Texto

**Autor:** Bernardo Silva Andrade

---

## 1. Introdução ao Projeto

Este trabalho tem como objetivo consolidar o conhecimento sobre **estruturas em árvore** e **compressão de dados** por meio da implementação prática do algoritmo de **Huffman**.

O programa desenvolve um método capaz de realizar a compressão de pequenos trechos de texto utilizando o Código de Huffman como técnica de **codificação estatística sem perdas (lossless)**. O algoritmo se baseia na frequência de ocorrência das palavras (símbolos) para construir uma árvore binária ponderada, que associa códigos binários menores aos símbolos mais frequentes, promovendo a redução do tamanho total da representação.

---

## 2. Estrutura e Pré-requisitos

### Pré-requisitos

* **Linguagem:** Python 3 (código compatível com sistemas Linux - Ubuntu 24.04 - e Windows).
* **Dependências:** O projeto utiliza apenas bibliotecas padrão do Python (como `heapq` e `os`), não requerendo instalações externas complexas.

### Estrutura Modular

O código-fonte foi dividido em módulos na pasta `src/` para garantir maior **organização e clareza**:

* **`huffman.py`:** Contém o núcleo do algoritmo (Nó, construção da árvore, cálculo de frequências, geração de códigos, serialização e decodificação).
* **`file_manager.py`:** Responsável pela orquestração do processo, lendo o `input.dat` e escrevendo os resultados no `output.dat`.
* **`main.py`:** Ponto de entrada e execução principal do programa.
* **`data/`:** Pasta que armazena os arquivos de entrada (`input.dat`) e saída (`output.dat`).

---

## 3. Como Executar o Código

### 3.1. Preparação

1.  **Verificação de Arquivos:** Certifique-se de que a pasta `data/` existe na raiz do projeto.
2.  **Configuração de Entrada:** No arquivo `data/input.dat`, insira os textos que deseja comprimir. Cada trecho de texto deve ser separado por uma linha em branco.

> 💡 **Dica:** Utilize frases em português com palavras recorrentes, pois a repetição de símbolos (palavras) é essencial para observar a eficiência do algoritmo de Huffman.

### 3.2. Execução por Linha de Comando

A execução deve ser feita a partir do **diretório raiz do projeto** para garantir que o Python localize a pasta `src/` e seus módulos:

### 3.3. Apenas execute o script principal
python src/main.py

---

## 🧩 4. Metodologia de Compressão

O programa implementa o algoritmo de Huffman com foco na **compressão por palavra (símbolo)** e segue as seguintes etapas:

### 1. Pré-processamento e Cálculo de Frequência
* A função `calcular_frequencia_palavras` lê o texto de entrada.
* Todas as palavras são convertidas para minúsculas.
* A pontuação básica (ex: `.,;:"'()`) é removida das palavras para garantir que as ocorrências sejam contadas como o mesmo símbolo (ex: "grande." e "grande" são tratados como `grande`).
* É calculado o total de ocorrências (frequência) de cada palavra única.

### 2. Construção da Árvore de Huffman
* A construção da árvore utiliza uma **fila de prioridade (Min-Heap)**, implementada pela biblioteca padrão do Python, `heapq`.
* Os dois nós com as **menores frequências** são extraídos e combinados em um novo nó interno, cuja frequência é a soma dos seus filhos.
* **Consistência de Códigos:** Para garantir a reprodutibilidade dos códigos, a regra de desempate estabelece que o nó de menor frequência seja sempre alocado ao **ramo esquerdo (código 0)** e o de maior frequência ao **ramo direito (código 1)**. Este processo se repete até que reste apenas um nó: a raiz da árvore. 

### 3. Geração dos Códigos e Compressão
* A função `gerar_codigos_huffman` percorre a árvore, gerando um código binário de tamanho variável para cada palavra.
* Os códigos são gerados de forma a serem **prefixos livres**, garantindo que nenhum código seja o prefixo de outro, o que permite a decodificação unívoca.
* O texto original é então percorrido, e cada palavra é substituída pelo seu respectivo código binário, gerando a sequência final de bits comprimidos.

### 4. Geração do Output
* O arquivo `output.dat` registra a **Estrutura da Árvore serializada** e o **Conjunto de Códigos**. Essas informações são essenciais e suficientes para permitir a decodificação completa do texto comprimido.

---

## 6. Exemplo de Uso e Resultados

Para ilustrar o processo de compressão, utilizamos o seguinte texto no arquivo `data/input.dat`:

### 6.1. Conteúdo de `data/input.dat`

```text
Minha casa nao tem um portão grande. 
O portão tem uma cor azul.
```
### 6.2. Conteúdo de `data/output.dat` (Resultado da Compressão)

O `output.dat` gerado exibe o resultado da compressão para o texto acima:

#### 1. Conjunto de Códigos Gerados (Símbolo: Código Binário)
```text
   'azul': 1111
   'casa': 1101
   'cor': 1110
   'grande': 0110
   'minha': 1100
   'nao': 0111
   'o': 010
   'portão': 100  <-- Código curto (Frequência 2)
   'tem': 00      <-- Código mais curto (Frequência 2)
   'um': 1010
   'uma': 1011
```
#### 2. Estrutura da Árvore de Huffman (Pré-Ordem)
```text
(I:13) (I:5) [tem:2] (I:3) [o:1] (I:2) [grande:1] [nao:1] (I:8) (I:4) [portão:2] (I:2) [um:1] [uma:1] (I:4) (I:2) [minha:1] [casa:1] (I:2) [cor:1] [azul:1]
```
#### 3. Texto Comprimido (Sequência de Bits)
```text
1100 1101 0111 00 1010 100 0110 010 100 00 1011 1110 1111
```
#### 4. Análise e Decodificação
```text
-> Palavras Únicas (Símbolos): 11
   -> Bits Comprimidos: 45
   -> Taxa de Compressão (Aprox.): 91.35%
   -> Decodificação de Teste: minha casa nao tem um portão grande o portão tem uma cor azul
```

### Conclusão

Este exercício reforça o entendimento da **codificação eficiente de dados** e a **manipulação de estruturas em árvore**. O funcionamento prático do código de Huffman é essencial para compreender os princípios de compactação utilizados em diversas aplicações modernas.
