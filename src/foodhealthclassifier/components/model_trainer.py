import os
import pandas as pd
import joblib

from pathlib import Path
from sklearn.linear_model import LogisticRegression
from foodhealthclassifier.logging import logger
from foodhealthclassifier.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config=ModelTrainerConfig):
        self.config = config

    def start_training(self):
        train_data = pd.read_csv(self.config.train_data_file)
        
        X_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]

        model = LogisticRegression(
            C=self.config.C,
            l1_ratio=self.config.l1_ratio,
            max_iter=self.config.max_iter,
            penalty=self.config.penalty,
            solver=self.config.solver
            )
        
        model.fit(X_train, y_train)
        joblib.dump(value=model, filename=os.path.join(self.config.root_dir, self.config.model_name))
        joblib.dump(value=model, filename=Path(f'models/{self.config.model_name}'))
        