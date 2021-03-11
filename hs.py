class CellObj(object):
	def __init__(self):
		self.x = self.y = self.z = 0
		self.create_sections()
		self.build_topology()
		self.build_subsets()
		self.define_geometry()
		self.define_biophysics()

#end