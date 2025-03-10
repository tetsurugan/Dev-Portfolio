from django.urls import path  # ✅ Import the `path` function to define URL patterns
from . import views  # ✅ Import views from the same directory

# URL patterns define which views handle different page requests
urlpatterns = [
    path('', views.task_list, name='task_list'),  # ✅ Homepage displays the task list
    path('add/', views.add_task, name='add_task'),  # ✅ Page to add a new task
    path('update/<int:task_id>/', views.update_task, name='update_task'),  # ✅ Page to update a task (requires task ID)
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # ✅ Page to delete a task (requires task ID)
    path('view/<int:task_id>/', views.view_task, name='view_task'),  # ✅ Page to view a single task's details
]

# ✅ Explanation:
# - The `urlpatterns` list tells Django which function should handle a given URL.
# - `path('', views.task_list, name='task_list')`:
#   - `' '` (empty string) means this is the **homepage**.
#   - Calls `task_list` from `views.py` to display all tasks.
# - `path('add/', views.add_task, name='add_task')`:
#   - The `/add/` URL directs to `add_task`, which allows creating a new task.
# - `path('update/<int:task_id>/', views.update_task, name='update_task')`:
#   - The `<int:task_id>` captures an **integer** from the URL and passes it to the view function.
#   - Example: `/update/3/` will call `update_task(request, task_id=3)`.
# - `path('delete/<int:task_id>/', views.delete_task, name='delete_task')`:
#   - Similar to update, but calls `delete_task`, passing the task ID.
# - `path('view/<int:task_id>/', views.view_task, name='view_task')`:
#   - Loads a specific task’s details when accessed.

