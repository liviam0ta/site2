from flask import Flask
import random

app = Flask(__name__)

fatos = [
    "Os polvos têm três corações!",
    "As abelhas conseguem reconhecer rostos!",
    "O dia em Vênus é mais longo que seu ano!",
    "As girafas têm a língua azul!",
    "Os flamingos nascem cinzentos e só ficam rosa por causa da alimentação!",
    "O coração de um camarão está localizado em sua cabeça!",
    "As borboletas sentem o gosto com os pés!",
    "Os morcegos sempre viram à esquerda ao sair de uma caverna!",
    "Os elefantes são capazes de saltar!",
    "As estrelas-do-mar podem regenerar seus braços perdidos!",
]

@app.route("/")
def home():
    return """
    <h1>Página inicial</h1>
    <p>Bem-vindo ao meu site!</p>
    <a href="/random_fact">Veja um fato aleatório!</a>
    """

@app.route("/random_fact")
def random_fact():
    fato = random.choice(fatos)
    return f"""
    <h1>Fato aleatório</h1>
    <p>{fato}</p>
    <a href="/">Voltar para a página inicial</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
