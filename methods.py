import requests
from config_reader import config as cr
import base64
import logging

logger = logging.getLogger(__name__)

username = cr.get('Auth', 'username')
api_key = cr.get('Auth', 'api_key')
testrail_url = cr.get('Server', 'testrail_url')

base64_auth_string = f"{username}:{api_key}"
base64_auth = base64.b64encode(base64_auth_string.encode("utf-8")).decode("utf-8")

headers = {
    'content-type': "application/json",
    'authorization': f"Basic {base64_auth}"
}

def make_api_request(endpoint):
    full_url = f"{testrail_url}{endpoint}"
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None

def get_users():
    return make_api_request("/api/v2/get_users")

def get_projects():
    return make_api_request("/api/v2/get_projects")

def get_statuses():
    return make_api_request("/api/v2/get_statuses")

def get_priorities():
    return make_api_request("/api/v2/get_priorities")

def get_case_types():
    return make_api_request("/api/v2/get_case_types")

def get_milestones(project_id):
    return make_api_request(f"/api/v2/get_milestones/{project_id}")

def get_templates(project_id):
    return make_api_request(f"/api/v2/get_templates/{project_id}")

def get_suites(project_id):
    return make_api_request(f"/api/v2/get_suites/{project_id}")

def get_cases(project_id, suite_id, section_id):
    return make_api_request(f"/api/v2/get_cases/{project_id}?suite_id={suite_id}&section_id={section_id}")

def get_sections(project_id, suite_id):
    return make_api_request(f"/api/v2/get_sections/{project_id}?suite_id={suite_id}")

def get_plans(project_id):
    return make_api_request(f"/api/v2/get_plans/{project_id}")

def get_plan(plan_id):
    return make_api_request(f"/api/v2/get_plan/{plan_id}")

def get_run(run_id):
    return make_api_request(f"/api/v2/get_run/{run_id}")

def get_runs(project_id):
    return make_api_request(f"/api/v2/get_runs/{project_id}")

def get_results_for_run(run_id):
    return make_api_request(f"/api/v2/get_results_for_run/{run_id}")

def get_results_for_test(test_id):
    return make_api_request(f"/api/v2/get_results/{test_id}")

def get_tests(run_id):
    return make_api_request(f"/api/v2/get_tests/{run_id}")
