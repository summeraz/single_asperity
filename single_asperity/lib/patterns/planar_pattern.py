import os
from pkg_resources import resource_filename

import mbuild as mb
import numpy as np


class PlanarPattern(mb.Pattern):
    def __init__(self, density=5.0):
        """Load a chain pattern for a planar surface

        Note: These patterns were generated prior to mBuild's ability to provide
              a seed for the random number generator in the Random2DPattern class.

        Parameters
        ----------
        density : float
            Density of chains (chains / nm^2)
        """
        pattern_dir = resource_filename('single_asperity', 'lib/patterns')

        filename = 'planar_pattern-{:.1f}chains_per_nmsq.xyz'.format(density)
        points = np.loadtxt(os.path.join(pattern_dir, filename), skiprows=2)[:, 1:]

        super(PlanarPattern, self).__init__(points=points, orientations=None)
