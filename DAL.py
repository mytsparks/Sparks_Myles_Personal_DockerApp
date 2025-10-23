import sqlite3
import os

# Database file path
DB_FILE = 'projects.db'

def init_db():
    """Initialize the database and create the projects table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create projects table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_file_name TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def get_all_projects():
    """Retrieve all projects from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, title, description, image_file_name FROM projects ORDER BY id DESC')
    projects = cursor.fetchall()
    
    conn.close()
    
    # Convert tuples to dictionaries for easier template usage
    return [{'id': project[0], 'title': project[1], 'description': project[2], 'image_file_name': project[3]} for project in projects]

def add_project(title, description, image_file_name=None):
    """Add a new project to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO projects (title, description, image_file_name)
        VALUES (?, ?, ?)
    ''', (title, description, image_file_name))
    
    conn.commit()
    conn.close()

def delete_project(project_id):
    """Delete a project by its ID."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    
    conn.commit()
    conn.close()

def get_project_by_id(project_id):
    """Get a specific project by its ID."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, title, description, image_file_name FROM projects WHERE id = ?', (project_id,))
    project = cursor.fetchone()
    
    conn.close()
    
    if project:
        return {'id': project[0], 'title': project[1], 'description': project[2], 'image_file_name': project[3]}
    return None
