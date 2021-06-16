import csv
import os

from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route('/')
def my_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page_navigation(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        file = database.write(f'\n{email},{subject},{body}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csvfile:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        csv_file = csv.writer(csvfile, delimiter=',',
                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, body])


@app.route('/submit_page', methods=['POST', 'GET'])
def page():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        write_to_csv(data)
        return 'submitted successfully'
    else:
        return "oops!"

# @app.route('/works.html')
# def works_page():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about_user_page():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')
#
#
# @app.route('/components.html')
# def component_page():
#     return render_template('components.html')

# @app.route('/<username>/<int:post_age>')
# def hello_world(username, post_age):
#     return render_template('index.html', name=username, age=post_age)
#
#
# @app.route('/view.html')
# def view():
#     return render_template('view.html')
#
#
# @app.route('/view/show')
# def show():
#     return ':)'
