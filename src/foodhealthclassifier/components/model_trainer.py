import os
import pandas as pd
import joblib
import mlflow

from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from foodhealthclassifier.logging import logger
from foodhealthclassifier.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config=ModelTrainerConfig):
        self.config = config

    def start_training(self):
        train_data = pd.read_csv(self.config.train_data_file)
        test_data = pd.read_csv(self.config.test_data_file)
        
        X_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]

        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        mlflow.set_experiment(experiment_name='Model Training')
        with mlflow.start_run() as run:
            mlflow.log_param(key='C', value=self.config.C)
            mlflow.log_param(key='l1_ratio', value=self.config.l1_ratio)
            mlflow.log_param(key='max_iter', value=self.config.max_iter)
            mlflow.log_param(key='penalty', value=self.config.penalty)
            mlflow.log_param(key='solver', value=self.config.solver)

            model = LogisticRegression(
                C=self.config.C,
                l1_ratio=self.config.l1_ratio,
                max_iter=self.config.max_iter,
                penalty=self.config.penalty,
                solver=self.config.solver
                )
        
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            mlflow.log_metric(key='accuracy', value=accuracy)
            
            joblib.dump(value=model, filename=os.path.join(self.config.root_dir, self.config.model_name))
            joblib.dump(value=model, filename=Path(f'models/{self.config.model_name}'))
        