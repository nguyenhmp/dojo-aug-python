from django.shortcuts import render, HttpResponse, redirect
# CONTROLLER!!!
# Create your views here.
def index(request):
	if 'id' in request.session:
		pass
	else:
		request.session['id'] = 0
	import random
	word = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789') for i in range(14))
	context = {
	'random_word' : word
	}
	return render(request, 'randomword/index.html', context)

def create(request):
	if request.method == 'POST':
		import random
		word = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789') for i in range(14))
		context = {
		'random_word' : word
		}
		request.session['id'] += 1
		return redirect('/random', context)
	else:
		return redirect('/random')