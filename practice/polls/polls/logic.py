"""polls Logic."""

from . import models


def flavor_percentages():
    """generates percentage value"""
    total_votes = sum(list(models.ice_cream_selections.values()))
    percent_by_flavor = {
        flavor: votes / total_votes
        for flavor, votes
        in models.ice_cream_selections.items()
    }
    return percent_by_flavor

