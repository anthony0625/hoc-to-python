class CellObj(object):
	def __init(self):
	        self.x = self.y = self.z = 0
        	self.create_sections()
	        self.build_topology()
        	self.build_subsets()
	        self.define_geometry()
        	self.define_biophysics()
	def create_sections(self):
        """Create the sections of the cell."""
        self.soma1 = h.Section(name='soma1', cell=self)
        self.dend = h.Section(name='dend', cell=self)
        #self.axon = h.Section(name='axon', cell=self)
    #
    def build_topology(self):
        """Connect the sections of the cell to build a tree."""
        self.dend.connect(self.soma1(1))
        
    #
    def define_geometry(self):
        """Set the 3D geometry of the cell."""
        self.soma1.L = self.soma1.diam = 12.6157 # microns
        self.dend.L = 200                      # microns
        self.dend.diam = 1                     # microns
        self.dend.nseg = 5
        self.shape_3D()    #### Was h.define_shape(), now we do it.
    #
    def define_biophysics(self):
        """Assign the membrane properties across the cell."""
        for sec in self.all: # 'all' exists in parent object.
            sec.Ra = 100    # Axial resistance in Ohm * cm
            sec.cm = 1      # Membrane capacitance in micro Farads / cm^2
        # Insert active Hodgkin-Huxley current in the soma
        self.soma1.insert('hh')
        for seg in self.soma1:
            seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
            seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
            seg.hh.gl = 0.0003    # Leak conductance in S/cm2
            seg.hh.el = -54.3     # Reversal potential in mV
        # Insert passive current in the dendrite
        self.dend.insert('pas')
        for seg in self.dend:
            seg.pas.g = 0.001  # Passive conductance in S/cm2
            seg.pas.e = -65    # Leak reversal potential mV
    #
    def build_subsets(self):
        """Build subset lists. For now we define 'all'."""
        self.all = h.SectionList()
        self.all.wholetree(sec=self.soma1)