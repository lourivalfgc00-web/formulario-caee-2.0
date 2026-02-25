from flask import Flask, render_template, request, send_file
from docxtpl import DocxTemplate
import os
from datetime import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELO = os.path.join(BASE_DIR, "modelo.docx")
PASTA_SAIDAS = os.path.join(BASE_DIR, "saidas")
os.makedirs(PASTA_SAIDAS, exist_ok=True)

def marca_checkbox(valor, esperado):
    return "X" if valor == esperado else " "

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/gerar")
def gerar():
    dados = request.form.to_dict()

    # Converte escolhas do select em "X" nos parênteses do modelo
    part = dados.get("PARTICIPACAO","")
    dados["PART_AUTONOMIA"] = marca_checkbox(part, "autonomia")
    dados["PART_APOIO"] = marca_checkbox(part, "apoio")
    dados["PART_PARCIAL"] = marca_checkbox(part, "parcial")
    dados["PART_RESISTENCIA"] = marca_checkbox(part, "resistencia")

    auto = dados.get("AUTONOMIA","")
    dados["AUTONOMIA_ALTA"] = marca_checkbox(auto, "alta")
    dados["AUTONOMIA_MEDIA"] = marca_checkbox(auto, "media")
    dados["AUTONOMIA_DESENV"] = marca_checkbox(auto, "desenvolvimento")

    # Gera o DOCX a partir do modelo
    doc = DocxTemplate(MODELO)
    doc.render(dados)

    nome_aluno = (dados.get("ALUNO") or "aluno").strip().replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    arquivo_saida = os.path.join(PASTA_SAIDAS, f"CAEE_Ficha_{nome_aluno}_{timestamp}.docx")
    doc.save(arquivo_saida)

    return send_file(
        arquivo_saida,
        as_attachment=True,
        download_name=os.path.basename(arquivo_saida),
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
