from model.evaluator import Evaluator
from model.dataset_loader import Dataset_Loader
from model.modelo import Model_Wine
import pandas as pd

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Dataset_Loader()
avaliador = Evaluator()

#  Parametros
url_dados_red = ('https://raw.githubusercontent.com/lucasvilela21/wine_datasets/main/winequality-red.csv')
url_dados_white = ('https://raw.githubusercontent.com/lucasvilela21/wine_datasets/main/winequality-white.csv ')

# Carga dos dados
dataset_red = carregador.load_dataset(url_dados_red)
dataset_white = carregador.load_dataset(url_dados_white)
# Criando base de dados total
dataset_wines = pd.concat([ dataset_red.assign(is_red=1), dataset_white.assign(is_red=0)])

# Seleção de features determinantes para a predição da cor do vinho
features = ['volatile acidity','alcohol','free sulfur dioxide','chlorides','is_red']

dataset_feature = dataset_wines[features]

# Separando em dados de entrada e saída
X = dataset_feature.iloc[:, 0:-1]
Y = dataset_feature.iloc[:, -1]   
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo():  
    # Importando o modelo de regressão logística
    lr_path = 'ml_model/model_wine.pkl'
    modelo_teste = Model_Wine.carrega_modelo(lr_path)
    # Carregando scaler
    ml_path = 'ml_model/scaler_wine.pkl'
    scaler_teste = Model_Wine.carrega_modelo(ml_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_teste, recall_teste, precisao_teste, f1_teste = avaliador.evaluate(modelo_teste,scaler_teste, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_teste >= 0.8 
    assert recall_teste >= 0.5 
    assert precisao_teste >= 0.5 
    assert f1_teste >= 0.5 
    

