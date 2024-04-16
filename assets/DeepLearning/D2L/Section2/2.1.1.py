import torch

#创建一个 0~11 的长度为 12 的向量（一维张量）
x = torch.arange(12)
print(x)

#访问张量的形状（沿每个轴的长度）
print(x.shape)

#张量中元素的总数
print(x.numel())

#改变一个张量的形状而不改变元素数量和元素值
X = x.reshape(3,4)
print(X)

#自动获取宽或高
X = x.reshape(4,-1)
print(X)

#全零张量
Y = torch.zeros((2,3,4))
print(Y)

#全 1 张量
Y = torch.ones((2,3,4))
print(Y)

#服从标准正态的随机张量
Z = torch.rand(3,4)
print(Z)

#从 Python 列表创建张量
W = torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]])
print(W)