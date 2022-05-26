from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])

def calculate():
    Cost=''
    if request.method=='POST' and 'total_cost' in request.form and 'n_pass' in request.form and 'pi' in request.form:
       Total_cost=float(request.form.get('total_cost')) 
       Passengers=float(request.form.get('n_pass'))
       Percentage=float(request.form.get('pi'))
       Cost=round((Passengers*Total_cost*(1-(Percentage/100)))/(Passengers*(Passengers-1)),2)
    return render_template("index.html",Cost=Cost)
