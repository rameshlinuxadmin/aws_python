import boto3

ec2 = boto3.resource('ec2')

class ec2_resource:
    def info():
        for i in ec2.instances.all():
            print(f"Current instance state = {i.state['Name']}")
            print(f"Instance type = {i.instance_type}")
            print(i.block_device_mappings)
            print(i.network_interfaces)

    def instance_start():
        for i in ec2.instances.all():
            if i.state['Name'] == 'stopped':
                i.start()
                print(f"{i.instance_id} successfully started and up and running")
            else:
                print(f"{i.instance_id} is in the state of {i.state['Name']}")
     
    def instance_stop():
        for i in ec2.instances.all():
            if i.state['Name'] == 'running':
                i.stop()
                print(f"{i.instance_id} Stop process initiated; wait for few mins")
            else:
                print(f"{i.instance_id} is in the state of {i.state['Name']}")
        
    def instance_stopping():
        for i in ec2.instances.all():
            if i.state['Name'] == 'stopping':
                print(f"{i.instance_id} Stop process already initiated; moodikitu iru")
            else:
                print(f"{i.instance_id} is in the state of {i.state['Name']}")
        
    def instance_reboot():
        for i in ec2.instances.all():
            if i.state['Name'] == 'running':
                i.reboot()
                print(f"{i.instance_id} reboot process is initiated")
                z = print(f"{i.instance_id} is {i.state['Name']}")
                return z
            else:
                print(f"{i.instance_id} is in the state of {i.state['Name']}")
        
    def instance_terminate():
        for i in ec2.instances.all():
            if i.state['Name'] == 'running' | 'stopped' | 'stopping':
                i.terminate()
                print(f"{i.instance_id} reboot process is initiated")
                z = print(f"{i.instance_id} is {i.state['Name']}")
                return z
            else:
                print(f"{i.instance_id} is in the state of {i.state['Name']}")