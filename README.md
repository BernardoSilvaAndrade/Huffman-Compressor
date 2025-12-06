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

O programa implementa as seguintes etapas para cada texto lido:

1.  **Cálculo de Frequência:** A frequência de cada palavra é calculada, e a pontuação é removida para padronizar os símbolos.
2.  **Construção da Árvore:** Utilizando a frequência, a árvore de Huffman é construída usando uma fila de prioridade, combinando os nós de menor frequência.
3.  **Geração dos Códigos:** Um percurso na árvore define os códigos binários: `0` para o ramo esquerdo e `1` para o ramo direito.
4.  **Compressão:** O texto é percorrido novamente, e cada palavra é substituída por seu respectivo código binário.

---

## 📝 5. Resultados e Exemplos

O arquivo de saída `data/output.dat` é gerado contendo, para cada texto processado:

1.  **Estrutura da Árvore de Huffman:** Em formato textual serializado (pré-ordem), essencial para a decodificação.
2.  **Conjunto de Códigos Gerados:** O mapa de símbolo (palavra) para Código Binário.
3.  **Texto Comprimido:** A sequência de bits (separada por espaço).
4.  **Análise:** Informações suficientes para permitir a decodificação, como a quantidade de bits comprimidos e a Taxa de Compressão obtida.

### Conclusão

Este exercício reforça o entendimento da **codificação eficiente de dados** e a **manipulação de estruturas em árvore**. O funcionamento prático do código de Huffman é essencial para compreender os princípios de compactação utilizados em diversas aplicações modernas.
