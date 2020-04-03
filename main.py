#from flask we are importing a flask app , render_templete,request
from flask import Flask ,  render_template , request
#declare the app
app=Flask(__name__)

#starting an app route which is '/'
@app.route('/')
#declaring the main function 
def main():
    return render_template('templete.html')








#decalaring the debug mode on 
if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

