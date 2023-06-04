from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    table = [
        {
            "name": "Soma",
            "phone": 17166044029,
            "value1": 2,
            "value2": 1,
            "value3": 1
        },
        {
            "name": "Sekhar",
            "phone": 18903459022,
            "value1": 3,
            "value2": 18,
            "value3": 1
        },
        {
            "name": "Li",
            "element": "Lithium",
            "atomic_mass": "6.941",
            "value1": 1,
            "value2": 2
        },
        {
            "name": "Be",
            "element": "Beryllium",
            "atomic_mass": "9.012182",
            "value1": 2,
            "value2": 2
        }
    ]
    return render_template('index.html', table=table)

if __name__ == '__main__':
    app.run()
