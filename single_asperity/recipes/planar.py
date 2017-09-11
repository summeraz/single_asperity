import mbuild as mb
from single_asperity.lib.surfaces import SilicaSurface

class Planar(mb.Compound):
    """ An optionally functionalized, planar amorphous
        silica surface.
    """

    def __init__(self, chains, fractions=None, backfill=None, pattern=None,
                 **kwargs):
        super(Planar, self).__init__()

        surface = SilicaSurface()

        if pattern:
            pattern.points /= 10.0
            pattern.points -= surface.boundingbox.mins
            pattern.points /= surface.boundingbox.lengths

        monolayer = mb.Monolayer(surface,
                                 chains,
                                 fractions=fractions,
                                 backfill=backfill,
                                 pattern=pattern,
                                 **kwargs)
        self.add(monolayer)
