from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.satge_01_data_ingestion import DataIngestionTrainingpipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import preparebasemodeltrainingpipeline
from src.cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_evalution import EvalutionPipeline
stage_name="Data Ingestion stage"

try:
    logger.info(f">>>>> stage {stage_name} started <<<<<")
    obj=DataIngestionTrainingpipeline()
    obj.main()
    logger.info(f"<<<<<<<< stage {stage_name} completed >>>>>>>")
except Exception as e :
    logger.exception(e)
    raise e

stage_name="Prepare Base Model"
try:
    logger.info(f">>>>> stage {stage_name} started <<<<<")
    obj=preparebasemodeltrainingpipeline()
    obj.main()
    logger.info(f"<<<<<<<< stage {stage_name} completed >>>>>>>")
except Exception as e :
        logger.exception(e)
        raise e   
    
STAGE_NAME="Training"
    
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")
except Exception as e :
    logger.exception(e)
    raise e
    
            
STAGE_NAME="Evalution stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj=EvalutionPipeline()
    obj.main()
    logger.info(f"<<<<<<<< stage {STAGE_NAME} completed >>>>>>>")
except Exception as e :
    logger.exception(e)
    raise e            


