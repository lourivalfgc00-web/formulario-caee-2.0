# Site (CAEE) – Gerador de Word (.docx)

## O que faz
- Abre um formulário no navegador
- Ao enviar, gera um arquivo Word (.docx) usando o **modelo.docx**
- Força o download do arquivo para o computador do usuário

## Como rodar no Windows (sem complicação)
1) Instale o Python 3.10+ (se ainda não tiver)
2) Abra o Prompt dentro desta pasta e rode:

    pip install -r requirements.txt
    python app.py

3) Abra no navegador:
   http://127.0.0.1:5000

## Como ajustar o modelo Word
- O arquivo `modelo.docx` já está preparado com campos do tipo `{{NOME_DO_CAMPO}}`.
- Se você editar o modelo, mantenha os placeholders.

## Onde ficam os arquivos gerados
- Na pasta `saidas/` (e também baixa no navegador).

