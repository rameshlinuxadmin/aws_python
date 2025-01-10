import json
import boto3 
f = open('requisites.json')
data = json.load(f)
ec2_client = boto3.client('ec2')

for i in data['instances']:
    print(f"AMI Image: {i['ami_image']}")
    print(f"VPC ID: {i['vpc-id']}")
    print(f"Security group ID: {i['securitygroups']}")
    print(f"Instance Type: {i['instance-type']}")
    print(f"Maximum count of Instance: {i['MaxInstanceCount']}")
    print(f"Minimum count of Instance: {i['MinInstanceCount']}")
    print(f"Key Pair: {i['keypair']}.pem")

with open("requisites.json") as file:
    data = json.load(file)
instance = data["instances"][0]

print(instance['ami_image'])
try:
    creation = ec2_client.run_instances(
        ImageId=instance['ami_image'],
        InstanceType=instance['instance-type'],
        KeyName=instance['keypair'],
        MinCount=instance['MinInstanceCount'],
        MaxCount=instance['MaxInstanceCount'],
        SecurityGroupIds=instance['securitygroups']
    )
    print("EC2 instance created successfully")
except Exception as e:
    print("error: ", str(e))

ec2 = boto3.resource('ec2')
def info():
    for i in ec2.instances.all():
        print(f"Current instance state = {i.state['Name']}")
        print(f"Instance type = {i.instance_type}")
        print(i.block_device_mappings)
        print(i.network_interfaces)
        print(f"{i.instance_id} is in the state of {i.state['Name']}")

info()