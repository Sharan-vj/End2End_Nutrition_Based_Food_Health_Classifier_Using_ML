import os
import pandas as pd

from sklearn.model_selection import train_test_split
from foodhealthclassifier.logging import logger
from foodhealthclassifier.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config=DataTransformationConfig):
        self.config = config

    def split_dataset(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)
        logger.info(msg=f'Splitted data into training and Test set')
        logger.info(msg=train.shape)
        logger.info(msg=test.shape)