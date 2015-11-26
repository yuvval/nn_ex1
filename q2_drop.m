clear
close all

load Q2_drop_parse_results_a.mat
iter_0=100;
% title_str is the filename, remember to change it according to Anna/Yuval
plot_comparison(hp, 1:length(hp), legend_drop_weight_decay,...
                                'Regularization- drop and weight decay',iter_0)
                            
res=load('Q2_parse_results_a.mat');
resdrop=load('Q2_drop_parse_results_a.mat');
hp_dec0_005={res.hp{2},resdrop.hp{2}};
hp_dec0={res.hp{4},resdrop.hp{4}};
leg_dec_0_005=['w\_d 0.005     '; 'drop w\_d 0.005'];
leg_dec_0=['w\_d 0     '; 'drop w\_d 0'];


plot_comparison(hp_dec0_005, 1:length(hp_dec0_005), leg_dec_0_005,...
                                'Regularization- drop and weight decay',iter_0)

plot_comparison(hp_dec0, 1:length(hp_dec0), leg_dec_0,...
                                'Regularization- drop and weight decay',iter_0)
                            