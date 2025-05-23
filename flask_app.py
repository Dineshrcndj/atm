from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

user_data={'dinesh':{'password':'123','amount':5000}}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username not in user_data:
            user_data[username]={'password':password,'amount':0}
            return redirect(url_for('login'))
        else:
            return 'Username already exists'
    return render_template('register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username in user_data and user_data[username]['password']==password:
            return redirect(url_for('dashboard',dashboard_username=username))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/dashboard/<dashboard_username>')
def dashboard(dashboard_username):
    return render_template('dashboard.html',wdash_username=dashboard_username)

@app.route('/deposit/<dusername>',methods=['GET','POST'])
def deposit(dusername):
    if request.method=='POST':
        amount=int(request.form['amount'])
        user_data[dusername]['amount']+=amount
        return redirect(url_for('dashboard',dashboard_username=dusername))
    return render_template('deposit.html',dusername=dusername)

@app.route('/withdraw/<wusername>',methods=['GET','POST'])
def withdraw(wusername):
    if request.method=='POST':
        amount=int(request.form['amount'])
        if user_data[wusername]['amount']>=amount:
            user_data[wusername]['amount']-=amount
            return redirect(url_for('dashboard',dashboard_username=wusername))
        else:
           return 'Not enough balance'
    return render_template('withdraw.html',wusername=wusername)

@app.route('/balance/<busername>')
def balance(busername):
    return render_template('balance.html',busername=busername,amount=user_data[busername]['amount'])

app.run(use_reloader=True,debug=True)