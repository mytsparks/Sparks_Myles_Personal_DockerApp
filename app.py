from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from DAL import init_db, get_all_projects, add_project, delete_project

app = Flask(__name__)

# Initialize database on startup
init_db()

# --- Static asset routes ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Page routes using templates ---
@app.get('/')
def home():
  return render_template('home.html')

@app.get('/about')
def about():
  return render_template('about.html')

@app.get('/contact')
def contact():
  return render_template('contact.html')

@app.get('/projects')
def projects():
  projects = get_all_projects()
  return render_template('projects.html', projects=projects)

@app.get('/resume')
def resume():
  return render_template('resume.html')

@app.get('/thankyou')
def thankyou():
  return render_template('thankyou.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
  if request.method == 'POST':
    title = request.form.get('title')
    description = request.form.get('description')
    image_file_name = request.form.get('image_file_name')
    
    if title and description:
      add_project(title, description, image_file_name)
      return redirect(url_for('projects'))
  
  return render_template('add_project.html')

@app.get('/delete/<int:project_id>')
def delete(project_id):
  delete_project(project_id)
  return redirect(url_for('projects'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))