from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_base_model import  PrepareBaseModel
from src.cnnClassifier import logger


stage_name="prepare base model"

class preparebasemodeltrainingpipeline:
    def __init__(self):
        pass
    def main(self):
         config = ConfigurationManager()
         prepare_base_model_config = config.get_prepare_base_model_config()
         prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
         prepare_base_model.get_base_model()
         prepare_base_model.update_base_model()
        
        
        
        
if __name__ == '__main__':
        try:
            logger.info(f">>>>> stage {stage_name} started <<<<<")
            obj=preparebasemodeltrainingpipeline()
            obj.main()
            logger.info(f"<<<<<<<< stage {stage_name} completed >>>>>>>")
        except Exception as e :
              logger.exception(e)
              raise e
           
                    