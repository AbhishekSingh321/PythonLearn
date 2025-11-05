from flask import *

app=Flask(__name__)

with open('data.json',encoding='utf-8') as f:
  data=json.load(f)

@app.route('/<name>')
def Profile(name):
  if name in data:
    user=data[name]
    return render_template('index.html',n=name,d=user)
  else:
    return render_template('error.html')

if __name__=='__main__':
  app.run(debug=True,port=3157)