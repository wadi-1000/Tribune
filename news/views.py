from django.shortcuts import render,redirect
from django.http import Http404,HttpResponseRedirect,HttpResponse
import datetime as dt
from .models import Article,NewsLetterRecipients
from .emails import send_welcome_email
from news.forms import NewsLetterForm
import news
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def news_of_day(request):
    date = dt.date.today()
    news=Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            print('valid')
            return HttpResponseRedirect('news_of_day')
    else:
        form = NewsLetterForm()
        return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})
        
def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_news(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    
    if date == dt.date.today():
        return redirect(news_of_day)
    return render(request, 'all-news/past-news.html', {"date": date})


    day = convert_dates(date)
   
    return HttpResponse(html)

# def news_today(request):
#     date = dt.date.today()
#     news = Article.todays_news()
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news})

# def past_days_news(request, past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     # if date == dt.date.today():
#     #     return redirect(news_today)

#     # news = Article.days_news(date)
#     # return render(request, 'all-news/past-news.html',{"date": date,"news":news})




def past_days_news(request, past_date):
    try:
        # Converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_of_day)
    day = convert_dates(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news": news})
# def news_today(request):
#     date = dt.date.today()
#     news = Article.todays_news()
#     if request.method == ‘POST’:
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data[‘your_name’]
#             email = form.cleaned_data[‘email’]
#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             HttpResponseRedirect(‘news_today’)
#     else:
#         form = NewsLetterForm()
#     return render(request, ‘all-news/today-news.html’, {“date”: date,“news”:news,“letterForm”:form})


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
        

@login_required(login_url='/accounts/login/')
def article(request,article_id):
    try:
        article = Article.objects.get(id =article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})



def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_today')
            print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})

def logout(request):
    return redirect('django_registration/login.html')

