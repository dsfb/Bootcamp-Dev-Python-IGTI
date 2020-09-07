import numpy as np
import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def previsao_diabetes(lista_valores_formulario):
  prever=np.array(lista_valores_formulario).reshape(1, 8)   # transforma os valores do formulario
  modelo_salvo = joblib.load('melhor_modelo.sav')           # realiza a carga do modelo salvo
  resultado = modelo_salvo.predict(prever)                  # aplica a previsao
  return resultado[0]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        lista_formulario=request.form.to_dict()
        lista_formulario=list(lista_formulario.values())
        lista_formulario= list(map(int,  lista_formulario))
        from IPython import embed; embed()
        resultado=previsao_diabetes(lista_formulario)
#       if int(resultado) == 1:
#           previsao = 'Possui diabetes'
#       else:
#           previsao = 'Nao possui diabetes'

#         # retorna o resultado para uma pagina html
#         return render_template("resultado.html", previsao=previsao)

if __name__ == "__main__":
    app.run(debug=True, reload=True)
