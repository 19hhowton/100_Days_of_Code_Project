from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired(), Length(max=20)])
    url = StringField('Cafe Cocation on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired(), Length(max=6)])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired(), Length(max=6)])
    
    coffee_rating = SelectField('Coffee Rating', choices=[
        ('☕','☕'),
        ('☕☕','☕☕'),
        ('☕☕☕','☕☕☕'), 
        ('☕☕☕☕','☕☕☕☕'), 
        ('☕☕☕☕☕','☕☕☕☕☕')])
    wifi_rating = SelectField('Wifi Strength Rating', choices=[
        ('💪','💪'),
        ('💪💪','💪💪'),
        ('💪💪💪','💪💪💪'), 
        ('💪💪💪💪','💪💪💪💪'), 
        ('💪💪💪💪💪','💪💪💪💪💪')])                       
    power_rating = SelectField('Power Socket Availability', choices=[
        ('🔌','🔌'),
        ('🔌🔌','🔌🔌'),
        ('🔌🔌🔌','🔌🔌🔌'), 
        ('🔌🔌🔌🔌','🔌🔌🔌🔌'), 
        ('🔌🔌🔌🔌🔌','🔌🔌🔌🔌🔌')])                      
    submit = SubmitField('Submit')
