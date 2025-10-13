# Terraform Lambda API

A minimal Terraform project that deploys a Python Lambda function with a REST API Gateway.

## Architecture

- **Lambda Function**: Python 3.9 function that returns a JSON response
- **API Gateway**: REST API with a single GET endpoint at `/hello`
- **IAM Role**: Execution role for Lambda with basic execution permissions

## Deployment

1. Initialize Terraform:
   ```bash
   terraform init
   ```

2. Plan the deployment:
   ```bash
   terraform plan
   ```

3. Apply the configuration:
   ```bash
   terraform apply
   ```

4. Test the API:
   ```bash
   curl $(terraform output -raw api_gateway_url)
   ```

## Cleanup

```bash
terraform destroy
```