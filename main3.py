from flask import Flask,render_template,request,flash,redirect,make_response
#import bcrypt
#import pdfkit
#import os
import mysql.connector
#import wkhtmltopdf
app=Flask(__name__)
config = {
  'user': '89Md18ICYd',
  'password': 'dhFpEPgWd1',
  'host': 'remotemysql.com',
  'database': '89Md18ICYd'
}
app.secret_key = 'many random bytes'
#mycursor=mydb.cursor()
@app.route('/EFT',methods=['POST','GET'])
def index():
        mydb=mysql.connector.connect(**config)
        #app.secret_key = 'many random bytes'
        mycursor=mydb.cursor()#mycursor.execute("SELECT Name,Comment FROM comment")
        mycursor.execute("select name,Comment from comment")
        data=mycursor.fetchall()
	#print(data)
        if(len(data)==0):
                print("no comments yet")
        if(len(data)!=0):
                #print(Name+" "+Comment)
                return render_template('Webpage.html',data=data)
                mycursor.close()
                mydb.close()
	#return render_template('Webpage.html')

@app.route('/comment',methods=['POST','GET'])
def comment():
	if(request.method=='POST'):
                data=request.form
                print(data)
                comment=data['comment']
                #print(comment)
                usrname=data['usrname']
                if len(comment)==0:
                       flash("Comment field should not be empty","warning")
                       return redirect('/EFT')
                if len(usrname)==0:
                       flash("Name field should not be empty","warning")
                       return redirect('/EFT')
                else:
                       mydb=mysql.connector.connect(**config)
                       mycursor=mydb.cursor()
                       mycursor.execute("insert into comment(Name,Comment) values(%s,%s)",(usrname,comment))
                       mydb.commit()
                       mycursor.close()
                       mydb.close()
                       flash("Posted","success")
                       return redirect('/EFT')
                       
        #return render_template('Webpage.html')
if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port='8081')

