from pathlib import Path
import boto3
from mypy_boto3_rekognition.type_defs import (
    CelebrityTypeDef,
    RecognizeCelebritiesResponseTypeDef,
)
from PIL import Image, ImageDraw, ImageFont


# Cliente do AWS Rekognition
rekognition_client = boto3.client("rekognition", region_name='us-west-2')


def obter_caminho_arquivo(nome_arquivo: str) -> str:
    """
    Retorna o caminho completo de um arquivo localizado no diretório 'imagens'.
    
    :param nome_arquivo: Nome do arquivo de imagem.
    :return: Caminho completo do arquivo.
    """
    return str(Path(__file__).parent / "images" / nome_arquivo)


def detectar_celebres(imagem: str) -> RecognizeCelebritiesResponseTypeDef:
    """
    Envia uma imagem para o AWS Rekognition e detecta celebridades nela.
    
    :param imagem: Caminho do arquivo da imagem.
    :return: Resposta da API contendo informações sobre as celebridades detectadas.
    """
    with open(imagem, "rb") as img:
        return rekognition_client.recognize_celebrities(Image={"Bytes": img.read()})


def desenhar_caixas_reconhecimento(
    caminho_imagem: str, caminho_saida: str, detalhes_faces: list[CelebrityTypeDef]
):
    """
    Desenha caixas ao redor das faces reconhecidas na imagem e salva a nova imagem.
    
    :param caminho_imagem: Caminho da imagem original.
    :param caminho_saida: Caminho onde a imagem processada será salva.
    :param detalhes_faces: Lista de detalhes das celebridades reconhecidas.
    """
    imagem = Image.open(caminho_imagem)
    desenhador = ImageDraw.Draw(imagem)
    fonte = ImageFont.truetype("Ubuntu-R.ttf", 20)

    largura, altura = imagem.size

    for face in detalhes_faces:
        caixa = face["Face"]["BoundingBox"]  # type: ignore
        esquerda = int(caixa["Left"] * largura)  # type: ignore
        topo = int(caixa["Top"] * altura)  # type: ignore
        direita = int((caixa["Left"] + caixa["Width"]) * largura)  # type: ignore
        inferior = int((caixa["Top"] + caixa["Height"]) * altura)  # type: ignore

        confianca = face.get("MatchConfidence", 0)
        if confianca > 90:
            desenhador.rectangle([esquerda, topo, direita, inferior], outline="blue", width=3)

            nome = face.get("Name", "")
            posicao_texto = (esquerda, topo - 20)
            bbox = desenhador.textbbox(posicao_texto, nome, font=fonte)
            desenhador.rectangle(bbox, fill="blue")
            desenhador.text(posicao_texto, nome, font=fonte, fill="white")

    imagem.save(caminho_saida)
    print(f"Imagem processada salva em: {caminho_saida}")


if __name__ == "__main__":
    lista_imagens = [
        obter_caminho_arquivo("bbc.jpg"),
        obter_caminho_arquivo("msn.jpg"),
        obter_caminho_arquivo("neymar-torcedores.jpg"),
    ]

    for caminho_imagem in lista_imagens:
        resposta = detectar_celebres(caminho_imagem)
        faces_detectadas = resposta["CelebrityFaces"]
        if not faces_detectadas:
            print(f"Nenhuma celebridade encontrada na imagem: {caminho_imagem}")
            continue
        caminho_saida = obter_caminho_arquivo(f"{Path(caminho_imagem).stem}-detectado.jpg")
        desenhar_caixas_reconhecimento(caminho_imagem, caminho_saida, faces_detectadas)

