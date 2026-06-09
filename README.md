# Legenda Viva

Transcrição de fala em tempo quase real, pensada para pessoas surdas ou com perda
auditiva acompanharem uma conversa pela tela do próprio celular. Gratuito e aberto.

> **Estado atual:** Semana 0 — provar que o núcleo de transcrição funciona.
> Veja [`STATUS.md`](STATUS.md) para saber exatamente onde o projeto está e qual é o próximo passo.

## Por que existe

Existem mais de 18 milhões de pessoas com deficiência no Brasil, e ferramentas de
legenda ao vivo no celular ou são pagas, ou dependem de serviços de nuvem caros.
O objetivo aqui é o menor caminho até algo que uma pessoa real consiga usar de graça.

## Como rodar (Semana 0)

Pré-requisito: Python 3.9 ou superior.

```bash
# 1. Crie e ative um ambiente virtual (recomendado)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Grave um áudio de teste no celular (uma frase qualquer), passe pro PC, e rode:
python transcribe.py meu_audio.wav
```

Na primeira execução o modelo é baixado automaticamente (pode levar alguns minutos).
Depois disso, roda offline.

## Roteiro

- [ ] **Semana 0** — transcrever um arquivo de áudio no terminal *(você está aqui)*
- [ ] **Semana 1** — virar um serviço: API FastAPI que recebe áudio e devolve texto
- [ ] **Semana 2** — tela web (React): botão de microfone → texto na tela
- [ ] **Semana 3** — usável no celular (responsivo, acessível) e quase em tempo real
- [ ] **Semana 4** — uma pessoa real usando, repositório público

Ideias que surgirem no meio do caminho vão para [`IDEIAS.md`](IDEIAS.md) — anotadas,
**não** implementadas, até a Semana 4 estar pronta.

## Licença
