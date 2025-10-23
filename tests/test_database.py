import os
import DAL


def test_db_init_and_crud(tmp_path):
    """Initialize a temporary DB, test add/get/delete via DAL functions."""
    db_file = str(tmp_path / "test_projects.db")

    # Point DAL to a temporary DB so we don't touch the real one
    DAL.DB_FILE = db_file
    # Initialize schema
    DAL.init_db()

    # DB file should be created
    assert os.path.exists(db_file)

    # Initially no projects
    projects = DAL.get_all_projects()
    assert isinstance(projects, list)
    assert projects == []

    # Add a project
    DAL.add_project('Test Project', 'A description for tests', 'test.png')

    projects = DAL.get_all_projects()
    assert len(projects) == 1
    p = projects[0]
    assert p['title'] == 'Test Project'
    assert 'description' in p and p['description'] == 'A description for tests'

    # Get by id
    fetched = DAL.get_project_by_id(p['id'])
    assert fetched is not None
    assert fetched['title'] == 'Test Project'

    # Delete and confirm gone
    DAL.delete_project(p['id'])
    assert DAL.get_all_projects() == []
