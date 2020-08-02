import os

path = '../data/labelled/'

def get_labelled(label):
    if label is 0:
        for r, d, f in os.walk(path + 'zero/'):
            files = f
            del r
            del d

        return files
    elif label is 1:
        for r, d, f in os.walk(path + 'one/'):
            files = f

        return files
    else:
        raise Exception('Label not understood')
