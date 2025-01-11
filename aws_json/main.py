import json #To import json program related librabries
import boto3 #To import boto3 which is used to make connection to AWS and terminal/shell/command prompt
import time

#Calling boto3 class and client and resource function of ec2
ec2_client = boto3.client('ec2') #To call the boto3 class for the client function of ec2
ec2 = boto3.resource('ec2')

#Calling the JSON file for instance creation
file =  open("requisites.json") #To open the info for instance creation
data = json.load(file) #To load info to the variable
instance = data["instances"][0] #To call the dictionary values  from the JSON file

for i in data['instances']: #To print the instance creation info in runtime
    print("******************INSTANCE CREATION INFO **********************")
    print(f"AMI Image: {i['ami_image']}")
    print(f"VPC ID: {i['vpc-id']}")
    print(f"Security group ID: {i['securitygroups']}")
    print(f"Instance Type: {i['instance-type']}")
    print(f"Maximum count of Instance: {i['MaxInstanceCount']}")
    print(f"Minimum count of Instance: {i['MinInstanceCount']}")
    print(f"Key Pair: {i['keypair']}.pem")
    print("***************************************************************")
    print("Loading.......")

try:
    creation = ec2_client.run_instances(    #To create the instance 
        ImageId=instance['ami_image'],      #AMI
        InstanceType=instance['instance-type'], #Instance Type
        KeyName=instance['keypair'],    #Keypair to be used
        MinCount=instance['MinInstanceCount'], #Minimum instance count
        MaxCount=instance['MaxInstanceCount'], #Maximum instance count
        SecurityGroupIds=instance['securitygroups'], #Security group
        DryRun=False #To check the creation, 'True' is to check the program running correctly without making any change. 'False' means it proceed with actual step
    )
    
    instance_id = creation["Instances"][0]["InstanceId"] #To get the instance id of created just now
    print(instance_id ,"EC2 instance created successfully")

except Exception as e: 
    print("error: ", str(e)) #It prints the error if throws............