import os

from dotenv import load_dotenv

from app.configuration.flask_configuration import create_app
from app.scheduler.schedule_job import run_job


def init_dotenv():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(base_dir, '.env'))


if __name__ == '__main__':
    init_dotenv()
    app = create_app()
    run_job()
    app.run(port=8087, debug=True)
