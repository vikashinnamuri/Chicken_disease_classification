from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger

 

stage_name="Data Ingestion stage"

class DataIngestionTrainingpipeline:
    def __init__(self):
        pass
    def main(self):
         config = ConfigurationManager()
         data_ingestion_config = config.get_data_ingestion_config()
         data_ingestion = DataIngestion(config=data_ingestion_config)
         data_ingestion.download_file()
         data_ingestion.extract_unzip_file()
        
        
        
if __name__ == '__main__':
        try:
            logger.info(f">>>>> stage {stage_name} started <<<<<")
            obj=DataIngestionTrainingpipeline()
            obj.main()
            logger.info(f"<<<<<<<< stage {stage_name} completed >>>>>>>")
        except Exception as e :
              logger.exception(e)
              raise e
           
            