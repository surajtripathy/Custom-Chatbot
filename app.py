from flask import Flask , render_template, request
from myfirstui import init_ui
import chatbot_test
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return 'THIS IS A PROGRAM.'

@app.route("/trigger_della", methods=["POST"])

def start_della():
    #chatbot_test.count_della_started
    msg=request.data.decode("utf-8");
    if(chatbot_test.count_della_started == 0):
        chatbot_test.count_della_started += 1
        if(msg == "Hello"):
            return_msg = chatbot_test.get_greetings()
        else:
            return_msg = "Please greet Della with 'Hello' to spark up a conversation!"
    elif(chatbot_test.count_della_started == 1):
        chatbot_test.count_della_started += 1
        return_msg = chatbot_test.get_cust_id(msg)

    else:
        return_msg_temp = chatbot_test.get_reply(msg)
        if(return_msg_temp[1] == 1):
            return_msg = "Productoboy says " + return_msg_temp[0]
        elif(return_msg_temp[1] == 2):
            return_msg =  "Jackotime says " + return_msg_temp[0]
    # implement the chatbot_test functionality with the msg as in input
    # reply = chatbot_test.get_reply(msg)
    # pass msg to chatbot_test to get data
    return return_msg,200;


if __name__ == "__main__":
    print("server is running on localhost")
    app.run(debug=True)


