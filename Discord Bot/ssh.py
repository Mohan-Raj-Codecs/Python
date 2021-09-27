import paramiko

Server_on = False
ip="65.0.139.80"
user="ubuntu"
passwd=""
#pem_file="MIRACLE.pem"
#key_file=paramiko.RSAKey.from_private_key_file(pem_file)
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def exe(x):
    x=str(x)
    cmd=x
    print("Logging in ssh")
    ssh_client.connect(hostname=ip,username=user,pkey=key_file)   #Authorization using PEM file
    #ssh_client.connect(hostname=ip,username=user,password=passwd)  #Authorization using password
    print("Logging Successfull")
    print("Executing....")
    stdin,stdout,stderr=ssh_client.exec_command(cmd)
    stdout=stdout.readlines()
    stderr=stderr.readlines()
    if stderr==[]:
        print("Executed Successfully\n")
        print(stdout)
    else:
        print(stderr)
