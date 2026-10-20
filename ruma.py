from pathlib import Path
import shutil


audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.odt', '.pdf']

def organizar(diretorio):
    AUDIOS_DIR = Path(diretorio).joinpath('áudios')
    VIDEOS_DIR = Path(diretorio).joinpath('vídeos')
    IMAGENS_DIR = Path(diretorio).joinpath('imagens')
    DOCS_DIR = Path(diretorio).joinpath('documentos')
    OUTROS_DIR = Path(diretorio).joinpath('outros')

    AUDIOS_DIR.mkdir(parents=True, exist_ok=True)
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGENS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    OUTROS_DIR.mkdir(parents=True, exist_ok=True)

    for arquivo in Path(diretorio).iterdir():
        if arquivo.is_dir():
            continue

        extensao = arquivo.suffix.lower()
    
        if extensao in audios_ext:
            nova_pasta = AUDIOS_DIR
        elif extensao in imagens_ext:
            nova_pasta = IMAGENS_DIR
        elif extensao in documentos_ext:
            nova_pasta = DOCS_DIR
        elif extensao in videos_ext:
            nova_pasta = VIDEOS_DIR
        else:
            nova_pasta = OUTROS_DIR

        shutil.move(arquivo, nova_pasta)
        print(f'Moveu {arquivo} → {nova_pasta}')
        
if __name__ == '__main__':
    pasta = input(r'Informe o caminho absoluto da pasta: ')
    organizar(pasta)