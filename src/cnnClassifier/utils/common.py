import os   #used to control the os 
from box.exceptions import BoxValueError   # 
import yaml
from src.cnnClassifier import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ read yaml file and return 
    
    args: 
         path_to_yaml (str):path like input
    
    raises:
         valueerror:if yaml file is empty 
         e:empty file 
     return:
         ConfigBox -configbox type         
    
    """
    
    # this beloow code is used the read the yaml file step by step
    try:
         with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f" yaml file:{yaml_file} successfully loaded")
            return ConfigBox(content)
    except BoxValueError:    
         raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
            