from foodhealthclassifier.logging import logger
from foodhealthclassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline



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