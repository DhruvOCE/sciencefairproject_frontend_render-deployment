from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def home_page():
    print("Home route accessed")
    return render_template('homepage.html')

@app.route('/about')
def about_us():
    print("About route accessed")
    return render_template('About.html') 
if __name__ == '__main__':
    app.run(debug=True)
