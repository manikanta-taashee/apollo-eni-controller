# ENI Failover Manager

`eni_failover_manager.py` is a Python script designed to monitor the health of an application and manage the failover of an Elastic Network Interface (ENI) between two AWS EC2 instances in case of application failure.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x**: Make sure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

- **AWS Credentials**: Configure your AWS credentials using the AWS CLI or by setting up the `~/.aws/credentials` file.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```


2. **Install Required Packages**:

   The required packages are listed in the `requirements.txt` file. Install them using pip:

   ```bash
   pip install -r requirements.txt
   ```


## Configuration

Before running the script, update the following parameters in `eni_failover_manager.py`:

- `network_interface_id`: Replace `'eni-xxxxxxxx'` with your ENI's ID.

- `instance_1_id`: Replace `'i-xxxxx'` with the ID of your first EC2 instance.

- `instance_2_id`: Replace `'i-xxxxx'` with the ID of your second EC2 instance.

- `application_url`: Replace `'http://localhost'` with the URL of the application you want to monitor.

For example:


```python
network_interface_id = 'eni-087be1476e95fcab6'
instance_1_id = 'i-0e274309f1446db33'
instance_2_id = 'i-020d57e4259d914a6'
application_url = 'http://43.205.175.155:8000'
```


## Usage

After configuring the script, run it using Python 3:


```bash
python3 eni_failover_manager.py
```


The script will check the application's health at the specified `application_url`. If the application is down, it will detach the ENI from its current instance and attach it to the other instance to facilitate failover.

## Important Considerations

- **Permissions**: Ensure that the AWS credentials used have the necessary permissions to describe instances, detach, and attach network interfaces.

- **Availability Zone**: Both EC2 instances and the ENI must reside in the same Availability Zone.

- **Primary ENIs**: The primary network interface of an instance cannot be detached. Ensure the ENI in question is a secondary interface.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following the steps outlined above, you can set up and run the `eni_failover_manager.py` script to monitor your application's health and manage ENI failover between two EC2 instances as needed. 
