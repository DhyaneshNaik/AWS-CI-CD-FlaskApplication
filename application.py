from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

application = Flask(__name__)
application.secret_key = "dhyanesh-naik"

# use while onnecting with local MySQL database
#app.config["MYSQL_USER"] = "root"
#app.config["MYSQL_PASSWORD"] = "Sunitanaik@0497"
#app.config["MYSQL_DB"] = "UserDetails"
#app.config["MYSQL_HOST"] = "localhost"
#app.config["MYSQL_CURSORCLASS"] = 'DictCursor'

# use while connecting with AWS MySQL database
application.config["MYSQL_HOST"] = "userdetails.ck2j6hk9ucgh.ap-south-1.rds.amazonaws.com"
application.config["MYSQL_USER"] = "admin"
application.config["MYSQL_PASSWORD"] = "Sunitanaik0497"
application.config["MYSQL_DB"] = "UserDetails"
application.config["MYSQL_CURSORCLASS"] = 'DictCursor'

mysql = MySQL(application)

@application.route("/")
def index():
    conn = mysql.connection.cursor()
    conn.execute("select * from Employees")
    data = conn.fetchall()
    conn.close()
    return render_template("index.html",employee=data)

@application.route("/add_employee",methods=['POST'])
def add_employee():
    conn = mysql.connection.cursor()
    try:
        if request.method == "POST":
            fname = request.form["fname"]
            lname = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]
            query = "INSERT INTO Employees (Fname,Lname,Emailid,Phone) values ('{0}','{1}','{2}','{3}')".format(fname,lname,email,phone)
            conn.execute(query)
            mysql.connection.commit()
            flash("Record Added Successfully.")
            return redirect(url_for("index"))
    except:
        flash("Error occurred.")
    finally:
        conn.close()

@application.route("/edit/<int:id>",methods=['POST','GET'])
def get_employee(id):
    conn = mysql.connection.cursor()
    conn.execute(f"select * from Employees where id = {id}")
    data = conn.fetchall()[0]
    conn.close()
    return render_template("edit.html",data=data)

@application.route("/update/<id>",methods=['POST'])
def update_employee(id):
    conn = mysql.connection.cursor()
    try:
        if request.method == "POST":
            fname = request.form["fname"]
            lname = request.form["lname"]
            email = request.form["email"]
            phone = request.form["phone"]
            query = f"update Employees set FName = '{fname}',Lname='{lname}',Emailid='{email}',Phone='{phone}' where id = {id}"
            conn.execute(query)
            mysql.connection.commit()
            flash("Record Updated")
            return redirect(url_for("index"))
    except:
        flash("Exception Occured")
    finally:
        conn.close()


@application.route("/delete/<id>")
def delete_employee(id):
    conn = mysql.connection.cursor()
    conn.execute(f"delete from Employees where id = {id}")
    mysql.connection.commit()
    conn.close()
    flash("Record deleted.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    application.run()#debug=True