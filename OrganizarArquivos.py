# -*- coding: UTF-8


# Created on 6 de jul. de 2021
# Organizador de pastas e Arquivos

# @author: Fabricio Calvete Campos

    # 1 Pegar o nome dos arquivos
    # 2 Verificar a exten�ao dos arquivos
    # 3 Criar pastas para imagens, videos, documentos, audios e outros
    # 4 Mover os arquivos para dentro das pastas
import os

audios_ext = ['.mp3','.wav']
videos_ext = ['.mp4','.mov','.avi']
imagens_ext = ['jpg','jpeg','png']
documentos_ext = ['.pdf','.doc','.docx','.txt', '.log']

def pegarextensao(nomearquivo):
    index = nomearquivo.rfind('.')

    return nomearquivo[index:]

def organizando(diretorio):    
    
    AUDIO_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio, "imagens")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    DOCUMENTOS_DIR = os.path.join(diretorio, "documentos")
    OUTROS_DIR = os.path.join(diretorio, "outros")
    
    
    If not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
        
    If not os.path.isdir(IMAGENS_DIR):    
        os.mkdir(IMAGENS_DIR)
        
    If not os.path.isdir(VIDEOS_DIR):        
        os.mkdir(VIDEOS_DIR)
        
    If not os.path.isdir(DOCUMENTOS_DIR):        
        os.mkdir(DOCUMENTOS_DIR)
        
    If not os.path.isdir(OUTROS_DIR):        
        os.mkdir(OUTROS_DIR)
    
    #retornar a lista de nome dos arquivos
    nomes_arquivos = os.listdir(diretorio)
    #Como terei que passar por todos eles vamos a um for
    
    for arquivo in nomes_arquivos:
        #extens�o do arquivo em letras minusculas
        extensao = str.lower(pegarextensao(arquivo))
        
        print(arquivo, extensao)
        
        nova_pasta = ''
        
        if extensao in audios_ext:
            nova_pasta = AUDIO_DIR
        elseif extensao in videos_ext:
            nova_pasta = VIDEOS_DIR
        elseif extensao in imagens_ext:
            nova_pasta = IMAGENS_DIR
        elseif extensao in documentos_ext:
            nova_pasta = DOCUMENTOS_DIR
        else
            nova_pasta = OUTROS_DIR
        
        velho = os.path.join(diretorio, arquivo)
        novo = os.path.join(nova_pasta, arquivo)   
        os.rename(velho, novo)
        
        print('Moveu do ', velho, ' -> ', novo)


if __name__ == '__main__':
    organizando('Downloads')

