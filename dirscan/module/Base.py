import requests


def TargetCheak(url):
    try:
        Tu=requests.get(url,timeout=3)
    except requests.exceptions.ReadTimeout:
        print('fail')
    except requests.exceptions.ConnectTimeout:
        print('fail')
    if('aspx' in Tu.text):
        return 'aspx'
    elif('php' in Tu.text):
        return 'php'
    elif('asp' in Tu.text):
        return 'asp'
    elif ('jspin' in Tu.text):
        return 'jsp'
    else:
        return 'dir'


def GenerateReport(target):
    filename1=target.replace()