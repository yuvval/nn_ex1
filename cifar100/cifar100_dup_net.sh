#!/bin/bash
/local_stuff/caffe/build/tools/caffe train --solver=network/cifar100_finecoarse_dup_solver.prototxt --weights  /cortex/yuvval/caffe/ex1/yuval/cifar100_coarse_full_base_lr_0.0001__weight_decay_4e-08__solver_type_SGD_iter_24000.caffemodel  >& log_finecoarse_dup.txt & 
