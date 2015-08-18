#!/usr/bin/env python

OUTPUTWIDTH = 60


def seperator():
    """
    Prints a separate line made of hyphens with a length of OUTPUTWIDTH
    """
    print "".center(OUTPUTWIDTH, '-')


def results(statsname, number):
    """
    Displays the results in a XX.X format

    Args:
        statsname (str): the name of the metric being printed
        number : the value of the metric being printed
    """
    print "%s %4.1f" % (statsname.ljust(OUTPUTWIDTH, '.'), number)


def title(titlename):
    """
    Displays the title for the metric being calculated

    Args:
        titlename (str): the name of the metric being calculated
    """
    print '\n'
    print (titlename.upper().center((OUTPUTWIDTH - len(titlename)), '*'))
