import json
import boto3

f = open('requisites.json')
data = json.load(f)
ec2_client = boto3.client('ec2')

for i in data['Amazonlinux_instance']:
    print(f"AMI Image: {i['ami_image']}")
    print(f"VPC ID: {i['vpc-id']}")
    print(f"Security group ID: {i['securitygroups']}")
    print(f"Instance Type: {i['instance-type']}")
    print(f"Maximum count of Instance: {i['MaxInstanceCount']}")
    print(f"Minimum count of Instance: {i['MinInstanceCount']}")
    print(f"Key Pair: {i['keypair']}.pem")

    try:
        creation = ec2_client.run_instances(
            ImageID=i['ami_image'],
            InstanceType=i['instance-type'],
            KeyName=i['keypair'],
            MinCount=i['MinInstanceCount'],
            MaxCount=i['MaxInstanceCount'],
            SecurityGroupsIds=i['securitygroups']
        )
        print("EC2  instance created successfully")
    except Exception as e:
        print("error: ", str(e))