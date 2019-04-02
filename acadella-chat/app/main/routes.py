from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    """Main route which will prompt for login"""
    return render_template('index.html')

