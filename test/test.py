import requests #用于向网络服务器发送HTTP请求并接收响应。在这个代码中，它被导入以便进行HTTP请求，可能用于从网络上获取数据
import random #内置模块，提供了生成随机数和随机选择的功能。在这个代码中，它被导入以便生成随机数，可能用于随机选择或生成一些数据
import os #内置模块，提供了与操作系统交互的功能，例如文件和目录操作。在这个代码中，它被导入以便执行与操作系统相关的任务，如文件操作、目录创建

file = []
url = []
error = []
bc = []
ip = []
headers = {}
user = input('Import TXT:')
banner = '''
 ____            _                            
|  _ \  ___  ___| |_ _ __ ___  _   _  ___ _ __
| | | |/ _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
| |_| |  __/\__ \ |_| | | (_) | |_| |  __/ |  
|____/ \___||___/\__|_|  \___/ \__, |\___|_|  
                               |___/       

Producer:Nine world
'''
useragent = []
twoo = []
print(banner)


def urls(): #定义一个名为urls的函数的开始
    dk = open('{}'.format(user), 'r') #打开一个文件，文件名是通过一个名为user的变量构建的。假设user是一个字符串，它将使用这个字符串来作为文件名。 'r' 参数表示以只读模式打开文件
    for k in dk.readlines(): #一个循环，遍历文件dk的每一行
        qcs = "".join(k.split('\n')) #处理每一行的内容，首先使用.split('\n')将每一行按换行符分割成一个字符串列表，然后使用"".join(...)将这个字符串列表重新连接起来，消除了换行符。这样做的目的可能是为了去除每行的换行符，以便在后续处理中更容易操作
        url.append(qcs) #将处理后的行添加到名为url的列表中
    print('[+]url.txt Load completion') #打印一个消息，指示文件加载完成
    print(' ') #打印两个空行，可能是为了在输出中创建一些间隔
    print(' ')


urls() #调用了这个函数，启动了上述操作


def judge(): #定义函数的语句，创建了一个名为judge的函数
    pd = os.listdir('御剑配置文件') #内置模块os中的listdir函数来列出指定文件夹 '御剑配置文件' 中的所有文件和子文件夹，并将结果存储在名为pd的列表中
    for name in pd: #for循环，它遍历了pd列表中的每个元素，也就是文件夹中的每个文件和子文件夹的名称，并将每个名称依次存储在变量name中
        file.append(name) #将每个文件和文件夹的名称添加到名为file的列表中。注意，代码中没有初始化file列表，所以在使用前应该先创建一个空的列表，如file = []

    for f in file: #for循环，它遍历了file列表中的每个元素，也就是文件和文件夹的名称，并将每个名称依次存储在变量f中
        print('[+]existence {}'.format(f)) #打印出存在的文件和文件夹的信息，其中{}被替换为变量f的值，以显示每个文件和文件夹的名称

    print(' ') #打印结果之间插入两个空行，以增加输出的可读性
    print(' ')

    dk = open('user-agent.txt', 'r') #打开名为 'user-agent.txt' 的文本文件，并将文件对象存储在变量dk中。'r'参数表示以只读模式打开文件
    for d in dk.readlines(): #for循环，它遍历了文件对象dk的每一行文本内容，并将每一行依次存储在变量d中
        qc = "".join(d.split('\n')) #将每一行文本中的换行符('\n')去除，并将结果存储在变量qc中。它通过split('\n')将文本按照换行符分割成列表，然后使用"".join()将列表中的元素连接成一个字符串，去除了换行符
        useragent.append(qc) #将处理后的文本行（去除了换行符的）添加到名为useragent的列表中
    print('[+]user-agent Load completion') #打印出用户代理加载完成的信息
    print(' ') #打印结果之间插入两个空行，以增加输出的可读性
    print(' ')


judge() #调用了这个函数，启动了上述操作


def errors():
    lv = open('Error/error.txt', 'r') #'Error/error.txt'的文件，以只读模式（'r'）打开。这意味着它将尝试读取该文件的内容
    for e in lv.readlines(): #for循环遍历文件中的每一行，将每一行的内容存储在变量e中
        qcsw = "".join(e.split('\n')) #使用.split('\n')方法将每一行按照换行符('\n')进行拆分，然后使用"".join(...)将拆分后的列表重新连接成一个字符串。这个操作似乎是为了去掉每一行末尾的换行符
        error.append(qcsw) #将去掉换行符的内容追加到名为error的列表中。注意，在代码中没有给出error列表的定义，所以在代码的其他部分应该有相关的定义
    print('[+]The filter file is loaded')
    print(' ')
    print(' ')


errors()


def forge(): #函数定义，函数名为 forge
    sj = [] #创建了一个空列表 sj，用于存储构建的HTTP请求头部信息
    dkw = open('ip.txt', 'r') #打开名为 'ip.txt' 的文本文件，并将文件对象赋值给变量 dkw。该文件应该包含一系列IP地址，每行一个
    for i in dkw.readlines(): #循环，它遍历文件 ip.txt 中的每一行
        k = "".join(i.split('\n')) #每一行，它首先使用 split('\n') 将行末尾的换行符去掉，然后使用 join 函数将行连接成一个字符串 k
        ip.append(k) #处理后的字符串 k 添加到名为 ip 的列表中。这里似乎有一个小问题，代码中没有定义 ip 列表，所以应该在函数开始的地方添加 ip = []

    for g in range(0, len(useragent)): #遍历了一个名为 useragent 的列表，假设这个列表包含了一系列用户代理(User-Agent)字符串
        u = 'User-Agent='      #u、x 和 c 是字符串常量，用于构建不同的HTTP头部字段
        x = 'X-Forwarded-For=' #useragent[g] 表示从 useragent 列表中获取的用户代理字符串
        c = 'Client-IP='       #ip[g] 表示从之前处理的IP地址列表中获取的IP地址构建好的字符串被添加到 sj 列表
        sj.append(u + useragent[g] + '&' + x + ip[g] + '&' + c + ip[g]) #构建了一个字符串 u + useragent[g] + '&' + x + ip[g] + '&' + c + ip[g]
    kc = list(set(sj)) #将列表 sj 转换成一个集合（set），这样可以去除重复的头部信息，然后再将集合转回列表，得到不重复的头部信息列表，并赋值给 kc 变量
    su = random.choice(kc) #使用 random.choice 函数从不重复的头部信息列表 kc 中随机选择一个头部信息，并赋值给 su 变量
    qc = str(su) #将选中的头部信息 su 转换为字符串，并赋值给 qc 变量
    for v in qc.split('&'): #遍历了字符串 qc 中的每个字段（使用 '&' 符号分隔字段）,代码使用 split('=') 分割每个字段，将键(key)和值(value)分开，并将它们添加到一个名为 headers 的字典中。这里假设 headers 是在函数外部定义的字典
        key, value = v.split('=', 1) #在每次循环中，v 是一个字段，例如 "key=value"。这行代码将字段 v 使用 '=' 符号分割成两部分，分别赋值给 key 和 value 变量。1 参数表示最多只分割一次，以防止键或值中包含多个 '=' 符号
        headers[key] = value #每次循环中，将分割后的键 key 和值 value 存储在字典 headers 中，以便后续代码可以通过键来检索相应的值


forge()


def exploit(): # 定义了一个名为exploit的函数。这个函数包含了整个脚本的逻辑
    wi = os.listdir('御剑配置文件') # 使用os.listdir()函数获取了一个目录下所有文件名的列表，并将结果存储在wi变量中。这个目录是名为'御剑配置文件'的文件夹
    for w in wi: #循环，它遍历了wi中的每一个文件名
        dp = open('{}'.format('御剑配置文件/' + w), 'r', encoding='gbk') # 打开了一个名为'御剑配置文件/' + w的文件，以只读模式打开，并且指定了使用'gbk'字符编码。将文件对象赋值给dp变量
        for s in dp.readlines(): #循环，它遍历了打开的文件对象dp的所有行
            we = "".join(s.split('\n')) #将当前行s中的换行符\n删除，并将结果存储在we变量中
            for u in url: #嵌套在第一个循环中的循环，它遍历了名为url的列表中的每一个URL
                up = '{}'.format(u).rstrip('/') + we #构建了一个新的URL，它将当前循环中的URL u 和之前处理的行内容we 结合在一起。同时，通过.rstrip('/')方法删除了URL末尾可能存在的斜杠
                try: #异常处理块，用来捕获可能发生的异常
                    requet = requests.get(url=up, headers=headers, timeout=3, allow_redirects=False) # 发起了一个GET请求，访问了构建好的URL up。请求的头部信息使用了一个名为headers的变量，超时设置为3秒，并禁止了重定向
                    for e in error: #嵌套在try块中的循环，它遍历了名为error的列表中的每一个错误标志
                        if requet.status_code == 200 and not e in requet.text: #检查HTTP响应的状态码是否为200，同时检查错误标志是否不在响应文本中
                            ok = '[+]code:{} url:{}'.format(requet.status_code, requet.url) # 如果满足上述条件，构建了一个包含响应状态码和URL的字符串，存储在ok变量中
                            if ok in twoo: continue #检查ok是否已经存在于名为twoo的列表中，如果存在则继续下一次循环，避免重复记录
                            twoo.append(ok) # 将ok添加到twoo列表中，用于记录已经扫描到的成功情况
                            print(ok)
                        else: #如果条件不满足，执行以下代码块
                            no = '[x]Not url :{}'.format(requet.url) #构建一个包含未成功的消息字符串，存储在no变量中
                            if no in bc: continue #检查no是否已经存在于名为bc的列表中，如果存在则继续下一次循环，避免重复记录
                            bc.append(no) #将no添加到bc列表中，用于记录未成功的情况
                            print(no)
                except Exception as u: #捕获可能发生的异常，并将异常对象赋值给u变量
                    print('[-]Error {}'.format(u))

    if len(twoo) > 0: #检查twoo列表中是否有成功的记录
        od = open('save.txt', 'w') #以写模式打开一个名为save.txt的文件。
        od.close() #od.close() - 关闭文件

        xr = open('save.txt', 'r') #只读模式打开save.txt文件
        for c in twoo: #遍历twoo列表中的每一个成功记录
            print(c, file=open('save.txt', 'a')) #将每一条成功记录写入到save.txt文件中


exploit()