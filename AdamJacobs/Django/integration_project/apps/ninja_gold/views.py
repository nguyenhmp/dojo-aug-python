from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	if 'score' in request.session:
		pass
	else:
		request.session['score'] = 0
	if 'list' in request.session:
		pass
	else:
		request.session['list'] = []
	return render(request, 'ninja_gold/index.html')

def process_money(request, building):
	import random
	from time import localtime, strftime
	if building == 'farm':
		rando = random.randint(10,20)
		request.session['score'] += rando
		time = time = strftime("%b, %d %Y %I:%M %p", localtime())
		sentence = 'Earned {} gold from the {} {}'.format(rando, building, time)
		color = 'green'
		request.session['list'].insert(0, {'text':sentence, 'color':color})
	if building == 'cave':
		rando = random.randint(5,10)
		request.session['score'] += rando
		time = time = strftime("%b, %d %Y %I:%M %p", localtime())
		sentence = 'Earned {} gold from the {} {}'.format(rando, building, time)
		color = 'green'
		request.session['list'].insert(0, {'text':sentence, 'color':color})
	if building == 'house':
		rando = random.randint(2,5)
		request.session['score'] += rando
		time = time = strftime("%b, %d %Y %I:%M %p", localtime())
		sentence = 'Earned {} gold from the {} {}'.format(rando, building, time)
		color = 'green'
		request.session['list'].insert(0, {'text':sentence, 'color':color})
	if building == 'casino':
		rando = random.randint(-50,50)
		request.session['score'] += rando
		time = time = strftime("%b, %d %Y %I:%M %p", localtime())
		if rando >= 0:
			sentence = 'Earned {} gold from the {} {}'.format(rando, building, time)
			color = 'green'
			request.session['list'].insert(0, {'text':sentence, 'color':color})
		if rando < 0:
			sentence = 'Lost {} gold from the {}...ouch {}'.format(rando, building, time)
			color = 'red'
			request.session['list'].insert(0, {'text':sentence, 'color':color})
	print request.session['list']
	return redirect(reverse('ninjagold'))


