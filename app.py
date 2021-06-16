from flask import Flask, request, render_template
from random import randint,  choice, sample
#from flask_debugtoolbar import DebugToolbarExtension
from stories import story
app = Flask(__name__)

    
@app.route('/')
def questions():

    '''Return questions form for the game to start'''
    word_prompt = story.prompts
    '''calls in the template questions to be "filled"'''
    return render_template('/questions.html', prompts = word_prompt)

@app.route('/answers')
def story_txt(): 
    '''generates compiled and organized final text'''
    sentence = story.generate(request.args)
    return render_template('/answers.html', text = sentence)