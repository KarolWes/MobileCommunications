%% COST MODEL
%   Script returns signal attenuation parameterized with distance and frequency
%   based on COST231-Hata Model
%
%   Authors: Enrique Caballero, Karol xxx
%   LHatadB = Losscost231hata(hBS, hMS, f, d, area)
%
%      LHatadB - radio signal attenuation [dB]
%
%      ht - physical height of the transmitting base station [m]
%           30 <= ht <= 200 m
%      hr -  physical height of the receiving device [m]
%           1 <= hr <= 10 m
%      f - frequency [MHz]
%           1500 <= f <= 2000 MHz
%      d - distance between antennas  [km]
%           1 <= d <= 20 km
clear all;
close all;
clc;

%      ht - effective base station antenna height [m]
%           30 <= ht <= 200 m
ht = 50; %[m]

%      hr - mobile station antenna height [m]
%           1 <= hr <= 10 m
hr = 2; %[m]

%      f - frequency [MHz]
%           1500 <= f <= 2000 MHz
max_f = 2000; 
min_f = 1500; 
precision_f = 100; 
f = min_f:precision_f:max_f; 

%      d - distance between antennas [km]
%           1 <= d <= 20 km
min_distance = 1; 
max_distance = 20; 
precision = 0.01; 
d = min_distance:precision:max_distance; 
fig = figure();
for i = 1:length(f)
    %   Loss Cost Function
    L(:,i) = Losscost231hata(ht, hr, f(i), d);

    clf reset;
    
    plot(d, L,'-');
    description = ['ht = ',num2str(ht),' [m]   hr = ',num2str(hr),' [m]   f = ',...
        num2str(min_f),'-',num2str(max_f),' [MHz]   d = ',num2str(min_distance),'-',num2str(max_distance),' [km]  '];
    annotation('textbox',[0.15 0.0 0.2 0.2],'String',{description},'FitBoxToText','on');
    grid on;
    axis auto;
    title({'Radio signal attenuation [dB] with Distance for different Frequencies';...
        'attenuation value based on COST231-Hata Model'});
    xlabel('d [km]');
    ylabel('L [dB]');
    hold on
    
end
x1 = [7 4];
y1 = [150 160];
[normx, normy] = coord2norm(fig.CurrentAxes, x1,y1);
annotation('textarrow', normx, normy,'String','Ascending Frequency');





