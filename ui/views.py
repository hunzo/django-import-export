from django.shortcuts import render, redirect
from .forms import CodeForm
# from .models import CodeModels


def Home(request):
    
    if request.method == "POST":
        form = CodeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("home")
        print("not valid") 
        return redirect("home")

    context = {
        "form": CodeForm()
    }

    

    return render(request, "index.html", context)
