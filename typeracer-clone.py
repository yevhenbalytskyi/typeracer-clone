from flask import Flask, render_template
import random

app = Flask(__name__)


texts = [
	"No more will my green sea go turn a deeper blue. I could not foresee this thing happening to you. If I look hard enough into the setting sun, my love will laugh with me before the morning comes.",
	"Say what you will. But a person just cannot know what he doesn't know. And you can't always see that a bad thing is going to happen before it happens. If you could, no bad would ever come.",
	"You must take life the way it comes at you and make the best of it.",
	"I don't care who you are, where you're from, what you did, as long as you love me. Every little thing that you have said and done feels like it's deep within me. Doesn't really matter if you're on the run, it seems like we're meant to be.",
	"You must have a goal because it's just as difficult to reach a destination you don't have, as it is to come back from a place you've never been.",
	"For as it is not one swallow or one fine day that makes a spring, so it is not one day or a short time that makes a man blessed and happy.",
	"Then we saw him pick up all the things that were down. He picked up the cake, and the rake, and the gown, and the milk, and the strings, and the books, and the dish, and the fan, and the cup, and the ship, and the fish.",
	"There is nothing sweeter in this sad world than the sound of someone you love calling your name.",
	"The quick brown fox jumps over the lazy dog.",
	"They can only see the mere show, and never can tell what it really means.",
	"You crushed us to build your monarchy on the backs of our blood and bone. Your mistake wasn't keeping us alive. It was thinking we'd never fight back!",
	"When a free man dies, he loses the pleasure of life. A slave loses his pain. Death is the only freedom a slave knows. That's why he's not afraid of it. That's why we'll win.",
	"Intrigued by that enigma, he dug so deeply into her sentiments that in search of interest he found love, because by trying to make her love him he ended up falling in love with her.",
	"JavaScript supports the basic data types of numbers and strings. All numbers are 64-bit double precision, and range from -5e-324 to 1.7976931348623157e308.",
	"But if in efficient causes it is possible to go on to infinity, there will be no first efficient cause, neither will there be an ultimate effect, nor any intermediate efficient causes; all of which is plainly false. Therefore it is necessary to admit a first efficient cause, to which everyone gives the name of God.",
]

@app.route('/')
def hello():
    return render_template('index.html', text=random.choice(texts))


if __name__ == '__main__':
	app.run(debug=True)