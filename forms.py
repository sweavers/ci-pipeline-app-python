from wtforms import BooleanField, TextField, PasswordField, validators, IntegerField, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import DateField, DateTimeField
from wtforms.validators import DataRequired, ValidationError, NumberRange, Email
from flask.ext.wtf import Form

class DeploymentForm(Form):
    lcr_number = SelectField('LCR Number', choices=[('32716', '32716 - Digital Register View'), ('32719', '32719 - Register Data Migration'), ('32724', '32724 - Land Charges'), ('32731', '32731 - Counter Fraud')])
    change_type = SelectField('Change Type', choices=[('Standard', 'Standard'), ('Emergency', 'Emergency')], default='Standard')
    tech_service_name = SelectField('Technical Service Name', choices=[('1', 'Application: Digital Register View'), ('2', 'Data Transport: Register Migration')])
    description = TextAreaField('Description', [validators.Length(min=1, max=500)])
    commit_info = TextField('Commit Information', [validators.Length(min=1, max=200)])
    contact_name = TextField('Contact Name', [validators.Length(min=1, max=200)])
    email_contacts = TextAreaField('Email Contacts', [validators.Length(min=1, max=500)])
    deployment_date = TextField('Deployment Date', [validators.Length(min=1, max=200)])
    start_time = SelectField('Deployment Time', choices=[('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], default='19')
