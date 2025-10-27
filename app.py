from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from config import Config
from models import db, User, Product, Client, Sale
from forms import LoginForm, ProductForm, ClientForm, SaleForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/products', methods=['GET', 'POST'])
@login_required
def products():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, category=form.category.data, price=form.price.data, quantity=form.quantity.data)
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully', 'success')
        return redirect(url_for('products'))
    products = Product.query.all()
    return render_template('products.html', form=form, products=products)

@app.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.category = form.category.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        db.session.commit()
        flash('Product updated successfully', 'success')
        return redirect(url_for('products'))
    return render_template('products.html', form=form, product=product)

@app.route('/products/delete/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('products'))

@app.route('/clients', methods=['GET', 'POST'])
@login_required
def clients():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(name=form.name.data, phone=form.phone.data, email=form.email.data)
        db.session.add(client)
        db.session.commit()
        flash('Client added successfully', 'success')
        return redirect(url_for('clients'))
    clients = Client.query.all()
    return render_template('clients.html', form=form, clients=clients)

@app.route('/clients/edit/<int:client_id>', methods=['GET', 'POST'])
@login_required
def edit_client(client_id):
    client = Client.query.get_or_404(client_id)
    form = ClientForm(obj=client)
    if form.validate_on_submit():
        client.name = form.name.data
        client.phone = form.phone.data
        client.email = form.email.data
        db.session.commit()
        flash('Client updated successfully', 'success')
        return redirect(url_for('clients'))
    return render_template('clients.html', form=form, client=client)

@app.route('/clients/delete/<int:client_id>', methods=['POST'])
@login_required
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    flash('Client deleted successfully', 'success')
    return redirect(url_for('clients'))

@app.route('/sales', methods=['GET', 'POST'])
@login_required
def sales():
    form = SaleForm()
    form.client.choices = [(client.id, client.name) for client in Client.query.all()]
    form.product.choices = [(product.id, product.name) for product in Product.query.all()]
    if form.validate_on_submit():
        product = Product.query.get(form.product.data)
        if product.quantity >= form.quantity.data:
            sale = Sale(product_id=form.product.data, client_id=form.client.data, quantity=form.quantity.data, total=product.price * form.quantity.data, sale_date=form.sale_date.data)
            product.quantity -= form.quantity.data
            db.session.add(sale)
            db.session.commit()
            flash('Sale registered successfully', 'success')
        else:
            flash('Insufficient stock', 'danger')
    return render_template('sales.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)