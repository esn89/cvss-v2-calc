#!/usr/bin/env python
import sys


def getbaseinput():
    """
    Grabs the user inputs for the Base Metrics.

    Args:
        None
    Returns:
        a list of arguments.
    """

    AccessVector = {
        'L': 0.39, 'A': 0.646, 'N': 1.0,
        "msg": "Access Vector type: "
        "[L]ocal, [A]djacent Network, [N]etwork: ",
        "accept": ['L', 'A', 'N']
        }

    AccessComplexity = {
        'H': 0.35, 'M': 0.61, 'L': 0.71,
        "msg": "Access Complexity type: "
        "[H]igh, [M]edium, [L]ow: ",
        "accept": ['H', 'M', 'L']
        }

    Authentication = {
        'M': 0.45, 'S': 0.56, 'N': 0.704,
        "msg": "Authentication type: "
        "[M]ultiple, [S]ingle, [N]one: ",
        "accept": ['M', 'S', 'N']
        }

    # Impact Metrics:
    ConfImpact = {
        'N': 0.0, 'P': 0.275, 'C': 0.660,
        "msg": "Confidentiality Impact type: "
        "[N]one, [P]artial, [C]omplete: ",
        "accept": ["N", "P", "C"]
        }

    IntegImpact = {
        'N': 0.0, 'P': 0.275, 'C': 0.660,
        "msg": "Integrity Impact type: "
        "[N]one, [P]artial, [C]omplete: ",
        "accept": ["N", "P", "C"]
        }

    AvailImpact = {
        'N': 0.0, 'P': 0.275, 'C': 0.660,
        "msg": "Availability Impact type: "
        "[N]one, [P]artial, [C]omplete: ",
        "accept": ["N", "P", "C"]
        }

    listofargs = []
    listofbasemetrics = [
        AccessVector, AccessComplexity, Authentication,
        ConfImpact, IntegImpact, AvailImpact
        ]

    # Iterates through each metric asking the user for the corresponding
    # input. (inp)
    # Checks against the metric's "accept" list to check if valid
    # If it is, appends the numeric value to "listofargs"
    for metric in listofbasemetrics:
        while True:
            inp = raw_input(metric["msg"])
            if inp.upper() not in metric["accept"]:
                print "Not a valid choice. Try again, or 'ctrl-c' to exit.\n"
                continue
            else:
                listofargs.append(metric[inp.upper()])
                break

    return listofargs


def gettemporalinput():
    """
    Grabs the user inputs for the Temporal Metrics.

    Args:
        None
    Returns:
        a list of arguments.
    """

    Exploitability = {
        'D': 1.0, 'H': 1.0, 'F': 0.95, 'P': 0.9, 'U': 0.85,
        "msg": "Exploitability type: : "
        "Not [D]efined, [U]nproven, [P]roof-of-Concept, "
        "[F]unctional, [H]igh: ",
        "accept": ['D', 'H', 'F', 'P', 'U']
        }

    RemediationLevel = {
        'O': 0.87, 'T': 0.90, 'W': 0.95, 'U': 1.00, 'D': 1.00,
        "msg": "Remediation level: "
        "Not [D]efined, [O]fficial-fix, [T]emporary-fix, "
        "[W]orkaround, [U]navailable: ",
        "accept": ['O', 'T', 'W', 'U', 'D']
        }

    ReportConfidence = {
        'F': 0.90, 'B': 0.95, 'C': 1.00, 'D': 1.00,
        "msg": "Report Confidence level: "
        "Uncon[F]irmed, Uncorro[B]orated, [C]onfirmed, "
        "Not [D]efined: ",
        "accept": ['F', 'B', 'C', 'D']
        }

    listofargs = []
    temporalmetrics = [Exploitability, RemediationLevel, ReportConfidence]

    # Iterates through each metric asking the user for the corresponding
    # input. (inp)
    # Checks against the metric's "accept" list to check if valid
    # If it is, appends the numeric value to "listofargs"

    # 'ndcount' keeps track of the number of times the users
    # entered 'Not Defined' as their option.
    #
    # We cannot simply check whether the entire listofargs is all
    # 1.0s, because in the 'Exploitability' metric, a 'High' is a 1.0
    ndcount = 0
    for metric in temporalmetrics:
        while True:
            inp = raw_input(metric["msg"])
            if inp.upper() == 'D':
                ndcount += 1

            if inp.upper() not in metric["accept"]:
                print "Not a valid choice. Try again or 'ctrl-c' to exit.\n"
                continue
            else:
                listofargs.append(metric[inp.upper()])
                break

    listofargs.append(ndcount)
    return listofargs


def getenvinput():
    """
    Grabs the user inputs for the Environmental Metrics.

    Args:
        None
    Returns:
        a list of arguments.
    """

    # General Modifiers:
    CollateralDmgPot = {
        'D': 0.00, 'N': 0.00, 'L': 0.1, 'I': 0.3, 'M': 0.4, 'H': 0.5,
        "msg": "Collateral Damage Potential: "
        "Not [D]efined, [N]one, [L]ow, Low-Med[I]um, [M]edium-High, [H]igh: ",
        "accept": ['D', 'N', 'L', 'I', 'M', 'H']
        }

    TargetDistrib = {
        'D': 1.00, 'N': 0.00, 'L': 0.25, 'M': 0.75, 'H': 1.00,
        "msg": "Target Distribution: "
        "Not [D]efined, [N]one, [L]ow, [M]edium, [H]igh: ",
        "accept": ['D', 'N', 'L', 'M', 'H']
        }

    # Impact Subscore Modifiers:
    ConfidentialReq = {
        'D': 1.0, 'L': 0.5, 'M': 1.0, 'H': 1.51,
        "msg": "Confidentiality Requirement: "
        "Not [D]efined, [L]ow, [M]edium, [H]igh: ",
        "accept": ['D', 'L', 'M', 'H']
        }

    IntegrityReq = {
        'D': 1.0, 'L': 0.5, 'M': 1.0, 'H': 1.51,
        "msg": "Integrity Requirement: "
        "Not [D]efined, [L]ow, [M]edium, [H]igh: ",
        "accept": ['D', 'L', 'M', 'H']
        }

    AvailabilityReq = {
        'D': 1.0, 'L': 0.5, 'M': 1.0, 'H': 1.51,
        "msg": "Availability Requirement: "
        "Not [D]efined, [L]ow, [M]edium, [H]igh: ",
        "accept": ['D', 'L', 'M', 'H']
        }

    listofargs = []
    envmetrics = [
        CollateralDmgPot, TargetDistrib, ConfidentialReq,
        IntegrityReq, AvailabilityReq
        ]

    # Iterates through each metric asking the user for the corresponding
    # input. (inp)
    # Checks against the metric's "accept" list to check if valid
    # If it is, appends the numeric value to "listofargs"
    #
    # 'ndcount' keeps track of the number of times the users
    # entered 'Not Defined' as their option.
    #
    # We cannot simply check whether the entire listofargs is all
    # 1.0s, because in the 'Integrity Requirements' metric, a 'High' is
    # also a 1.0
    ndcount = 0
    for metric in envmetrics:
        while True:
            # checks to see if all is all 'Not 'Defined':
            inp = raw_input(metric["msg"])
            if inp.upper() == 'D':
                ndcount += 1

            if inp.upper() not in metric["accept"]:
                print "Not a valid choice.  Try again, or 'ctrl-c' to exit.\n"
                continue
            else:
                listofargs.append(metric[inp.upper()])
                break
    listofargs.append(ndcount)
    return listofargs


def prompt(title):
    """
    Grabs the user inputs for the subsequent metrics.

    Args:
        title (str): The title of the metric to be measured next
    """

    while True:
        prompt = raw_input("Would you like the %s Score: [Y/n]? " % str(title))
        if prompt.upper() == "Y":
            break
        if prompt.upper() == "N":
            print "\n Now exiting. Bye\n"
            sys.exit(0)
        else:
            print "Sorry, I didn't understand you."
