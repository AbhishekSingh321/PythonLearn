from flask import *

app=Flask(__name__)

@app.route('/')
def Home():
  return 'Hello This is Flask Server'

if __name__=='__main__':
  app.run(debug=True,port=3157)