import pyrebase
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse


config={
  "apiKey": "AIzaSyBWCHffbPKbZPDeMBdW_RlLWrVD065At2U",
  "authDomain": "rfid-aa9b8.firebaseapp.com",
  "databaseURL": "https://rfid-aa9b8-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "rfid-aa9b8",
  "storageBucket": "rfid-aa9b8.appspot.com",
  "messagingSenderId": "605391587609",
  "appId": "1:605391587609:web:8dbc1520abe4c9e81f1d88"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def welcome(request):
    uid = database.child("RFID").get().val()
    date = database.child("RFID").child("uid").get().val()
    return render(request, 'index.html', {
        "uid":uid,
        "date":date
    })