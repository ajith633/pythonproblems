
import os
import getpass
import base64
import requests
import json, yaml
import logging
import multiprocessing
import argparse
from myDeploy import myDeploy


def process_args():
    parser = argparse.ArgumentParser(description='This udeploy utility helps automate smaller and repetitive tasks',
                                     epilog='Good luck')
    parser.add_argument('-f', '--force-auth', action='store_true', help="To force auth")
    parser.add_argument('-o', '--only-changed', action='store_true', help="To disable force deploy")
    parser.add_argument('-a', '--application', help="UCD application name")
    parser.add_argument('-c', '--configrepo', help="UCD integration-tools repo name")
    parser.add_argument('-b', '--branch', help="UCD integration-tools branch ")
    parser.add_argument('-e', '--environments', nargs='*', help='list of environments (eg: ddev dsit)')
    parser.add_argument('-s', '--steps', nargs='*', help='list of steps (eg: import deploy stop activate start )')
    parser.add_argument('-y', '--yaml', help='yaml file to load')
    args = vars(parser.parse_args())
    print
    args
    return args


if __name__ == '__main__':
    # Initialize globals, Enhance to accept params via command line
    in_data = process_args()
    forced = in_data['force_auth']
    if in_data['yaml'] is not None:
        print("Yaml file supplied, Ignoring rest of the inputs")
        in_data = yaml.load(open(in_data['yaml']))
        print("Proceeding with below input, Type Y/y to continue")
        print(json.dumps(in_data, indent=2))
        userinput = raw_input("Enter yes or no :")
        if userinput[0] == 'y' or userinput[0] == 'Y':
            pass
        else:
            exit()
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)

    ucdurl = 'https://ucd.sample.com:8443'
    if in_data['application'] is None:
        application = 'DCT_WIBCE_Hogan-Mq-Kafka-Replicator-Topology_Application'
    else:
        application = in_data['application']
    onlyChanged = in_data['only_changed']

    if in_data['steps'] is None:
        steps = ['deploy', 'activate']
    else:
        steps = in_data['steps']
    if in_data['environments'] is None:
        envs = ['ddev', 'dsit']
    else:
        envs = in_data['environments']

    # Initial UCD object
    ucd = myDeploy(ucdurl)
    ucd.authenticate_and_check(forced=forced)

    for env in envs:
        for step in steps:
            logging.info(
                "============================ Performing {} on {} ===================================".format(step,
                                                                                                              env))
            process = {}
            process['application'] = application
            process['environment'] = env
            process['applicationProcess'] = step
            process['onlyChanged'] = str(onlyChanged)
            process['properties'] = {}

            if step == 'import':
                if in_data['branch'] is None or in_data['configrepo'] is None:
                    if in_data['branch'] is None: logging.error(
                        "Branch to import not supplied, run with -h to display help")
                    if in_data['configrepo'] is None: logging.error(
                        "Config repo not supplied, run with -h to display help")
                    exit()
                process['properties']['release'] = in_data['branch']
                process['properties']['integration_tools_repo_name'] = in_data['configrepo']
                process['properties']['folders_to_import'] = env
            elif step == 'deploy' or step == 'activate':
                if 'snapshot' in in_data.keys() and in_data['snapshot'] is not None:
                    process['snapshot'] = in_data['snapshot']
                else:
                    process['versions'] = in_data['versions']
            elif step == 'stop' or step == 'start':
                if 'startstopsnapshot' in in_data.keys() and in_data['startstopsnapshot'] is not None:
                    process['snapshot'] = in_data['startstopsnapshot']
                else:
                    process['versions'] = in_data['startstopversions']
            logging.debug("Using " + json.dumps(process))
            success = ucd.runProcess(process)
            if not success:
                logging.error("Process failed {} on {}".format(step, env))
                exit()
            else:
                logging.info("Process successful {} on {}".format(step, env))
