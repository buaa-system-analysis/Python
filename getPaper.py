import requests
import time



def getidlist(lens,kwd,header):
	i = 0
	idlist = []

	while i < lens:
		print(i)
		url = 'https://xueshu.baidu.com/s?wd=' + kwd + '&pn=' + str(i) + '&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_type%3D%7B1%7D&sc_f_para=sc_tasktype%3D%7BrecommendKeyword%7D&bcp=2&sc_hit=1'
		html = requests.get(url,headers = header)
		print(html)

		content = html.text.split("wd=paperuri%3A%28");
		for strs in content:
			nowid = strs[0:len('eca60ef68a6f74fa3ff5eb5ae41c9111')]
			if (nowid not in idlist):
				idlist.append(nowid)

		i = i + 10

	
	return idlist
