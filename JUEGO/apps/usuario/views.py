from django.shortcuts import render,render_to_response
from django.template import RequestContext

# Create your views here.
def pajina_principal(request):
	return render_to_response("blog/principal.html",{},context_instance=RequestContext(request))