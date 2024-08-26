# IAM Roles with S3 Access

This Python script identifies IAM roles in your AWS account that have access to Amazon S3 and exports them to a CSV file. It uses the Boto3 library to interact with the AWS Identity and Access Management (IAM) service.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [get_iam_roles_with_s3_access](#get_iam_roles_with_s3_access)
  - [save_roles_to_csv](#save_roles_to_csv)
- [License](#license)

## Prerequisites

- Python 3.x
- AWS credentials configured on your machine (e.g., via `aws configure` or by setting up a profile in `~/.aws/credentials`)
- Boto3 library installed

## Installation

1. Clone the repository or copy the script to your local machine.
2. Install the required dependencies using pip:

   ```bash
   pip install boto3

Usage
Ensure your AWS credentials are properly configured. You can specify the profile name in the script or leave it empty to use the default profile.

Run the script:

bash
Copy code
python script_name.py
After the script runs, a file named s3_access_roles.csv will be generated in the current directory, containing the list of IAM roles with S3 access.

Functions
get_iam_roles_with_s3_access()
This function retrieves all IAM roles in the AWS account and checks whether they have any attached policies that grant access to Amazon S3. It returns a list of role names with S3 access.

Parameters: None
Returns: list - A list of IAM role names with S3 access.
save_roles_to_csv(roles, filename='s3_access_roles.csv')
This function saves the list of IAM roles to a CSV file.

Parameters:
roles (list): A list of IAM role names.
filename (str): The name of the output CSV file. Default is s3_access_roles.csv.
