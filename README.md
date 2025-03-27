# flask-app

# Steps to Create an AWS CodeBuild Project
Step 1: Log in to AWS Management Console
Go to the AWS Management Console.
Navigate to CodeBuild in the AWS console.
Step 2: Create a New CodeBuild Project
In the AWS CodeBuild dashboard, click Create project.
Step 3: Configure the Project
Project Name: Enter a name for your project, like FlaskAppBuild.
Source Provider: Choose GitHub and authenticate your GitHub account if you haven’t already.


It takes you to another for authentication

Enter your personal access token
Repository:then Select the repository where you pushed your Flask app code.
Build Environment:
Environment image: Select Managed image.
Operating system: Choose Amazon Linux.
Runtime: Choose Standard.
Image: Choose an appropriate image, this is prepopulated by default
Service role: Create a new role or use an existing role with sufficient permissions for CodeBuild.
Buildspec: Choose Use the buildspec.yml in the source code root directory (since you already created the buildspec.yml in your Flask app).
Step 4: Add Artifacts (Optional)
You can specify where to store build artifacts, but this step is optional for a simple project like this. You can leave it as the default.
Step 5: Create the Project
Click Create build project to finish creating the AWS CodeBuild project.



3. Start a Build in AWS CodeBuild
Step 1: Start a Build
After creating the project, go back to the CodeBuild Dashboard.
Select your newly created project (e.g., FlaskAppBuild).
Click on Start build.
Step 2: Monitor the Build
You can monitor the progress of your build in the Build details section.
When the build is complete, you can check the logs to ensure the process ran correctly.

4. Next Steps - CodeDeploy
If everything went well, AWS CodeBuild should now have successfully built your Flask app.
You can deploy the app using AWS services like AWS Elastic Beanstalk or AWS EC2.
