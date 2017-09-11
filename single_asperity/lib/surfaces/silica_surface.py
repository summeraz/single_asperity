import mbuild as mb
import numpy as np


class SilicaSurface(mb.Compound):
    def __init__(self):
        """Load an amorphous silica surface

        Loads an amorphous silica surface from a PDB file into an mBuild Compound.
        Ports are attached to surface oxygens for chain attachment.

        Note: This surface was generated prior to mBuild's ability to provide
              a seed for the random number generator in the SilicaInterface class.
        """
        super(SilicaSurface, self).__init__()

        mb.load('silica_surface.pdb',
                compound=self,
                relative_to_module=self.__module__)

        self.periodicity = np.array([15.0, 15.0, 0.0])

        for atom in self.particles():
            if atom.name == 'OS':
                port = mb.Port(anchor=atom, orientation=[0, 0, 1], separation=0.1)
                self.add(port, "port_{}".format(len(self.referenced_ports())))
