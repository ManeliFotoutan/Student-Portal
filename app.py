import json
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

data_dir = os.path.join(os.path.dirname(__file__), 'data')

data_file = 'student_details.json'
courses_file='courses_data.json'

def limit_words(description, word_count=10):
    words = description.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'
    return description

app.jinja_env.filters['limit_words'] = limit_words

def load_courses():
    try:
        with open(courses_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_courses(courses):
    with open(courses_file, 'w') as file:
        json.dump(courses, file, indent=4)

def load_student_details():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            'name': 'your name',
            'email': 'example@gmail/email/....com',
            'major': 'what you study',
        }

def save_student_details(details):
    with open(data_file, 'w') as file:
        json.dump(details, file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=['GET'])
def profile():
    student_details = load_student_details()
    return render_template('profile.html', student=student_details)

@app.route('/profile/update', methods=['POST'])
def update_profile():
    name = request.form.get('name')
    email = request.form.get('email')
    major = request.form.get('major')

    student_details = {
        'name': name,
        'email': email,
        'major': major,
    }
    
    save_student_details(student_details)

    return redirect(url_for('profile'))

@app.route('/courses')
def courses():
    courses_list = load_courses()
    return render_template('courses.html', courses=courses_list)

@app.route('/courses/<int:course_id>')
def course_detail(course_id):
    courses_list = load_courses()
    course = next((course for course in courses_list if course['id'] == course_id), None)
    if course is None:
        return "Course not found", 404
    return render_template('course_detail.html', course=course)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        teacher = request.form.get('teacher')
        schedule = request.form.get('schedule')
        location = request.form.get('location')

        if not all([name, description, teacher, schedule, location]):
            return "All fields are required!", 400

        courses_list = load_courses()

        new_id = max(course['id'] for course in courses_list) + 1 if courses_list else 1

        new_course = {
            'id': new_id,
            'name': name,
            'description': description,
            'teacher': teacher,
            'schedule': schedule,
            'location': location,
        }
        courses_list.append(new_course)

        save_courses(courses_list)

        return redirect(url_for('courses'))

    return render_template('add_course.html')


if __name__ == '__main__':
    app.run(debug=True)
