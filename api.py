"""
Legenda Viva — Semana 1
API FastAPI que recebe um arquivo de áudio e devolve o texto transcrito.

Uso:
    uvicorn api:app --reload
    # Depois, POST /transcrever com o áudio no campo "audio".
"""

import tempfile
from pathlib import Path

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from transcribe import transcrever

app = FastAPI(
    title="Legenda Viva",
    description="Transcrição de fala para texto, gratuita e aberta.",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/transcrever")
async def endpoint_transcrever(
    audio: UploadFile = File(...),
    modelo: str = "small",
    idioma: str = "pt",
):
    """Recebe um arquivo de áudio e devolve o texto transcrito."""
    sufixo = Path(audio.filename).suffix if audio.filename else ".wav"

    with tempfile.NamedTemporaryFile(delete=False, suffix=sufixo) as tmp:
        conteudo = await audio.read()
        tmp.write(conteudo)
        tmp_path = tmp.name

    try:
        idioma_param = None if idioma == "auto" else idioma
        texto = transcrever(tmp_path, modelo, idioma_param)
        return {"texto": texto, "arquivo": audio.filename}
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
    finally:
        Path(tmp_path).unlink(missing_ok=True)
