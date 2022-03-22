from django.http import HttpResponse

# Create your views here.
def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1  # this gets value of old cookie from session
    request.session['num_visits'] = num_visits             # this actualy revrites value of given cookie in session (<'num_visits'> was 0 now is 1)
    response = HttpResponse(f'view count={num_visits}')    # this creates http response (already learnt, basic "f" string)
    response.set_cookie('dj4e_cookie', '38b12ca2', max_age=1000)        #this adds addtional cookie with age in se
    return response