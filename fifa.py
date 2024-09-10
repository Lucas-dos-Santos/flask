from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pandas as pd
import pickle
import numpy as np
import random

app = Flask(__name__, template_folder='docs')



class Times:
    def __init__(self, nome, orcamento, liga, ext, obj, des):
        self.nome = nome
        self.orcamento = orcamento
        self.liga = liga
        self.ext = ext
        self.obj = obj
        self.des = des


times = [
    Times("Brentford", "22.206.392", "Premier League", "",
          "Ganhar a Premier League", "Procurar promessas em times pequenos"),
    Times("UD Ibiza", "1.777.044", "La Liga Smartbank", "",
          "Subir para La Liga", "Focar em jogadores nativos das Ilhas Baleares"),
    Times("Athletic Bilbao", "21.830.000", "La Liga", "", "Ganhar a La Liga",
          "Seguir a tradição de contratar apenas jogadores de origem basca"),
    Times("Andorra", "baixo", "La Liga Smartbank", "Time do jogador Pique",
          "Levar o time a La Liga", "Focar em jogadores de origem catalã"),
    Times("Real Valladolid", "baixo", "La Liga", "Time do jogador Ronaldo",
          "Classificar o time para competição internacional", "Focar em jogadores brasileiros"),
    Times("Wrexham United", "baixo", "Ligas galesas na quinta divisão inglesa", "Time do ator Ryan Reynolds",
          "Levar o time à elite do futebol inglês", "Focar em promessas e investir na base"),
    Times("Bordeaux", "baixo", "Ligue 2", "Time que disputava competições internacionais, rebaixado por problemas financeiros",
          "Levar o time à elite do futebol novamente", "Focar em jogadores jovens e promessas"),
    Times("Union Berlin", "baixo", "Bundesliga", "Um time em grande ascensão",
          "Levar o time para competições internacionais", "Focar em promessas"),
    Times("Fiorentina", "médio", "Serie A italiana", "Time de tradição com poucos títulos",
          "Superar rivais e ganhar títulos expressivos", "Fazer contratações pontuais"),
    Times("Nottingham Forest", "baixo", "Premier League", "Time que contratou mais de 20 atletas para se manter na liga",
          "Ficar na parte de cima da tabela", "Focar em jogadores promissores")
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    if request.method == 'POST':
        time = random.choice(times)
        return render_template('resultado.html', resultado=time)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
