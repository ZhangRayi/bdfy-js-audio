import requests
import os
import translate

'''def inputTEXT():
    text = input('输入要翻译的词句：')
    for t in text:
        if '\u4e00' <= t <= '\u9fa5':
            return 'zh', text
    return 'en', text
'''


def save_Audio():
    url = 'https://fanyi.baidu.com/gettts'
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36 Edg/81.0.410.1"
    }
    while True:
        bd = translate.BD_trans()
        bd.trans()
        print(bd.query_info, bd.result)
        f_lan, t_lan = bd.query_info['f2t'].split('2')
        req_str = bd.query_info['input']
        res_str = bd.result['out']
        if f_lan == 'en':
            f_spd = 3
        else:
            f_spd = 5
        parameter = {
            "lan": "%s" % f_lan,
            "text": "%s" % req_str,
            "spd": "%d" % f_spd,
            "source": "web"
        }
        response = requests.get(url, headers=header, params=parameter)
        audio = response.content
        with open(os.path.dirname(__file__) + '/Audio/{0}/{1}.mp3'.format(f_lan, parameter["text"].replace('？', '').replace('@', 'at').replace('.', '').replace('/', 'slash').replace('<', '').replace('>', '').replace('?', '').replace(':', '').replace('\\', '').replace('|', 'or').replace('"', '').replace('*', '')), 'wb') as f:
            f.write(audio)
        if t_lan == 'en':
            t_spd = 3
        else:
            t_spd = 5
        parameter = {
            "lan": "%s" % t_lan,
            "text": "%s" % res_str,
            "spd": "%d" % t_spd,
            "source": "web"
        }
        response = requests.get(url, headers=header, params=parameter)
        audio = response.content
        with open(os.path.dirname(__file__) + '/Audio/{0}/{1}.mp3'.format(t_lan, parameter["text"].replace('？', '').replace('@', 'at').replace('.', '').replace('/', 'slash').replace('<', '').replace('>', '').replace('?', '').replace(':', '').replace('\\', '').replace('|', 'or').replace('"', '').replace('*', '')), 'wb') as f:
            f.write(audio)
        del bd


# def zh_audio
# if __name__ == '__main__':
#     save_Audio()


if __name__ == '__main__':
    if 'Audio' not in os.listdir(os.path.dirname(__file__)):
        # os.mkdir(os.path.dirname(__file__)+os.sep+'Audio')
        os.mkdir(os.path.dirname(__file__) + '/Audio/en')
        os.mkdir(os.path.dirname(__file__) + '/Audio/zh')
        print('已在当前目录下建立 Audio 文件夹')
        save_Audio()
        print('音频文件保存完毕')
    else:
        print('语音文件将储存于./Audio/en 和 ./Audio/zh')
        print('Voice files will be saved in ./Audio/en AND ./Audio/zh')
        save_Audio()
        print('音频文件保存完毕')
