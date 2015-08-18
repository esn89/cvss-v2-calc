#!/usr/bin/env python


class TemporalMetrics(object):
    """
    The class for Temporal Score Metrics

    Attributes:
        exp (int): Exploitability value
        rem (int): Remediation level value
        rep (int): Report Confidence value
        ndcount (int): Number of 'Not Defined' entries
    """

    def __init__(self, exp, rem, rep, ndcount):
        self.exp = exp
        self.rem = rem
        self.rep = rep
        self.ndcount = ndcount

    def temporalscore(self, basescore, impact):
        """
        Calculates the temporal score

        Args:
            basescore (int): The basescore from Base Score Metrics
            impact (string): The type of impact we want, 'Normal' or
                             'Adjusted'
        """
        # this means that we have ALL "Not Defined"
        if self.ndcount == 3 and impact.upper() == 'NORMAL':
            return 0
        else:
            return round(basescore * self.exp * self.rem * self.rep, 1)
