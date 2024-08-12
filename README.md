# Student Portal

Welcome to the Student Portal project! This web application allows students to view their profiles, see a list of courses, and view details about each course. Teachers can add new courses and manage student enrollments. The portal is built using Flask, a lightweight web framework for Python.

## Features

- **Student Profile Management**: Students can view and update their profile information.
- **Course List**: Students can view a list of available courses.
- **Course Details**: Students can view details about each course.
- **Course Management**: Teachers can add new courses to the portal.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Jinja2**: Templating engine used by Flask for rendering HTML.
- **JSON**: Used for storing and retrieving data.

## Usage

-**Students**:
View and update your profile by navigating to /profile.
Browse available courses at /courses.
View details about a course by selecting it from the list.
-**Teachers**:
Add new courses by going to /add_course.

## Code Explanation

### `app.py`
- **Purpose**: Contains the core application logic, including route definitions and request handlers for the Flask web application.
- **Details**: Handles routing for different endpoints such as the home page, profile management, course listing, and course details. It also includes functions for loading and saving data.

### `data/student_details.json`
- **Purpose**: Stores student profile information.
- **Details**: This JSON file contains basic information about students, such as their name, email, and major. It is used by the application to display and update student profiles.

### `data/courses_data.json`
- **Purpose**: Stores course details.
- **Details**: This JSON file holds information about the courses available in the portal. Each course entry includes details such as the course name, description, teacher, schedule, and location.

## Contact

For any questions, feedback, or inquiries, please reach out to [maneli0foroutan@gmail.com](mailto:maneli0foroutan@gmail.com).

