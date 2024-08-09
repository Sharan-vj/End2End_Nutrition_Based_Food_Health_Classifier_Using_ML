import os
import pandas as pd

from foodhealthclassifier.logging import logger
from foodhealthclassifier.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config

    
    def validate_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for cols in all_cols:
                if cols not in all_cols:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f'Validation status: {validation_status}')
                
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f'Validation status: {validation_status}')

            return validation_status


        except Exception as e:
            raise e