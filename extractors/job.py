class Job:
	def __init__(self, company, position, region, link, reference):
		self.company = company
		self.position = position
		self.region = region
		self.link = link
		self.reference = reference

	def values(self):
		return [self.company, self.position, self.region, self.link]