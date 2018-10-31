# Kononov Sergey BD-21
# save/load pytohn objects with pickle module

import pickle

def save_obj(obj, filepath='compressed.pckl'):
    f = open(filepath, 'w')
    protocol = pickle.HIGHEST_PROTOCOL
    pickle.dump(obj, f, protocol)

def load_obj(filepath='compressed.pckl'):
    f = open(filepath, 'r')
    return pickle.load(f)
