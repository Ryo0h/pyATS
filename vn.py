import pandas as pd
import yaml
import os
import pyats

INVENTORY = ".\inventory.csv"

def file_to_yaml(file):
    yaml = pd.read_csv(file)
    
    return yaml


print(file_to_yaml(INVENTORY))
