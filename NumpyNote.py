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


#数组性质
print data.shape#数组的形状
print data.dtype#数组元素的类型
print data.ndim#数组的维度