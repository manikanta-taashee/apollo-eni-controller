# ENI Failover Manager

`eni_failover_manager.py` is a Python script designed to monitor the health of an application and manage the failover of an Elastic Network Interface (ENI) between two AWS EC2 instances in case of application failure.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x**: Make sure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

- **AWS Credentials**: Configure your AWS credentials using the AWS CLI or by setting up the `~/.aws/credentials` file.

## Installation

1. **Clone the Repository**:

   ```bash
   https://github.com/manikanta-taashee/apollo-eni-controller.git
   cd apollo-eni-controller
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


## Usage

After configuring the script, run it using Python 3:


```bash
python3 eni_failover_manager.py
```


The script will check the application's health at the specified `application_url`. If the application is down, it will detach the ENI from its current instance and attach it to the other instance to facilitate failover.

By following the steps outlined above, you can set up and run the `eni_failover_manager.py` script to monitor your application's health and manage ENI failover between two EC2 instances as needed. 
