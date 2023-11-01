from django.shortcuts import redirect

def  auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        #print('middleware')
        print(request.session.get('email'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not (request.session.get('email')):
           return  redirect(f'/log-in/?return_url={returnUrl}')
        

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware