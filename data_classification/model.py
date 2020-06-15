import json
import numpy as np

def load_model(inp_file):
    model = None
    with open(inp_file, 'r') as inp:
        model = json.loads(inp.read())
    return np.array(model['data'])

def dump_model(out_file, model):
    with open(out_file, 'w') as out:
        out.write(json.dumps(model))

def load_labels(inp_file):
    labels = None
    with open(inp_file, 'r') as inp:
        labels = json.loads(inp.read())
    return np.array(labels['labels'])