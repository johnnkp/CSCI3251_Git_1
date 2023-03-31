from flask import Flask


def check_type(my_name=None, my_id=None):
    if not my_name:
        return False
    else:
        if not isinstance(my_name, str):
            raise TypeError("name must be a string")
        if my_id:
            if not (isinstance(my_id, int) or (isinstance(my_id, str) and my_id.isdigit())):
                return False
            # if isinstance(my_id, str):
            #     if not my_id.isdigit():
            #         return False
        return True


# imagine these data is from db
myName = "Ng Kai Pong"
myId = "1155144829"
### end of data

app = Flask(__name__)


@app.route("/")
def hello_world():
    if check_type(myName, myId):
        return f"<p> Hello, my name is {myName}, my sid is {myId}</p>"
    else:
        return "<p> Hello, my name is unknown, my sid is unknown</p>"


""" import mysql.connector

class DBmanager:
    def __init__(self, database="example", user="root", password="mypass", host="localhost", port="3306"):
        self.conn = mysql.connector.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def get_stu_info(self, sid):
        self.cursor.execute(f"SELECT * FROM students WHERE stuid = {sid}")
        return self.cursor.fetchone()

conn = None

@app.route("/exp01")
def exp01():
    global conn
    if not conn:
        conn = DBmanager()
    rec = conn.get_stu_info(sid=1155144829)
    return f"<p> Hello, my name is {rec[1]}, my sid is {rec[0]}</p>"

@app.route("/test")
def test():
    rec = DBmanager().get_stu_info(sid=1155144829)
    return f"<p>Sid: {rec[0]}</p> <p>Name: {rec[1]}</p>" """

if __name__ == "__main__":
    app.run(debug=True)
