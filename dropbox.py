#!/usr/bin/env python3
import sys
import os
import json
import urllib.request
import argparse

url_chunk = 'https://api-content.dropbox.com/1/chunked_upload?param=val'
url_chunk_commit = 'https://api-content.dropbox.com/1/commit_chunked_upload/auto/'
url_metadata = 'https://api.dropbox.com/1/metadata/auto/'
url_file_get = 'https://api-content.dropbox.com/1/files/auto/'
url_file_put = 'https://api-content.dropbox.com/1/files_put/auto/'

def get_token():
	envname = 'DropboxAccessToken'
	get = os.getenv(envname)
	if get:
		global access_token
		access_token = get
	else:
		print('NOT find %s, Run shell cmd "export %s=<Your Token>"'%(envname,envname))
		exit(1)

def color(str,clr=''):
	if clr == 'yellow':
		return '\033[33;1m' + str + '\033[0m'
	else:
		return '\033[36;1m' + str + '\033[0m'

def up_chunk(localfile,remote_path):
	url0 = '%s&access_token=%s'%(url_chunk,access_token)
	url_commit = '%s%s/%s?access_token=%s'%(url_chunk_commit,remote_path,os.path.basename(localfile),access_token)
	DATA = open(localfile,'rb')
	url2 = None
	while 1:
		cDATA = DATA.read(54857600)  # 1024 * 1024 * 100 = 100MB
		if not cDATA: break
		if url2:
			url = url2
		else:
			url = url0
		req = urllib.request.Request(url,data=cDATA,method='PUT')
		req.add_header('Content-Type','application/x-www-form-urlencoded;')
		try:
			res = urllib.request.urlopen(req)
		except urllib.error.HTTPError as e:
			print(e.code)
			print(e.fp.read().decode('utf-8'))
			exit(1)
		else:
			pp = (json.loads(res.read().decode('utf-8')))
			upid = pp['upload_id']
			offset = pp['offset']
			url2 = url0 + '&upload_id=%s&offset=%d'%(upid,offset)
			print(json.dumps(pp,indent=4))
	DATA.close()

	#Commit
	pdata = 'upload_id=%s'%upid
	req = urllib.request.Request(url_commit,data=pdata.encode('utf-8'))
	req.add_header('Content-Type','application/x-www-form-urlencoded;')
	try:
		res = urllib.request.urlopen(req)
	except urllib.error.HTTPError as e:
		print(e.code)
		print(e.fp.read().decode('utf-8'))
	else:
		pp = (json.loads(res.read().decode('utf-8')))
		print(json.dumps(pp,indent=4))




def up_file(localfile,remote_path):
	url = '%s%s/%s?access_token=%s&param=val'%(url_file_put,remote_path,os.path.basename(localfile),access_token)
	#print(url)
	DATA = open(localfile,'rb')
	length = os.path.getsize(localfile)
	req = urllib.request.Request(url,data=DATA.read(),method='PUT')
	req.add_header('Content-Type','application/x-www-form-urlencoded;')
	try:
		res = urllib.request.urlopen(req)
	except urllib.error.HTTPError as e:
		print(e.code)
		print(e.fp.read().decode('utf-8'))
	else:
		pp = (json.loads(res.read().decode('utf-8')))
		print(json.dumps(pp,indent=4))
	DATA.close()


def down_file(remote_path):
	url = '%s%s?access_token=%s'%(url_file_get,remote_path,access_token)
	localfile = os.path.basename(remote_path)
#	print(url)
	if os.path.exists(localfile):
		print('%s already exist'%localfile)
		exit(1)
	try:
		filename,headers = urllib.request.urlretrieve(url,localfile)
	except urllib.error.HTTPError as e:
		print(e.code)
		print(e.fp.read().decode('utf-8'))
	else:
		#for i,j in headers.items():
		#	print(i,j)
		pp = json.loads(headers['x-dropbox-metadata'])
		print(json.dumps(pp,indent=4))

def get_meta(remote_path):
	url = '%s%s?access_token=%s'%(url_metadata,remote_path,access_token)
	#print(url)
	try:
		res = urllib.request.urlopen(url)
	except urllib.error.HTTPError as e:
		print(e.code)
		print(e.fp.read().decode('utf-8'))
	else:
		jsmeta = json.loads(res.read().decode('utf-8'))
		if not jsmeta['is_dir']:
			print(json.dumps(jsmeta,indent=4))
		if jsmeta['is_dir']:
			print(color('Path: %s'%jsmeta['path'],clr='yellow'))
			space = '\t\t'
			for i in jsmeta['contents']:
				cot = i['path'].split('/')[-1]
				if i['is_dir']:
					print(color(cot) + space,end='')
				else:
					print(cot + space,end='')
			print()

def optparse():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--download')
	parser.add_argument('-l','--list',nargs='?',const='/')
	parser.add_argument('-u','--upload',nargs=2,help='--upload <local_file> <remote_path>')
	args = parser.parse_args()
	if len(sys.argv) == 1:
		parser.parse_args(['--help'])
	else:
		return args

def main():
	get_token()
	argvs = optparse()
	#print(argvs)
	if argvs.download:
		down_file(argvs.download)
		return
	if argvs.upload:
		up_chunk(argvs.upload[0],argvs.upload[1])
		#up_file(argvs.upload[0],argvs.upload[1])
		return
	if argvs.list:
		get_meta(argvs.list)
		return

if __name__ == '__main__':
	main()
