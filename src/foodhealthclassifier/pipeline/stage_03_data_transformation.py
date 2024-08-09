from pathlib import Path
from foodhealthclassifier.logging import logger
from foodhealthclassifier.config.configuration import Configuration_manager
from foodhealthclassifier.components.data_transformation import DataTransformation


STAGE_NAME = 'Data Transformation'

class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status = f.read().split(' ')[-1]

            if status == 'True':
                config = Configuration_manager()
                data_transformation_config = config.get_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.split_dataset()
        except Exception as e:
            raise e 
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    