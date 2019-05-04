import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold,datasets
from sklearn import decomposition

#handwriting
digits=datasets.load_digits(n_class=6)
x=digits.data
y=digits.target
n=20
img=np.zeros((200,200))
for i in range(n):
    ix=10*i+1
    for j in range(n):
        iy=10*j+1
        img[ix:ix+8,iy:iy+8]=x[i*n+j].reshape((8,8))
plt.figure(figsize=(8,8))
plt.imshow(img,cmap=plt.cm.binary)
plt.xticks([])
plt.yticks([])
plt.show()

#t-SNE
tsne=manifold.TSNE(n_components=2,init='pca',perplexity=50,learning_rate=50,n_iter=1000)
x_tsne=tsne.fit_transform(x)
x_min1=x_tsne.min(0)
x_max1=x_tsne.max(0)
x_norm1=(x_tsne-x_min1)/(x_max1-x_min1)
plt.figure(figsize=(8,8),dpi=300)
for i in range(x_norm1.shape[0]):
    plt.text(x_norm1[i][0],x_norm1[i][1],str(y[i]),color=plt.cm.Set1(y[i]),fontdict={'weight':'bold','size':9})
plt.xticks([])
plt.yticks([])
plt.title('t-SNE',fontdict={'weight':'bold','size':9})
plt.show()

#PCA
pca=decomposition.PCA(n_components=2)
x_pca=pca.fit_transform(x)
x_min2=x_pca.min(0)
x_max2=x_pca.max(0)
x_norm2=(x_pca-x_min2)/(x_max2-x_min2)
plt.figure(figsize=(8,8),dpi=300)
for i in range(x_norm2.shape[0]):
    plt.text(x_norm2[i][0],x_norm2[i][1],str(y[i]),color=plt.cm.Set1(y[i]),fontdict={'weight':'bold','size':9})
plt.xticks([])
plt.yticks([])
plt.title('PCA',fontdict={'weight':'bold','size':9})
plt.show()

#KPCA
kpca=decomposition.KernelPCA(n_components=2)
x_kpca=kpca.fit_transform(x)
x_min3=x_kpca.min(0)
x_max3=x_kpca.max(0)
x_norm3=(x_kpca-x_min3)/(x_max3-x_min3)
plt.figure(figsize=(8,8),dpi=300)
for i in range(x_norm3.shape[0]):
    plt.text(x_norm3[i][0],x_norm3[i][1],str(y[i]),color=plt.cm.Set1(y[i]),fontdict={'weight':'bold','size':9})
plt.xticks([])
plt.yticks([])
plt.title('KPCA',fontdict={'weight':'bold','size':9})
plt.show()

#MDS
mds=manifold.MDS(n_components=2)
x_mds=mds.fit_transform(x)
x_min4=x_mds.min(0)
x_max4=x_mds.max(0)
x_norm4=(x_mds-x_min4)/(x_max4-x_min4)
plt.figure(figsize=(8,8),dpi=300)
for i in range(x_norm4.shape[0]):
    plt.text(x_norm4[i][0],x_norm4[i][1],str(y[i]),color=plt.cm.Set1(y[i]),fontdict={'weight':'bold','size':9})
plt.xticks([])
plt.yticks([])
plt.title('MDS',fontdict={'weight':'bold','size':9})
plt.show()

#ISOMap
iso=manifold.Isomap(n_components=2,n_neighbors=10)
x_iso=iso.fit_transform(x)
x_min5=x_iso.min(0)
x_max5=x_iso.max(0)
x_norm5=(x_iso-x_min5)/(x_max5-x_min5)
plt.figure(figsize=(8,8),dpi=300)
for i in range(x_norm5.shape[0]):
    plt.text(x_norm5[i][0],x_norm5[i][1],str(y[i]),color=plt.cm.Set1(y[i]),fontdict={'weight':'bold','size':9})
plt.xticks([])
plt.yticks([])
plt.title('ISOMap',fontdict={'weight':'bold','size':9})
plt.show()

#LLE
lle=manifold.LocallyLinearEmbedding(n_components=2,n_neighbors=10)
x_lle=lle.fit_transform(x)
x_min6=x_lle.min(0)
x_max6=x_lle.max(0)
x_norm6=(x_lle-x_min6)/(x_max6-x_min6)
plt.figure(figsize=(8,8),dpi=300)
for i in range(x_norm6.shape[0]):
    plt.text(x_norm6[i][0],x_norm6[i][1],str(y[i]),color=plt.cm.Set1(y[i]),fontdict={'weight':'bold','size':9})
plt.xticks([])
plt.yticks([])
plt.title('LLE',fontdict={'weight':'bold','size':9})
plt.show()
