import requests
from selenium import webdriver
import PyV8


header = {
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',\
'accept-encoding':'gzip, deflate, sdch',\
'accept-language':'zh-CN,zh;q=0.8', \
'cache-control':'max-age=0',\
#'cookie':'testcookie=yes; __jsluid=df6f3702eb9b742adcbada5f12d09a48; __guid=dEYeCp58c2ada67d7397.77568780; LiveWSMBY90996241=1489153431701400961066; LiveWSMBY90996241sessionid=1489153431701400961066; NMBY90996241fistvisitetime=1489153431715; NMBY90996241visitecounts=1; vlstatId=vlstat-1489153431000-695576923; __jsl_clearance=1489163106.315|0|eVh2DbOci3Ly44YLiVVzJ%2F3LYlg%3D; NMBY90996241lastvisitetime=1489163100214; NMBY90996241visitepages=5; Hm_lvt_c4e8e5b919a5c12647962ea08462e63b=1489153432; Hm_lpvt_c4e8e5b919a5c12647962ea08462e63b=1489163100; _ga=GA1.2.79895231.1489153432; ip_city=gz; PHPSESSID=ide0t8tvq7n0vb7moh1n99dd25',\
'upgrade-insecure-requests':'1',\
'referer':'https://www.91160.com/doctors/index/docid-1286.html',\
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36'}

url = 'http://www.cnvd.org.cn/'
web_url = 'https://www.91160.com/doctors/index/docid-1286.html'
# w = webdriver.PhantomJS()
# w.get(web_url)
# i = w.find_element_by_id('doc_details').text
# print(i)
r = requests.get(web_url,headers=header)
# r = requests.get(url,headers=header)
print(r.text)
# ctxt = PyV8.JSContext()
# ctxt.enter()

