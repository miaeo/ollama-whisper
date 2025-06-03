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

### 1. Clone o repositório

```bash
git clone https://github.com/miaeo/whisper-ollama-projeto.git
cd whisper-ollama-projeto
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
```
No Powershell, ative seu ambiente virtual

```bash
.\venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

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

- Transcrever o áudio usando Whisper.
- Enviar o texto transcrito para o Ollama (modelo llama2).
- Gerar e exibir um resumo com os pontos-chave.
