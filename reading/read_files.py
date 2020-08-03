import os 
import pandas as pd
import tqdm as tqdm
import numpy as np

path = '../data/'
path_labelled = path + 'labelled/'

def get_labelled(label):
    if label is 0:
        for r, d, f in os.walk(path_labelled + 'zero/', topdown = True):
            files = f
            del r
            del d

        return files
    elif label is 1:
        for r, d, f in os.walk(path_labelled + 'one/', topdown= True):
            files = f
            del r
            del d

        return files
    else:
        raise Exception('Label not understood')


def get_all():
    for r, d, f in os.walk(path + '/', topdown = True):
            files = f
            del r
            del d

    return files


def get_path_labelled(para):
    if para is 1:
        return str(path_labelled) + 'one/'
    elif para is 0:
        return str(path_labelled) + 'zero/'


def get_label_files(param):
    files = get_labelled(param)
    x = pd.DataFrame()
    # pbar = tqdm.
    print("Reading Files for Label '"+ str(param) +"'")
    with tqdm.tqdm(total = len(files), position= 0, leave= True, bar_format='{l_bar}{bar:40}{r_bar}', unit='files') as pbar:
        for name in files:
            t = pd.read_csv(get_path_labelled(param) + str(name))
            x = x.append(t, ignore_index = True)
            pbar.update(1)

    pbar.close()
    print("Got " + str(len(files)) + " Files for Label '"+ str(param) +"'\n")

    return x

# def 