function plot_comparison(hp, hp_inds, lgd, txt,iter_0)

figure
for k = hp_inds
   i0 = find(hp{k}.train_losses(:,1) >= iter_0,1);
   plot(hp{k}.train_losses(i0:end,1), hp{k}.train_losses(i0:end,2));
   hold on
   lgd_train(k,:)  = ['train ' lgd(k,:)];
end

for k = hp_inds
   i0 = find(hp{k}.test_losses(:,1) >= iter_0,1);
   plot(hp{k}.test_losses(i0:end,1), hp{k}.test_losses(i0:end,2), '--');
   hold on
   lgd_test(k,:)  = ['test  ' lgd(k,:)];
end



legend([lgd_train ; lgd_test]);
title_str = ['Objective losses ' txt];
title(title_str)
xlabel('iteration number')
ylabel('objective loss')
hold off

% title_str is the filename, remember to change it according to Anna/Yuval
save_plot(title_str, gcf, '~/www/figs/', true, false, false, false, true )

figure
for k = hp_inds
   i0 = find(hp{k}.test_accuracies(:,1) >= iter_0,1);
   plot(hp{k}.test_accuracies(i0:end,1), hp{k}.test_accuracies(i0:end,2));
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
