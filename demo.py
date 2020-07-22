import boto3
import os
import subprocess
import time
ec2 = boto3.resource('ec2', region_name='ap-south-1')


def start(id):
    minstance = ec2.Instance(id)
    print(minstance.start())
    minstance.wait_until_running()
    print(minstance.public_ip_address)
    time.sleep(20)
    subprocess.Popen(["ssh", "-D", "8123","-q", "-f", "-C", "-N", "-i", "/Users/aryanganotra/Downloads/flask-api.pem","-o","StrictHostKeyChecking no", "ubuntu@"+minstance.public_ip_address], stdout=subprocess.PIPE)
    #ami-02d55cb47e83a99a0

def stop(id):
    minstance = ec2.Instance(id)
    print(minstance.stop())

def terminate(id):
    minstance = ec2.Instance(id)
    print(minstance.terminate())

def create():
    instance = ec2.create_instances(
    ImageId='ami-02d55cb47e83a99a0',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='flask-api',
    SecurityGroups=[ 
        'launch-wizard-4',
    ],
)
    instance[0].wait_until_running()
    print(instance[0])
    minstance = ec2.Instance(instance[0].id)
    # print(minstance.start())
    # minstance.wait_until_running()
    print(minstance.public_ip_address)
    time.sleep(20)
    subprocess.Popen(["ssh", "-D", "8123","-q", "-f", "-C", "-N", "-i", "/Users/aryanganotra/Downloads/flask-api.pem","-o","StrictHostKeyChecking no", "ubuntu@"+minstance.public_ip_address], stdout=subprocess.PIPE)
    #ami-02d55cb47e83a99a0
    
