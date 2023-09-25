import requests


def GetTypeOfScript(url): #定义了一个名为GetTypeOfScript的函数，该函数接受一个参数url，用于判断输入URL对应的网页类型
	try: #异常处理
		r=requests.get(url,timeout=3)
	except requests.exceptions.ReadTimeout:
		print("Conncet failure,can't judge the script.")
	except requests.exceptions.ConnectTimeout:
		print("Conncet failure,can't judge the script.") #尝试向给定的URL发送HTTP请求，如果遇到连接超时（requests.exceptions.ConnectTimeout）或读取超时（requests.exceptions.ReadTimeout）的异常，则打印相应错误信息
	if("aspx" in r.text): #判断网页类型
		return "aspx"
	elif("php" in r.text):
		return  "php"
	elif("asp" in r.text):
		return  "asp" 
	elif("jsp" in r.text):	
		return  "jsp" 
	else:
		return "dir" #通过检查HTTP响应文本，判断网页类型是否包含特定的字符串（aspx、php、asp、jsp），如果包含则返回相应的网页类型，否则返回"dir"表示目录

def GenerateReport(target): #生成报告的函数
	filename1=target.replace("http://","_")
	filename2=filename1.replace("/","_")
	filename3=filename2.replace(".","_")
	return filename3
#定义了一个名为GenerateReport的函数，接受一个参数target，用于生成报告文件的文件名。在此函数中，将target中的"http://"替换为""，将斜杠"/"替换为""，将点"."替换为"_"，最终生成文件名

def AddUrlToReport(url,filename): #将URL添加到报告的函数
	with open(filename+".txt","a") as f:
		f.write(url+"\n")
#定义了一个名为AddUrlToReport的函数，接受两个参数：url和filename。该函数将给定的URL以追加方式写入到文件名为filename + ".txt"的文件中