"""
Legenda Viva — Semana 0
Transcrição de áudio com faster-whisper.

Objetivo desta etapa: provar que o núcleo funciona. O script recebe um
arquivo de áudio e imprime o texto transcrito no terminal. Nada mais.

Uso:
    python transcribe.py caminho/do/audio.wav
    python transcribe.py caminho/do/audio.wav --modelo small --idioma pt
"""

import argparse
import sys
from pathlib import Path

from faster_whisper import WhisperModel


def formatar_tempo(segundos: float) -> str:
    """Converte segundos em MM:SS para exibir junto de cada trecho."""
    minutos, seg = divmod(int(segundos), 60)
    return f"{minutos:02d}:{seg:02d}"


def transcrever(caminho_audio: str, modelo: str = "small", idioma: str = "pt", verbose: bool = True) -> str:
    arquivo = Path(caminho_audio)
    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {arquivo}")

    if verbose:
        print(f"Carregando modelo '{modelo}'...")
        print("(na primeira vez o modelo e baixado, pode demorar alguns minutos)\n")

    # device='cpu' + compute_type='int8' roda em qualquer maquina, sem GPU.
    # Quando voce tiver GPU NVIDIA, troque para device='cuda'.
    model = WhisperModel(modelo, device="cpu", compute_type="int8")

    if verbose:
        print(f"Transcrevendo: {arquivo.name}\n")
    segmentos, info = model.transcribe(str(arquivo), language=idioma, beam_size=5)

    if verbose:
        print(f"(idioma detectado: {info.language} | confianca: {info.language_probability:.0%})\n")

    partes = []
    for seg in segmentos:
        inicio = formatar_tempo(seg.start)
        fim = formatar_tempo(seg.end)
        texto = seg.text.strip()
        if verbose:
            print(f"[{inicio} -> {fim}] {texto}")
        partes.append(texto)

    texto_completo = " ".join(partes)
    if verbose:
        print("\n----- Texto completo -----")
        print(texto_completo)
    return texto_completo


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transcreve um arquivo de audio para texto."
    )
    parser.add_argument(
        "audio",
        help="Caminho do arquivo de audio (.wav, .mp3, .m4a, .ogg...)",
    )
    parser.add_argument(
        "--modelo",
        default="small",
        help="Tamanho do modelo: tiny, base, small, medium (padrao: small)",
    )
    parser.add_argument(
        "--idioma",
        default="pt",
        help="Idioma do audio (padrao: pt). Use 'auto' para deteccao automatica.",
    )
    args = parser.parse_args()

    idioma = None if args.idioma == "auto" else args.idioma
    try:
        transcrever(args.audio, args.modelo, idioma)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
