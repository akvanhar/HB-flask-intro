from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Webpage of Compliments</title>
        </head>
        <body>
            <h1>Hi! This is the home page.</h1>
            <a href="/hello">Take me to the 'hello' page!</a>
        </body>
    </html>
    """


# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet" method='post'>
                <label>What's your name? <input type="text" name="person"></label>
                <label>
                    Choose the compliment you would like to receive!
                <select name="compliment">
                    <option value="awesome">Awesome</option>
                    <option value="terrific">Terrific</option>
                    <option value="fantastic">Fantastic</option>
                    <option value="neato">Neato</option>
                    <option value="wowza">Wowza</option>

                </select>
                </label>
                <input type="submit">
            </form>

            <form action="/diss">
                <label>What's your name? <input type="text" name="person"></label>
                <label>
                    Choose the insult you would prefer to receive!
                <select name="insult">
                    <option value="smelly">Smelly</option>
                    <option value="terrible">Terrible</option>
                    <option value="poopy">Poopy</option>
                    <option value="gross">Gross</option>
                    <option value="bleh">Bleh</option>
                </select>
                </label>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet', methods=['POST'])
def greet_person():
    player = request.form.get("person")
    compchoice = request.form.get("compliment")

    #AWESOMENESS = [
    #    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

   # compliment = choice(AWESOMENESS)

    return html_gen("Compliment", player, compchoice)

@app.route('/diss')
def insult_person():
    player = request.args.get("person")
    insult = request.args.get("insult")

    return html_gen("Insult", player, insult)

def html_gen(descriptor, player, input_str):
    return_html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>%s for you</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (descriptor, player, input_str)
    return return_html

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
