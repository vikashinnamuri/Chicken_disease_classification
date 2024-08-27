import os 
import  urllib.request as request  #used to download the file from the url
import zipfile  # used for unzip file 
from src.cnnClassifier import logger  #used to enter the loggers into logs folders
from src.cnnClassifier.utils.common import get_size # this gives the size of the file 
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with the info of:\n {header}")
        else:
            logger.info(f"The file already exisit with the size of{get_size(Path(self.config.local_data_file))}")
            
    def extract_unzip_file(self):
        """_summary_
        
            zip_file_path:str
            extract the zip file data into the data dictornary 
            functio return none
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
          
                