import os
import time
import getpass
import base64
import requests
import json
import yaml
import logging
import multiprocessing
import argparse


class myDeploy():
    my_url = None
    my_auth = None
    my_header = None
    auth_file = os.environ['HOME'] + "/.ssh/.ucdauthstring"

    def __init__(self, url="https://ucd.sample.com:8443", authstring=None):
        self.my_url = url;

    def authenticate(self, forced=False):
        if self.my_url is None:
            logging.critical("UCD url is not set, Fatal")
            quit()
        elif self.my_auth and not forced:
            logging.info("Already authenticated")
            return
        elif not forced:
            try:

                logging.debug("About to read")
                with open(self.auth_file, 'r') as authfile:
                    self.my_auth = authfile.read().encode('ascii').rstrip()
                    logging.debug("Read from the file:" + self.my_auth.decode('ascii').rstrip())
                    self.my_header = {'Authorization': 'Basic ' + self.my_auth, 'Accept': 'application/json',
                                      'Content-Type': 'application/json'}
                    return
            except Exception as e1:
                logging.error(e1)
        try:
            user = raw_input("Enter your username:")
            password = getpass.getpass(prompt="Enter your password:")
            userstring = user + ":" + password
            abytes = userstring.encode('ascii')
            self.my_auth = base64.b64encode(abytes)
            self.my_header = {'Authorization': 'Basic ' + self.my_auth}

            # logging.debug("user={},password={},base64={}",user,p,str(self.my_auth.decode('ascii')))
            with open(self.auth_file, 'w') as f:
                f.write(self.my_auth.decode('ascii'))
                logging.info("Stored auth info in the file: " + self.auth_file)

        except Exception as e2:
            logging.error(e2)
            print(e2)
            exit()
        # logging.debug(self.my_auth.decode('ascii'))

    def authenticate_and_check(self, forced=False):
        self.authenticate(forced)
        result = self.head("/cli/systemConfiguration")
        if result == 0 or result == 401:
            logging.error("Unable to authenticate, please delete " + self.auth_file + " and retry")
            quit()

    def head(self, context):
        url = self.my_url + context
        logging.debug(url + " " + json.dumps(self.my_header))
        try:
            res = requests.get(url, headers=self.my_header, verify=False)
            return res.status_code
        except Exception as er:
            logging.error(er)
            return 0

    def get(self, context, params={}, accept="application/json", debug=False):
        url = self.my_url + context
        logging.debug(url + " " + json.dumps(self.my_header) + "," + json.dumps(params))
        try:
            res = requests.get(url, headers=self.my_header, params=params, verify=False)
            if res.status_code == 200:
                try:
                    j = json.loads(res.text)
                    logging.debug(json.dumps(j, indent=4))
                    return j
                except:
                    logging.debug(res.txt)
                    return res.text
            else:
                return False
        except Exception as er:
            logging.error(er)
            return False

    def put(self, context, params={}, data={}, accept="application/json"):
        url = self.my_url + context
        logging.debug(url + " " + str(self.my_header) + "," + json.dumps(params) + "," + json.dumps(data))
        res = requests.put(url, headers=self.my_header, params=params, data=data, verify=False)
        logging.debug(res.text)
        print(res.content)
        if res.status_code < 300 and res.status_code >= 200:
            try:
                j = json.loads(res.text)
                logging.debug(json.dumps(j, indent=4))
                if 'requestId' in j.keys():
                    return j['requestId']
            except:
                logging.debug(res.text)
            return True
        else:
            return False

    def delete(self, context, params={}, data={}, accept="application/json"):
        url = self.my_url + context
        logging.debug(url + " " + str(self.my_header) + "," + json.dumps(params) + "," + json.dumps(data))
        res = requests.delete(url, headers=self.my_header, params=params, data=data, verify=False)
        if res.status_code < 300 and res.status_code >= 200:
            return True
        else:
            logging.error(res.text)
            return False

    def post(self, context, data={}, accept="application/json"):
        url = self.my_url + context
        logging.debug(url + " " + str(self.my_header) + "," + json.dumps(params) + "," + json.dumps(data))
        res = requests.post(url, headers=self.my_header, data=data, verify=False)
        j = json.loads(res.text)
        logging.debug(json.dumps(j, indent=4))

    def removeteams(self, application, top, name, rawtext):
        j = json.loads(rawtext)
        for team in j['extendedSecurity']['teams']:
            teamLabel = team.get('teamLabel')
            resourceRoleLabel = team.get('resourceRoleLabel', "NONE")
            if resourceRoleLabel == 'Controlled Prod Environment' and teamLabel == 'DCT':
                logging.debug("Keeping " + teamLabel + resourceRoleLabel)
            else:
                logging.debug("Deleting " + teamLabel + resourceRoleLabel)
                params = {'application': application, 'environment': name, 'team': teamLabel}
                if resourceRoleLabel != "NONE":
                    params['type'] = resourceRoleLabel
                self.delete("/cli/environment/teams", params=params)

    def createEnvironments(self, application, paths):
        for path in paths:
            # Lets Create Environment
            name = path.split('/')[-1]
            top = path.split('/')[0]
            data = {'application': application, 'environment': name}
            envdata = self.get("/cli/environment/info", data)
            if envdata:
                logging.info("Environment {} already exists".format(name))
            else:
                params = {'application': application, 'name': name}
                logging.info("Creating environemnt {}".format(name))
                success = self.put("/cli/environment/createEnvironment", params=params)
                if not success:
                    logging.error("Unable to create environment {}".format(name))
                    return False
                envdata = self.get("/cli/environment/info", data)
            if top == 'prod' or top == 'staging':
                logging.info("Cleaning up teams for environment=" + name)
                logging.info("Takes few minutes ..")
                self.removeteams(application, top, name, envdata)

    def createBaseResources(self, application, paths):
        cache_dict = {}
        for path in paths:
            # Lets create base resources
            parent = '/' + application
            for group in path.split('/'):
                data = json.dumps({'name': group, 'parent': parent})
                # Build new parent for next loop
                parent = parent + "/" + group
                if parent in cache_dict or self.get("/cli/resource/info", {'resource': parent}):
                    cache_dict[parent] = True
                    logging.info("Resource already exists {}".format(parent))
                else:
                    logging.info("Creating :{}".format(data))
                    success = self.put("/cli/resource/create", data=data)
                    if not success:
                        logging.error("Unable to create resource {}".format(parent))

    def createEnvMappings(self, application, paths):
        for path in paths:
            # Lets create base resources
            logging.info("Mapping base resource " + path)
            name = path.split('/')[-1]
            params = {'application': application, 'environment': name, 'resource': '/' + application + '/' + path}
            success = self.put("/cli/environment/addBaseResource", params=params)
            if not success:
                logging.error("Unable to map base resources {} -> {}".format(name, path))

    def runProcess(self, process):
        # Lets create base resources
        logging.info("Executing process " + str(process))
        reqid = self.put("/cli/applicationProcessRequest/request", data=json.dumps(process))
        if not reqid:
            logging.error(
                "Unable to run process {} -> {}".format(process['applicationProcess'], process['environment']))
            return
        logging.debug("Request ID: {}".format(reqid))
        result = self.get("/cli/applicationProcessRequest/requestStatus", params={'request': reqid})
        while result['status'] in ['PENDING', 'EXECUTING']:
            logging.debug(result)
            logging.info("Waiting 10 seconds ...........")
            time.sleep(10)
            result = self.get("/cli/applicationProcessRequest/requestStatus", params={'request': reqid})
        logging.debug(result)
        if result['result'] == 'SUCCEEDED':
            return True
        else:
            return False


