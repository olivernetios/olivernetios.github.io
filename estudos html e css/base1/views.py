def base_view(request):
    if (5 == 5):
        info = 'yes'
    else:
        info = 'no'
        context = {'info' : info}
        return render(request, "base.html", context)