from foodhealthclassifier.logging import logger
from foodhealthclassifier.config.configuration import Configuration_manager
from foodhealthclassifier.components.data_validation import DataValidation


STAGE_NAME = 'Data Validation'

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_manager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_columns()
    

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} Started <<<<<')
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<')
    
    except Exception as e:
        logger.log(msg=e, level=1)
        raise(e)