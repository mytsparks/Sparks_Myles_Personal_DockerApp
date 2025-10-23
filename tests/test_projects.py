import os
import tempfile
import DAL
import app as flask_app_module


def setup_temporary_db(tmp_path):
    db_file = str(tmp_path / "test_projects.db")
    DAL.DB_FILE = db_file
    DAL.init_db()
    return db_file


def test_projects_page_shows_no_projects(tmp_path):
    # Setup temp DB
    setup_temporary_db(tmp_path)

    app = flask_app_module.app
    app.config['TESTING'] = True

    with app.test_client() as client:
        resp = client.get('/projects')
        assert resp.status_code == 200
        body = resp.get_data(as_text=True)
        assert 'No Projects Yet' in body or 'Add your first project' in body


def test_add_project_and_listed(tmp_path):
    # Setup temp DB
    setup_temporary_db(tmp_path)

    app = flask_app_module.app
    app.config['TESTING'] = True

    with app.test_client() as client:
        # Post a new project
        resp = client.post('/add', data={
            'title': 'Posted Project',
            'description': 'Posted via test',
            'image_file_name': ''
        }, follow_redirects=True)

        # Should redirect to /projects and show the new title
        assert resp.status_code == 200
        body = resp.get_data(as_text=True)
        assert 'Posted Project' in body
        assert 'Posted via test' in body
