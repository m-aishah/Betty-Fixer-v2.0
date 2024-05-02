from flask import Flask, render_template, request
import subprocess
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get the text from the form
        c_code = request.form['text']

        # Write the text to a file
        with open('input.c', 'w') as original_file:
            original_file.write(c_code)

        # Invoke the C code as a subprocess, passing the filename as an argument
        c_files = glob.glob("BettyFixerFiles/Betty-Fixer/*.c")
        command = ["gcc"] + c_files + ["-o", "bettyfixer"]
        subprocess.run(command)
        subprocess.run(["./bettyfixer", "input.c"])
        # Read the formatted output from the file generated by the c code
        with open('input.c', 'r') as formatted_file:
            formatted_code = formatted_file.read()
        
        # Render a template with the formatted code
        return render_template('formatted.html', formatted_code=formatted_code)

if __name__ == '__main__':
    app.run(debug=True)