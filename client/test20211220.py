# print(1+1)
# def move(n,a,b,c):
#     if n==1:
#         print(a,'-->',c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# move(4,'A','B','C')
# def findMinAndMax(L):
#     for i in range(len(L)-1):
#         if L[i]<L[i+1]:
#            max=L[i+1]
#            min=L[i]
#         else:
#            L[i+1],L[i]=L[i],L[i+1]
#            max=L[i+1]
#            min=L[i]
#            # L[i + 1] = max
#            # L[i]=min
#     return (min, max)
# print(findMinAndMax([7, 1, 3, 9, 5]))

# def bubble_sort(our_list):
#     n=len(our_list)
#     lastExchangeIndex=0 #记录最后一次交换元素的位置
#     sortBorder=n-1 #无序数列边界
#     for i in range(n):
#         flag=True #有序标记，每轮开始初始值均为True
#         for j in range(0,sortBorder):
#             if our_list[j]>our_list[j+1]:
#                 our_list[j],our_list[j+1]=our_list[j+1],our_list[j]
#                 flag=False #有元素交换，则将标记设置为False
#                 lastExchangeIndex=j
#         sortBorder=lastExchangeIndex
#         if flag:
#             break
#     return our_list
# bubble_sort([1,0,3,5,8,7,9,4,2,6])
# bubble_sort([7, 1, 3, 9, 5])

# def bubble_sort1(our_list):
#     n=len(our_list)
#     sortBorder=n-1
#     lastExchangeIndex=0
#     for i in range(n):
#         flag=True
#         for j in range(0,sortBorder):
#             if our_list[j]>our_list[j+1]:
#                 our_list[j],our_list[j+1]=our_list[j+1],our_list[j]
#                 flag=False
#                 lastExchangeIndex=j
#         sortBorder=lastExchangeIndex
#         if flag:
#             break
#     return our_list
# bubble_sort1([7, 1, 3, 9, 5])


# def findMinAndMax(L):
#     if not L:
#         return (None,None)
#     else:
#         n=len(L)
#         idx=n-1
#         exchangeidx=0
#         for i in range(n):
#             flag=True
#             for j in range(idx):
#                 if L[j] > L[j + 1]:
#                     L[j], L[j + 1] = L[j + 1], L[j]
#                     flag=False
#                     exchangeidx=j
#             idx=exchangeidx
#             min = L[0]
#             max = L[-1]
#             if flag:
#                break
#         return (min, max)
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')
# def findMinAndMax(L):
#     if not L:
#         return (None,None)
#     else:
#         min=L[0]
#         max=L[0]
#         for i in L:
#             if i<min:
#                 min=i
#             elif i>max:
#                 max=i
#         return (min,max)
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')
# import os
# print([d for d in os.listdir('.')])
# print(pwd())
# def triangles():
#     L = [1]
#     while True:
#          yield L
#          X = [0] + L
#          Y = L + [0]
#          L = [X[i] + Y[i] for i in range(len(X))]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# abs()
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# 
# def _not_divisible(n):
#     return lambda x: x % n > 0
# 
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
# sorted()
# def createCounter():
#     n=0
#     def counter():
#         nonlocal n
#         # n=0
#         n=n+1
#         return n
#     return counter
# # 测试:
# counterA = createCounter()
# print(counterA())
# print(counterA())
# print(counterA())
# print(counterA())
# print(counterA()) # 1 2 3 4 5
# counterB = createCounter()
# print(counterB())
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())
# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
#
#
# a_function_requiring_decoration()
# # outputs: "I am the function which needs some decoration to remove my foul smell"
#
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#
#
# # now a_function_requiring_decoration is wrapped by wrapTheFunction()
#
# a_function_requiring_decoration()
# outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()

# from functools import wraps


# def logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#
#     return with_logging
#
#
# @logit
# def addition_func(x):
#     """Do some math."""
#     return x + x
#
#
# result = addition_func(4)
# print(result)

from functools import wraps

#
# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile，并写入内容
#             with open(logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的logfile
#                 opened_file.write(log_string + '\n')
#             return func(*args, **kwargs)
#
#         return wrapped_function
#
#     return logging_decorator
#
#
# @logit()
# def myfunc1():
#     pass
#
#
# myfunc1()
#
#
# # Output: myfunc1 was called
# # 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串
#
# @logit(logfile='func2.log')
# def myfunc2():
#     pass
#
#
# myfunc2()
# # Output: myfunc2 was called
# # 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
#
from functools import wraps
import logging

# class logit(object):
#     def __init__(self, logfile='out.log'):
#         self.logfile = logfile
#
#     def __call__(self, func):
#         # @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile并写入
#             with open(self.logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的文件
#                 opened_file.write(log_string + '\n')
#             # 现在，发送一个通知
#             self.notify()
#             return func(*args, **kwargs)
#
#         return wrapped_function
#
#     def notify(self):
#         # logit只打日志，不做别的
#         pass
# @logit()
# def myfunc1():
#     pass
# myfunc1()


# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             elif level == "info":
#                 logging.info("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
#
#     return decorator
#
# @use_logging(level="warn")
# # name='foo'
# def foo(name='foo'):
#     print("i am %s" )
#
# foo()

# def log(text):
#     def decorator(func):
#         def wrapper():
#             print('%s %s():' % (text, func.__name__))
#
#             return func()
#
#         return wrapper
#
#     return decorator
# @log('execute')
# def now():
#     print('2015-3-25')
#
# now()
#
# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self):
#         # @wraps(self._func)
#         def wraps1(*args,**kw):
#             print ('class decorator runing')
#             # func()
#             self._func()
#             print ('class decorator ending')
#             return self._func(*args,**kw)
#         return  wraps1
# @Foo()
# def bar():
#     print ('bar')
#
# bar()


# class logit(object):
#     def __init__(self, logfile='out.log'):
#         self.logfile = logfile
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile并写入
#             with open(self.logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的文件
#                 opened_file.write(log_string + '\n')
#             # 现在，发送一个通知
#             self.notify()
#             return func(*args, **kwargs)
#
#         return wrapped_function
#
#     def notify(self):
#         # logit只打日志，不做别的
#         pass
# @logit()
# def myfunc1():
#     pass
# myfunc1()

# 装饰器
# def logged(func):
#     def with_logging(*args, **kwargs):
#         print (func.__name__ )     # 输出 'with_logging'
#         print (func.__doc__  )     # 输出 None
#         return func(*args, **kwargs)
#     return with_logging
#
# # 函数
# @logged
# def f(x):
#    """does some math"""
#    return x + x * x
#
# a=logged(f)
# print(a(3))

# from functools import wraps
# #定义一个装饰器名称的类
# class  with_para_decorator:
#     #在类的__init__函数内接受装饰器参数，并赋值给类的实例参数，这样可以让其他函数随时使用
#     #当然，如果装饰器没有参数，此处不转a,b即可，相当于类无参实例化
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     #在类的__call__函数内接受被装饰函数，并具体定义装饰器
#     def __call__(self,func):
#         @wraps(func)
#         def wrap_function(arg1,arg2):
#             print('装饰带参数的函数，函数传的参数为：{0}, {1}'.format(arg1,arg2))
#             print('带参数的装饰器，装饰器传的参数为：{0}, {1}'.format(self.a,self.b))
#             return func(arg1,arg2)
#         return wrap_function
# #使用装饰器
# @with_para_decorator(1,2)
# def need_decorate(a,b):
#     pass
# need_decorate(4,5)


# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self):
#         print ('class decorator runing')
#         self._func()
#         print ('class decorator ending')
#
# @Foo
# def bar():
#     print ('bar')
#
# bar()
# functools.wraps


# def metric(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         t_start=time.time() #取函数开始时间
#         func(*args, **kw) #执行函数一次
#         t_end=time.time() #取函数结束时间
#         print('func %s executed in %s ms'%(func.__name__,(t_end-t_start)*1000))
#         return func(*args, **kw)
#     return wrapper

# def callfunc(func):
#     @wraps(func)
#     def wrappers(*args,**kw):
#         print('begin call')
#         print(func(*args,**kw))
#         print('end call')
#         return func(*args,**kw)
#     return wrappers
# @callfunc
# def cal_sum(x,y):
#     return x+y
# cal_sum(1,4)

# class logit(object):
#     def __init__(self,):
#
# def log(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapper():
#             print('%s %s():' % (text, func.__name__))
#
#             return func()
#
#         return wrapper
#
#     return decorator
# @log('execute')
# def now():
#
#     print('2015-3-25')
#
# now()
# print(now.__name__)

# def log1(text):
#     # @wraps(func)
#     def wrapper(func):
#
#         print('%s %s():' % (text, func.__name__))
#         return func()
#     return wrapper
# @log1('execute')
# def now1():
#     print('2015-3-25')

# def log(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now(x,y):
#     print('2021-12-7')
#     return x+y
#
# L1 = now
# print('.')
# print(L1)
#
# L2 = now(3,4)#L2为now()的返回值，如果此时now()有return 值则会返回，如果没有则返回None
# print(',')
# print(L2)


# def log(text):
#     def wrapper(func):
#         print('%s %s():' % (text, func.__name__))
#         return func()
#     return wrapper
#
# @log('execute')
# def now():
#     print('2021-12-7')
# L1 = now
# print('.')
# print(L1)
#
# L2 = now()
# print(',')
# print(L2)


# def log(func):
#     def wrapper(*args, **kw):
#         print('begin call %s():' % func.__name__)
#         s = func(*args, **kw)
#         print('end call %s():' % func.__name__)
#         return s
#         return wrapperdef log2(text, t = 'ddd'):
#         def decorator(func):
#             def wrapper(*args, **kw):
#                 print('begin %s %s() text:' % (text, func.__name__))
#                 s = func(*args, **kw)
#                 print('end %s %s() text:' % (text, func.__name__))
#                 print(t)
#                 return s
#                 return wrapper
#                 return decorator@log@log2('exe')
# def now():
#     print('2021/11/24')
# now()


# def now():
#
#     print('2015-3-25')
#
# def decorator(func,text):
#
#     def wrapper(*args, **kw):
#
#         print('%s %s():' % (text, func.__name__))
#
#         return func(*args, **kw)
#
#     return wrapper
#
# now=decorator(now , 'hi!')
#
# now()


# def log(text):
#     def wrapper(func):
#         print('%s %s():' % (text, func.__name__))
#         return func()
#     return wrapper
#
# @log('execute')
# def now():
#     print('2021-12-7')

# def a(func):
#     print('a')
#     def b():
#         print('b')
#         return 2
#         def c():
#             print('c')
#     return 1
# @a
# def d():
#     print('cccc')

# def log(*args,**kwargs):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             print('begin call')
#             func(*args,**kwargs)
#             print('end call')
#             return func(*args,**kwargs)
#         return wrapper
#     return decorator
# @log
# def f():
#     pass
# f()


# import time
# from functools import wraps
#
#
# def metric(txt_or_func):
#     if isinstance(txt_or_func, str):
#         text = txt_or_func
#
#         def decorator(func):
#             @wraps(func)
#             def wrapper(*args, **kw):
#                 start = time.time()
#                 result = func(*args, **kw)
#                 end = time.time()
#                 print('%s %s in %s ms' % (func.__name__, text, end - start))
#                 return result
#
#             return wrapper
#
#         return decorator
#     else:
#         return metric('call')(txt_or_func)
#
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
#
# @metric('execute')
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# def logit(text):
#     @wraps(text)
#     def wrapper1(*args,**kwargs):
#         print('begin call')
#         text(*args,*kwargs)
#         print('end call')
#         return text(*args,**kwargs)
#     def decorator(func):
#         @wraps(func)
#         def wrapper2(*args,**kwargs):
#             print(text,'begin call')
#             func(*args,*kwargs)
#             print(text,'end call')
#             return func(*args,**kwargs)
#         return wrapper2
#     if isinstance(text,str):
#         return decorator
#     elif type(text)==type(lambda x:x):
#         return wrapper1
#     else:
#         print('error:请正确使用@logit')
#         return  None
# @logit('function')
# def f():
#     print('yes')
# f()



# def logit(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print('begin call')
#         func(*args,*kwargs)
#         print('end call')
#         return func(*args,**kwargs)
#     return wrapper
# @logit('function')
# def f():
#     print('yes')
# f()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

# import sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__=='__main__':
#     test()

# def logit(arg):
#     if isinstance(arg,str):
#         def decorator(func):
#             @wraps(func)
#             def wrapper2(*args,**kwargs):
#                 print(arg,'begin call')
#                 r=func(*args,*kwargs)
#                 print(arg,'end call')
#                 return r
#             return wrapper2
#         return decorator
#     else:
#         @wraps(arg)
#         def wrapper1(*args,**kwargs):
#             print('begin call')
#             r=arg(*args,*kwargs)
#             print('end call')
#             return r
#         return wrapper1
# @logit('f')
# def f():
#     print('yes')
# f()

# def logit(arg):
#     if type(arg)==type(lambda x:x):
#         @wraps(arg)
#         def wrapper1(*args,**kwargs):
#             print('begin call')
#             r=arg(*args,*kwargs)
#             print('end call')
#             return r
#         return wrapper1
#     else:
#         def decorator(func):
#             @wraps(func)
#             def wrapper2(*args,**kwargs):
#                 print(arg,'begin call')
#                 r=func(*args,*kwargs)
#                 print(arg,'end call')
#                 return r
#             return wrapper2
#         return decorator
#
# @logit(1)
# def f():
#     print('yes')
# f()

#
# import random
# class Fish(object):
#     def __init__(self, x, y):
#         self.x = random.randint(0, 10)
#         self.y = random.randint(0, 10)
# d = Fish(1, 2)
# print(d.x)

# import random
# class Fish():
#     def __init__(self):
#         self.x = random.randint(0, 10)
#         self.y = random.randint(0, 10)
# d = Fish()
# print(d.x)
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()

# class Dog(Animal):
#
#     def run(self):
#         print('Dog is running...')
#
#     def eat(self):
#         print('Eating meat...')
# class Dog(Animal):
#
#     def run(self):
#         print('Dog is running...')
#
# class Cat(Animal):
#
#     def run(self):
#         print('Cat is running...')
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()

# class Animal(object):
#     def run(self):
#         print("Animal is run...")
#
#     def eat(self):
#         print("Animal is eating...")
#
#
# class Dog(Animal):
#     def run(self):
#         print("dog is run...")
#
#
# class Cat(Animal):
#     def run(self):
#         print("cat is run...")
#
#
# def run_eat(Animal):
#     Animal.eat()
#     Animal.run()
#
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
#
# # run_eat(animal)
# # run_eat(dog)
# run_eat(cat)

# class animal(object):
#
#     def __init__(self,character):
#
#         self.__character=character
#
# class dog(animal):
#
#     def run(self):
#
#         print('dog is running')
#
#     def eat(self):
#
#         print('eating meat')
#
# dog1=dog('furry')
# print(dog)
# print(dog1)
#
# # print(isinstance(dog,animal))
#
# # True
#
# print(isinstance(dog1,dog))
#
# print(type(animal))


# class Test(object):
#
#     def test(self):
#
#         return 10
#
# print("Test().test()", Test().test())
#
# print("Test().test", Test().test)
#
# print("Test.test", Test.test)

#
# class Gender_horse(object):
#     def seta(self, gender):
#         setattr(self, '__gender', gender)
#
#     def set(self, gender):
#         self.__gender = gender
#
#     def geta(self):
#         return getattr(self, '__gender')
#
#     def get(self):
#         return self.__gender
#
#
# dilu = Gender_horse()
# # 在 class 中定义私有属性
# dilu.set('Female')
# print(hasattr(dilu, '__gender'), dir(dilu))
# print(getattr(dilu, '__gender', None), dilu.get())
# dilu.seta('Lesbian')
# print(hasattr(dilu, '__gender'), dir(dilu))
# print(getattr(dilu, '__gender', None), dilu.get(), dilu.geta())

# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def showScore(self):
#         print(self.name,self.score)
#
# class Animal(object):
#     def run(self):
#         print("animal is running")
#
# xiaoming = Student("xiaoming",22)
# animal = Animal();
#
# # 动态语言的语法权限实在是太大了,可以运行时将一个对象的方法指向另一个对象的方法
#
# setattr(xiaoming, "showScore", animal.run)
# xiaoming.showScore()

# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count=Student.count+1
#
#
#
# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
#
# class Student(object):
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Student.count=Student.count+1
# a=Student('a')
# b=Student('b')
# c=Student('c')
# print(Student.count)

# a = [1, 2]
# b = a     # 传址，b和a指向同一内存地址
# a[0] = 100   # 创建新的内存存放100，同时列表的第一个元素指向新的内存地址。注意：并非将原内存地址上的0修改为100
# print(b)    # [100，2] ，因为都是地址引用，所以同步更新

# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count+=1
# a=Student('zl')
# print(a.name)
# print(a.count)
# print(Student.count)

from types import MethodType
# class Student(object):
#     pass
# def set_age(self, age):
#         self.age = age
# s = Student()
#
# # Student.set_age = MethodType(set_age, Student)
# Student.set_age = set_age
# print(Student.set_age(s,78))
# #
# print(s.age)
#
# print(Student.age)
#
# s.set_age(8)
#
# print(s.age)
#
# print(Student.age)

# Student.set_age = set_age

# class Student(object):
#      def __init__(self, name):
#          self.name = name
#      def __str__(self):
#          return 'Student object (name: %s)' % self.name
# print(Student('Michael'))

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name=%s)' % self.name
#     __repr__ = __str__
# s = Student('Michael')
# print(s)
# D:\Anaconda3\python.exe "D:\python\PyCharm 2019.3.3\plugins\python\helpers\pydev\pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 51971 --file E:/工作文件/模型监控/ModelPlatform-dev-a6c6d6485269c6db80cf5ed0b37cc938c6b4ada8/client/test20211220.py
# pydev debugger: process 9836 is connecting
#
# Connected to pydev debugger (build 193.6494.30)
#
# Process finished with exit code -1073741571 (0xC00000FD)
# print(1+1)
# class Chain(object):
#    def __init__(self, path=''):
#        self.__path = path
#
#    def __getattr__(self, path):
#        return Chain('%s/%s' % (self.__path, path))
#
#    def __call__(self, path):
#        return Chain('%s/%s' % (self.__path, path))
#
#    def __str1__(self):
#        return self.__path
#
#    __repr__ = __str1__
# # urls = Chain().users
# # print(urls)
# # #
# print(Chain().users('michael').repos)
# # /users/michael/repos

# from enum import Enum
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# from enum import Enum, unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
# print(Gender.Female.value)
# print(Gender(1))
# print(Gender.Male)

# from enum import Enum, unique
# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
#
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#
# # 测试:
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')
#
#
# Gender= Enum('gender',('Male','Female'))

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
# main()

# err.py:
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('2')
#
# print(main())


# err_raise.py
# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')

# from functools import reduce
#
# def str2num(s):
#     try:
#         return int(s)
#     except ValueError:
#         try:
#             return float(s)
#         except ValueError:
#             raise ValueError('Invalid Value:%s' % s)
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# def foo(s):
#     n = int(s)
#     #assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     return foo('2')
#
# print(main())

# import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="test.log",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     format="【%(asctime)s %(levelname)s】 %(lineno)d: %(message)s"
# )
# logging.debug("ffff")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")

# import unittest
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#             if self.score >= 80 and self.score<=100:
#                 return 'A'
#             elif self.score >= 60 and self.score<=79:
#                 return 'B'
#             elif self.score >= 0 and self.score<=59:
#                 return 'C'
#             else:
#                 raise ValueError('invalid score %s'% self.score)
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     unittest.main()


# def fact(n):
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# fact(-1)
# print(fact(-1))

try:
    f=open(r'E:\工作文件\adhoc\IO1.txt','r')
    print(f.read(2)) #这个就是read(size)
    print(f.read())
finally:
    if f:
        f.close()




















