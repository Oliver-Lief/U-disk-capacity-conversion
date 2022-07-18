# U-disk-capacity-conversion
我们都知道，存储器的容量厂家和电脑的计算是不一致的，主要表现在电脑显示的容量小于你所购买的任容量，如果购买了U盘或硬盘，怎么知道容量是否正确，本项目帮你解决。

本项目依赖Pyqt5

win下：

`pip install PyQt5`

`pip install pyqt5-tools`

然后运行`U_disk.py`即可

# v1
样例：

![example](example.png)
# v2
1. 调整布局

2. 更改逻辑结构，实现界面与功能分离

- ....ui为样式文件
- ..._UI.py为样式函数
- ..._convert.py为功能函数
- ..._main.py为主函数，执行该函数即可运行
- ![example2](example2.png)