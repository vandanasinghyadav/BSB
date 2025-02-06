from django.shortcuts import render,redirect
from courses.models import Courses
from category.models import Category
from student.models import Student
def homePage(request):
     if request.method == "POST":
          username = request.POST.get('email')
          password = request.POST.get('password')
          try:
               user = Student.objects.get(stuemail=username)
               if password==user.stupassword:  # Compare hashed password
                    request.session['user_id'] = user.id
                    return redirect('dashboard')  # Replace 'home' with your desired dashboard or home page
               else:
                    return render(request, 'index.html', {'error': 'Invalid credentials.'})
          except Student.DoesNotExist:
               return render(request, 'index.html', {'error': 'Invalid credentials.'})
     return render(request,'index.html')
def dashboard(request):
     user = Student.objects.get(id=request.session['user_id'])
     course_data = Courses.objects.all()
     cat_data=Category.objects.all()
     return render(request,'dashboard.html',{'courses':course_data,'category':cat_data,'student':user})
def view_course(request,cid):
     user = Student.objects.get(id=request.session['user_id'])
     course_data=Courses.objects.get(id=cid)
     cat_data=Category.objects.all()
     return render(request,'course.html',{'cdata':course_data,'category':cat_data,'student':user})
def course_list(request,cid):
     user = Student.objects.get(id=request.session['user_id'])
     course_data=Courses.objects.filter(course_cat=cid)
     cat_data=Category.objects.all()
     return render(request,'dashboard.html',{'courses':course_data,'category':cat_data,'student':user})
def registration(request):
     if request.method == "POST":
          stu_fname = request.POST.get('stufname')
          stu_lname = request.POST.get('stulname')
          stu_email = request.POST.get('stuemail')
          stu_password = request.POST.get('stupassword')
          restu_password = request.POST.get('restupassword')
          stu_mobile = request.POST.get('stumobile')
          # Basic validation
          if not stu_fname or not stu_email or not stu_password:
               return render(request, 'registration.html', {'error': 'All fields are required!'})
          if  stu_password!=restu_password:
               return render(request, 'registration.html', {'error': 'Confirm Password Not Match'})
          # Save the data to the database
          user = Student(stufname=stu_fname, stulname=stu_lname, stuemail=stu_email,stupassword=stu_password,stumobile=stu_mobile)
          user.save()
          return redirect('signup_success')  # Redirect to a success page (create if needed)
     return render(request,'registration.html')
def signup_success(request):
    return render(request,'success.html')
def logout(request):
    request.session.flush()  # Clear the session data
    return redirect('login')  
