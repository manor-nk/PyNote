#!/usr/bin/python
# -*- coding: utf-8 -*-
#This is a note of numpy
#Created by Yuan Zhuang on 12/19/2018.
import numpy as np

#ndarray: n dimension array. 多维数组对象，所有数据必须是相同类型

#创建ndarray，创建数组
##将序列或嵌套序列转化成np.array数组
data1 = [1,2,3,4,5]
data2 = [[1,2,3],[4,5,6]]
arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.asarray(arr1)#如果arr1是np.array数组则不复制，如果不是则转换成np.array数组
##内置函数新建数组
data = np.arange(5)#range函数数组版，返回array([0, 1, 2, 3, 4])
data = np.zeros(10)#创建全0数组
data = np.ones((3,6))#创建全1数组
data = np.zeros_like(data1)#根据data1的形状创建全0数组
data = np.ones_like(data2)#根据data2的形状创建全1数组
data = np.empty((2,3,2))#创建新数组，但不填充值，只分配内存
data = np.empty_like(data2)#根据data2的形状创建新数组，但不填充值，只分配内存
data = np.eye(5)#创建5*5的单位矩阵
data = np.identity(5)#创建5*5的单位矩阵
##生成随机数数组
np.random.seed()#设置随机数生成器种子，默认根据时间选择
data = np.random.normal(size=(4,4))#生成标准正态分布的样本数组
data = np.random.permutation(5)#返回0～4的随机排列
data = np.random.permutation([4,6,9])#返回[4,6,9]的随机排列
data = np.random.shuffle([4,6,9])#返回[4,6,9]的随机排列
np.random.shuffle(data)#对data序列就地随机排列，不返回值
data = np.random.rand(5)#返回均匀分布的样本值，默认返回一个数
data = np.random.randint(low, high, size, dtype)#返回给定范围随机整数
data = np.random.randn(3,9,5)#返回维度为(3,9,5)的标准正态分布样本值
data = np.random.binomial(n,p,size)#返回二项分布样本值
data = np.random.beta(a,b,size)#返回Beta分布样本值
data = np.random.gamma(shape, scale, size)#返回Gamma分布样本值
data = np.random.uniform(low, high, size)#返回均匀分布样本值
data = np.random.chisquare(df, size)#返回卡方分布样本值

#数组性质
print data.shape#数组的形状
print data.dtype#数组元素的类型
print data.ndim#数组的维度
arr1 = np.array(data1,dtype=np.int32)#显式指定数据类型
arr2 = arr1.astype(np.float64)#显式转换类型
##转置

#数组运算
##与标量运算/一元通用函数
data +-*/ 10#各元素分别加减乘除10
1 / data#各个元素取倒数
data**2#各个元素取平方
np.square(data)#各个元素取平方
data**0.5#各个元素开根号
np.sqrt(data)#各个元素开根号
np.exp(data)#计算各个元素e^x
np.abs(data)#计算各个元素绝对值。复数返回模长。
np.fabs(data)#计算各个元素绝对值
np.log(data)#计算各个元素lnx
np.log10(data)#计算各个元素log10x
np.log2(data)#计算各个元素log2x
np.log1p(data)#计算各个元素ln(1+x)
np.sign(data)#计算各个元素正负号（1，0，-1）
np.ceil(data)#计算各个元素大于等于该值最小整数
np.floor(data)#计算各个元素小于等于该值最大整数
np.rint(data)#

##统计方法

##数组与数组运算/二元通用函数
data1 +-*/ data2#对应元素加减乘除

##集合运算

##矩阵运算

#索引与切片

#布尔型数组

#输入输出


