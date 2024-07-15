from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def Student(models.Model):
    name = name.charField(max_length=100)
    age = age.IntegerField()
    email = email.EmailField()
    contact = contact.IntegerField()
    # return render(request, 'home/student.html', {'name': name, 'age': age, 'email': email, 'contact': contact})