from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.evalution import Evaluation
from src.cnnClassifier import logger

stage_name="Evalution stage"


class EvalutionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        val_config=config.get_validation_config()
        evaluation=Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        
        

        
if __name__ == '__main__':
        try:
            logger.info(f">>>>> stage {stage_name} started <<<<<")
            obj=EvalutionPipeline()
            obj.main()
            logger.info(f"<<<<<<<< stage {stage_name} completed >>>>>>>")
        except Exception as e :
              logger.exception(e)
              raise e
                   
        
        
    