from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	if 'run' in request.session:
		pass
	else:
		request.session['run'] = 0
	return render(request, 'index.html')

def results(request):
	return render(request, 'results.html')

def process(request):
	if request.method == 'POST':
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		if request.POST['comment']:
			request.session['comment'] = request.POST['comment']
		else:
			request.session['comment'] = None
		request.session['run'] += 1
		return redirect('/survey/results')
	else:
		return redirect('/survey')
