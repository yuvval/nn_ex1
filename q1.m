clear
close all

load Q1_parse_results_a.mat
iter_0=500;
% title_str is the filename, remember to change it according to Anna/Yuval
plot_comparison(hp, 1:3, legend_SGD(1:3,:), 'SGD Momentum',iter_0)


plot_comparison(hp, [1,5], legend_AGAGRAD, 'ADAGRAD vs SGD',iter_0)


plot_comparison(hp, [6,7, 1], legend_NEST, 'NESTEROV',iter_0)


plot_comparison(hp, [8,9, 1], legend_SGD_LR, 'SGD Learning Rate',iter_0)

