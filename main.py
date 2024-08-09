from foodhealthclassifier.logging import logger
from foodhealthclassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from foodhealthclassifier.pipeline.stage_02_data_validation import DataValidationPipeline


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