from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Enter your Gmail address
app.config['MAIL_PASSWORD'] = 'your_password'         # Enter your Gmail password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_message', methods=['POST'])
def submit_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    msg = Message('New Message from Portfolio Contact Form',
                  sender='your_email@gmail.com',   # Enter your Gmail address
                  recipients=['nikhilbiradar800@gmail.com'])  # Enter your email address

    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    
    mail.send(msg)
    
    return 'Message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
