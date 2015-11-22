
import re

def parse_caffe_training(fname):

    f = open(fname)
    filetxt = f.read()

    test_accuracies = re.findall('Iteration (\d+).*\\n.*accuracy = (\d+\.\d+)', filetxt)
    test_losses = re.findall('Iteration (\d+).*\\n.*\\n.*Test.*loss = (\d+\.\d+)', filetxt)
    train_losses = re.findall('Iteration (\d+).*\\n.*Train.*loss = (\d+\.\d+)', filetxt)

    return train_losses, test_losses, test_accuracies

