from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('dia_LR.pkl')


@app.route('/')
def webpage():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    

    print (preg , plas , pres , skin , test , mass , pedi , age )

    output = model.predict([[preg , plas , pres , skin , test , mass , pedi , age]])
    if output[0]==1:
        out = 'Diabetic'
    else:
        out = 'Not Diabetic'
    return render_template('predict.html', pred = out)

if __name__ == '__main__':
        app.run(debug=True)

