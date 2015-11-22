
import re
import numpy as np

def parse_caffe_training(fname):

    f = open(fname)
    filetxt = f.read()

    test_accuracies = re.findall('Iteration (\d+).*\\n.*accuracy = (\d+\.\d+)', filetxt)
    test_losses = re.findall('Iteration (\d+).*\\n.*\\n.*Test.*loss = (\d+\.\d+)', filetxt)
    train_losses = re.findall('Iteration (\d+).*\\n.*Train.*loss = (\d+\.\d+)', filetxt)

    test_accuracies = [(int(x[0]), float(x[1])) for x in test_accuracies]
    test_losses = [(int(x[0]), float(x[1])) for x in test_losses]
    train_losses = [(int(x[0]), float(x[1])) for x in train_losses]

    test_accuracies = np.array(test_accuracies)
    test_losses = np.array(test_losses)
    train_losses = np.array(train_losses)

    return train_losses, test_losses, test_accuracies

