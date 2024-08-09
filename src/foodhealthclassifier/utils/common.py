import os 
import yaml
import json
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from foodhealthclassifier.logging import logger


def yaml_reader(filepath: Path, log: True) -> ConfigBox:
    with open(filepath, 'r') as file:
        content = yaml.safe_load(file)
        if log:
            logger.info(f"Yaml file: {filepath} loaded successfully")
        return ConfigBox(content)
    

def create_directory(directory_path: list, log: True):
    for path in directory_path:
        os.makedirs(path, exist_ok=True)
        if log:
            logger.info(f"Directory created successfully")


def save_json(path: Path, data: dict, log: True):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        if log:
            logger.info(msg=f"Json file saved to {path}")


def load_json(path: Path, log: True) -> ConfigBox:
    with open(path, 'r') as f:
        content = json.load(f)
        if log:
            logger.info(msg="Json file loaded to {path}")
        return ConfigBox(content)


def save_binary(data: Any, path: Path, log: True):
    joblib.dump(value=data, filename=path)
    if log:
        logger.info(msg="Binary file saved to {path}")


def load_binary(path: Path, log: True):
    data = joblib.load(filename=path)
    if log:
        logger.info(msg="Binary file loaded from {path}")
    return data


def get_size(path: Path):
    size_kb = round(os.path.getsize(path)/1024)
    return f"{size_kb} KB"


def load_filemodel():
    model_path = Path("models/sales_predictor.pkl")
    model = joblib.load(filename=model_path)
    return model