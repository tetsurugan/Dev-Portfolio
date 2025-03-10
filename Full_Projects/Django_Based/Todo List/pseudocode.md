📝 Pseudo-Code Breakdown for To-Do App

1️⃣ User Authentication (Optional but Recommended)
	•	Ask if the user is an existing or new user.
	•	If existing:
	•	Prompt for username and password.
	•	Check if the username exists in the database.
	•	If it exists, check if the password matches.
	•	✅ If yes, load the user’s task dashboard.
	•	❌ If no, print “Invalid username or password” and offer to retry.
	•	If new user:
	•	Prompt for a valid username (alphanumeric, cannot start with a number).
	•	Prompt for a secure password (must meet security requirements).
	•	Save the user profile in the database.

2️⃣ Task CRUD Functionality

Create Task
	•	Users can create a task.
	•	Each task should have:
	•	Title (Required)
	•	Description (Optional)
	•	Due date (Optional)
	•	Completed status (Default: False)
	•	Created timestamp (Auto-generated)
	•	Assign the task to the logged-in user.

Read Tasks
	•	Display all incomplete tasks for the logged-in user.
	•	Show completed tasks separately.

Update Task
	•	Users can:
	•	Change task title, description, or due date.
	•	Mark a task as complete (Moves to “Completed Tasks” section).

Delete Task
	•	Users can delete a task.
	•	Show a confirmation page before deletion.

3️⃣ Django App Setup
	•	Create Django project and app (todo).
	•	Create models for User and Task.
	•	Implement views for:
	•	Task list (todo_list.html)
	•	Task form (todo_form.html)
	•	Task delete confirmation (delete_task.html)
	•	Set up Django authentication:
	•	register, login, logout
	•	Configure Django templates and static files.        