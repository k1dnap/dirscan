import queue #提供了队列数据结构，用于在多线程编程中安全地进行数据传递和共享。通常，在多线程环境下，使用队列可以避免竞态条件（race conditions）和数据不一致性问题
import common #导入了一个名为"common"的自定义模块
import requests #用于进行HTTP请求。它允许程序通过HTTP协议与Web服务进行通信，例如发送GET或POST请求并处理响应
import threading #提供了多线程编程的功能，允许在同一个程序中运行多个线程以实现并行执行
import random #提供了生成随机数的函数，通常用于模拟随机性或在程序中进行随机选择
import time #提供了与时间相关的功能，如延迟程序执行、获取当前时间等

class SingleScan: #义了一个名为 SingleScan 的Python类                 #表示对象本身

	def __init__(self,url,Type,filename,ThreadNum=20,Sleeptime=3): #类的构造函数，用于初始化对象的属性
		self.url=url #传递给构造函数的 url 参数赋值给对象的 url 属性，以便在对象中可以访问该值
		self.Type=Type #将传递给构造函数的 Type 参数赋值给对象的 Type 属性，以便在对象中可以访问该值
		self.ThreadNum=ThreadNum #将传递给构造函数的 ThreadNum 参数赋值给对象的 ThreadNum 属性，以便在对象中可以访问该值。这个属性表示线程数量，默认为 20
		self.Targets=queue.Queue() #创建了一个队列对象并将其赋值给对象的Targets,属性,这个队列可能会在后续的代码中用于存储一些数据
		self.Pro=[] #创建了一个空列表并将其赋值给对象的 Pro 属性
		self.RandomProxy="" #将一个空字符串赋值给对象的 RandomProxy 属性
		self.Sleeptime=Sleeptime #将传递给构造函数的 Sleeptime 参数赋值给对象的 Sleeptime 属性,表示休眠时间，默认为 3 秒
		self.filename=filename #将传递给构造函数的 filename 参数赋值给对象的 filename 属性，以便在对象中可以访问该值

	def OpenDir(self): #用于读取配置文件中的目录，并将生成的目标URL放入队列 Targets 中
		NameOfDir=["asp","php","aspx","jsp","unknown"] #根据给定的 Type，它会打开对应的配置文件并读取其中的内容，将生成的URL加入队列
		for i in range(0,5): #循环，它遍历了从0到4的整数，即循环5次，因为列表中有5个目录类型
			if(self.Type==NameOfDir[i]): #条件语句，它检查类实例的属性 Type 是否与 NameOfDir[i] 相等。self.Type 存储了一个目录类型，它表示当前要处理的目录类,如果相等，说明找到了匹配的目录类型
				with open("config/"+self.Type+".txt","r") as f: #用于打开文件的语句，它打开名为 self.Type + ".txt" 的配置文件，文件位于 "config/" 目录下，并以只读模式（"r"）打开
					for line in f.readlines(): #循环，它遍历打开的配置文件中的每一行
						payload=self.url+line.strip() #将 self.url 和去掉行末尾空白字符的 line 组合成一个新的字符串，并将其存储在 payload 变量中。这个新字符串表示一个目标URL
						if(payload!=self.url): #条件语句，它检查 payload 是否与 self.url 不相等,这是为了确保生成的目标URL不与原始的 self.url 相同
							self.Targets.put(payload) #如果条件满足，将 payload 添加到名为 Targets 的队列中,是将生成的目标URL存储在队列中的关键步骤
			else:
				with open("config/"+self.Type+".txt","r") as f:
					for line in f.readlines():
						payload=self.url+line.strip()
						if(payload!=self.url):
							self.Targets.put(payload)

	def FindDir(self): #这个方法用于扫描目标URL，检查是否存在可访问的目录。它从队列 Targets 中获取目标URL，然后发送HTTP头请求，如果响应状态码为200，表示目录存在，将其打印并记录到输出文件中
		while not self.Targets.empty(): #循环语句，它会一直执行，直到 self.Targets 这个队列为空,self.Targets 似乎是一个队列，用于存储目标URL
			target=self.Targets.get() #从 self.Targets 队列中获取一个目标URL，并将其存储在变量 target 中
			try: #异常处理块，用于捕获可能出现的异常
				filename=common.GenerateReport(self.url) #调用名为 common.GenerateReport 的方法，传递 self.url 作为参数，并将返回的结果存储在变量 filename 中,可能用于生成报告文件的文件名
				r=requests.head(target,timeout=3) #发送一个HTTP头请求（HTTP HEAD请求）到目标URL target，并设置请求的超时时间为3秒,HTTP头请求通常用于仅获取目标的响应头信息而不获取响应体内容
				if(r.status_code==200): #检查HTTP响应的状态码是否为200，状态码200表示请求成功，通常用于表示目标存在
					print(target) #目标存在，将目标URL打印出来
					common.AddUrlToReport(target,self.filename) #调用名为 common.AddUrlToReport 的方法，将目标URL和文件名 self.filename 作为参数传递给该方法
			except: #异常处理块的结尾，用于捕获任何可能发生的异常。如果发生异常，代码将继续执行
				continue

	def Work(self): #这个方法启动多线程执行目录扫描任务。根据 ThreadNum 的值创建多个线程，并让它们执行 FindDir 方法
		Threads=[] #空列表，用来存储线程对象
		for i in range(self.ThreadNum): #for循环，它将迭代self.ThreadNum次，self.ThreadNum是类的一个属性，表示要创建的线程数量
			t=threading.Thread(target=self.FindDir) #指定线程的执行目标是类中的FindDir方法。这意味着每个线程将执行FindDir方法中定义的任务
			Threads.append(t) #将创建的线程对象t添加到Threads列表中，以便稍后可以管理这些线程
			t.start() #启动线程，开始执行与FindDir方法相关联的任务
		for t in Threads:
			t.join(3) #对于每个线程，调用join方法，此处参数3表示最多等待3秒钟。join方法会等待线程完成其任务，或者在指定的超时时间内返回。这样做的目的是确保所有线程都能在一定时间内完成，然后程序继续执行下一步操作

	def GetProxy(self): #这个方法用于从配置文件中获取代理服务器的地址，并将这些地址存储在 Pro 属性中
		with open("config/proxy.txt","r") as f: #这是一个上下文管理器，用于打开文件 "config/proxy.txt" 以供读取。"r" 表示以只读模式打开文件，as f 将文件对象赋给变量 f，以便后续操作文件
			for line in f.readlines(): #循环，它遍历打开的文件 f 中的每一行
				proxy="https://"+line.strip()+"/" #创建了一个代理服务器地址字符串。line.strip() 用于去除每一行末尾的换行符和空白字符，然后将 "https://" 添加到每一行的前面，并在最后添加了一个斜杠 "/"。最终的 proxy 变量将包含一个代理服务器的完整地址，例如 "https://example.com/"
				self.Pro.append(proxy) #将创建的代理服务器地址 proxy 添加到类的属性 Pro 中。self.Pro 是一个列表，用于存储代理服务器地址

	def Bypass(self): #是用于通过代理服务器进行目录扫描，与 FindDir 类似
		while not self.Targets.empty(): #while 循环，它会在 "self.Targets" 队列不为空的情况下执行。该队列存储了目标 URL
			target=self.Targets.get() #从 "self.Targets" 队列中获取一个目标 URL
			flag=0 #初始化一个标志位 "flag"，用于表示是否已经找到了目标
			i=random.randint(0,len(self.Pro)-1) #生成一个随机数 "i"，用于随机选择一个代理服务器地址
			self.RandomProxy=self.Pro[i] #从代理服务器列表 "self.Pro" 中选择一个随机的代理服务器地址，并将其存储在 "self.RandomProxy" 变量中
			try: #开始一个 try 块，捕获可能发生的异常
				proxy="https://"+self.RandomProxy+"/" #创建一个代理服务器的URL，将self.RandomProxy添加到URL中，形成一个完整的代理服务器地址
				proxies={"https":proxy}	#创建一个字典proxies，用于配置HTTP请求的代理服务器，将之前创建的代理服务器URL添加到字典中
				r=requests.head(target,timeout=3,proxies=proxies) #向目标URL发送一个HTTP头请求，同时指定了代理服务器。这个请求会在3秒内超时，如果请求成功，响应对象会被存储在变量r中
				if(r.status_code==200)&(flag==0): # 检查HTTP响应的状态码是否为200，同时检查flag是否为0。如果两个条件都满足，表示请求成功且flag为0，执行下面的操作
					print(target) #打印目标URL，表示这个URL响应成功
					common.AddUrlToReport(target,self.filename) #调用一个名为AddUrlToReport的函数，将目标URL添加到某种报告中，同时传递了target和self.filename作为参数
					flag=1 #将flag设置为1，以避免在同一个目标URL上重复操作
			except:
				continue
			
	def Sleep(self): #用于带有休眠间隔的目录扫描
		while not self.Targets.empty(): #循环语句，它会一直执行，直到self.Targets为空。self.Targets看起来是一个队列或者栈的数据结构，程序会不断地从中获取目标进行处理
			target=self.Targets.get() #从self.Targets中获取一个目标，赋值给target变量
			try: #异常处理的开始，意味着下面的代码块可能会引发异常
				r=requests.head(target,timeout=3) #发送一个HTTP HEAD请求到target指定的URL，等待最多3秒钟来获取响应信息。结果会被保存在r变量中
				if(r.status_code==200): #检查HTTP响应的状态码是否为200，这表示请求成功
					print(target) #如果响应状态码为200，就打印目标URL
					common.AddUrlToReport(target,self.filename) #调用一个名为common.AddUrlToReport的函数，将目标URL和self.filename作为参数传递给它。这个函数的功能是将目标URL添加到报告中，但代码中并没有提供common模块的定义，所以需要查看其他地方是否定义了这个函数
				time.sleep(self.Sleeptime) #处理完目标后，通过time.sleep函数休眠一段时间，时间长度由self.Sleeptime决定。这个休眠可能是为了限制请求的频率，以防止过多的请求导致服务器负载过重
			except: #异常处理的部分，用来捕获在try块中出现的任何异常，并继续循环处理下一个目标。这意味着如果请求失败或出现其他异常，代码不会停止执行，而是继续处理下一个目标
				continue

	def WorkByProxy(self): #启动多线程执行通过代理服务器的目录扫描任务，与 Work 方法类似，但使用代理服务器发送请求
		Threads=[] #创建一个空的列表，用于存储后续创建的线程对象
		for i in range(self.ThreadNum): #通过一个循环，将线程的创建操作重复self.ThreadNum次。self.ThreadNum应该是一个在类中定义的属性，表示要创建的线程数量
			t=threading.Thread(target=self.Bypass) #在每次循环迭代中，创建一个新的线程对象t，并将self.Bypass作为该线程的目标函数。这意味着线程将执行self.Bypass方法中的代码
			Threads.append(t) #将创建的线程对象t添加到Threads列表中，以便稍后可以管理这些线程
			t.start() #启动线程，使其开始执行self.Bypass方法中的代码
		for t in Threads: #在所有线程都创建并启动后，通过另一个循环迭代遍历线程列表
			t.join(3) #对于每个线程t，调用join(3)方法。这意味着主线程将等待每个子线程最多3秒钟，然后继续执行。join方法用于等待线程执行完成。在这里，它的参数是3，表示最多等待3秒钟。如果线程在3秒内完成，主线程将继续执行，否则将继续等待，直到超过3秒
