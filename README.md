# 实验二 Python数据结构与流程控制

## 导航

[返回](https://github.com/ZKLlab/python-computing-experiments)

## 实验要求

1. Python流程控制：编写循环控制代码用下面公式逼近圆周率(精确到小数点后 15 位)，并且和`math.pi`的值做比较

   ![{\displaystyle\frac1{\pi}=\frac{2\sqrt2}{9801}\sum_{k=0}^\infty\frac{\left(4k\right)!\left(1103+26390k\right)}{k!^4\left(396^{4k}\right)}.}](https://render.githubusercontent.com/render/math?math=%7b%5cdisplaystyle%5cfrac1%7b%5cpi%7d%3d%5cfrac%7b2%5csqrt2%7d%7b9801%7d%5csum_%7bk%3d0%7d%5e%5cinfty%5cfrac%7b%5cleft(4k%5cright)!%5cleft(1103%2b26390k%5cright)%7d%7bk!%5e4%5cleft(396%5e%7b4k%7d%5cright)%7d.%7d)

2. Python流程控制：阅读[https://en.wikipedia.org/wiki/Koch_snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)，通过修改koch.py绘制其中一种泛化的Koch曲线。

3. 生日相同情形的概率分析：

   1. 生成M (M≥1000)个班级，每个班级有N名同学，用`input`接收M和N；

   2. 用`random`模块中的`randint`生成随机数作为N名同学的生日；

   3. 计算M个班级中存在相同生日情况的班级数Q，用P=Q/M作为对相同生日概率的估计；

   4. 分析M，N和P之间的关系。
   
4. 参照验证实验1中反序词实现的示例代码，设计Python程序找出words.txt中最长的“可缩减单词”（所谓“可缩减单词”是指：每次删除单词的一个字母，剩下的字母依序排列仍然是一个单词，直至单字母单词`'a'`或者`'i'`）。提示：

   1. 可缩减单词示例：

      sprite → spite → spit → pit → it → i。

   2. 如果递归求解，可以引入单词空字符串`''`作为基准。

   3. 一个单词的子单词不是可缩减的单词，则该单词也不是可缩减单词。因此，记录已经查找到的可缩减单词可以提速整个问题的求解。
