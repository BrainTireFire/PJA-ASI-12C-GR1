
import os
import opendatasets as od

def download_dataset(url, destination):
    od.download(url, destination)
    print('Dataset downloaded and extracted successfully')
