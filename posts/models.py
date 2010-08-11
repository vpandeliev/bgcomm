# -*- coding: iso-8859-15 -*-
from django.db import models
from tinymce import models as tinymce_models
import datetime
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class OverwriteStorage(FileSystemStorage):
    
    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Person(models.Model):
	namebg = models.CharField('Име (кирилица)',max_length=140)
	nameen = models.CharField('Име (латиница)',max_length=140)
	contact_email = models.EmailField('Контакт (e-mail) (optional)', blank=True)
	contact_phone = models.CharField('Контакт (phone) (optional)', blank=True, max_length=30)
	
	def __unicode__(self):
	        return u'%s' % (self.namebg)

class Member(Person):
	member_until = models.DateField('Член до', default="2010-12-31")
	paid = models.BooleanField('Платено', default=False)
	def __unicode__(self):
	        return u'Member %s - %s' % (self.nameen, self.member_until.year)
	
class Executive(Person):
	posbg = models.CharField('Длъжност (BG)', max_length=140)
	posen = models.CharField('Длъжност (EN)', max_length=140)
	posfr = models.CharField('Длъжност (FR)', max_length=140, blank=True)
	def __unicode__(self):
	        return u'Executive %s - %s' % (self.nameen, self.posen)



class Post(models.Model):
	author = models.CharField('Author', max_length=140)
	image = models.FileField('Картинка',upload_to='postimgs', storage=OverwriteStorage(), blank=True)
	titlebg = models.CharField('Title (BG)',max_length=140)
	textbg = tinymce_models.HTMLField('Text (BG)')
	titleen = models.CharField('Title (EN)',max_length=140)
	texten = tinymce_models.HTMLField('Text (EN)')
	titlefr = models.CharField('Title (FR)',max_length=140)
	textfr = tinymce_models.HTMLField('Text (FR)')
	date = models.DateTimeField('Date and time of release')
	first_paragraph_bg = None
	first_paragraph_en = None
	first_paragraph_fr = None
	def __unicode__(self):
	        return u'%s - %s' % (self.titleen, self.date)
	
	
'''	titlebg = models.CharField('Заглавие (BG)',max_length=140)
	titleen = models.CharField('Заглавие (EN)',max_length=140)
	titlefr = models.CharField('Заглавие (FR)',max_length=140)
	author = models.CharField('Автор', max_length=140)
	textbg = models.CharField('Кратък текст (BG)', max_length=3000)
	moretextbg = models.CharField('Още текст (BG) (optional)', max_length=30000, blank=True)
	texten = models.CharField('Кратък текст (EN)', max_length=3000)
	moretexten = models.CharField('Още текст (EN) (optional)', max_length=30000, blank=True)
	textfr = models.CharField('Кратък текст (FR)', max_length=3000)
	moretextfr = models.CharField('Още текст (FR) (optional)', max_length=30000, blank=True)
	date = models.DateTimeField('Дата (използвайте Today)')'''
	


class Category(models.Model):
	titlebg = models.CharField('Категория (BG)',max_length=140)
	titleen = models.CharField('Категория (EN)',max_length=140, blank=True)
	titlefr = models.CharField('Категория (FR)',max_length=140, blank=True)
	
	bg = models.BooleanField("На български", default=True)
	en = models.BooleanField("На английски", default=True)
	fr = models.BooleanField("На френски", default=True)
	def __unicode__(self):
		if self.titlebg != "":
			return u'%s' % (self.titlebg)
		elif self.titleen != "":
			return u'%s' % (self.titleen)
		elif self.titlefr != "":
			return u'%s' % (self.titlefr)
		else:
			return u''
		

	def links(self):
		return self.link_set.all()
	
class Link(models.Model):
	titlebg = models.CharField('Текст на връзката (BG)',max_length=140, blank=True)
	titleen = models.CharField('Текст на връзката (EN)',max_length=140, blank=True)
	titlefr = models.CharField('Текст на връзката (FR)',max_length=140, blank=True)
	link = models.URLField('URL')
	category = models.ForeignKey(Category)
	
	def __unicode__(self):
		if self.titlebg != "":
			return u'%s - %s' % (self.titlebg, self.link)
		elif self.titleen != "":
			return u'%s - %s' % (self.titleen, self.link)
		elif self.titlefr != "":
			return u'%s - %s' % (self.titlefr, self.link)
		else:
			return u'%s' % ("Please enter at least one link title!")

class Poll(models.Model):
	ACTIVE_CHOICES = (
        (1, 'Активна (ще се вижда на сайта)'),
        (0, 'Неактивна (няма да се вижда)'),
    )
	name = models.CharField('Вътрешно име на анкетата', max_length=140)
	code = models.CharField('Paste-нете кода от Polldaddy.com', max_length=600)
	active = models.IntegerField(max_length=1, choices=ACTIVE_CHOICES)
	date = models.DateTimeField('Дата (използвайте Today)')
	expirydate = models.DateField('Видим до дата')
 	
	def __unicode__(self):
		if self.active==1:
			r = '  --ACTIVE'
		else:
			r = ''
		if self.expirydate < datetime.datetime.now().date():
			s = '  --EXPIRED'
		else:
			s = ''
		return u'%s - %s: %s %s' % (self.name, self.date, r, s)


class Cost(models.Model):
	value = models.IntegerField('$')
	def __unicode__(self):
		return u'%s' % (self.value)

class TicketType(models.Model):
	namebg = models.CharField('Ticket Type (BG)',max_length=140)
	nameen = models.CharField('Ticket Type (EN)',max_length=140)
	namefr = models.CharField('Ticket Type (FR)',max_length=140)
	def __unicode__(self):
		return u'%s' % (self.namebg)
	


class Price(models.Model):
	category = models.ForeignKey(TicketType)
	cost = models.ForeignKey(Cost)
	
	
	def __unicode__(self):
		"""docstring for __unicode__"""
		return u'%s - %s$' % (self.category.namebg, self.cost)


		
class Event(models.Model):
	namebg = models.CharField('Title (BG)',max_length=140)
	
	descriptionbg = tinymce_models.HTMLField('Text (BG)')
	image = models.FileField('Картинка',upload_to='eventimgs', storage=OverwriteStorage(), blank=True)
	nameen = models.CharField('Title (EN)',max_length=140)
	descriptionen = tinymce_models.HTMLField('Text (EN)')
	namefr = models.CharField('Title (FR)',max_length=140)
	descriptionfr = tinymce_models.HTMLField('Text (FR)')
	location = models.CharField('Aдрес (на латиница)', max_length=400)
	cost = models.ManyToManyField(Price, blank=True, null=True)
	contact_name = models.CharField('Контакт за сведение (име на латиница)', blank=True, max_length=50)
	contact_email = models.EmailField('Контакт за сведение (e-mail) (optional)', blank=True)
	contact_phone = models.CharField('Контакт за сведение (phone) (optional)', blank=True, max_length=30)
	date = models.DateTimeField('Дата и час')
	
	def __unicode__(self):
		return u'%s - %s' % (self.namebg, self.date.date())

class Ad(models.Model):
	titlebg = models.CharField('Заглавие (BG)', max_length=140)
	titleen = models.CharField('Заглавие (EN)', max_length=140)
	titlefr = models.CharField('Заглавие (FR)', max_length=140)
	location = models.CharField('Aдрес (на латиница) (optional)', max_length=400, blank=True)
	image = models.FileField('Банер',upload_to='ads', storage=OverwriteStorage())
	largeimage = models.FileField('Графика',upload_to='ads', blank=True,storage=OverwriteStorage())
	justimage = models.BooleanField('Рекламата се състои само от графиката')
	descriptionbg = tinymce_models.HTMLField('Текст (BG)')
	descriptionen = tinymce_models.HTMLField('Текст (EN)')
	descriptionfr = tinymce_models.HTMLField('Текст (FR)')
	contact_name = models.CharField('Контакт за сведение (име на латиница)', blank=True, max_length=50)
	contact_email = models.EmailField('Контакт за сведение (e-mail) (optional)', blank=True)
	contact_phone = models.CharField('Контакт за сведение (phone) (optional)', blank=True, max_length=30)
	expirydate = models.DateField('Платена до дата')
	link = models.URLField('URL', blank=True)
	def __unicode__(self):
		return u'%s - valid until %s' % (self.titlebg, self.expirydate)