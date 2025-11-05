from flask import *

app=Flask(__name__)

@app.route('/<name>')
def Profile(name):
  data={
    'age' : 21,
    'class' : 'TE'
  }
  return render_template('index.html',n=name,d=data)

if __name__=='__main__':
  app.run(debug=True,port=3157)