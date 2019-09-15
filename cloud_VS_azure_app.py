from flask import Flask
cloud_VS_azure_app=Flask(__name__)

@cloud_VS_azure_app.route("/")
def hello():
    return "welcome to flaskthing"
