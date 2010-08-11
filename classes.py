class SideMenuItem():
    def __init__(self, bg, en, fr, link):
        self.bg = bg
        self.en = en
        self.fr = fr
        self.link = link

	def text(lg):
		if lg=="bg":
			return self.bg
		elif lg=="en":
			return self.en
		elif lg=="fr":
			return self.fr
		else:
			return ""