import pathlib

import pandas as pd
import datetime
import os

training_data = "data/s&p.csv"

now = datetime.datetime.now()
trained_model_dir = f"trained_models/{now}"
os.makedirs(trained_model_dir)
