import os,demo
"""
certifi==2021.5.30
charset-normalizer==2.0.4
click==8.0.1
colorama==0.4.4

Flask==2.0.1
idna==3.2
importlib-metadata==4.7.1
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
requests==2.26.0
typing-extensions==3.10.0.0
urllib3==1.26.6
Werkzeug==2.0.1
zipp==3.5.0

"""
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        sttr = demo.main2()
        saar=sttr[0]
        saar=str(saar)
        return saar
    except Exception as e:
        zz=str(e)
        aa=zz+"yyyyyyyyyyyy"
        return aa
    return "uuuuuuuuuuuuuuu"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
