import requests
import boto3
import time

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name='ap-south-1')

# Parameters
network_interface_id = 'eni-xxxxxxxx'
instance_1_id = 'i-xxxxx'
instance_2_id = 'i-xxxxx'
application_url = 'http://localhost'

# Function to check application status
def check_application_status(url):
    try:
        response = requests.get(url, timeout=10)
        print("Application Status Code ", response.status_code)
        print("Application is Up and Running.")
        return True
    except requests.RequestException as error:
        print(f"Error accessing application: {error}")
        return False

# Function to get the current attachment of the ENI
def get_eni_attachment(eni_id):
    try:
        response = ec2_client.describe_network_interfaces(NetworkInterfaceIds=[eni_id])
        network_interface = response['NetworkInterfaces'][0]
        attachment = network_interface.get('Attachment')
        if attachment:
            instance_id = attachment['InstanceId']
            print(f"ENI {eni_id} is currently attached to instance {instance_id}.")
            return instance_id
        else:
            print(f"ENI {eni_id} is not attached to any instance.")
            return None
    except Exception as e:
        print(f"Error retrieving ENI attachment: {e}")
        return None

# Function to detach the ENI from its current instance
def detach_eni(eni_id):
    try:
        response = ec2_client.describe_network_interfaces(NetworkInterfaceIds=[eni_id])
        attachment = response['NetworkInterfaces'][0].get('Attachment')

        if attachment:
            attachment_id = attachment['AttachmentId']
            ec2_client.detach_network_interface(AttachmentId=attachment_id, Force=True)
            print(f"Detaching ENI {eni_id} from instance {attachment['InstanceId']}...")

            # Wait for the ENI to become available
            while True:
                response = ec2_client.describe_network_interfaces(NetworkInterfaceIds=[eni_id])
                status = response['NetworkInterfaces'][0]['Status']
                if status == 'available':
                    print(f"ENI {eni_id} is now available.")
                    break
                time.sleep(2)
        else:
            print(f"ENI {eni_id} is not attached to any instance.")
    except Exception as e:
        print(f"Error detaching ENI: {e}")

# Function to attach the ENI to the specified instance
def attach_eni(eni_id, instance_id):
    try:
        # Determine the next available device index on the target instance
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        network_interfaces = response['Reservations'][0]['Instances'][0]['NetworkInterfaces']
        device_indices = [int(eni['Attachment']['DeviceIndex']) for eni in network_interfaces]
        next_index = max(device_indices) + 1 if device_indices else 1

        # Attach the ENI
        ec2_client.attach_network_interface(
            NetworkInterfaceId=eni_id,
            InstanceId=instance_id,
            DeviceIndex=next_index
        )
        print(f"Attaching ENI {eni_id} to instance {instance_id} at device index {next_index}.")
    except Exception as e:
        print(f"Error attaching ENI: {e}")

# Main logic
if not check_application_status(application_url):
    current_instance_id = get_eni_attachment(network_interface_id)

    if current_instance_id:
        # Determine the target instance
        target_instance_id = instance_2_id if current_instance_id == instance_1_id else instance_1_id

        # Detach from the current instance
        detach_eni(network_interface_id)

        # Attach to the target instance
        attach_eni(network_interface_id, target_instance_id)
    else:
        print("ENI is not currently attached to any instance.")
else:
    print("No action required as the application is running.")

# For Testing
# print(check_application_status(url="http://localhost:8000"))
