import xlsxwriter as xl

class wc(object):
	'''Workbook Container object to store workbook related metadata'''

	def __init__(self, xlsx_workbook):
		self.workbook = xlsx_workbook
		self.formats = {}
		self.worksheets = {}




	class wsc(object):
		'''Worksheet Container object to store worksheet related metadata:'''

		def __init__(self, xlsx_worksheet):
			self.worksheet = xlsx_worksheet
			self.columns = {}
			self.data = {}



	class dc(object):
		'''Data container to store table/text metadata'''






