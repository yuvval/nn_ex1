function fig_http = save_plot(title_str, hfig, figpath, overwrite_fig, legend_off, title_off, legend_boxoff, fig_boxoff )
if nargin<6
    title_off = true;
end
if nargin <7
legend_boxoff = true;
end
if nargin <8
fig_boxoff = true;
end



tmp_hfig = gcf; % save gcf
figure(hfig);
ax =gca;
if fig_boxoff
ax.Box = 'off';
end
if legend_boxoff
legend BOXOFF 
end
ext = 'png';
nowstr = regexprep(datestr(now,0), '-? ?:?', '_');
fig_fname = pubfig.titlestr_to_fname(title_str);
full_fig_fname = fullfile(figpath, fig_fname);
if exist([full_fig_fname '.' ext], 'file') && ~overwrite_fig
    full_fig_fname = [full_fig_fname '_' nowstr];
end
saveas(hfig, full_fig_fname, ext)
fig_http = [regexprep(full_fig_fname, '~/www', 'http://chechiklab.biu.ac.il/~yuvval') '.' ext];
fprintf('saved figure on %s.%s\n', full_fig_fname, ext)
fprintf('%s\n', fig_http)

%% saving .eps + .fig versions for paper (no title + option to turn off legend)
if legend_off
    legend HIDE
end
if title_off
    title('') % remove title
end

print(hfig,'-depsc2',[full_fig_fname '.eps'])
saveas(hfig, full_fig_fname, 'fig')

% revert back to title + legend
if title_off
    title(regexprep(title_str, '_', '\\_'));
end

if legend_off
    legend SHOW
end

%revert to gcf
figure(tmp_hfig);

end