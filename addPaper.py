from SearchControl import addPaper
from getPaper import getidlist
import requests
import re

cookie = 'BAIDUID=66B96D01820503BBD960243831160CF9:FG=1; BIDUPSID=66B96D01820503BBD960243831160CF9; PSTM=1553515072; __cfduid=d7cbe96813175b3eb74ae73723f88c4dd1555557797; BDUSS=FJKMmJRckRieTVVcnhLZTdBZzBmaHQ5NXpuVTN5Mk1WTjFxQ35ZZnZGUTNiLVZjRVFBQUFBJCQAAAAAAAAAAAEAAAC-SVkmMG9Etfe1xLuqwPZvMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADfivVw34r1cW; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=654575616; delPer=0; BD_HOME=0; H_PS_PSSID=; Hm_lvt_f28578486a5410f35e6fbd0da5361e5f=1557906928; Hm_lpvt_f28578486a5410f35e6fbd0da5361e5f=1557906928; BD_CK_SAM=1; Hm_lvt_43172395c04763d0c12e2fae5ce63540=1557907157; PSINO=1; BDRCVFR[w2jhEs_Zudc]=mbxnW11j9Dfmh7GuZR8mvqV; Hm_lpvt_43172395c04763d0c12e2fae5ce63540=1557907569; BDSVRTM=439'
header = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
	'connection' : 'keep-alive',
	'cookie': cookie,
	'Host' : 'xueshu.baidu.com',
	'upgrade-insecure-requests': '1',
	'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

def getinner(strs,beg,ens):
	return strs.split(beg)[1].split(ens)[0].strip()


idlist = getidlist(100,'BERT',header);
print(idlist)
for i in range(8,len(idlist)):
	nowid = idlist[i];

	url = 'http://xueshu.baidu.com/usercenter/paper/show?paperid=' + nowid + '&site=xueshu_se'

	try:
		content = requests.get(url,headers = header).text.split('class="main-info">')[1];
	except:
		continue

	title = getinner(re.findall(r"data-click=\"{'act_block':'main','button_tp':'title'}\" target=\"_blank\">.*</a>",content)[0],">","<")

	authors = []
	try:
		authorss = re.findall(r"data-click=\"{'button_tp':'author'}\">.*?</a>",content)
		for author in authorss:
			authors.append(getinner(author,">","<"))
	except:
		pass

	abstract = ''
	try:
		abstract = getinner(re.findall(r'p class="abstract" data-sign="">.*</p>',content)[0],">","<")
	except:
		pass

	publishment = ''
	try:
		publishment = getinner(re.findall(r"data-click=\"{'button_tp':'doi'}\">\n.*",content)[0],">","<")
	except:
		pass

	citation = 0
	try:
		citation = int(getinner(re.findall(r"data-click=\"{'button_tp':'sc_cited'}\">\n.*",content)[0],">","<"))
	except:
		pass

	fields = []
	try:
		fieldss = re.findall(r"data-click=\"{'button_tp':'sc_search'}\" target=\"_blank\" title=\".*?\"",content)
		for field in fieldss:
			fields.append(field.split("\"")[5])
	except:
		pass

	price = i

	fulltextURL = ''
	try:
		fulltextURL = re.findall(r"href=\".*?{'button_tp':'link','libbuy':'0'}",content)[0].split("\"")[1]
	except:
		pass

	addPaper(title=title,authors=authors,abstract=abstract,publishment=publishment,citation=citation,field=fields,price=price,fulltextURL=fulltextURL)

	print(str(i) + " finished")