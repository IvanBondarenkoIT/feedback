from django.shortcuts import render


# Create your views here.
def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        print(entered_username)
        return render(request,'reviews/thank_you.html')

    return render(request, 'reviews/review.html')


def thank_you(request):
    pass