# 百度翻译 逆js 得sign，gettts获取语音
通过逆向js访问百度翻译v2transapi获取翻译值，并且请求gettts获取audio文件



## trasnlate.py
运行translate.py，会自动调用当前文件夹下的bdfy_sign.js，此js是将输入要查询的字符串转换为sign码。
因为有main函数接口所以会自动运行，命令行中输入任意字符串即可获取相对于的英文/中文，并自动在user_log.txt中生成部分记录。


## TextToAudio.py
运行TextToAudio.py，也会自动运行，调用translate.py程序并获取相关信息。
向百度翻译的/gettts发送相关请求，接受二进制音频文件，并保存在 $File_Dir$/Audio/en 和 $File_Dir$/Audio/zh 下。
en中保存英语语音，zh中保存中文语音，若不存在Audio文件夹，程序会自动创建。

## 承诺：
整个代码中不含任何恶意代码及收集信息和发送任何隐私数据。

## 请悉知：
下载后各位大神可以简化代码，自己改编、改写，对改写后的任何代码我不负任何责任。
