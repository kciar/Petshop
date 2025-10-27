from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, Length, NumberRange, ValidationError
from models import User, Product, Client

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProductForm(FlaskForm):
    id = HiddenField()  # <- campo oculto para edição
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    category = StringField('Category', validators=[DataRequired(), Length(min=1, max=100)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        product = Product.query.filter_by(name=name.data).first()
        if product and (not self.id.data or int(self.id.data) != product.id):
            raise ValidationError('Product name already exists.')

class ClientForm(FlaskForm):
    id = HiddenField()  # <- campo oculto para edição
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        client = Client.query.filter_by(email=email.data).first()
        if client and (not self.id.data or int(self.id.data) != client.id):
            raise ValidationError('Email already exists.')

class SaleForm(FlaskForm):
    client = SelectField('Client', coerce=int, validators=[DataRequired()])
    product = SelectField('Product', coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    sale_date = DateField('Sale Date', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Confirm Sale')
