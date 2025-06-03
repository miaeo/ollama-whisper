# whisper_ollama

Projeto simples de **transcrição de áudio** utilizando o modelo `Whisper` e de geração de resumos com pontos chave com **Ollama**, executado localmente. Desenvolvido para a disciplina de Tópicos Avançados em Sistemas para Internet I.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/)
- [Ollama](https://ollama.com/) instalado e configurado localmente
- [ffmpeg](https://www.ffmpeg.org/download.html) configurado no PATH (necessário para o Whisper)
- Git

---

## Instalação

### 1. Configure o FFmpeg

Após download, faça a extração da pasta e copie o caminho da pasta `bin`. Exemplo:

```bash
C:\ffmpeg\bin
```
Adicione este caminho nas varíaveis de ambiente do Windows.

### 2. Clone o repositório

```bash
git clone https://github.com/miaeo/whisper-ollama-projeto.git
cd whisper-ollama-projeto
```

### 3. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
```
No Powershell, ative seu ambiente virtual

```bash
.\venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```


## Execução

### 1. Inicie o Ollama

Certifique-se de que o Ollama esteja rodando antes de executar o script!

```bash
ollama run llama2
```

### 2. Em outro terminal, execute o script

```bash
python whisper_ollama.py
```

O script irá:

- Transcrever o áudio usando **Whisper**.
- Enviar o texto transcrito para o **Ollama**.
- Gerar e exibir um resumo com os pontos-chave.

---

## Exemplos de uso

### Prepare seu arquivo de áudio

Coloque seu áudio na pasta do script, em formatos `.wav` ou `.mp3`, e execute o script.

### Saída esperada:

```bash
————  Texto transcrito:  ————
"Aqui vai o texto completo transcrito do seu áudio."

————  Pontos-chave:  ————
- Primeiro ponto.
- Segundo ponto.
- Terceiro ponto.
```
