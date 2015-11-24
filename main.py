from flask import Flask, render_template, request
from forms import DeploymentForm
import re
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somethingsomethingdarkside'

@app.route('/')
def index():
    json_file = open('static/calendar_info.json', encoding='utf-8')
    json_text = json_file.read()

    return render_template('home.html', json_text=json_text)

@app.route('/new_deployment', methods=['GET', 'POST'])
def new():
    json_file = 'static/calendar_info.json'
    form = DeploymentForm(request.form)

    if request.method == 'GET':
        return render_template('deployment_form.html', form=form, json_file=json_file)
    elif request.method == 'POST':
        lcr_number = form.lcr_number.data
        change_type = form.change_type.data
        tech_service_name = form.tech_service_name.data
        description = form.description.data
        commit_info = form.commit_info.data
        contact_name = form.contact_name.data
        email_contacts = form.email_contacts.data
        deployment_date = form.deployment_date.data
        start_time = form.start_time.data

        data = {}
        deployment_date_time = deployment_date + 'T' + start_time
        json_dict = {"title": lcr_number, "start": deployment_date_time}

        with open(json_file) as f:
            data = json.load(f)

        data.append(json_dict)

        with open(json_file, 'w') as f:
            json.dump(data, f)

        return render_template('home.html', form=form, json_text=data)

@app.route('/calendar_json', methods=['GET', 'POST'])
def calendar_json():
    json_file = open('static/calendar_info.json')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
