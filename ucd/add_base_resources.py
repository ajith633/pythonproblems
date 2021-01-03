
import os
import getpass
import base64
import requests
import json
import logging
import multiprocessing
import argparse
from myDeploy import myDeploy


def process_args():
    parser = argparse.ArgumentParser(description='This udeploy utility helps automate smaller and repetitive tasks',
                                     epilog='Good luck')
    parser.add_argument('-f', '--force-auth', action='store_true', help="To force auth")
    parser.add_argument('-A', '--application', help="UCD application name")
    parser.add_argument('-B', '--base-resources',
                        help='list of base resources wihtout the applicaiton prefix(eg: preprod/agile/development/ddev)')
    args = vars(parser.parse_args())
    print
    args
    return args


if __name__ == '__main__':
    # Initialize globals, Enhance to accept params via command line
    in_data = process_args()
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)

    ucdurl = 'https://ucd.sample.com:8443'
    application = in_data['application']
    if application is None:
        # You can supply --application argument to avoid hard coding
        application = 'DCT_WIBCE_Hogan-Mq-Kafka-Replicator-Topology_Application'
    # paths=['preprod/agile/development/temp','prod/prod-temp']
    paths = ['preprod/agile/development/ddev', 'preprod/agile/development/dsit', 'preprod/agile/agilerelease/rsit',
             'preprod/agile/agilerelease/rqa',
             'preprod/agile/agilerelease/rvqa', 'preprod/agile/agilerelease/rpte',
             'staging', 'prod/prod-al', 'prod/prod-az', 'prod/prod-mn']
    paths = ['preprod/agile/development/ddev', 'preprod/agile/development/dsit', 'preprod/agile/agilerelease/rsit',
             'preprod/agile/agilerelease/rqa']

    # Initial UCD object
    ucd = myDeploy(ucdurl)
    ucd.authenticate_and_check(forced=in_data['force_auth'])

    # Create base resources
    ucd.createBaseResources(application, paths)

    # Create environments and adjust teams
    ucd.createEnvironments(application, paths)

    # Create environment to base resource mapping
    ucd.createEnvMappings(application, paths)
    # ucd.get("/cli/component/info", { 'component' : 'DCT_BPAY_Bpmds_Certificates_PreProd_Component'})

