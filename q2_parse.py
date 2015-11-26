import matplotlib.pyplot as plt
import numpy as np
import parse_caffe
import scipy.io


hp = [] # hyper params
hp += [{'weight_decay' : '0.05'}]
hp += [{'weight_decay' : '0.0005'}]
hp += [{'weight_decay' : '0.00005'}]
hp += [{'weight_decay' : '0'}]
ab_select = '_b' # '_a' or '_b'

for hp_id, comb in enumerate(hp):
    tmp_str = '__'.join(['%s_%s'%(k,comb[k]) for k in comb.keys()]) + ab_select

    logfname = 'log_{tmp_str}.txt'.format(**locals())

    train_losses, test_losses, test_accuracies = parse_caffe.parse_caffe_training(logfname)
    hp[hp_id]['train_losses'] = train_losses
    hp[hp_id]['test_losses'] = test_losses
    hp[hp_id]['test_accuracies'] = test_accuracies




# plot SGD momentum comparison
legend_weight_decay = ['weight decay = %s'%comb['weight_decay'] for comb in hp]

results = {'hp': hp,
           'legend_weight_decay': legend_weight_decay
           }

scipy.io.savemat('Q2_parse_results' + ab_select + '.mat', results)

