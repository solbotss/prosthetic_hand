clc;
clear all;
file='manoharhello1.wav';
x=audioread(file);
%y=reshape(x,264192,1);
plot(x);
sound(x);