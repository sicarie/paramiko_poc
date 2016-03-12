import paramiko
import time

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='user', password='P@ssw0rd!', port=22)

stdin, stdout, stderr = ssh.exec_command('echo hi; ls /etc')

print "- ssh.exec_command -------------"
print stdout.readlines()
print "--------------------------------"
