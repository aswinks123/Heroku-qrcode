#Created By : Aswin KS
#This API check whether a number is plindrome or amstrong

from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/amstrong/<int:n>')
def amstrong(n):
    sum=0
    order=len(str(n))
    copy_n=n
    while(n>0):
        digit=n%10
        sum+=digit **order
        n=n//10
    if (sum==copy_n):

        result={

            "Number":copy_n,
            "Is Amstrong ?": True

        }


    else:
        print("not Amstrong")
        result = {

            "Number": copy_n,
            "Amstrong": False

        }

    return jsonify(result)

@app.route('/palindrome/<int:n>')
def palindrome(n):
    x=n
    num = n
    temp = num
    rev = 0
    while(num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if(temp == rev):
        result = {

            "Number": x,
            "Palindrome": True

        }
    else:
        result = {

            "Number": x,
            "Palindrome": False

        }
    return jsonify(result)









if __name__ == '__main__':
    app.run(debug=True)