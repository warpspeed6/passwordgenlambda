# Serverless Password Genrator

This lambda function get triggered by API Gateway based URL. When the URL is queried in the browser, it returns a randomly generated password and a Timestamp.

This can be deployed using Chalice:

$ chalice new-project app
# cd app

Clone the repository here. 

$ chalice deploy
Enter MFA code: 
Regen deployment package.
Updating IAM policy for role: app-dev
Updating lambda function: app-dev
API Gateway rest API already found: 3ojsan8vs5
Deploying to API Gateway stage: api
https://xxxxx.execute-api.ap-southeast-2.amazonaws.com/api/


Demo: When API Gateway Endpoint is queried in browser or via Curl.

$ curl https://3ojsan8vs5.execute-api.ap-southeast-2.amazonaws.com/api/

Your random password is: XXXXXXXX
You queried this at: 04:05:57.90Delivered via Lambda Function; triggered by API Gateway
