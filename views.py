# -*- coding: iso-8859-15 -*-
from django.shortcuts import render_to_response
from django.http import *
from bgcomm.dict import *
from bgcomm.posts.models import *
from django.template import loader, RequestContext
from django.core.mail import send_mail
import datetime
import random
from settings import *
#from bgcomm.models import *

### HELPER FUNCTIONS
def langcheck(lg):
	"""Returns a language-specific dictionary to populate menus and common text"""
	if lg=="bg":
		return menu_bg
	elif lg=="en":
		return menu_en
	elif lg=="fr":
		return menu_fr
	else:
		return -1
		#RAISE ERROR HERE

def ad_year_context(request):
	"""Returns the dynamically updated list of years in the archive and a random selection of banner ads"""
	from django.conf import settings
	return {'years':a_years(), 'ads': update_ads(), 'aff': SIDE_MENU_ITEMS, 'MEDIA_URL': settings.MEDIA_URL}


def a_years():
	"""Returns the year values that should populate the archive menu:
	-Finds the years of the earliest and latest post in the database (not including future posts)
	- generates a full list of years between the two
	- sorts them in reverse (latest year on top of the list)
	- returns the list to be rendered in the side menu"""
	archive_years = []
	a = Post.objects.order_by("date")[0:1]
	if a.count() > 0:
		a = a[0].date.year
		b = Post.objects.exclude(date__gt=datetime.datetime.now()).order_by("-date")[0:1]
		b = b[0].date.year
		for s in range(a,b+1):
			archive_years.append(s)
		archive_years.sort()
		archive_years.reverse()
	return archive_years


def randomize(total, select):
	"""Takes two parameters: total and select.
	Returns select unique random ids in the range (0-total).
	If total < select, returns a random ordering of the range (0-select)
	Used to populate the ad banner side menu item
	"""
	retlist = []
	if total>0:
		if total<=select:
			retlist = range(total)
		else:	
			while select>0:
				select-=1;
				r = -1
				while True:
					r = random.randint(0, total-1)
					if r not in retlist:
						break
				retlist.append(r)
	return retlist

def update_ads():
	"""Returns a list of the desired number of Ad objects from among all ads in the database"""
	ads = Ad.objects.all().exclude(expirydate__lt=datetime.datetime.now()).order_by("titlebg").order_by("-image")
	dice = randomize(ads.count(), SIDEBAR_ADS)
	retads = []
	if ads.count > 0:
		for x in dice:
			retads.append(ads[x])
	return retads

def error_gen(lg):
	"""Returns a list of language-specific data validation error messages for the contact and membership forms.
	It is a bit of a hack."""
	if lg=="bg":
		return ["Моля въведете тема.", "Моля въведете съобщение.", "Моля въведете валиден e-mail адрес.", "Моля въведете Вашето име", "Моля въведете e-mail-и"]
	elif lg=="en":
		return ["Enter a subject.", "Enter a message.", "Enter a valid e-mail address.", "Please enter your name", "Please enter your e-mail(s)"]
	elif lg=="fr":
		return ["Entrez un sujet SVP.", "Entrez un message SVP.", "Entrez un courriel valide.", "Entrez votre nom", "Entrez les courriels"]
	else:
		return -1
		#RAISE ERROR HERE

### RENDERING FUNCTIONS - these are all called by a matched pattern in the urls.py file


def index(response):
	"""Renders the landing page (the Bulgarian/English/French selection page, index.html)"""
	return render_to_response('index.html')


def home_page(request, lg):
	"""Renders the home page (home.html), populating it with the latest MAX_POSTS posts, the latest MAX_EVENTS events and an optional poll"""
	
	#Get all posts before now (future posts are not rendered) and keep the latest MAX_POSTS
	post_list = Post.objects.exclude(date__gt=datetime.datetime.now()).order_by("-date")[0:max(MAX_POSTS,0)]
	#Set the summary paragraph on each (only the first paragraph of each post will be shown on the home page)
	for x in post_list:
		x.first_paragraph_bg = x.textbg[0:x.textbg.find("</p>")+4]
		x.first_paragraph_en = x.texten[0:x.texten.find("</p>")+4]
		x.first_paragraph_fr = x.textfr[0:x.textfr.find("</p>")+4]

	#Get the latest non-expired active poll
	poll_list = Poll.objects.filter(active=1).exclude(expirydate__lt=datetime.datetime.now().date()).order_by("-date")[0:1]

	#Get all events with future dates and render the most recent MAX_EVENTS
	event_list = Event.objects.exclude(date__lt=datetime.datetime.now().date()).order_by("date")[0:max(MAX_EVENTS,0)]
	
	#Render home.html, passing in the generated lists above
	return render_to_response("home.html", {'posts': post_list, 'polls': poll_list, 'events': event_list},
	context_instance = RequestContext(request, processors=[langcheck(lg)]))

def single_post(request, lg, pid):
	"""Retrieves a single post (post.html) from the database by id and renders it"""
	post = Post.objects.get(id=pid) #get post from database
	return render_to_response("post.html", {'item':post}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

	
def list_of_events(request, lg):
	"""Renders the full list of events (events.html), past and future"""
	event = Event.objects.all()
	return render_to_response("events.html", {'events':event}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def single_event(request, lg, pid):
	"""Retrieves a single event (event.html) from the database by id and renders it"""
	event = Event.objects.get(id=pid)
	return render_to_response("event.html", {'item':event}, context_instance = RequestContext(request, processors=[langcheck(lg)]))


def list_of_ads(request, lg):
	"""Renders a list of all banner ads (ads.html)"""
	ads = Ad.objects.all()
	return render_to_response("ads.html", {'adverts':ads}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def single_ad(request, lg, pid):
	"""Renders a single ad (ad.html) by id as specified in the database"""
	ad = Ad.objects.get(id=pid)
	return render_to_response("ad.html", {'item':ad}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def list_of_links(request, lg):
	"""Renders a list of links by category (links.html). Renders only categories marked visible in the language specified"""
	r = langcheck(lg)
	if r==menu_bg:
		categories = Category.objects.filter(bg=True)
	elif r==menu_en:
		categories = Category.objects.filter(en=True)
	elif r==menu_fr:
		categories = Category.objects.filter(fr=True)
	else:
		categories = None

	return render_to_response("links.html", {'cats':categories}, context_instance = RequestContext(request, processors=[langcheck(lg)]))


def single_year_archive(request, lg, year):
	"""Retrieves all the posts for the specified year from the database and renders them in descending order (archive.html)"""
	posts = Post.objects.filter(date__year=year).exclude(date__gt=datetime.datetime.now()).order_by("-date")
	return render_to_response("archive.html", {'year':year,'posts': posts}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def about_page(request, lg):
	"""Retrieves the list of community executives from the database and renders the about us page (about.html) with it"""	
	items = Executive.objects.order_by("nameen")
	return render_to_response("about.html", {'execs':items,}, context_instance = RequestContext(request, processors=[langcheck(lg)]))


def static_page(request, lg, page):
	"""Used to render most static pages.
	E.g. a URL in the form /bg/pagename will render pagename.html in Bulgarian"""
	return render_to_response(page + ".html",context_instance = RequestContext(request, processors=[langcheck(lg)]))


def send_message(request, lg):
	"""Validates the form submitted for correct formatting and sends an e-mail to the community's receiving address"""
	errors = []
	error_dict = error_gen(lg)
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append(error_dict[0])
		if not request.POST.get('message', ''):
			errors.append(error_dict[1])
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append(error_dict[2])
			
		#If the form is correct, send an e-mail and redirect to thanks page
		if not errors:
            # To be added when an e-mail server is configured: http://docs.djangoproject.com/en/dev/topics/email/
			
			#send_mail(
            #    'Site Feedback:' + request.POST['subject'],
            #    request.POST['message'],
            #    request.POST.get('email', 'noreply@example.com'),
            #    FEEDBACK_EMAILS, fail_silently=False
            #)
			return HttpResponseRedirect('/'+lg+'/thanks')

	#If form is not correct, re-render contact page with errors specified
	return render_to_response("contact.html", {'errors': errors,
	 		'subject': request.POST.get('subject', ''),
			        'message': request.POST.get('message', ''),
			        'emailaddr': request.POST.get('emailaddr', '')}, context_instance = RequestContext(request, processors=[langcheck(lg)]))


def contact_thanks_page(request, lg):
	"""Renders the feedback thanks page (thanks.html)"""
	return render_to_response("thanks.html",context_instance = RequestContext(request, processors=[langcheck(lg)]))


def membership_request(request, lg):
	"""Validates the form submitted and sends an e-mail to everyone in MEMBERSHIP_EMAIL"""
	errors = []
	error_dict = error_gen(lg)
	if request.method == 'POST':
		if not request.POST.get('name', ''):
			errors.append(error_dict[3])
		if not request.POST.get('emailaddr', ''):
			errors.append(error_dict[4])
		if not request.POST.get('email') or '@' not in request.POST['email']:
			errors.append(error_dict[2])
			
		if not errors:
            # To be added when an e-mail server is configured: http://docs.djangoproject.com/en/dev/topics/email/
			m = request.POST.get('name','') + ' requests a membership for ' + request.POST.get('memtype') + ". They wish to pay by " + request.POST.get('billtype') + " and would like the following e-mail(s) included in the Forum: " + request.POST.get('emailaddr')
			print m
			#send_mail(
            #    request.POST['Membership: ' + request.POST.get('name')],
            #    request.POST.get('name','') + ' requests a membership for ' + request.POST.get('memtype') + ". They wish to pay by " + request.POST.get('billtype') + " and would like the following e-mail(s) included in the Forum: " + request.POST.get('emailaddr'),
            #    request.POST.get('email'),
            #    MEMBERSHIP_EMAILS,
            #)
			return HttpResponseRedirect('/'+lg+'/thanks/' + request.POST.get('billtype')[0])

	return render_to_response("join.html", {'errors': errors,
	 		'name': request.POST.get('name', ''),
			        'emailaddr': request.POST.get('emailaddr', '')}, context_instance = RequestContext(request, processors=[langcheck(lg)]))

def membership_thanks_page():
	"""docstring for membership_thanks_page"""
	pass


	