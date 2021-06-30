#!/usr/bin/python
import paramiko
import time,sys,re,os
import socket
import threading,Queue


root_cmd = r''' pwd  '''
node = 'd3.txt'

upload_file = '/etc/passwd'
user_cmd = r'''  df -h  '''
issu = 0

login_user = 'xiaoming'
key_file = 'id_rsa'
sshport = 22
time_out = 20
Numer_Thread = 20


q = Queue.Queue()
socket.setdefaulttimeout(time_out)
lock = threading.Lock()
onlydir = dir()

def sshgo(host,rootuser,rootpwd):
	rtn = []
	key = paramiko.RSAKey.from_private_key_file(key_file)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.load_system_host_keys()

	rtn.append('________________________________%s'%host)
	try:
		ssh.connect(host,sshport,login_user,pkey=key)
	except Exception,e:
		rtn.append('%s__ERROR_________________________%s'%(e,host))
		return rtn
	if 'upload_file' in onlydir:
		try:
			sftp = ssh.open_sftp()
			sftp.put(upload_file,os.path.basename(upload_file))
			sftp.close()
		except Exception,e:
			rtn.append('%s__ERROR__sftp___________________%s'%(e,host))
	if 'user_cmd' in onlydir:
		stdin, stdout, stderr = ssh.exec_command('LANG=en_US.UTF-8;LANGUAGE=en_US.UTF-8; %s'%user_cmd)
		rtn.append(stdout.read() + stderr.read())
	if not issu:
			return rtn
	shell = ssh.invoke_shell()
	while not shell.recv(4096).endswith(']$ '):
		time.sleep(0.1)

	buff  =''
	shell.send('LANG=en_US.UTF-8;LANGUAGE=en_US.UTF-8;su - %s'%rootuser)
	shell.send('\n')
	while not buff.endswith('Password: '):
		time.sleep(0.1)
		resp = shell.recv(4096)
		buff += resp
		if buff.endswith('exist') or buff.endswith(']$ '):
			rtn.append('ERROR_SSH.RECV_____1________________%s'% resp)
			return rtn
	buff  =''
	shell.send(rootpwd)
	shell.send('\n')
	while not buff.endswith(']# '):
		time.sleep(0.1)
		resp = shell.recv(4096)
		buff += resp
		if buff.endswith('password') or buff.endswith(']$ '):
			rtn.append('ERROR_SSH.RECV_____2________________%s'% resp)
			return rtn
	shell.send('LANG=en_US.UTF-8;LANGUAGE=en_US.UTF-8; %s '%root_cmd)
	shell.send('\n')
	buff = ''
	while not buff.endswith(']# '):
		time.sleep(0.1)
		resp = shell.recv(4096)
		buff += resp
		if buff.endswith(']$ '):
			rtn.append('ERROR_SSH.RECV_____3________________%s'% resp)
			break
		elif buff.endswith('? '):
			rtn.append('ERROR_SSH.RECV_____4________________??')
			break
	#print buff
	rtn.append('\n'.join(buff.split('\n')[1:-1]))
	ssh.close()
	return rtn

def do_echo(host,rootuser,rootpwd):
	result = sshgo(host,rootuser,rootpwd)
	lock.acquire()
	for pp in result:
		print pp
	print
	sys.stdout.flush()
	lock.release()

def working():
	while 1:
		args = q.get()
		do_echo(args[0],args[1],args[2])
		q.task_done()

for i in range (Numer_Thread):
	t = threading.Thread(target=working)
	t.setDaemon(1)
	t.start()

fn = open(node)
for i in fn:
	if not re.match('#',i) and re.search('.',i):
		c = i.split()
		q_args = [c[0],c[1],c[2]]
		q.put(q_args)
fn.close()
q.join()

