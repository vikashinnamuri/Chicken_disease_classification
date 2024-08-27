import os   #used to control the os 
from box.exceptions import BoxValueError   # used as an exception in the try cath method 
import yaml   #used to read the yaml file using python 
from src.cnnClassifier import logger #imported from same dir
import json 
import joblib   #used for parallel processing
from ensure import ensure_annotations  # it will take care of passing proper error  and makes easy to debug 
from box import ConfigBox   # configbox make the code reability easy when compard to normal 
from pathlib import Path
from typing import Any
import base64


@ensure_annotations  #This decorator is used to ensure that all function annotations (such as type hints) are present and correct according to the function's definition. 
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
            logger.info(f" yaml file:{path_to_yaml} successfully loaded")
            return ConfigBox(content)
    except BoxValueError:    
         raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list ,verbose=True):
     """ 
     create the list of directories
     
     agrs:
     path_to_directories(list): list of path directories
     ignoe_log: ignore if multiple dirc are exist
     
     """
     for path in path_to_directories:
          os.makedirs(path,exist_ok=True)
          if verbose:
               logger.info(F"Created directories at: {path}")     
          
@ensure_annotations
def save_json(path: Path,data: dict):
     """
        This function is used to store the data into json
        
        args:
        path(path):path to json
        data(dict):data to be stored in json
     
     """ 
     with open(path,"w") as f:
          json.dump(data,f,indent=4)
     logger.info(f"json file saved at:{path}")               
     
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

     
@ensure_annotations
def load_bin(path: Path)->Any:
     """_summary_
        load binary 
     Args:
         path (path): path to binary file 

     Returns:
         Any: object store in the file 
     """
     data=joblib.load(path)
     logger.info(f"binary file loaded from:{path}")
     return data


@ensure_annotations
def get_size(path: Path)->str:
     """
     This function is used to get the size of the file

     Args:
         path (path): path of the file

     Returns:
         str: size in kb
     """
     size_in_KB=round(os.path.getsize(path)/1024)
     return f"~{size_in_KB} KB"

def decodeimage(imgstring,fileName):
     imgdata=base64.b64decode(imgstring)
     with open(fileName,'wb') as f:
          f.write(imgdata)
          f.close()
       
       
def encodedimageintobas64(croppedImagePath):
     with open(croppedImagePath,"rb") as f:
          return base64.b64encode(f.read())
               
