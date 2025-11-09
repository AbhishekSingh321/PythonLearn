from flask import *

app=Flask(__name__)

@app.route('/')
def Home():                                          
  return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def Login():                                            #request.method and  request.form
  if(request.method=='POST'):
    name=request.form.get('name')
    password=request.form.get('pass')
    if name and password:
      return f'{name} your validation completed!'
    else:
      return 'Not Validate!'
  return render_template('login.html')


if __name__=='__main__':
  app.run(debug=True,port=3157)