from foodhealthclassifier.logging import logger
from foodhealthclassifier.config.configuration import Configuration_manager
from foodhealthclassifier.components.data_ingestion import DataIngestion


STAGE_NAME = 'Data Ingestion'

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_manager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_dataset()
        data_ingestion.extract_zip_file()
    

if __name__ == "__main__":
    try: 
        logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    
    except Exception as e:
        logger.log(level=1, msg=e)
        raise e 