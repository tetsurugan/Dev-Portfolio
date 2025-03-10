from django.shortcuts import render, redirect # here we are importing shortcuts render and redirect im thinking render allows a page to be dyynamically displayed.  Redirect obviously takes you from one page and takes you to another
from django.contrib.auth.decorators import login_required  #im still getting a handle on decorators but from what it looks like with django having login_required in theory will make it so you have to log in first
from .models import Task #with it being .models it is in the same folder and we are importing the task model which are the entries on your todo list
from .forms import TaskForm #forms.py is probably a page where it has form logic TaskForm being a page where you can make forms.

@login_required
def task_list(request): # this is creating a method called task_list and in this case it has a paraemer request which idk probably is like a get post put del request?
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')# this calls the objects aka dictionary items or maybe jsonitems and it filters them im guessing by the user name and ordering them by the time they were created
    return render(request, 'todo/task_list.html', {'tasks': tasks})#im assuming the render will dynamically request task_list.html and {tasks will }print a list of the tasks from tasks variable

@login_required
def add_task(request):#you need to log in but this is add_task method and it takes your request and if it is a post method that is normally used to create new and if i recall the preferred method of updating instead of put but if it is that form is created which would be taskform from models.py  im not seeing how it makes sure its that specific task user though
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign user before saving
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

@login_required
def update_task(request, task_id):
    # Get the specific task for the logged-in user
    task = Task.objects.get(id=task_id, user=request.user)

    # If the user submits the form (POST request)
    if request.method == 'POST':
        # Create a form instance, linking it to the existing task
        form = TaskForm(request.POST, instance=task)  
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the changes to the task
            return redirect('task_list')  # Redirect back to task list
    else:
        # If it's a GET request, show the form with existing data pre-filled
        form = TaskForm(instance=task)

    return render(request, 'todo/update_task.html', {'form': form})

@login_required  # Ensures the user is logged in before accessing this function
def delete_task(request, task_id):
    """
    Deletes a task if it belongs to the logged-in user.

    Args:
        request: The HTTP request object.
        task_id: The ID of the task to be deleted.

    Process:
        - Retrieves the task with the given ID that belongs to the user.
        - If the request method is POST, the task is deleted.
        - Redirects back to the task list after deletion.
        - If the request is GET, it renders a confirmation page.
    """
    task = Task.objects.get(id=task_id, user=request.user)  # Fetches the task belonging to the logged-in user

    if request.method == 'POST':  # Confirms deletion via a POST request
        task.delete()  # Deletes the task from the database
        return redirect('task_list')  # Redirects user back to task list

    return render(request, 'todo/delete_task.html', {'task': task})  # Displays delete confirmation page


@login_required  # Requires the user to be logged in to view a task
def view_task(request, task_id):
    """
    Retrieves and displays a task if it belongs to the logged-in user.

    Args:
        request: The HTTP request object.
        task_id: The ID of the task to be viewed.

    Process:
        - Uses `get_object_or_404` to fetch the task if it exists.
        - If the task doesn’t exist for the user, it returns a 404 error.
        - Renders the 'view_task.html' template with the task data.
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Fetches task or raises a 404 error if not found

    return render(request, 'todo/view_task.html', {'task': task})  # Passes the task to the template for display