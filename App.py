from flask import Flask, render_template, url_for, redirect, flash, session, request
from conexao_mysql import *

from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='register'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)



@app.route('/')
def home():
    title = 'Home'
    return render_template('/pages/home.html', title=title)

@app.route('/about')
def about():
    title = 'About'
    return render_template('/pages/about.html', title=title)

@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('/pages/contact.html', title=title)




@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Register'
    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['upass']
        age = request.form['age']
        address = request.form['address']
        contact = request.form['contact']
        mail = request.form['mail']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO users (name, password, age, address, contact, mail) 
        VALUES (%s, %s, %s, %s, %s, %s)''',
                    [uname, password, age, address, contact, mail])
        mysql.connection.commit()
        flash('User Created Successfully', 'success')
        return redirect(url_for('login'))
    try:
        if session['aname'] != '':
            return render_template('/admin/manager.html', title='Manager')
    except Exception as e:
        print(e)
    try:
        if session['name'] != '':
            return render_template('/panel/dashboard.html', title='Dashboard')
    except Exception as e:
        print(e)
    return render_template('/pages/register.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login'
    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['upass']
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM users WHERE name=%s and password=%s', [name, password])
            res = cursor.fetchone()
            if res:
                session['name'] = res['name']
                session['pid'] = res['pid']
                return redirect(url_for('/panel/dashboard'))
            else:
                flash('Invalid User or Password.', 'danger')
                return redirect(url_for('login'))
        except Exception as e:
            print(e)
        finally:
            mysql.connection.commit()
            cursor.close()
    try:
        if session['name'] != '':
            return render_template('/panel/dashboard.html', title='Dashboard')
    except Exception as e:
        print(e)
    try:
        if session['aname'] != '':
            return render_template('/admin/manager.html', title='Manager')
    except Exception as e:
        print(e)
    return render_template('/pages/login.html', title=title)

@app.route('/user_profile')
def user_profile():
    title = 'User Profile'
    try:
        if session['name'] != '':
            cursor = mysql.connection.cursor()
            id = session['pid']
            query = 'SELECT * FROM users WHERE pid = %s'
            cursor.execute(query,[id])
            data = cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Users Not Found...!!!!', 'danger')
            else:
                return render_template('/pages/user_profile.html',res=data, title=title)
    except Exception as e:
        print(e)
    try:
        if session['aname'] != '':
            return render_template('/admin/manager.html', title='Manager')
    except Exception as e:
        print(e)
    return render_template('/pages/home.html', title='Home')

@app.route('/update_user',methods=['GET','POST'])
def update_user():
    if request.method == 'POST':
        name = request.form['name']
        #password = request.form['password']
        age = request.form['age']
        address = request.form['address']
        contact = request.form['contact']
        mail = request.form['mail']
        pid = session['pid']
        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE users 
        SET name = %s, age = %s, address = %s, contact = %s, mail = %s 
        WHERE pid = %s''',[name, age, address, contact, mail, pid])
        mysql.connection.commit()
       
        flash('User Updated Successfully', 'success')
        return redirect(url_for('user_profile'))
    return render_template('/pages/user_profile.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    title = 'Dashboard'
    try:
        if session['name'] != '':
            return render_template('/panel/dashboard.html', title=title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html')





@app.route('/admin', methods=['GET', 'POST'])
def admin():
    title = 'Admin'
    if request.method == 'POST':
        aname = request.form['aname']
        apass = request.form['apass']
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM admin WHERE aname = %s and apass = %s', [aname, apass])
            res = cursor.fetchone()
            if res:
                session['aname'] = res['aname']
                session['aid'] = res['aid']
                return redirect(url_for('manager'))
            else:
                flash('Invalid User or Password.', 'danger')
                return render_template('/admin/admin.html') 
        except Exception as e:
            print(e)
        finally:
            mysql.connection.commit()
            cursor.close()
    try:
        if session['aname'] != '':
            return render_template('/admin/manager.html', title='Manager')
    except Exception as e:
        print(e)
    try:
        if session['name'] != '':
            return render_template('/panel/dashboard.html', title='Dashboard')
    except Exception as e:
        print(e)
    return render_template('/admin/admin.html', title=title)

@app.route('/manager')
def manager():
    title = 'Manager'
    try:
        if session['aname'] != '':
            return render_template('/admin/manager.html', title=title)
    except Exception as e:
        print(e)
    return render_template('/pages/home.html')

@app.route('/view_users')
def view_users():
    title = 'View Users'
    try:
        if session['aname'] != '':
            cursor = mysql.connection.cursor()
            query = 'SELECT * FROM users'
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                flash('Users Not Found...!!!!', 'danger')
            return render_template('/admin/view_users.html',res=data, title=title)
        else:
            redirect(url_for('home'))
    except Exception as e:
        print(e)
    return render_template('/pages/home.html')   

@app.route('/delete_users/<string:id>', methods=['GET', 'POST'])
def delete_users(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM users WHERE pid = %s', [id])
    mysql.connection.commit()
    flash('User Deleted Successfully', 'danger')
    return redirect(url_for('view_users'))





if __name__ == '__main__':
    app.run(debug = True)