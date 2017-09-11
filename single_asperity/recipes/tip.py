import mbuild as mb
from single_asperity.lib.surfaces import SilicaTip

class Tip(mb.Compound):

    def __init__(self, chains, fractions=None, backfill=None, pattern=None,
                 **kwargs):
        super(Tip, self).__init__()

        surface = SilicaTip()

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
