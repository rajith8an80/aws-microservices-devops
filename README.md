
# AWS Microservices DevOps Project

## Project Overview
This project demonstrates Git-based source control management and CI/CD automation for deploying three microservices to AWS.

## Microservices

### User Service
- Framework: Python Flask
- Port: 5001
- API Endpoint: /users

### Product Service
- Framework: Python Flask
- Port: 5002
- API Endpoint: /products

### Order Service
- Framework: Python Flask
- Port: 5003
- API Endpoint: /orders

## Technologies Used
- Git and GitHub
- Python and Flask
- Docker
- Jenkins
- AWS
- Kubernetes

## Branching Strategy
- main: Production-ready code
- develop: Development integration
- feature/*: Individual development changes
- release/*: Release preparation

## CI/CD Workflow
GitHub -> Jenkins -> Build -> Test -> Docker -> AWS Deployment

## Security
Sensitive credentials and private keys must not be committed to GitHub.

Webhook integration testing completed.
