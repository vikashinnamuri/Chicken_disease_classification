from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.satge_01_data_ingestion import DataIngestionTrainingpipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import preparebasemodeltrainingpipeline
stage_name="Data Ingestion stage"

try:
    logger.info(f">>>>> stage {stage_name} started <<<<<")
    obj=DataIngestionTrainingpipeline()
    obj.main()
    logger.info(f"<<<<<<<< stage {stage_name} completed >>>>>>>")
except Exception as e :
    logger.exception(e)
    raise e
try:
    logger.info(f">>>>> stage {stage_name} started <<<<<")
    obj=preparebasemodeltrainingpipeline()
    obj.main()
    logger.info(f"<<<<<<<< stage {stage_name} completed >>>>>>>")
except Exception as e :
        logger.exception(e)
        raise e   
    
    
 