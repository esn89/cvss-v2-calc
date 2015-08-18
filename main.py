#!/usr/bin/env python
import sys

import basemetrics as b
import temporalmetrics as t
import environmentalmetrics as e
import inputhandler as ih
import formatter as display


def run():
    print "\nCalculating Base Scores: "
    display.seperator()
    # args is arguments for my first class, BaseMetrics
    args, vectorstring = ih.getbaseinput()
    base = b.BaseMetrics(*args)

    display.title("base scores")
    display.seperator()
    display.results("Exploitability", base.exploitability())
    display.results("Impact", base.impact())
    basescore = base.calcbasescore()
    display.results("Base score", basescore)
    display.results("Overall", basescore)
    # print "\n%s %s\n" % ("Vector String", vectorstring)
    display.vstring(vectorstring)

    ih.prompt("Temporal")

    print "\nCalculating Temporal Score: "
    display.seperator()
    # tempargs is the arguments for the second class temporal Metrics
    tempargs, vectorstring = ih.gettemporalinput()
    temporal = t.TemporalMetrics(*tempargs)

    display.title("temporal scores")
    display.seperator()
    tempscore = temporal.temporalscore(basescore, 'normal')
    display.results("Temporal Score", tempscore)

    # If temp score is 0, use base score as overall
    if tempscore != 0:
        display.results("Overall", tempscore)
    else:
        tempscore = basescore
        display.results("Overall", basescore)
    display.vstring(vectorstring)
    display.seperator()

    ih.prompt("environmental scores")

    print "\nCalculating Environmental Scores: "
    display.seperator()
    envargs, vectorstring = ih.getenvinput()
    environmental = e.EnvironmentalMetrics(*envargs)

    display.title("environmental scores")
    display.seperator()
    adjustedimpact = environmental.adjustedimpact(base.ci, base.ii,
                                                  base.ai)
    display.results("Adjusted Impact", adjustedimpact)
    # This gives us a new basescore based on 'adjusted impact',
    # by setting BaseMetrics' instance variable 'self.adjbasescore'
    base.calcbasescore(adjustedimpact)
    # We got adjbasescore now, use it for Temporal Equation:
    adjustedtemporal = temporal.temporalscore(base.adjbasescore, 'adjust')
    # We have adjusted temporal now, use it for Environmental Score:
    envscore = (environmental.environmentalscore(adjustedtemporal))
    display.results("Environmental Score", envscore)

    # Final basescore:
    if envscore != 0:
        display.results("Overall", envscore)
    else:
        display.results("Overall", tempscore)
    display.vstring(vectorstring)
    display.seperator()


def main():
    run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\n Now exiting. Bye\n"
        sys.exit(0)
