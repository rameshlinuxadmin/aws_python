import boto3

ec2 = boto3.resource('ec2')

for i in ec2.instances.all():
    if i.instance_id == "i-0520559ffb53b9724":
        print(f"Current instance state = {i.state['Name']}")
        print(f"Instance type = {i.instance_type}")
        print(i.block_device_mappings)
        print(i.network_interfaces)

    if i.state['Name'] == 'stopped':
        i.terminate()
        print(f"{i.instance_id} successfully started and up and running")
    
    elif i.state['Name'] == 'stopping':
        print(f"{i.instance_id} stop process iniatiated and wait for few mins")
    
    elif i.state['Name'] == 'running':
        i.stop()
        print(f"{i.instance_id} running")

    elif i.state['Name'] == 'terminating':
        print(f"{i.instance_id} terminated")
    else:
        #i.stop()
        print(f"{i.instance_id} instance stop process initiated")