import numpy as np
import pickle
import joblib

class Model_Wine:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, scaler, form):
        """Avalia se o vinho é vermelho ou branco
        """
        X_input = np.array([form.vol_acid, 
                            form.alcohol, 
                            form.free_diox, 
                            form.chlorides ])
        x_input_scaled = scaler.transform(X_input.reshape(1, -1))
        # Faremos o reshape para que o modelo entenda que estamos passando
        is_red = model.predict(x_input_scaled)
        return int(is_red[0])