from sklearn.model_selection import train_test_split

class Dataset_PreProcess:

# Pre processa o dataset conforme os features informados
    def pre_process_dataset(self,dataset, test_percentual,seed, feature1, feature2 = None , feature3 = None, feature4 = None):
        # feature selection
        features = []
        for feature in [feature1, feature2, feature3,feature4, 'is_red']: # include target variable in the lats column
          if feature is not None:
            features.append(feature)
        
        dataset_feature = dataset[features]

        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset_feature,
                                                                  test_percentual,
                                                                  seed)

        return (X_train, X_test, Y_train, Y_test)
# prepara os grupos de treino e de teste considerando o target como ultima coluna
    def __prepare_holdout(self, dataset, test_percentual, seed):
        datas = dataset.values
        X = datas[:, 0:-1]
        Y = datas[:, -1]
        return train_test_split(X, Y, test_size=test_percentual, shuffle=True, random_state=seed)
