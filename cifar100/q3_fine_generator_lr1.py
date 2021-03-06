import os

#solver_type: SGD
#base_lr: 0.001
#momentum: 0.9

hp = [] # hyper params
hp += [{'solver_type' : 'SGD', 'base_lr' : '0.00001', 'weight_decay' : '4e-10' }]

for ab_select in ['']:

    fscript_fname = 'cifar100_hp_search{ab_select}.sh'.format(**locals())

    with open (fscript_fname, 'w') as fscript:
        fscript.write('#!/bin/bash\n')

        with open('network/cifar100_fine_full_solver_BASELINE.prototxt') as f:
            baseline_txt = f.read()

            for comb in hp:
                tmp_str = '__'.join(['%s_%s'%(k,comb[k]) for k in comb.keys()]) + ab_select

                lines = '\n'.join(['%s: %s'%(k,comb[k]) for k in comb.keys()])
                lines += '\nsnapshot_prefix: "/cortex/yuvval/caffe/ex1/yuval/cifar100_fine_lr1_full_{tmp_str}"\n'.format(**locals())


                fname = 'network/cifar100_fine_full_solver_%s.prototxt'%tmp_str

                with open(fname, 'w') as fproto:
                    fproto.write(lines + '\n' + baseline_txt)

                fscript.write(
                    '/local_stuff/caffe/build/tools/caffe train --solver={fname} --weights  /cortex/yuvval/caffe/ex1/yuval/cifar100_fine_full_base_lr_0.0001__weight_decay_4e-10__solver_type_SGD_iter_36000.caffemodel  >& log_fine_lr1_{tmp_str}.txt & \n'.format(**locals()))

    os.system('chmod +x ' + fscript_fname)








