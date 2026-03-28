\# ☁️ AWS Cloud Fun Facts Generator



A full-stack serverless application built on AWS that generates witty and engaging cloud computing facts using AI.



\## 🌐 Live Demo

https://production.d267ub7bzsf10.amplifyapp.com



\## 📋 Project Overview

This project demonstrates how to connect multiple AWS services together to build a real-world serverless application. A user clicks a button and receives a fun, AI-generated cloud computing fact.



\## 🏗️ Architecture

User → AWS Amplify → API Gateway → Lambda → DynamoDB + Amazon Bedrock (Claude AI)



\## ⚙️ AWS Services Used

\- \*\*AWS Lambda\*\* — Serverless backend function (Python 3.13)

\- \*\*Amazon API Gateway\*\* — REST API endpoint to expose Lambda

\- \*\*Amazon DynamoDB\*\* — NoSQL database storing 15 cloud facts

\- \*\*Amazon Bedrock\*\* — Generative AI (Claude 3.5 Haiku) to make facts witty

\- \*\*AWS Amplify\*\* — Frontend hosting with automatic HTTPS

\- \*\*AWS IAM\*\* — Secure permissions and role management



\## 🚀 How It Works

1\. User visits the Amplify-hosted website

2\. Clicks "Generate Fun Fact" button

3\. Frontend calls the API Gateway endpoint

4\. API Gateway triggers the Lambda function

5\. Lambda fetches a random fact from DynamoDB

6\. Lambda sends the fact to Amazon Bedrock (Claude AI)

7\. Claude makes the fact witty and engaging

8\. Witty fact is returned and displayed on the website



\## 📁 Project Structure

\- `lambda\_function.py` — Lambda function code (Python)

\- `index.html` — Frontend website code (HTML/CSS/JavaScript)



\## 🛠️ Setup Instructions



\### Stage 1: Lambda + API Gateway

1\. Create Lambda function (Python 3.13) named `CloudFunFacts`

2\. Add the code from `lambda\_function.py`

3\. Create HTTP API Gateway named `FunfactsAPI`

4\. Add route: GET /funfact → CloudFunFacts Lambda



\### Stage 2: DynamoDB

1\. Create DynamoDB table named `CloudFacts` with partition key `FactID`

2\. Add 15 cloud facts with attributes `FactID` and `FactText`

3\. Attach `AmazonDynamoDBReadOnlyAccess` policy to Lambda IAM role



\### Stage 3: Amazon Bedrock (GenAI)

1\. Request access to Claude 3.5 Haiku in Amazon Bedrock

2\. Attach `AmazonBedrockFullAccess` policy to Lambda IAM role

3\. Update Lambda code to call Bedrock and make facts witty



\### Stage 4: AWS Amplify Frontend

1\. Create `index.html` with the frontend code

2\. Update API\_URL with your API Gateway endpoint

3\. Deploy to AWS Amplify using drag and drop



\## 💡 Key Concepts Learned

\- Serverless architecture with AWS Lambda

\- REST API design with API Gateway

\- NoSQL database management with DynamoDB

\- Generative AI integration with Amazon Bedrock

\- Frontend hosting with AWS Amplify

\- IAM roles and least privilege security principle

\- CORS configuration for cross-origin requests



\## 📸 Screenshots

!\[Cloud Fun Facts App](screenshot.png)



\## ⚠️ Cost

\- Lambda, API Gateway, DynamoDB, Amplify → AWS Free Tier

\- Amazon Bedrock → Minimal cost per API call (fractions of a cent)

