from foodhealthclassifier.logging import logger
from foodhealthclassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from foodhealthclassifier.pipeline.stage_02_data_validation import DataValidationPipeline
from foodhealthclassifier.pipeline.stage_03_data_transformation import DataTransformationPipeline
from foodhealthclassifier.pipeline.stage_04_model_trainer import ModelTrainerPipeline

STAGE_NAME = 'Data Ingestion'
if __name__ == "__main__":
    try: 
        logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    
    except Exception as e:
        logger.log(level=1, msg=e)
        raise e
    

STAGE_NAME = 'Data Validation'
if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} Started <<<<<')
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<')
    
    except Exception as e:
        logger.log(msg=e, level=1)
        raise(e)
    

STAGE_NAME = 'Data Transformation'
if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} Started <<<<<')
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<')

    except Exception as e:
        logger.log(msg=e, level=1)
        raise(e)
    

STAGE_NAME = 'Model Training'
if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Stage {STAGE_NAME} Started <<<<<')
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<')

    except Exception as e:
        logger.log(msg=e, level=1)
        raise(e)