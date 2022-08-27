from app.configuration.flask_configuration import create_app
from app.scheduler.schedule_job import run_job
from waitress import serve


if __name__ == '__main__':
    app = create_app()
    run_job()
    app.run(port=8087, debug=True)
