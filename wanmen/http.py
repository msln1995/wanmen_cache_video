import requests
import json
import re
import time
import datetime

def getVideoInfoUrl(_id):
    return "https://api.wanmen.org/4.0/content/lectures/"+_id+"?routeId=spare"

def getMethod(url, Authorization, x_time, xtoken):
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type":"application/json; charset=utf-8",
        "x-sa":"9e2fc61b78106962a1fa5c5ba6874acaaf0cabfecb6f85ae2d4a082b672b9139f1466529572da95c36dd39a7cf9c8444",
        "x-platform":"web",
        "x-app":"uni",
        "x-time":x_time,
        "x-token":xtoken,
        "Authorization":"Bearer " + Authorization
    }
    # 设置session的请求头信息
    session.headers = headers
    response = session.get(url)
    return response

def getVidenInfo(_id, Authorization, token):
    info2 = getMethod(getVideoInfoUrl(_id), Authorization , token['x_time'], token['xtoken'])
    res = info2.content;
    视频资源信息 = json.loads(res)
    if 视频资源信息['actions']['watch'] != True and 视频资源信息['actions']['download'] != True:
        print("没有课程的权限");
        exit() 
    return {'pcHigh':视频资源信息["hls"]["pcHigh"], '_id':视频资源信息['_id']}

def download(url,download_path,Authorization, x_time, xtoken):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "orgin": "https://www.wanmen.org",
        "referer": "https://www.wanmen.org",
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site": "same-site",
        # "Authorization":"Bearer " + Authorization
    }
    res = getMethod(url, Authorization, x_time, xtoken)
    res.encoding = res.apparent_encoding
    ts_urls = re.findall(r'\n(.*\.ts)', res.text)
    print(str(len(ts_urls)) + "个片段")
    for i in range(len(ts_urls)):
        ts_url = ts_urls[i]
        file_name = ts_url.split("/")[-1]
        print("开始缓存 %s" %file_name)
        start = datetime.datetime.now().replace(microsecond=0)
        try:
            #在前面加上
            requests.packages.urllib3.disable_warnings()
            response = requests.get("https://media.wanmen.org/"+ts_url,stream=True,verify=False,headers=headers)
        except Exception as e:
            print("异常请求：%s"%e.args)
            return

        ts_path = download_path+"/{0}.ts".format(i)
        with open(ts_path,"wb+") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        end = datetime.datetime.now().replace(microsecond=0)
        print("耗时：%s"%(end-start))

