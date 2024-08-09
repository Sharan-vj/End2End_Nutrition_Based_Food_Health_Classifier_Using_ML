from foodhealthclassifier.constants import *
from foodhealthclassifier.utils.common import create_directory, yaml_reader
from foodhealthclassifier.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)


class Configuration_manager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = yaml_reader(filepath=config_filepath, log=False)
        self.params = yaml_reader(filepath=params_filepath, log=False)
        self.schema = yaml_reader(filepath=schema_filepath, log=False)

        create_directory(directory_path=[self.config.artifact_root], log=True)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory(directory_path=[config.root_dir], log=True)

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directory(directory_path=[config.root_dir], log=True)

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            status_file=config.STATUS_FILE,
            all_schema=config.all_schema
        )

        return data_validation_config
    
    def get_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directory(directory_path=[config.root_dir], log=True)

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.LogisticRegression
        schema = self.schema.TARGET_COLUMN
        create_directory(directory_path=[config.root_dir], log=True)

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_file=config.train_data_file,
            test_data_file=config.test_data_file,
            model_name=config.model_name,
            C=params.C,
            l1_ratio=params.l1_ratio,
            max_iter=params.max_iter,
            penalty=params.penalty,
            solver=params.solver,
            target_column=schema.name
        )

        return model_trainer_config