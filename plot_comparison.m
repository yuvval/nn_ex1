function plot_comparison(hp, hp_inds, lgd, txt)

figure
for k = hp_inds
   plot(hp{k}.train_losses(:,1), hp{k}.train_losses(:,2));
   hold on
end

legend(lgd);
title_str = ['Training losses ' txt];
title(title_str)
xlabel('iteration number')
ylabel('objective loss')
hold off
% title_str is the filename, remember to change it according to Anna/Yuval
save_plot(title_str, gcf, '~/www/figs/', true, false, false, false, true )



figure
for k = hp_inds
   plot(hp{k}.test_losses(:,1), hp{k}.test_losses(:,2));
   hold on
end

legend(lgd);
title_str = ['Testing losses ' txt];
title(title_str)
xlabel('iteration number')
ylabel('objective loss')
hold off

% title_str is the filename, remember to change it according to Anna/Yuval
save_plot(title_str, gcf, '~/www/figs/', true, false, false, false, true )

figure
for k = hp_inds
   plot(hp{k}.test_accuracies(:,1), hp{k}.test_accuracies(:,2));
   hold on
end

legend(lgd);
title_str = ['Testing accuracies ' txt];
title(title_str)
xlabel('iteration number')
ylabel('objective loss')
hold off
% title_str is the filename, remember to change it according to Anna/Yuval
save_plot(title_str, gcf, '~/www/figs/', true, false, false, false, true )
