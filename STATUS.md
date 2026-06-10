# STATUS

> Atualize este arquivo em UMA linha no fim de cada sessão de trabalho.
> Ele é a memória do projeto: qualquer conversa futura (sua ou com a IA) lê
> isto e retoma na hora, sem você reexplicar nada.

## Onde estamos
Semana 1 — API FastAPI criada (`api.py`). Endpoint POST `/transcrever` recebe
áudio e devolve JSON com o texto. Falta testar com um áudio real via curl/Swagger.

## Próxima entrega
Subir `uvicorn api:app --reload`, enviar um áudio via curl ou Swagger (`/docs`)
e confirmar que a resposta JSON contém o texto correto.

## Regras do projeto (não esquecer)
- Nada de feature nova antes da Semana 4. Ideia que surgir vai para IDEIAS.md.
- Check-in semanal: domingo à noite, responder "entreguei a da semana? sim/não, por quê".

## Histórico
- [Semana 0] Repositório iniciado. Script transcribe.py + README + estrutura.
- [Semana 0] Teste com áudio real: transcrição funcionou no terminal.
- [Semana 1] API FastAPI criada (api.py). Endpoints: GET /health, POST /transcrever.
