#!/usr/bin/env python


class EnvironmentalMetrics(object):
    """
    The class for Environmental Score Metrics

    Attributes:

        cdp (int): Collateral Damage Potential value
        td (int): Target Distribution value
        cr (int): Confidentiality Requirement value
        ir (int): Integrity Requirement value
        ar (int): Availability Requirement value
        ndcount (int): the number of "not defined" entries
    """

    def __init__(self, cdp, td, cr, ir, ar, ndcount):
        self.cdp = cdp
        self.td = td
        self.cr = cr
        self.ir = ir
        self.ar = ar
        self.ndcount = ndcount

    def adjustedimpact(self, confimpact, integimpact, availimpact):
        """
        Calculates and returns the adjusted impact

        Args:
            confimpact (int): Confidentiality Impact value
            integimpact (int): Integrity Impact value
            availimpact (int): Availability  Impact value

        Returns:
            The minimum value between 10 and the adjust impact,
            'score'.
        """
        # This means that ALL attributes are "NOT DEFINED"
        # No need to do calculations
        if self.ndcount == 5:
            return 0
        else:
            score = (10.41 * (1 - (1 - confimpact * self.cr) *
                     (1 - integimpact * self.ir) *
                     (1 - availimpact * self.ar)))
            return min(10, score)

    def environmentalscore(self, adjtemp):
        """
        Calculates and returns environemntal score

        Args:
            adjtemp (int): Adjusted temporal score

        Returns:
            The environmental score value
        """
        # This means that ALL attributes are "NOT DEFINED"
        # No need to do calculations
        if self.ndcount == 5:
            return 0
        else:
            return round((adjtemp + (10 - adjtemp) * self.cdp) * self.td, 1)
