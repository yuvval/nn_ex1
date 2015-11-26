clear
close all

load Q2_parse_results_a.mat
iter_0=100;
% title_str is the filename, remember to change it according to Anna/Yuval
plot_comparison(hp, 1:length(hp), legend_weight_decay,...
                                'Regularization- weight decay',iter_0)