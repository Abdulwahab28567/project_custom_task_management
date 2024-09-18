Project Custom Task Management

Overview Project Custom Task Management is an Odoo module designed to enhance task management by adding new fields to project tasks and automating certain processes. This module introduces additional fields that are linked to each other, allowing automatic updates of field values and sending notifications when certain conditions are met. Specifically, it is designed to help businesses manage tasks that are overdue and need immediate action from the accounting team.

Features New Fields for Project Tasks: Additional fields are added to Odoo's project task model to track key metrics. 
Automatic Field Updates: If the task exceeds its due date, a field is automatically updated to "Overdue for Payment". 
Automated Notifications: When a task becomes overdue, a notification is sent via the Odoo Bot to alert the accounting department to take appropriate actions with the client.
 How it Works Task Field Addition: New fields have been added to the project task form, allowing for better tracking of due dates and payment status. 
Automatic Field Update: If a task's due date is passed without payment, the system automatically updates the task status to "Overdue for Payment". 
Odoo Bot Notification: The Odoo Bot automatically sends a notification to the accountant when a task is marked as "Overdue for Payment". The accountant is prompted to review the client's status and take necessary actions.
