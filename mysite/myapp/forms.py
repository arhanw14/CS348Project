from django import forms

class add_form(forms.Form):
	DoctorID = forms.CharField(label="Doctor ID", max_length=100)
	PatientID = forms.CharField(label="Patient ID", max_length=100)
	DT = forms.DateTimeField(label="Date and Time", input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD HH:MM'}))
	duration = forms.CharField(label="Duration (mins)", max_length=100)
	RoomID = forms.CharField(label="Room ID", max_length=100)

class formr(forms.Form):
	SurgeryID = forms.ChoiceField(label = "Surgery ID")	

class edit_form(forms.Form):
	SurgeryID = forms.ChoiceField(label = "Surgery ID")
	DoctorID = forms.CharField(label="Doctor ID", max_length=100)
	PatientID = forms.CharField(label="Patient ID", max_length=100)
	DT = forms.DateTimeField(label="Date and Time", input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD HH:MM'}))
	duration = forms.CharField(label="Duration (mins)", max_length=100)
	RoomID = forms.CharField(label="Room ID", max_length=100)

class edit_form2(forms.Form):
	DoctorID = forms.CharField(label="Doctor ID", max_length=100)
	PatientID = forms.CharField(label="Patient ID", max_length=100)
	DT = forms.DateTimeField(label="Date and Time", input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD HH:MM'}))
	duration = forms.CharField(label="Duration (mins)", max_length=100)
	RoomID = forms.CharField(label="Room ID", max_length=100)

class filter_form(forms.Form):
	FromDate = forms.DateTimeField(label="Starting Date/Time", input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD HH:MM'}))
	ToDate = forms.DateTimeField(label="Ending Date/Time", input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD HH:MM'}))
	RoomID = forms.ChoiceField(label="Room ID")


