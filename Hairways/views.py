from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import UpdateView
from django.core.files.storage import FileSystemStorage
from Hairways.forms import SignUpForm
from Hairways.models import Users
from Hairways.models import Salons
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):

    items = Salons.objects.all()
 # for pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items,10)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'salons': salons})


def faqs(request):
    return render(request, "faqs.html")


def about(request):
    return render(request, "about.html")


class SignUpcreateView(UpdateView):
    model = Users
    form_class = SignUpForm
    template_name = 'Hairways/signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    return render(request, "dashboard/dashboard.php")


def user(request):
    return render(request, "dashboard/user.php")


def productsServices(request):
    return render(request, "dashboard/productsServices.php")


def staffClients(request):
    return render(request, "dashboard/staffClients.php")


def map(request):
    return render(request, "dashboard/map.php")


def calendar(request):
    return render(request, "dashboard/calendar.php")


def upgrade(request):
    return render(request, "dashboard/upgrade.php")


def pricing(request):
    return render(request, "pricing.html")


def moreinfo(request):
    return render(request, "moreinfo.php")


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


#   TO BE RIVIEWWD DISPLAYS IMAGES
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'book_list.html', {
#         'books': books
#     })
#
#
# def delete_book(request, pk):
#     if request.method == 'POST':
#         book = Book.objects.get(pk=pk)
#         book.delete()
#     return redirect('book_list')
#
#
# class BookListView(ListView):
#     model = Book
#     template_name = 'class_book_list.html'
#     context_object_name = 'books'
