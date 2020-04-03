#from flask we are importing a flask app , render_templete,request
from flask import Flask ,  render_template , request
#declare the app
app=Flask(__name__)

#starting an app route which is '/'
@app.route('/')
#declaring the main function 
def main():
    return render_template('templete.html')


#form submission url
@app.route('/send',methods=['POST'])
def send(sum=sum):
    if request.method=='POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('templete.html',sum=sum)
        elif operation == 'devide':
            sum = float(num1) / float(num2)
            return render_template('templete.html',sum=sum)
        elif operation == 'substract':
            sum = float(num1) - float(num2)
            return render_template('templete.html',sum=sum)
        elif operation == 'multiply':
            sum  = float(num1) * float(num2)
            return render_template('templete.html',sum=sum)
        else :
            return render_template('templete.html')

        







#decalaring the debug mode on 
if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

