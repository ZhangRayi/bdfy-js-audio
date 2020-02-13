import requests
import execjs
import os


class BD_trans(object):
    def __init__(self):
        self.result = {}
        self.query_info = {}

    def inputTEXT(self):
        text = input('输入要翻译的词句：')
        for t in text:
            if '\u4e00' <= t <= '\u9fa5':
                self.query_info['f2t'] = 'zh2en'
                self.query_info['input'] = text
                return 'zh2en', text
        self.query_info['f2t'] = 'en2zh'
        self.query_info['input'] = text
        return 'en2zh', text

    def load_js(self, keyword):
        with open('bdfy_sign.js', 'r') as f:
            js = f.read()
        sign = execjs.compile(js).call("trans", keyword)
        self.query_info['signum'] = sign
        # print(sign)
        return sign

    def trans(self, user_log=True):
        s_lan, s_text = self.inputTEXT()
        lan = s_lan.split('2')
        f_lan, t_lan = lan[0], lan[1]
        # print(f_lan, t_lan)
        sign = self.load_js(s_text)
        url = 'https://fanyi.baidu.com/v2transapi'
        header = {
            "origin": "https://fanyi.baidu.com",
            "referer": "https://fanyi.baidu.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36 Edg/81.0.410.1",
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "BAIDUID=47CF74858B31BF54FA560D0F929B00B4:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1581417936; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BIDUPSID=47CF74858B31BF54FA560D0F929B00B4; PSTM=1581419219; H_PS_PSSID=30748_1458_21123_30717; delPer=0; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1581421001"
        }
        parameter = {
            "from": f_lan,
            "to": t_lan
        }
        data = {
            "from": f_lan,
            "to": t_lan,
            "query": s_text,
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "b68a046ddef1a8cc8e3f14806fb7687b"
        }
        response = requests.post(url, data=data, params=parameter, headers=header).json()
        result1 = response.get("trans_result").get('data')[0].get('dst')
        self.result['out'] = result1
        result2 = response.get("trans_result").get('phonetic')
        print(result1)
        hz, py = ['None'], ['None']
        if result2 is not None:
            hz.clear()
            py.clear()
            for item in result2:
                hz.append(item['src_str'])
                py.append(item['trg_str'])
        if user_log is True:
            self.write_log(cx=s_text, jg=result1, py=py, hz=hz, sig=sign)
            print('已记录使用日志')
        print('{0}finish{0}'.format('-' * 10))

    def write_log(self, cx, jg, py, hz, sig):
        current_log_path = os.path.dirname(__file__) + os.sep + 'user_log.txt'
        if not os.path.exists(current_log_path):
            print(f'创建日志：{current_log_path}')
        with open(current_log_path, 'a+') as log:
            log.writelines('查询：{: <8}；结果：{: <8}，相关：{: <15}；附加信息：{},\n'
                           .format(cx, jg, ''.join(py) + '，' + ''.join(hz), sig))


if __name__ == '__main__':
    while True:
        bd = BD_trans()
        bd.trans()
