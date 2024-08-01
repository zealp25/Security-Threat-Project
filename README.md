Security Test for Threat Analysis
1. Introduction
The project includes setting up a secure development environment on GitHub, defining security thresholds, and setting up a notification system to alert in case of potential threats.
2. Project Objectives
The primary objectives of this project were:
•
To set up a repository with code files and branches.
•
To store the code securely and ensure only authorized access.
•
To define and implement safety thresholds to monitor repository activities.
•
To set up a notification system that alerts the team in case of security breaches or other threats.
3. Setup and Configuration
3.1 Set of Files / Code Branches
•
Repository Name: Security-Threat-Project
•
Main Branch: main
•
Additional Branches: Table, UI
•
Files Added:
o
Table
o
UI
3.2 Storage of Files
•
The repository is hosted on GitHub and is configured with branch protection rules to ensure the integrity and security of the code.
3.3 Secure Access for Programmers
•
Three programmers were added as collaborators with restricted permissions to ensure secure access.
•
Collaborators Added:
o
KAVAL42, Nikunjrajput26 , zpatel14
•
Two-factor authentication (2FA) was enforced to add an additional layer of security.
4. Defining Safety Thresholds
4.1 Branch Protection Rules
•
Branch: main
•
Protection Rules:
o
Pull request reviews are required before merging.
o
Status checks must pass before a pull request can be merged.
o
A minimum of one approving review is required.
o
Allow force push to specific person
4.2 Code Scanning and Status Checks
A simple Python syntax check was implemented to ensure that all Python files in the repository are free from syntax errors.
•
Workflow File: .github/workflows/python-syntax-check.yml
•
Key Features:
o
Triggers on push and pull request events targeting the main branch.
o
Runs a Python syntax check using the command python -m compileall ..
o
Scheduled to run weekly on Sundays.
4.3 Testing and Results
•
The workflow was tested by pushing code to the main branch and opening a pull request.
•
The syntax check ran successfully, verifying the correctness of the Python code in the repository.
•
No syntax errors were detected, and the workflow completed without issues.
5. Notifications
5.1 Email Notification Setup
An email notification system was implemented to send alerts when code is pushed to the main branch.
•
Workflow File: .github/workflows/email-notification.yml
•
Notification Details:
o
Emails are sent using the dawidd6/action-send-mail@v3 GitHub Action.
o
Notifications are triggered on push events to the main branch.
o
Recipients receive an email alert with the subject "Notification: Code Pushed to Main" and details of the push event.
5.2 Testing and Results
•
The notification system was tested by pushing code to the main branch.
•
An email was successfully sent to the specified recipients, confirming that the system is functioning correctly.
Repository Link
Security-Threat-Project
