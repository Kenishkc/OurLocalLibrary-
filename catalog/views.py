from django.shortcuts import render ,redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages 
from library.models import UserProfile
from django.http import JsonResponse
from datetime import date
from django.contrib.auth.decorators import login_required


from library.models import Book, Author, BookInstance, Genre , BorrowedBook  

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    books=Book.objects.all()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'books':books,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def register(request):
    if request.method == "POST":
         form = UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
             
            login(request,user)
            messages.success(request,("Registration Success"))
            return redirect('home') 
    else:
        form = UserCreationForm()
               
        
    return render(request, 'register.html',{
    'form':form,
    })
    
def login_user(request):
    if request.method =="POST":
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request,username=username,password=password)
     if user is not None:
        login(request,user)
        messages.success(request,("Sucessfully Login"))
        return redirect('home')
     else:
      messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html')    

def logout_user(request):
    logout(request)
    messages.success(request,("You are logout"))
    return redirect('home')

def addprofile(request):
    return render(request,'addprofile.html')

def profile(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            borrow_book = BorrowedBook.objects.filter(user=request.user)
        except UserProfile.DoesNotExist:
            # Handle the case where the profile doesn't exist
            
           return redirect('add_profile')
        print(borrow_book)
        return render(request, 'profile.html', {'profile': profile,
                                                'borrowbook':borrow_book})
    else:
        return redirect('login_user')
 
def saveprofile(request):
    if request.method == "POST":
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.firstname = request.POST.get('firstname')
        profile.lastname = request.POST.get('lastname')
        profile.email = request.POST.get('email')
        profile.bio = request.POST.get('bio')
        profile.mobile_number = request.POST.get('mobile_number')
        profile.gender = request.POST.get('gender')
        profile.address = request.POST.get('address')
        profile.profile_picture = request.FILES.get('profile_picture')  # Corrected line
        profile.save()
        return render(request, 'profile.html', {'profile': profile})
        
         
def editprofile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'editprofile.html', {'profile': profile})
        
        
def updateprofile(request):
     if request.method == "POST":
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.firstname = request.POST.get('firstname')
        profile.lastname = request.POST.get('lastname')
        profile.email = request.POST.get('email')
        profile.bio = request.POST.get('bio')
        profile.mobile_number = request.POST.get('mobile_number')
        profile.gender = request.POST.get('gender')
        profile.address = request.POST.get('address')
        # Check if a new profile picture is uploaded
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        profile.save()
        return render(request, 'profile.html', {'profile': profile})            
    
    
def bookdetails(request,id):
    book = Book.objects.get(id=id)
    
    return render(request,'bookdetails.html',{'book':book})


def borrow_book(request, book_instance_id):
    if request.method == 'POST':
        book_instance = get_object_or_404(BookInstance, id=book_instance_id)
        if book_instance.status == 'a':
            due_date = request.POST.get('due_date')  # Get the due_date from POST data

            if due_date:
                borrowed_book = BorrowedBook(user=request.user, book_instance=book_instance,borrowed_date=date.today(), due_date=due_date)
                borrowed_book.save()

                # Update the book instance status
                book_instance.status = 'o'  # Assuming 'o' represents "On Loan"
                book_instance.save()

                  # Set a success message
                messages.success(request, 'Book borrowed successfully.')

                return redirect('/profile/')  # Redirect to the profile page
            else:
                messages.error(request, 'Due date is missing or invalid.')
                return JsonResponse({'error': 'Due date is missing or invalid'})
        else:
            messages.error(request, 'Book is not available for borrowing.')
            return JsonResponse({'error': 'Book is not available for borrowing'})