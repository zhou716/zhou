
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from MyQR import myqr
#import os
 

#os.chdir('C:/Users/dell/数据分析师/python基础语法')

myqr.run(
    words='http://weixin.qq.com/r/kzlje9TEE4lsrZAY92yB',
    # 扫描二维码后，显示的内容，或是跳转的链接
    #version=5,  # 设置容错率
    #level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='Python.gif',  # 图片所在目录，可以是动图
    colorized=True  # 黑白(False)还是彩色(True)
    #contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    #brightness=1.0,  # 用来调节图片的亮度，用法同上。
    #save_name='Python.gif',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )

#报错：Wrong picture! Input a filename that exists and be tailed with one of {'.jpg', '.png', '.bmp', '.gif'}!
#解决方案：picture与save_name 设置一致




'''
pic = "set.gif" # 背景图片的名称
pic_ = 'myset.gif' #生成后二维码的名称
words1 = "https://weixin.qq.com/g/A-06oJZDCAGPjbee" # 网址(前面要加http(s)://)
 
qr_name = myqr.run(
    words = words1,
    version = 5,        # 设置容错率为最高
    level = 'H',        # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture = pic,      # 将二维码和图片合成
    colorized = True,   # 彩色二维码
    contrast = 2.0,     # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
    brightness = 1.0,   # 用来调节图片的亮度，其余用法和取值同上
    save_name = pic_,   # 保存文件的名字，格式可以是jpg,png,bmp,gif
    save_dir = os.getcwd() # 控制位置
    )


print(qr_name)
'''





'''
# 先导入模块
words ='http://weixin.qq.com/r/kzlje9TEE4lsrZAY92yB'

myqr.run(
    words,
    # 扫描二维码后，显示的内容，或是跳转的链接
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='set.gif',  # 图片所在目录，可以是动图
    colorized=True,  # 黑白(False)还是彩色(True)
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name='set.gif',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )

'''
'''

a = 5
b = 3

st = 'a大于b' if a > b else 'a小于b'
print(st)

print('')

st = print('crazyit'), 'a 大于 b' if a > b else 'a 小于 b'
print(st)

print('')

st = print('crazyit'); x = 20 if a > b else 'a 小于 b'
print(st)
print(x)

print('')

c = 5
d = 5
print('c 大于 d') if c > d else (print('c 小于 d') if c < d else print('c 等于 d'))
'''
