from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import mysql.connector
import pandas as pd

from .forms import add_form
from .forms import formr
from .forms import edit_form
from .forms import filter_form

def index(request):
    return render(request, 'home.html')

def home(request):
	db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
	cursor = db.cursor()
	query = "SELECT * FROM Surgery"
	cursor.execute(query)
	ans = cursor.fetchall()
	#return render(request, "test.html")
	return render(request, "render.html", {'cursor':ans});
# Create your views here.

def add(request):

	if request.method == "POST":
		form = add_form(request.POST)
		if form.is_valid():
			dID = form.cleaned_data["DoctorID"]
			pID = form.cleaned_data["PatientID"]
			DT = pd.to_datetime(form.cleaned_data["DT"])
			DT = DT.strftime('%Y-%m-%d %H:%M')
			duration = form.cleaned_data["duration"]
			rID = form.cleaned_data["RoomID"]
			db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
			cursor = db.cursor()
			query = "CALL AddSurgery("+dID+","+pID+",'"+str(DT)+"',"+duration+","+rID+")"
			#print(query)
			cursor.execute(query)
			#query2 = "INSERT INTO Surgery (DoctorID, PatientID, `date-time`, duration, RoomID) VALUES (%s, %s, %s, %s, %s)"
			#cursor.execute(query2, (dID, pID, DT, duration, rID))
			#cursor.callproc('AddSurgery', args=(dID, pID, DT, duration, rID))
			db.commit()
			db.close()
			return redirect("home")
	else:
		form = add_form()
	return render(request, 'add.html', {"form": form})

def remove(request):
	if request.method == "POST":
		form = formr(request.POST)
		db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
		cursor = db.cursor()
		cursor.execute("SELECT SurgeryID FROM Surgery")
		choices = cursor.fetchall()
		choices = [(choice[0], choice[0]) for choice in choices]
		form.fields['SurgeryID'].choices = choices
		if form.is_valid():
			ID = form.cleaned_data["SurgeryID"]
			query = "DELETE FROM Surgery WHERE SurgeryID = %s"
			cursor.execute(query, (ID,));
			db.commit()
			db.close()
			return redirect("home")
	else:
		form = formr()	
		db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
		cursor = db.cursor()
		cursor.execute("SELECT SurgeryID FROM Surgery")
		choices = cursor.fetchall()
		choices = [(choice[0], choice[0]) for choice in choices]
		form.fields['SurgeryID'].choices = choices
		db.close()


	return render(request, 'add.html', {"form": form})

def edit(request):
	if request.method == "POST":
		form = edit_form(request.POST)
		db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
		cursor = db.cursor()
		cursor.execute("SELECT DISTINCT SurgeryID FROM Surgery")
		choices = cursor.fetchall()
		choices = [(choice[0], choice[0]) for choice in choices]
		form.fields['SurgeryID'].choices = choices
		if form.is_valid():
			SurgeryID = form.cleaned_data["SurgeryID"]
			DoctorID = form.cleaned_data["DoctorID"]
			PatientID = form.cleaned_data["PatientID"]
			DT = form.cleaned_data["DT"]
			duration = form.cleaned_data["duration"]
			RoomID = form.cleaned_data["RoomID"]
			
			cursor.callproc("EditSurgery", (SurgeryID, DoctorID, PatientID, DT, duration, RoomID))
			db.commit()
			db.close()
			return redirect("home")

	else:
		form = edit_form()
		db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
		cursor = db.cursor()
		cursor.execute("SELECT DISTINCT SurgeryID FROM Surgery")
		choices = cursor.fetchall()
		choices = [(choice[0], choice[0]) for choice in choices]
		form.fields['SurgeryID'].choices = choices
		db.close()
	return render(request, 'add.html', {"form": form})

def filter(request):
	if request.method == "POST":
		form = filter_form(request.POST)
		db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
		cursor = db.cursor()
		cursor.execute("SELECT DISTINCT RoomID FROM Surgery")
		choices = cursor.fetchall()
		choices = [(choice[0], choice[0]) for choice in choices]
		form.fields['RoomID'].choices = choices
		#db.close()
		if form.is_valid():
			RoomID = form.cleaned_data["RoomID"]
			DT1 = form.cleaned_data["FromDate"]
			DT2 = form.cleaned_data["ToDate"]
			query = "SELECT * FROM Surgery WHERE RoomID = %s AND `date-time` BETWEEN %s AND %s"
			cursor.execute(query, (RoomID, DT1, DT2))
			ans = cursor.fetchall()

			return render(request, "render.html", {'cursor':ans});

	else:
		form = filter_form()
		db = mysql.connector.connect(host="34.30.254.102", user="root", password="123456", database="project")
		cursor = db.cursor()
		cursor.execute("SELECT DISTINCT RoomID FROM Surgery")
		choices = cursor.fetchall()
		choices = [(choice[0], choice[0]) for choice in choices]
		form.fields['RoomID'].choices = choices
		db.close()

	return render(request, 'add.html', {"form": form})
