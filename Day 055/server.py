from flask import Flask
import random

app = Flask(__name__)

RANDOM_NUMBER = random.randint(0, 9)
print(RANDOM_NUMBER)

@app.route("/")
def home():
    return '<h1 style="text-align: left">Guess a number between 0 and 9</h1>' \
           '<img src="https://media1.giphy.com/media/Kehzyp9EFa2IYDte8P/' \
           '200w.webp?cid=ecf05e47s3d4amr73pnpphwbua15wexi2pwp4i6fb2yubosz&rid=200w.webp&ct=g" width=400>'


@app.route('/<int:number>')
def input_number(number):
    print(number)
    if number == RANDOM_NUMBER:
        return f'<h1 style="color: Green">You guessed the correct number! {number}!!</h1>' \
               f'<img src="https://media3.giphy.com/media/a0h7sAqON67nO/200w.webp?' \
               f'cid=ecf05e47zad1n62d26kb8gqq76i27sgytnnigyabm7xj61ao&rid=200w.webp&ct=g" width=400>'
    elif number < RANDOM_NUMBER:
        return f'<h1 style="color: Red">Too low, Try again!</h1>' \
               f'<img src="https://media4.giphy.com/media/3og0IJXQEKwIdIEYpy/200w.webp?' \
               f'cid=ecf05e47qsiu5fri1goq57krbv4enqyu9p80ta6qs1e86ugp&rid=200w.webp&ct=g" width=400>'
    else:
        return f'<h1 style="color: Violet">Too high, Try again!</h1>' \
               f'<img src="https://media3.giphy.com/media/fLyfhjZr9g47fTJMuk/200w.webp?' \
               f'cid=ecf05e47qsiu5fri1goq57krbv4enqyu9p80ta6qs1e86ugp&rid=200w.webp&ct=g" width=400>'


if __name__ == "__main__":
    app.run(debug=True)
