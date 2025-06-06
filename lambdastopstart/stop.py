import boto3
region = '{region}'
instances = ['{instance_name}']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instance: ' + str(instances))