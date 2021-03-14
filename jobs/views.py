from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all().order_by('-job_pub_time')

    paginator = Paginator(jobs, 8)

    page = request.GET.get('page')
    jobs = paginator.get_page(page)


    return render(request, 'jobs/index.html', {'jobs': jobs})
