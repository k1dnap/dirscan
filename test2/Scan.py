import optparse #主要用于解析命令行参数和选项，是用来处理命令行参数的一个常见工具
from module import SingleScan #optparse 模块已经被废弃，被 argparse 模块所取代
from module import MultiScan
from module import common


def main(): #定义主函数的开始
	#这里创建了一个命令行参数解析器，它使用 optparse 模块。该解析器定义了程序接受的命令行参数以及它们的说明
	parser=optparse.OptionParser("-u <Target url> -r <Target list> --level <Bypass or not> -t <Thread number>\nExamples: Scan by multi threads : -u http://example.com/ --level=1\n          Scan by proxies : -u http://example.com/ --level=2\n          Scan by Delay : -u http://example.com/  --level=3\n          Multi Scan by proxies : -r dic.txt --level=2 \n ")
	#这一系列语句用于向解析器添加命令行选项
	parser.add_option("-u",dest='url',type="string",help="Please input the target url .")
	parser.add_option("--level",dest='level',type="string",help="Please choose which level to use .")
	parser.add_option("-r",dest='filename',type="string",help="Please input target urls .")
	parser.add_option("-t",dest='threadnum',type="int",help="Please input number of threads .")
#-u：用于指定目标URL。--level：用于指定扫描级别。-r：用于指定目标URL列表的文件名。-t：用于指定线程数量

	(options,args)=parser.parse_args() #解析实际的命令行参数，并将结果存储在 options 和 args 变量中。options 包含了解析后的命令行选项的值，而 args 包含了不属于选项的其余命令行参数
	url=options.url
	level=options.level
	threadnum=options.threadnum	
	filename=options.filename

#接下来的一系列 if 语句根据命令行参数的不同组合来执行不同的操作
	if (url!=None)&(level=="1"):     #提供了 -u 参数并且 --level 参数为 "1"，则执行默认扫描，不绕过任何安全机制
		Type=common.GetTypeOfScript(url)
		print("[+] The script of this web is "+Type+".")
		if(threadnum!=None):
			name=common.GenerateReport(url)
			Default=SingleScan.SingleScan(url,Type,threadnum,name)
			Default.OpenDir()
			Default.FindDir()
			Default.Work()
		else:
			name=common.GenerateReport(url)
			Default=SingleScan.SingleScan(url,Type,name)  # Default 3 threads
			Default.OpenDir()
			Default.FindDir()
			Default.Work()			
	elif (url!=None)&(level=="2"):     #提供了 -u 参数并且 --level 参数为 "2"，则使用代理进行扫描
		Type=common.GetTypeOfScript(url)
		print("[+] The script of this web is "+Type+".")
		name=common.GenerateReport(url)
		Default=SingleScan.SingleScan(url,Type,name)
		Default.filename=name
		Default.OpenDir()
		Default.GetProxy()	
		Default.WorkByProxy()
	elif (url!=None)&(level=="3"):     #提供了 -u 参数并且 --level 参数为 "3"，则使用时间延迟进行扫描
		Type=common.GetTypeOfScript(url)
		print("[+] The script of this web is "+Type+".")
		name=common.GenerateReport(url)
		Default=SingleScan.SingleScan(url,Type,name)
		Default.filename=name
		Default.OpenDir()
		Default.Sleep()
	elif(filename!=None)&(level=="1"): #提供了 -r 参数并且 --level 参数为 "1"，则执行多个目标的默认扫描
		MultiScan.MultiScan(filename,1)
	elif(filename!=None)&(level=="2"): #提供了 -r 参数并且 --level 参数为 "2"，则执行多个目标的代理扫描
		MultiScan.MultiScan(filename,2)
	elif(filename!=None)&(level=="3"): #提供了 -r 参数并且 --level 参数为 "3"，则执行多个目标的时间延迟扫描
		MultiScan.MultiScan(filename,3)
	else: #如果没有提供有效的参数组合，则显示警告消息和示例用法
		print("\nWarning :  Wrong input.... ")
		print("\nTips: Add \"http or https\" in url. \n")
		print("Examples: Scan by multi threads : -u http://example.com/ --level=1\n")
		print("          Scan by proxies : -u http://example.com/ --level=2 \n ")
		print("          Scan by Delay : -u http://example.com/  --level=3 \n ")
		print("          Multi Scan by proxies : -r dic.txt --level=2 \n ")
#根据不同的扫描级别和参数，程序会调用不同的函数，例如 common.GetTypeOfScript() 、common.GenerateReport()、SingleScan.SingleScan()、MultiScan.MultiScan() 等，执行相应的扫描操作
main()
