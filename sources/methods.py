import requests
from sources.config_reader import config as cr
import base64

# Get data from config file
username = cr.get('Auth', 'username')
# password = cr.get('Auth', 'password')
api_key = cr.get('Auth', 'api_key')
testrail_url = cr.get('Server', 'testrail_url')

# Encode username and password to base64 string
base64_auth_string = username + ":" + api_key
base64_auth = base64.b64encode(bytes(base64_auth_string, "utf-8"))
base64_auth = bytes(base64_auth).decode("utf-8")

# Auth
headers = {
    'content-type': "application/json",
    'authorization': "Basic {}".format(base64_auth)
    }


def get_users():
    get_users_endpoint = {"/api/v2/get_users": ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_users_endpoint)
    return response.json()

def get_projects():
    get_projects_endpoint = {"/api/v2/get_projects": ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_projects_endpoint)
    return response.json()

def get_statuses():
    get_statuses_endpoint = {"/api/v2/get_statuses": ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_statuses_endpoint)
    return response.json()

def get_priorities():
    get_priorities_endpoint = {"/api/v2/get_priorities": ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_priorities_endpoint)
    return response.json()

def get_case_types():
    get_cases_types_endpoint = {"/api/v2/get_case_types": ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_cases_types_endpoint)
    return response.json()

def get_milestones(project_id):
    get_milestones_endpoint = {"/api/v2/get_milestones/{}".format(project_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_milestones_endpoint)
    return response.json()

def get_templates(project_id):
    get_templates_endpoint = {"/api/v2/get_templates/{}".format(project_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_templates_endpoint)
    return response.json()

def get_suites(project_id):
    get_suites_endpoint = {"/api/v2/get_suites/{}".format(project_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_suites_endpoint)
    return response.json()

def get_cases(project_id,suite_id, section_id):
    # get_cases_endpoint = {"/api/v2/get_cases/{}".format(project_id): "","suite_id":"{}".format(suite_id)}
    # get_cases_endpoint = {"/api/v2/get_cases/{}&suite_id={}&section_id={}".format(project_id, suite_id, section_id)}
    get_cases_endpoint = {"/api/v2/get_cases/{}".format(project_id): "", "suite_id": "{}".format(suite_id), "section_id": "{}".format(section_id)}
    response = requests.request("GET", testrail_url, headers=headers, params=get_cases_endpoint)
    return response.json()

def get_sections(project_id,suite_id):
    get_sections_endpoint = {"/api/v2/get_sections/{}".format(project_id): "","suite_id":"{}".format(suite_id)}
    response = requests.request("GET", testrail_url, headers=headers, params=get_sections_endpoint)
    return response.json()

def get_plans(project_id):
    get_plans_endpoint = {"/api/v2/get_plans/{}".format(project_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_plans_endpoint)
    return response.json()

def get_plan(plan_id):
    get_plan_endpoint = {"/api/v2/get_plan/{}".format(plan_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_plan_endpoint)
    return response.json()

def get_run(run_id):
    get_run_endpoint = {"/api/v2/get_run/{}".format(run_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_run_endpoint)
    return response.json()

def get_runs(project_id):
    get_runs_endpoint = {"/api/v2/get_runs/{}".format(project_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_runs_endpoint)
    return response.json()

def get_results_for_run(run_id):
    get_results_for_run_endpoint = {"/api/v2/get_results_for_run/{}".format(run_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_results_for_run_endpoint)
    return response.json()

def get_results_for_test(test_id):
    get_results_for_test_endpoint = {"/api/v2/get_results/{}".format(test_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_results_for_test_endpoint)
    return response.json()

def get_tests(run_id):
    get_tests_endpoint = {"/api/v2/get_tests/{}".format(run_id): ""}
    response = requests.request("GET", testrail_url, headers=headers, params=get_tests_endpoint)
    return response.json()