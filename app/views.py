from datetime import datetime
from app import app
from flask import Flask,  render_template, request, redirect, url_for, flash

###
# Routing for your application.
###


@app.route('/')
def home():
   """Render website's home page."""
   return render_template('home.html')



@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jhanell Edwards")

@app.route('/profile')
def  profile():
    profile_data = {
        'full_name': 'Jhanell Edwards',
        'username': 'kalex',
        'location': 'Kingston',
        'join_date': '2021, 2, 21',
        'short_bio': 'As a computer science student, I am fascinated by algorithms and problem-solving, especially in AI and machine learning.Proficient in Python, Java, and C++, I am passionate about developing scalable software solutions. Engaging in coding competitions and collaborative projects, I am dedicated to mastering the dynamic landscape of computer science.',
        'num_posts': 100,
        'num_followers': 500,
        'num_following': 300
    }
   
    return render_template('profile.html', profile_data=profile_data)



def format_date_joined(date):
    # Assuming date is a datetime object
    return date.strftime("%b, %Y")
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
