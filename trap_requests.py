import methods, file_writer
from config_reader import config as cr
import datetime
from telegram_notifications import send_telegram_message as stm
from logger import logger


def main():
    stm("TestRail Stats Collector script started ▶")
    start_time = datetime.datetime.now()

    try:
        logger.info('Process Started')
        project_name = cr.get('TestRail Filters', 'project_name')

        try:
            users = methods.get_users()
            file_writer.write_data_to_file("users.json", users)

            projects = methods.get_projects()
            file_writer.write_data_to_file("projects.json", projects)

            # Additional data collection and file writing
            case_types = methods.get_case_types()
            file_writer.write_data_to_file("case_types.json", case_types)

            statuses = methods.get_statuses()
            file_writer.write_data_to_file("statuses.json", statuses)

            priorities = methods.get_priorities()
            file_writer.write_data_to_file("priorities.json", priorities)

            # Process filtered projects
            filtered_projects = [d for d in projects if d['name'] == project_name]
            if filtered_projects:
                project_id = filtered_projects[0]["id"]

                # Fetching and writing templates data
                templates = methods.get_templates(project_id)
                file_writer.write_data_to_file("templates.json", templates)

                # Fetching and writing milestones data
                milestones = methods.get_milestones(project_id)
                file_writer.write_data_to_file("milestones.json", milestones)

                # Fetching and writing suites data
                suites = methods.get_suites(project_id)
                file_writer.write_data_to_file("suites.json", suites)

                # Fetching and writing plans data
                plans = methods.get_plans(project_id)
                file_writer.write_data_to_file("plans.json", plans)

            end_time = datetime.datetime.now()
            duration = end_time - start_time
            logger.info(f'Process Finished in {duration}')
            stm(f"TestRail Stats Collector script finished successfully ✅. Completed in {duration}")

        except Exception as e:
            logger.error(f"Error during processing: {e}")
            stm(f"TestRail Stats Collector script terminated with error ⛔. Duration: {datetime.datetime.now() - start_time}")

    except Exception as e:
        logger.error(f"Critical error: {e}")
        stm(f"TestRail Stats Collector script failed to start ⛔.")


if __name__ == "__main__":
    main()
