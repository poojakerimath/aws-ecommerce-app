# AWS Ecommerce App 
*A 3-Tier, Highly Available E-Commerce Application Deployed with ECS Fargate*

![Architecture](docs/architecture-v1.png)

---

## 📌 Project Overview
This project demonstrates a production-ready e-commerce application deployed on AWS. 
The goal was to design a scalable, secure, and monitored 3-tier architecture using core AWS services.

*Key Highlights:*
- Migrated from EC2 to serverless *ECS Fargate* for zero server management
- Implemented CI/CD with *GitHub Actions*
- Built for *High Availability* across 2 Availability Zones

---

## 🏗️ Architecture
                    +-------------------+
                    |       Users       |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |     Amazon Route 53|
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |    Amazon CloudFront|
                    +---------+---------+
                              |
                +-------------+-------------+
                |                           |
                v                           v
      +-------------------+       +-------------------+
      |   Frontend (S3)    |       | Application Load  |
      |  HTML/CSS/React    |       |     Balancer      |
      +-------------------+       +---------+---------+
                                            |
                                            v
                                  +-------------------+
                                  |     EC2 Instance  |
                                  |  Backend (Spring  |
                                  |  Boot/Node.js)    |
                                  +---------+---------+
                                            |
                    +-----------------------+-----------------------+
                    |                                               |
                    v                                               v
          +-------------------+                         +-------------------+
          |     Amazon RDS    |                         |      Amazon S3    |
          | (MySQL/PostgreSQL)|                         |  Product Images   |
          +-------------------+                         +-------------------+

                                            |
                                            v
                                  +-------------------+
                                  |   Amazon Cognito  |
                                  | Authentication    |
                                  +-------------------+

                                            |
                                            v
                                  +-------------------+
                                  | Amazon CloudWatch |
                                  |     Monitoring    |
                                  +-------------------+

---

## 🛠️ AWS Services Used

| Service | Purpose |
| --- | --- |
| *VPC* | Network isolation with Public + Private subnets across 2 AZs |
| *ALB* | Distribute traffic and perform health checks |
| *ECS Fargate* | Run Docker containers without managing EC2 servers |
| *RDS MySQL Multi-AZ* | Managed database with automatic failover |
| *S3 + CloudFront* | Store and deliver product images with low latency |
| *SQS + SNS* | Decouple order processing and send email notifications |
| *CloudWatch* | Metrics, Logs, Alarms, and Dashboard |
| *CloudTrail* | Audit API calls for security and compliance |
| *Route53 + ACM* | Custom domain name with HTTPS |
| *ECR + GitHub Actions* | CI/CD pipeline for automated deployments |

---

## ✅ Requirements

### Functional Requirements
1.  Product Catalog: Users can view products with images
2.  Add to Cart: Users can add products to cart
3.  Place Order: Orders are stored in RDS
4.  Notifications: Email sent to admin on new order via SNS
5.  Image Storage: Product images stored in S3 and delivered via CloudFront

### Non-Functional Requirements
1.  *High Availability*: Multi-AZ deployment for app and database
2.  *Scalability*: Auto Scaling for ECS Fargate based on CPU
3.  *Security*: Application in private subnet. Only ALB is public
4.  *Monitoring*: CloudWatch Alarms for CPU > 70% and 5xx errors

---

## 🚀 Tech Stack
- *Backend*: Python Flask
- *Database*: MySQL 8.0
- *Containerization*: Docker
- *CI/CD*: GitHub Actions
- *Frontend*: HTML, CSS, Bootstrap

---

## 📂 Project Structure
aws-ecommerce-app/
│
├── app/
│
├── docs/
│
├── .github/
│   └── workflows/
│
├── Dockerfile
│
├── cloudformation.yaml
│
└── README.md

---

## ⚡ How to Deploy
1.  *Prerequisites*: AWS Account, Docker, Git
2.  *Step 1*: Create VPC and Networking - See docs/day1-vpc.png
3.  *Step 2*: Push Docker image to ECR
4.  *Step 3*: Deploy to ECS Fargate
5.  *Step 4*: CI/CD: Push to main branch triggers GitHub Actions

---

## 📈 What I Learned
- Designing HA architecture in AWS
- Containerizing and deploying apps with ECS Fargate
- Implementing CI/CD for cloud applications
- Using CloudWatch for monitoring and alerting
---

---

## 🚀 Implementation Journey

### Phase 1 - VPC & Networking
- Created custom VPC with CIDR 10.0.0.0/16 for isolated networking
- Created 2 public subnets across 2 different Availability Zones for high availability
- Attached Internet Gateway for public access
- Created Security Group allowing inbound traffic on port 5000 and 80
- Verified VPC and subnets in console

**Screenshots:** `docs/vpc.png`, `docs/subnet.png`, `docs/security-group.png`

---

### Phase 2 - RDS Database
- Created DB subnet group using the 2 subnets from Phase 1
- Launched MySQL RDS instance in private subnet for security
- Connected RDS to VPC security group for controlled access
- Disabled public access to keep database private
- Verified database is running and connected

**Screenshot:** `docs/rds.png`

---

### Phase 3 - Docker & ECR
- Built custom Docker image named ecommerce-app from Dockerfile
- Created private ECR repository named ecommerce-app in us-east-1
- Tagged local image with ECR repository URI
- Pushed image to ECR successfully
- Verified image is available in ECR console as latest tag

**Screenshots:** `docs/docker-build.png`, `docs/ecr-repo.png`, `docs/ecr-push.png`

---

### 📦 Final Output
- ECR Image: `578620462075.dkr.ecr.us-east-1.amazonaws.com/ecommerce-app:latest`
- All proof stored in `docs/` folder
- Application runs on port 5000

## 👩‍💻 Author
Girija
AWS Cloud Engineer | 2 Years Experience
LinkedIn: [https://www.linkedin.com/in/girija-kerimath/] | Email: poojakerimath797@gmail.com