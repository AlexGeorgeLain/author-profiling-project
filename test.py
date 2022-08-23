import tensorflow as tf
from tensorflow import keras
import numpy as np
import sklearn as sk
import spacy
import pandas as pd

nlp = spacy.load('en_core_web_sm')


df = pd.read_xml("/Users/alexlain/github/author-profiling-project/0aa7bace-924c-40fb-a2e5-3c7012ede244.xml")

print(df.head())
