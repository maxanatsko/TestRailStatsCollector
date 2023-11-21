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
            # ...

            filtered_projects = [d for d in projects if d['name'] == project_name]
            if filtered_projects:
                project_id = filtered_projects[0]["id"]
                templates = methods.get_templates(project_id)
                file_writer.write_data_to_file("templates.json", templates)
                # Additional processing for milestones, suites, etc.
                # ...

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
