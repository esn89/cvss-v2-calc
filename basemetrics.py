#!/usr/bin/env python


class BaseMetrics(object):
    """
    The class for Base Score Metrics

    Attributes:

        av (int): Access Vector value
        ac (int): Access Complexity value
        au (int): Authentication value
        ci (int): Confidentiality Impact value
        ii (int): Integrity Impact value
        ai (int): Availability Impact value
    """

    def __init__(self, av, ac, au, ci, ii, ai):
        self.av = av
        self.ac = ac
        self.au = au
        self.ci = ci
        self.ii = ii
        self.ai = ai

    def exploitability(self):
        return 20 * self.av * self.ac * self.au

    def impact(self):
        return 10.41 * (1 - (1 - self.ci) *
                        (1 - self.ii) * (1 - self.ai))

    def fimpact(self):
        if self.impact() == 0:
            return 0
        else:
            return 1.176

    def calcbasescore(self, typeofimpact=None):
        """
        Returns the base score or adjusted base score

        Args:
            typeofimpact : if 'None' it calculates base score, else
                           it is the value from adjusted base score
        Returns:
            basescore
        """

        if typeofimpact is None:
            # If impact is None, we want the normal basescore
            score = ((0.6 * self.impact()) +
                     (0.4 * self.exploitability()) - 1.5)
            # the abs is there to prevent negative numbers in case
            # exploitability and impact is zero
            self.basescore = abs(round(score * self.fimpact(), 1))
            return self.basescore
        else:
            # If we are here, that means our 'typeofimpact' is
            # the impact passed from EnvironmentalMetric's
            # AdjustedImpact.
            score = ((0.6 * typeofimpact) +
                     (0.4 * self.exploitability()) - 1.5)
            # the abs is there to prevent negative numbers in case
            # exploitability and impact is zero
            self.adjbasescore = abs(round(score * self.fimpact(), 1))
            return self.adjbasescore
