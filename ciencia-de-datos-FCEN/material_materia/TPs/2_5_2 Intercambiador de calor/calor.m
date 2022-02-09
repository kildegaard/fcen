close all; clear all; clc

load ('superficie')

figure,scatter3(Qf,Qc,tf-Qc*5-80./Qf)%-(Qc.^2+Qf.^2)/10)
xlabel('Qf')
ylabel('Qc')
title('Tf')


figure,scatter3(Qf,Qc,tf)%-(Qc.^2+Qf.^2)/10)
xlabel('Qf')
ylabel('Qc')
title('tf')


figure,scatter3(H(:,1),H(:,2),H(:,4))
xlabel('Qf')
ylabel('Qc')
title('tf')


figure,scatter3(H(:,1),H(:,2),(H(:,3))-(H(:,4)))
xlabel('Qf')
ylabel('Qc')
title('Tf-tf')

figure,scatter3(H(:,1),H(:,2),(H(:,3)-H(:,4))-(H(:,1).*H(:,1)/10))
xlabel('Qf')
ylabel('Qc')
title('Tf-tf')

[x,y] = meshgrid(0:0.1:20,0:.1:20);
z=1-1./(1+.5*x+.5*y)-(x+y)/40;
figure,surf(x,y,z)