import json
import requests
import base64

def json_byte_to_dict(json_byte_file):
    """
    将byte格式的json文件转换成字典格式的文件
    """
    str_json = json_byte_file.decode()
    str_dict = json.loads(str_json)
    return str_dict


def get_token(api_key, secret_key):
    """
    动态获取获取token
    :param api_key:
    :param secret_key:
    :return: access_token
    """
    URL = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key \
           + '&client_secret=' + secret_key
    r = requests.post(URL)
    access_token = r.json()['access_token']
    return access_token


def censor_text(content, access_token):
    # http://ai.baidu.com/docs#/TextCensoring-API/top
    URL = 'https://aip.baidubce.com/rest/2.0/antispam/v2/spam?access_token={0}&content={1}'
    r = requests.post(URL.format(access_token, content))
    return r.json()


def censor_image(path, access_token):
    # http://ai.baidu.com/docs#/ImageCensoring-API/top
    URL = 'https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/user_defined?access_token={0}'
    with open(path, 'rb') as f:
        img = base64.b64encode(f.read())
    r = requests.post(URL.format(access_token), data={'image': img})

    return r.json()


if __name__ == '__main__':
    from config import *
    access_token = get_token(API_KEY, SECRET_KEY)
    print(censor_image('wyg.jpg'))
    print(censor_text('你他妈的太他妈的帅了吧'))