import SingleScan
import common #导入了两个自定义模块，这些模块包含了程序需要使用的功能和方法


def MultiScan(filename,level): #定义了一个名为MultiScan的函数，接受两个参数 filename 和 level
	with open (filename,"r") as f: #打开了一个文件，该文件名由传入的filename参数确定，并使用r模式以只读方式打开
		for line in f.readlines(): #遍历文件中的每一行
			url="http://"+line.strip()+"/" #将从文件中读取的每一行（去除首尾空格和换行符）作为基础，构造了一个以http://开头，以/结尾的URL
			Type=common.GetTypeOfScript(url) #调用了common模块中的GetTypeOfScript函数，该函数返回了网站所使用的脚本类型，并将其赋值给Type变量
			print("[+] The script of this web is "+Type+".") #打印出网站所使用的脚本类型
			if(level==1): #根据传入的level参数的不同，执行不同的扫描操作。分别对应不同的扫描模式
				name=common.GenerateReport(url)
				Default=SingleScan.SingleScan(url,Type,name)
				Default.OpenDir()
				Default.FindDir()
				Default.Work()
			elif(level==2):
				name=common.GenerateReport(url)
				Default=SingleScan.SingleScan(url,Type,name)
				Default.OpenDir()
				Default.GetProxy()
				Default.WorkByProxy()
			elif(level==3):
				name=common.GenerateReport(url)
				Default=SingleScan.SingleScan(url,Type,name)
				Default.OpenDir()
				Default.Sleep()
				#在每个分支中，首先调用了common.GenerateReport(url)函数生成了一个报告的名字，然后创建了一个名为Default的对象，该对象使用SingleScan.SingleScan类对指定的URL进行扫描
			    #每个分支中的Default对象接着调用了一系列方法，例如OpenDir()、FindDir()、GetProxy()等，执行具体的扫描操作
			else:
				print("\nWarning :  Wrong input.... ")
				print("\nTips: The max level is 3 . \n")
				print("Examples: Scan by multi threads : -u http://example.com/ --level=1\n")
				print("          Scan by proxies : -u http://example.com/ --level=2 \n ")
				print("          Scan by Delay : -u http://example.com/  --level=3 \n ")
				print("          Multi Scan by proxies : -r dic.txt --level=2 \n ")
			#如果传入的level参数不在1到3之间，会输出一条警告信息，指出输入的level参数无效，并提供了一些示例和提示
