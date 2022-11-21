from flask import Flask, request, Response


app = Flask(__name__)


@app.route('/alkuluku/<numero>')
def primecheck(numero):
    number = int(numero)
    if number > 1:

        for i in range(2, number):
            if (number % i) == 0:
                print(number, " ei alkuluku.")
                break
        else:
            print(number, " alkuluku.")

    else:
        print(number, " ei alkuluku.")


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)