clear
close all

load Q3_parse_results.mat
iter_0=500;
% title_str is the filename, remember to change it according to Anna/Yuval
plot_comparison(hp, 1:3, legend_SGD, 'SGD ',iter_0)
