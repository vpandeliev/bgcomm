from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField()
	email = forms.EmailField(required=False)
	message = forms.CharField(widget=forms.Textarea)

	def fields(lg):
		if lg="bg":
			subject.label = "Тема"
			email.label = "Вашият e-mail"
			message.label = "Съобщение"
		else if lg="en":
			subject.label = "Subject"
			email.label = "Your e-mail"
			message.label = "Message"
		else:
			subject.label = "Sujet"
			email.label = "Votre courriel"
			message.label = "Message"