close all; clear all; clc

load ('Qc');
Qc=data;
load ('Qf');
Qf=data;
load ('Tf');
Tf=data;

load('superficie_10C')
load ('tf2');
tf=data;


figure,scatter3(Qf,Qc,tf-Qc./Qf*4)%-(Qc.^2+Qf.^2)/10)
xlabel('Qf')
ylabel('Qc')
title('tf-4* Qc/Qf')


figure,scatter3(Qf,Qc,tf)
xlabel('Qf')
ylabel('Qc')
title('tf')


