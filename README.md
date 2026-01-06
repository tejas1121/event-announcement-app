# Event Announcement App (Serverless AWS Project)

A fully serverless **Event Announcement System** built using AWS.  
Admins can create events, store them in DynamoDB, notify subscribers via email, and display events on a clean frontend UI.

---

## 🚀 Project Overview
This project solves the problem of **event notifications** for organizations without maintaining any servers.  
Users can create events, and subscribers automatically receive email notifications.

The frontend is hosted on **Amazon S3**, while the backend uses **AWS Lambda**, **API Gateway**, **DynamoDB**, and **SNS**.

---

## 🧩 Features
- Create events via a user-friendly frontend
- Fetch and display upcoming events
- Store events in **DynamoDB**
- Send email notifications to subscribers via **SNS**
- Fully serverless backend
- Clean architecture with separation of frontend and backend

---

## 🏗️ Architecture

**Flow:**
1. User submits an event through the frontend
2. API Gateway triggers AWS Lambda
3. Lambda stores the event in DynamoDB
4. Lambda publishes the event message to SNS
5. Subscribers receive email notifications

**AWS Services Used:**
- **AWS Lambda** – Serverless backend functions
- **API Gateway** – REST API endpoints
- **DynamoDB** – NoSQL database for storing events
- **SNS** – Email notifications
- **S3** – Frontend static website hosting
- **IAM** – Permissions and security

---

## 📁 Project Structure

