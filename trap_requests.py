import methods
import file_writer
from config_reader import config as cr
import datetime
from telegram_notifications import send_telegram_message as stm
from logger import logger

stm("TestRail Stats Collector script started ▶")

try:
    logger.info('Process Started')
    print("{}: Started logger".format(datetime.datetime.now()))

    # getting project name from config
    project_name = cr.get('TestRail Filters', 'project_name')
    print("{}: Finished reading config file".format(datetime.datetime.now()))
    logger.info('Finished reading config file')

    users = methods.get_users()
    projects = methods.get_projects()
    case_types = methods.get_case_types()
    statuses = methods.get_statuses()
    priorities = methods.get_priorities()

    print("{}: Finished getting users, projects, case types, statuses and priorities".format(datetime.datetime.now()))
    logger.info('Finished getting users, projects, case types, statuses and priorities')

    filtered_projects = []
    project_id = [d for d in projects if d['name'] == "{}".format(project_name)][0]
    filtered_projects.append(project_id)
    templates = methods.get_templates(filtered_projects[0]["id"])  # available starting from v5 of TestRail

    print("{}: Getting milestones".format(datetime.datetime.now()))
    logger.info('Getting milestones')
    milestones = []
    for p in projects:
        milestones.append(methods.get_milestones(p["id"]))

    print("{}: Getting suites".format(datetime.datetime.now()))
    logger.info('Getting suites')
    suites = []
    for p in projects:
        suites.append(methods.get_suites(p["id"]))

    print("{}: Getting cases".format(datetime.datetime.now()))
    logger.info('Getting cases')
    cases = []
    sections = []
    for p in filtered_projects:
        suites = methods.get_suites(p["id"])
        # suites = [{"id": 2113}]
        for s in suites:
            sections_iteration = methods.get_sections(p["id"], s["id"])
            sections.append(sections_iteration)
            # sections = [{"id": 26676}]
            for section in sections_iteration:
                cases.append(methods.get_cases(p["id"], s["id"], section["id"]))

    plans = methods.get_plans(filtered_projects[0]["id"])

    print("{}: Getting plans".format(datetime.datetime.now()))
    logger.info('Getting plans')
    runs = []
    run_ids_from_plans = []
    run_ids_from_plans_set = set()
    for p in plans:
        plan_info = methods.get_plan(p["id"])
        entries = plan_info["entries"]
        if entries.__len__() > 0:
            for e in entries:
                runs.append(e["runs"])
            for run in runs:
                run_ids_from_plans.append(run[0]["id"])
                run_ids_from_plans_set.add(run[0]["id"])

    print("{}: Getting runs".format(datetime.datetime.now()))
    logger.info('Getting runs')
    runs_from_plans = []
    for run_id in run_ids_from_plans_set:
        runs_from_plans.append(methods.get_run(run_id))

    runs_raw = methods.get_runs(filtered_projects[0]["id"])
    all_runs = [runs_from_plans, runs_raw]

    print("{}: Getting tests".format(datetime.datetime.now()))
    logger.info('Getting tests')
    tests = []
    for runs in all_runs:
        for run in runs:
            tests.append(methods.get_tests(run["id"]))

    print("{}: Getting test results".format(datetime.datetime.now()))
    logger.info('Getting test results')
    results = []
    for lists_in_tests in tests:
        for list_in_lists in lists_in_tests:
            results.append(methods.get_results_for_test(list_in_lists["id"]))

    # writing data to files
    print("{}: Writing data to disk".format(datetime.datetime.now()))
    logger.info('Writing data to disk')
    file_writer.write_data_to_file("users.json",users)
    file_writer.write_data_to_file("projects.json",projects)
    file_writer.write_data_to_file("milestones.json",milestones)
    file_writer.write_data_to_file("suites.json",suites)
    file_writer.write_data_to_file("cases.json",cases)
    file_writer.write_data_to_file("plans.json",plans)
    file_writer.write_data_to_file("results.json",results)
    file_writer.write_data_to_file("sections.json",sections)
    file_writer.write_data_to_file("case_types.json",case_types)
    file_writer.write_data_to_file("templates.json",templates)  # available starting from v5 of TestRail
    file_writer.write_data_to_file("statuses.json",statuses)
    file_writer.write_data_to_file("priorities.json",priorities)
    file_writer.write_data_to_file("tests.json",tests)
    file_writer.write_data_to_file("runs.json",all_runs)

    # finish timestamp in the log
    print("{}: All done!".format(datetime.datetime.now()))
    logger.info('Process Finished')
    stm("TestRail Stats Collector  script finished successfully ✅")
except:
    stm("TestRail Stats Collector  script terminated with error ⛔")