from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) #this code  in Python is used to define a data class where instances are immutable
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path