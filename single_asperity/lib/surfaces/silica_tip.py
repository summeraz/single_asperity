import mbuild as mb
import numpy as np


class SilicaTip(mb.Compound):
    """ """
    def __init__(self):
        super(SilicaTip, self).__init__()

        mb.load('silica_tip-2nm.pdb',
                compound=self,
                relative_to_module=self.__module__)
        self.periodicity = np.array([0.0, 0.0, 0.0])
        self.spin(np.pi, around=[1, 0, 0])

        for atom in self.particles():
            if atom.name == 'OS':
                port = mb.Port(anchor=atom, orientation=[0, 0, 1], separation=0.1)
                self.add(port, "port_{}".format(len(self.referenced_ports())))

if __name__ == "__main__":
    tip = SilicaTip(2) 
