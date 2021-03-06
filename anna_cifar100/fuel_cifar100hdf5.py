import os
import tarfile

import h5py
import numpy
import six
from six.moves import cPickle

from fuel.converters.base import fill_hdf5_file, check_exists


DISTRIBUTION_FILE = '/home/lab/yuvval/nn_ex1/cifar100/cifar-100-python.tar.gz'


@check_exists(required_files=[DISTRIBUTION_FILE])
def convert_cifar100(directory, output_directory,
                     output_filename='cifar100'):
    """Converts the CIFAR-100 dataset to HDF5.
    Converts the CIFAR-100 dataset to an HDF5 dataset compatible with
    :class:`fuel.datasets.CIFAR100`. The converted dataset is saved as
    'cifar100.hdf5'.
    This method assumes the existence of the following file:
    `cifar-100-python.tar.gz`
    Parameters
    ----------
    directory : str
        Directory in which the required input files reside.
    output_directory : str
        Directory in which to save the converted dataset.
    output_filename : str, optional
        Name of the saved dataset. Defaults to 'cifar100.hdf5'.
    Returns
    -------
    output_paths : tuple of str
        Single-element tuple containing the path to the converted dataset.
    """
    output_train = os.path.join(output_directory, output_filename + '_train.hdf5')
    output_val = os.path.join(output_directory, output_filename + '_validation.hdf5')
    output_test = os.path.join(output_directory, output_filename + '_test.hdf5')
    h5file_train = h5py.File(output_train, mode="w")
    h5file_val = h5py.File(output_val, mode="w")
    h5file_test = h5py.File(output_test, mode="w")
    input_file = os.path.join(directory, 'cifar-100-python.tar.gz')
    tar_file = tarfile.open(input_file, 'r:gz')

    file = tar_file.extractfile('cifar-100-python/train')
    try:
        if six.PY3:
            train = cPickle.load(file, encoding='latin1')
        else:
            train = cPickle.load(file)
    finally:
        file.close()

    alltrain_data = train['data'].reshape(train['data'].shape[0],
                                           3, 32, 32)
    alltrain_coarse_labels = numpy.array(train['coarse_labels'],
                                      dtype=numpy.uint8)
    alltrain_fine_labels = numpy.array(train['fine_labels'],
                                    dtype=numpy.uint8)

    train_data = alltrain_data[0:40000,:,:,:]
    val_data = alltrain_data[40000:,:,:,:]

    train_coarse_labels = alltrain_coarse_labels[0:40000]
    val_coarse_labels = alltrain_coarse_labels[40000:]

    train_fine_labels = alltrain_fine_labels[0:40000]
    val_fine_labels = alltrain_fine_labels[40000:]

    file = tar_file.extractfile('cifar-100-python/test')
    try:
        if six.PY3:
            test = cPickle.load(file, encoding='latin1')
        else:
            test = cPickle.load(file)
    finally:
        file.close()

    test_data = test['data'].reshape(test['data'].shape[0],
                                         3, 32, 32)
    test_coarse_labels = numpy.array(test['coarse_labels'], dtype=numpy.uint8)
    test_fine_labels = numpy.array(test['fine_labels'], dtype=numpy.uint8)


    h5file_train.create_dataset("data", data=train_data.astype(float)/255)
    h5file_train.create_dataset("fine_labels", data=train_fine_labels.reshape((-1, 1)).astype(float))
    h5file_train.create_dataset("coarse_labels", data=train_coarse_labels.reshape((-1, 1)).astype(float))
    h5file_train.flush()
    h5file_train.close()

    h5file_val.create_dataset("data", data=val_data.astype(float)/255)
    h5file_val.create_dataset("fine_labels", data=val_fine_labels.reshape((-1, 1)).astype(float))
    h5file_val.create_dataset("coarse_labels", data=val_coarse_labels.reshape((-1, 1)).astype(float))
    h5file_val.flush()
    h5file_val.close()

    h5file_test.create_dataset("data", data=test_data.astype(float)/255)
    h5file_test.create_dataset("fine_labels", data=test_fine_labels.reshape((-1, 1)).astype(float))
    h5file_test.create_dataset("coarse_labels", data=test_coarse_labels.reshape((-1, 1)).astype(float))
    h5file_test.flush()
    h5file_test.close()

    return (output_train,output_test)


def fill_subparser(subparser):
    """Sets up a subparser to convert the CIFAR100 dataset files.
    Parameters
    ----------
    subparser : :class:`argparse.ArgumentParser`
        Subparser handling the `cifar100` command.
    """
    return convert_cifar100