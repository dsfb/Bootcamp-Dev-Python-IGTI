import joblib

# salvando o modelo no disco
nome_do_arquivo = 'melhor_modelo.sav' #
joblib.dump(melhor_modelo, nome_do_arquivo) 
# melhor_modelo = modelo com a maior acuracia
# nome_arquivo = caminho do local onde deve ser salvo o modelo



# carregando o modelo
modelo_salvo = joblib.load(nome_do_arquivo) # realiza a carga do modelo salvo
