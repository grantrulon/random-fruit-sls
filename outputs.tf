output "api_gateway_url" {
  description = "API Gateway endpoint URL"
  value       = "${aws_api_gateway_deployment.deployment.invoke_url}/hello"
}

output "lambda_function_name" {
  description = "Lambda function name"
  value       = aws_lambda_function.api_lambda.function_name
}