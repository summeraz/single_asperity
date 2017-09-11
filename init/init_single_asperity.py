'''
#### Imports ####
'''
import os
from pkg_resources import resource_filename

import mbuild as mb
from mbuild.examples.alkane_monolayer.alkylsilane import AlkylSilane
from mbuild.lib.atoms import H
from mbuild.recipes import Monolayer
import numpy as np

from single_asperity.recipes import DualSurface, Planar, Tip
from single_asperity.lib.patterns import PlanarPattern

'''
#### Define system parameters ####
'''
# Number of carbons per chain
chainlength = 18

# Force field file
forcefield = 'oplsaa.xml'

# Density of chains (chains / nm^2)
density = 2.0

'''
#### Build the system ####
'''
# Create prototype for a single chain
chain = AlkylSilane(chainlength)

# Load pattern positions from file
planar_pattern = PlanarPattern(density=density)

# Create monolayer-coated surface
planar_monolayer = Planar(chain, backfill=H(), pattern=planar_pattern)

# Create hemispherical silica tip with radius=2nm
tip = Tip(chains=H(), guest_port_name='up')

# Shift tip to the center of the monolayer
tip.translate_to([planar_monolayer.center[0], planar_monolayer.center[1],
                  tip.center[2]])

# Combine the tip and monolayer-coated surface into a single system
single_asperity = DualSurface(tip, planar_monolayer)

'''
#### Save the system ####
'''
# Define box dimensions
box = mb.Box(mins=np.array([0.0, 0.0, -0.2]), maxs=np.array([15.0, 15.0, 10.0]))

# Save as PDB structure and LAMMPS data format
forcefield_dir = resource_filename('single_asperity', 'lib/forcefields')
system_name = 'single-asperity-c{}-{}density'.format(chainlength, density)
single_asperity.save('{}.pdb'.format(system_name), box=box)
single_asperity.save('{}.lammps'.format(system_name),
    forcefield_files=os.path.join(forcefield_dir, 'oplsaa.xml'),
    box=box)
