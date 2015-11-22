import os

#solver_type: SGD
#base_lr: 0.001
#momentum: 0.9

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

for ab_select in ['_a', '_b']:

    fscript_fname = 'mnist_hp_search{ab_select}.sh'.format(**locals())

    with open (fscript_fname, 'w') as fscript:
        fscript.write('#!/bin/bash\n')

        with open('examples/mnist/lenet_solver_baseline.prototxt') as f:
            baseline_txt = f.read()

            for comb in hp:
                tmp_str = '__'.join(['%s_%s'%(k,comb[k]) for k in comb.keys()]) + ab_select

                lines = '\n'.join(['%s: %s'%(k,comb[k]) for k in comb.keys()])
                lines += '\nsnapshot_prefix: "examples/mnist/lenet_{tmp_str}"\n'.format(**locals())


                fname = 'examples/mnist/lenet_solver_%s.prototxt'%tmp_str

                with open(fname, 'w') as fproto:
                    fproto.write(lines + '\n' + baseline_txt)

                fscript.write(
                    '/local_stuff/caffe/build/tools/caffe train --solver={fname} >& log_{tmp_str}.txt & \n'.format(**locals()))

    os.system('chmod +x ' + fscript_fname)








