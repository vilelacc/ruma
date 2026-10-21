# ruma
Script em Python que organiza automaticamente os arquivos de um diretório em pastas de acordo com suas extensões.

# Requisitos

* Git
* Python 3

# Como executar

1. Clone o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/vilelacc/ruma.git
```

2. Acesse o diretório

```bash
cd ruma
```

3. Execute o programa

```bash
python3 ruma.py
```

4. Informe o diretório

Quando solicitado, digite o caminho absoluto da pasta que deseja organizar.

Exemplo:

```bash
Informe o caminho absoluto da pasta: /home/usuario/Downloads
```

# Como funciona

O algoritmo identifica a extensão de cada arquivo e o move para uma pasta correspondente:

| Pasta         | Extensões                |
|---------------|--------------------------|
| `áudios/`     | `.mp3`, `.wav`           |
| `vídeos/`     | `.mp4`, `.mov`, `.avi`   |
| `imagens/`    | `.jpg`, `.jpeg`, `.png`  |
| `documentos/` | `.txt`, `.odt`, `.pdf`   |
| `outros/`     | Demais extensões         |


