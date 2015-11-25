import matplotlib.pyplot as plt
import numpy as np
import parse_caffe
import scipy.io


hp = [] # hyper params
hp += [{'solver_type' : 'SGD', 'base_lr' : '0.01', 'momentum' : '0.9'}]
hp += [{'solver_type' : 'SGD', 'base_lr' : '0.01', 'momentum' : '0.5'}]
hp += [{'solver_type' : 'SGD', 'base_lr' : '0.01', 'momentum' : '0'}]
hp += [{'solver_type' : 'SGD', 'base_lr' : '0.01', 'momentum' : '1'}]

hp += [{'solver_type' : 'ADAGRAD', 'base_lr' : '0.01'}]

hp += [{'solver_type' : 'NESTEROV', 'base_lr' : '0.01', 'momentum' : '0.9'}]
hp += [{'solver_type' : 'NESTEROV', 'base_lr' : '0.01', 'momentum' : '0'}]

hp += [{'solver_type' : 'SGD', 'base_lr' : '0.001', 'momentum' : '0.9'}]
hp += [{'solver_type' : 'SGD', 'base_lr' : '0.1', 'momentum' : '0.9'}]

ab_select = '_a' # '_a' or '_b'

for hp_id, comb in enumerate(hp):
    tmp_str = '__'.join(['%s_%s'%(k,comb[k]) for k in comb.keys()]) + ab_select

    logfname = 'log_{tmp_str}.txt'.format(**locals())

    train_losses, test_losses, test_accuracies = parse_caffe.parse_caffe_training(logfname)
    hp[hp_id]['train_losses'] = train_losses
    hp[hp_id]['test_losses'] = test_losses
    hp[hp_id]['test_accuracies'] = test_accuracies




# plot SGD momentum comparison
legend_SGD = ['SGD, Momentum = %s'%comb['momentum'] for comb in hp[0:4]]

legend_AGAGRAD = ['SGD, Momentum = 0.9', 'ADAGRAD']

legend_NEST = ['NESTEROV, Momentum = %s'%comb['momentum'] for comb in hp[5:7]]
legend_NEST += ['SGD, Momentum = 0.9']

legend_SGD_LR = ['SGD, base\_lr = %s'%comb['base_lr'] for comb in hp[7:9]]
legend_SGD_LR += ['SGD, base\_lr = 0.01']

results = {'hp': hp,
           'legend_SGD': legend_SGD,
           'legend_AGAGRAD': legend_AGAGRAD,
           'legend_NEST': legend_NEST,
           'legend_SGD_LR': legend_SGD_LR,
           }

scipy.io.savemat('Q1_parse_results' + ab_select + '.mat', results)



# fieldname = 'train_losses'
# plt.plot(hp[0][fieldname][:, 0], hp[0][fieldname][:, 1])
# plt.plot(hp[1][fieldname][:, 0], hp[1][fieldname][:, 1])
# plt.plot(hp[2][fieldname][:, 0], hp[2][fieldname][:, 1])
# plt.plot(hp[3][fieldname][:, 0], hp[3][fieldname][:, 1])
# plt.legend(lgd)
# plt.show()
#
# fieldname = 'test_losses'
# plt.plot(hp[0][fieldname][:, 0], hp[0][fieldname][:, 1])
# plt.plot(hp[1][fieldname][:, 0], hp[1][fieldname][:, 1])
# plt.plot(hp[2][fieldname][:, 0], hp[2][fieldname][:, 1])
# plt.plot(hp[3][fieldname][:, 0], hp[3][fieldname][:, 1])
# plt.legend(lgd)
# plt.show()
#
#
# fieldname = 'test_accuracies'
# plt.plot(hp[0][fieldname][:, 0], hp[0][fieldname][:, 1])
# plt.plot(hp[1][fieldname][:, 0], hp[1][fieldname][:, 1])
# plt.plot(hp[2][fieldname][:, 0], hp[2][fieldname][:, 1])
# plt.plot(hp[3][fieldname][:, 0], hp[3][fieldname][:, 1])
# plt.legend(lgd)
# plt.show()
