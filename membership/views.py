import pyrebase
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NameForm, adlog
from django.contrib import messages
import json
import xlwt

# Create your views here.


config = {
    "apiKey": "AIzaSyAPppt439TK0Xra0JrUXzPG5Y_nzwjw9VM",
    "authDomain": "ven-u-book.firebaseapp.com",
    "projectId": "ven-u-book",
    "storageBucket": "ieee-membership.appspot.com",
    "messagingSenderId": "53562799873",
    "appId": "1:53562799873:web:0a1aa858e90885461a8d00",

    "databaseURL": "https://ieee-membership-default-rtdb.firebaseio.com/",

}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def index(request):
    form = NameForm()
    return render(request, 'index.html', {'form': form, })


def insert(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            contact = form.cleaned_data["contact"]
            year = form.cleaned_data["year"]
            branch = form.cleaned_data["branch"]
            x = database.child('count').get().val()
            database.child('students').child(x).child('name').set(name)
            database.child('students').child(x).child('email').set(email)
            database.child('students').child(x).child('contact').set(contact)
            database.child('students').child(x).child('year').set(year)
            database.child('students').child(x).child('branch').set(branch)
            database.child('count').set(x + 1)
            messages.add_message(request, messages.SUCCESS, name + ' ' + 'Submitted Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'ERROR OCCURRED')

    return redirect('home')


def adm(request):
    form = adlog()
    return render(request, 'admin.html', {'form': form})


def proc(request):
    if request.method == 'POST':
        form = adlog(request.POST)
        if form.is_valid():
            adname = form.cleaned_data["adname"]
            adpass = form.cleaned_data["adpass"]
            mdses = form.cleaned_data["mdses"]
            name = database.child('admin').child('user').get().val()
            passn = database.child('admin').child('pass').get().val()
            print(mdses)
            print(type(mdses))
            if adname == name and adpass == passn:
                if mdses == '0':
                    response = HttpResponse(content_type='application/ms-excel')
                    response['Content-Disposition'] = 'attachment; filename="IEEEMD.xls"'
                    wb = xlwt.Workbook(encoding='utf-8')
                    row_num = 0
                    ws = wb.add_sheet('IEEE MEMBER DATA')  # this will make a sheet named Users Data
                    columns = ['Name', 'Contact', 'Branch', 'Email', 'Year']
                    for col_num in range(len(columns)):
                        ws.write(row_num, col_num, columns[col_num])
                    s = database.child('students').shallow().get().val()
                    for i in s:
                        row_num += 1
                        stud = database.child('students').child(i).child('name').get().val()
                        con = database.child('students').child(i).child('contact').get().val()
                        br = database.child('students').child(i).child('branch').get().val()
                        em = database.child('students').child(i).child('email').get().val()
                        yr = database.child('students').child(i).child('year').get().val()

                        ws.write(row_num, 0, stud)
                        ws.write(row_num, 1, con)
                        ws.write(row_num, 2, br)
                        ws.write(row_num, 3, em)
                        ws.write(row_num, 4, yr)

                    wb.save(response)
                    return response

                elif mdses == '1001':
                    response = HttpResponse(content_type='application/ms-excel')
                    response['Content-Disposition'] = 'attachment; filename="IEEEMD.xls"'
                    wb = xlwt.Workbook(encoding='utf-8')
                    row_num = 0
                    ws = wb.add_sheet('IEEE MEMBER DATA')  # this will make a sheet named Users Data
                    columns = ['Name', 'Contact', 'Branch', 'Email', 'Year']
                    for col_num in range(len(columns)):
                        ws.write(row_num, col_num, columns[col_num])
                    s = database.child('students').shallow().get().val()
                    for i in s:
                        row_num += 1
                        stud = database.child('students').child(i).child('name').get().val()
                        con = database.child('students').child(i).child('contact').get().val()
                        br = database.child('students').child(i).child('branch').get().val()
                        em = database.child('students').child(i).child('email').get().val()
                        yr = database.child('students').child(i).child('year').get().val()

                        ws.write(row_num, 0, stud)
                        ws.write(row_num, 1, con)
                        ws.write(row_num, 2, br)
                        ws.write(row_num, 3, em)
                        ws.write(row_num, 4, yr)

                        database.child('count').set(0)
                    database.child('students').remove()
                    wb.save(response)
                    return response
    return redirect('ad1')
