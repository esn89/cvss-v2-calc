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
    # EXPLOITABILITY METRICS

    # Access Vector
    AV = {
        'L': 0.39, 'A': 0.646, 'N': 1.0,
        "msg": "Access Vector type: "
        "[L]ocal, [A]djacent Network, [N]etwork: ",
        "accept": ['L', 'A', 'N'],
        "name": "AV"
        }
    # Access Complexity
    AC = {
        'H': 0.35, 'M': 0.61, 'L': 0.71,
        "msg": "Access Complexity type: "
        "[H]igh, [M]edium, [L]ow: ",
        "accept": ['H', 'M', 'L'],
        "name": "AC"
        }
    # Authentication
    Au = {
        'M': 0.45, 'S': 0.56, 'N': 0.704,
        "msg": "Authentication type: "
        "[M]ultiple, [S]ingle, [N]one: ",
        "accept": ['M', 'S', 'N'],
        "name": "Au"
        }
    # IMPACT METRICS

    # Confidentiality Impact
    C = {
        'N': 0.0, 'P': 0.275, 'C': 0.660,
        "msg": "Confidentiality Impact type: "
        "[N]one, [P]artial, [C]omplete: ",
        "accept": ["N", "P", "C"],
        "name": "C"
        }
    # Integrity Impact
    I = {
        'N': 0.0, 'P': 0.275, 'C': 0.660,
        "msg": "Integrity Impact type: "
        "[N]one, [P]artial, [C]omplete: ",
        "accept": ["N", "P", "C"],
        "name": "I"
        }
    # Availability Impact
    A = {
        'N': 0.0, 'P': 0.275, 'C': 0.660,
        "msg": "Availability Impact type: "
        "[N]one, [P]artial, [C]omplete: ",
        "accept": ["N", "P", "C"],
        "name": "A"
        }

    listofargs = []
    listofbasemetrics = [
        AV, AC, Au,
        C, I, A
        ]
    vectorstring = ""

    # Iterates through each metric asking the user for the corresponding
    # input. (inp)
    # Checks against the metric's "accept" list to check if valid
    # If it is, appends the numeric value to "listofargs"
    for metric in listofbasemetrics:
        vectorstring += metric["name"] + ":"
        while True:
            inp = raw_input(metric["msg"])
            if inp.upper() not in metric["accept"]:
                print "Not a valid choice. Try again, or 'ctrl-c' to exit.\n"
                continue
            else:
                # it is a valid value, append to our vector string
                vectorstring += inp.upper() + "/"
                # appends to our arguments list for our constructor
                listofargs.append(metric[inp.upper()])
                break
    vectorstring = vectorstring.rstrip('/')
    return listofargs, vectorstring


def gettemporalinput():
    """
    Grabs the user inputs for the Temporal Metrics.

    Args:
        None
    Returns:
        a list of arguments.
    """

    Exploitability = {
        'ND': 1.0, 'H': 1.0, 'F': 0.95, 'POC': 0.9, 'U': 0.85,
        "msg": "Exploitability type: : "
        "[ND] Not Defined, [U]nproven, [POC] Proof-of-Concept, "
        "[F]unctional, [H]igh: ",
        "accept": ['ND', 'H', 'F', 'POC', 'U'],
        "name": "E"
        }

    RemediationLevel = {
        'OF': 0.87, 'TF': 0.90, 'W': 0.95, 'U': 1.00, 'ND': 1.00,
        "msg": "Remediation level: "
        "[ND] Not Defined, [OF]ficial-fix, [TF] Temporary-fix, "
        "[W]orkaround, [U]navailable: ",
        "accept": ['OF', 'TF', 'W', 'U', 'ND'],
        "name": "RL"
        }

    ReportConfidence = {
        'UC': 0.90, 'UR': 0.95, 'C': 1.00, 'ND': 1.00,
        "msg": "Report Confidence level: "
        "[ND] Not Defined, [UC] Unconfirmed, [UR] Uncorroborated, "
        "[C]onfirmed: ",
        "accept": ['UC', 'UR', 'C', 'ND'],
        "name": "RC"
        }

    listofargs = []
    temporalmetrics = [Exploitability, RemediationLevel, ReportConfidence]
    vectorstring = ""

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
        vectorstring += metric["name"] + ":"
        while True:
            inp = raw_input(metric["msg"])
            if inp.upper() == 'ND':
                ndcount += 1
            if inp.upper() not in metric["accept"]:
                print "Not a valid choice. Try again or 'ctrl-c' to exit.\n"
                continue
            else:
                vectorstring += inp.upper() + "/"
                listofargs.append(metric[inp.upper()])
                break

    vectorstring = vectorstring.rstrip('/')
    listofargs.append(ndcount)
    return listofargs, vectorstring


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
        'ND': 0.00, 'N': 0.00, 'L': 0.1, 'LM': 0.3, 'MH': 0.4, 'H': 0.5,
        "msg": "Collateral Damage Potential: "
        "[ND] Not Defined, [N]one, [L]ow, [LM] Low-Medium, "
        "[MH] Medium-High, [H]igh: ",
        "accept": ['ND', 'N', 'L', 'LM', 'MH', 'H'],
        "name": "CDP"
        }

    TargetDistrib = {
        'ND': 1.00, 'N': 0.00, 'L': 0.25, 'M': 0.75, 'H': 1.00,
        "msg": "Target Distribution: "
        "[ND] Not Defined, [N]one, [L]ow, [M]edium, [H]igh: ",
        "accept": ['ND', 'N', 'L', 'M', 'H'],
        "name": "TD"
        }

    # Impact Subscore Modifiers:
    ConfidentialReq = {
        'ND': 1.0, 'L': 0.5, 'M': 1.0, 'H': 1.51,
        "msg": "Confidentiality Requirement: "
        "[ND] Not Defined, [L]ow, [M]edium, [H]igh: ",
        "accept": ['ND', 'L', 'M', 'H'],
        "name": "CR"
        }

    IntegrityReq = {
        'ND': 1.0, 'L': 0.5, 'M': 1.0, 'H': 1.51,
        "msg": "Integrity Requirement: "
        "[ND] Not Defined, [L]ow, [M]edium, [H]igh: ",
        "accept": ['ND', 'L', 'M', 'H'],
        "name": "IR"
        }

    AvailabilityReq = {
        'ND': 1.0, 'L': 0.5, 'M': 1.0, 'H': 1.51,
        "msg": "Availability Requirement: "
        "[ND] Not Defined, [L]ow, [M]edium, [H]igh: ",
        "accept": ['ND', 'L', 'M', 'H'],
        "name": "AR"
        }

    listofargs = []
    envmetrics = [
        CollateralDmgPot, TargetDistrib, ConfidentialReq,
        IntegrityReq, AvailabilityReq
        ]
    vectorstring = ""

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
        vectorstring += metric["name"] + ":"
        while True:
            # checks to see if all is all 'Not 'Defined':
            inp = raw_input(metric["msg"])
            if inp.upper() == 'ND':
                ndcount += 1

            if inp.upper() not in metric["accept"]:
                print "Not a valid choice.  Try again, or 'ctrl-c' to exit.\n"
                continue
            else:
                vectorstring += inp.upper() + "/"
                listofargs.append(metric[inp.upper()])
                break

    vectorstring = vectorstring.rstrip('/')
    listofargs.append(ndcount)
    return listofargs, vectorstring


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
