# 🐍 Flask App – AWS CodeBuild Setup Guide

This guide explains how to set up an **AWS CodeBuild project** for your Flask application.

---

## 🚀 Steps to Create an AWS CodeBuild Project

### Step 1: Log in to AWS Management Console
1. Go to the **AWS Management Console**.  
2. Navigate to **CodeBuild** in the AWS console.  

---

### Step 2: Create a New CodeBuild Project
1. In the **AWS CodeBuild dashboard**, click **Create project**.  

---

### Step 3: Configure the Project
- **Project Name**: Enter a name for your project (e.g., `FlaskAppBuild`).  
- **Source Provider**: Choose **GitHub** and authenticate your GitHub account.  
  - You’ll be redirected for authentication.  
  - Enter your **personal access token**.  
- **Repository**: Select the repository where you pushed your Flask app code.  

**Build Environment**:
- **Environment image**: Select **Managed image**.  
- **Operating system**: Choose **Amazon Linux**.  
- **Runtime**: Choose **Standard**.  
- **Image**: Select the prepopulated default (appropriate image).  
- **Service role**: Create a new role or use an existing IAM role with sufficient permissions for CodeBuild.  
- **Buildspec**: Choose **Use the buildspec.yml in the source code root directory** (you already created this in your Flask app).  

---

### Step 4: Add Artifacts (Optional)
You can specify where to store build artifacts.  
For a simple project like this, you can leave the defaults.

---

### Step 5: Create the Project
Click **Create build project** to finish creating the AWS CodeBuild project.  

---

## ▶️ Start a Build in AWS CodeBuild

### Step 1: Start a Build
1. Go back to the **CodeBuild Dashboard**.  
2. Select your newly created project (e.g., `FlaskAppBuild`).  
3. Click **Start build**.  

### Step 2: Monitor the Build
- Track the progress in the **Build details** section.  
- When the build completes, review the logs to ensure the process ran correctly.  

---

## 📦 Next Steps – CodeDeploy
Once the build succeeds:  
- You can deploy the Flask app using AWS services such as:  
  - **AWS Elastic Beanstalk**  
  - **AWS EC2**  

---
