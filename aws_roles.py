import boto3
import csv

def get_iam_roles_with_s3_access():
    session = boto3.Session(profile_name='')
    iam_client = session.client('iam')
    
    roles = iam_client.list_roles()['Roles']
    
    s3_access_roles = []
    
    for role in roles:
        
        role_name = role['RoleName']
        # print(role_name)
        policies = iam_client.list_attached_role_policies(RoleName=role_name)['AttachedPolicies']
        
        for policy in policies:
            
            policy_arn = policy['PolicyArn']
            policy_details = iam_client.get_policy(PolicyArn=policy_arn)['Policy']
            policy_version = iam_client.get_policy_version(
                PolicyArn=policy_arn,
                VersionId=policy_details['DefaultVersionId']
            )['PolicyVersion']
            
            if 'Document' in policy_version and 'Statement' in policy_version['Document']:
                statements = policy_version['Document']['Statement']
                if not isinstance(statements, list):
                    statements = [statements]
                    
                for statement in statements:
                    if 'Action' in statement and 's3:' in str(statement['Action']):
                        s3_access_roles.append(role_name)
                        break
    
    return s3_access_roles

def save_roles_to_csv(roles, filename='s3_access_roles.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Role Name'])
        for role in roles:
            writer.writerow([role])
    print(f"Roles with S3 access have been saved to {filename}")

if __name__ == '__main__':
    roles_with_s3_access = get_iam_roles_with_s3_access()
    save_roles_to_csv(roles_with_s3_access)