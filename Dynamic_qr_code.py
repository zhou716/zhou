
# -*- coding: utf-8 -*-

from MyQR import myqr

 
myqr.run(
    words='http://weixin.qq.com/r/kzlje9TEE4lsrZAY92yB',
    # 扫描二维码后，显示的内容，或是跳转的链接
    picture='Python.gif',  # 图片所在目录，可以是动图
    colorized=True  # 黑白(False)还是彩色(True)
    )

