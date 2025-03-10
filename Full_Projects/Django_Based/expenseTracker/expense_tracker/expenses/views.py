from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from rest_framework import generics
from .serializers import ExpenseSerializer
from django.shortcuts import get_object_or_404, redirect

# Home page
def index(request):
    return render(request, 'expenses/index.html')

# Add Expense View
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Redirect to list after adding
    else:
        form = ExpenseForm()
    
    return render(request, 'expenses/add_expense.html', {'form': form})


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect('expense_list')


def expense_list(request):
    expenses = Expense.objects.all()
    total_expenses = sum(expense.amount for expense in expenses)  # Calculate total

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_expenses': total_expenses
    })
# API: List & Create Expenses
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# API: Retrieve, Update & Delete Expense
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer