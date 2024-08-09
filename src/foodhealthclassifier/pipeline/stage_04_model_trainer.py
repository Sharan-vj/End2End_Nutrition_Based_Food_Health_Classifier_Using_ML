from foodhealthclassifier.logging import logger
from foodhealthclassifier.config.configuration import Configuration_manager
from foodhealthclassifier.components.model_trainer import ModelTrainer


STAGE_NAME = 'Model Training'

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_manager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.start_training()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} Started <<<<<')
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<')
    
    except Exception as e:
        logger.exception(e)
        raise e 