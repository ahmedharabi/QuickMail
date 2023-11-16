import flet as ft
from email.message import EmailMessage
from flet_core.control_event import ControlEvent
import smtplib
from flet import TextField,Row,Column


def main(page: ft.Page):

    #window sizing
    page.title = "QuickMail"
    page.window_width=400
    page.window_height=500
    page.window_resizable=False
    page.window_maximizable=False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #colors
    c1=color = ft.colors.with_opacity(1, '#191a1e')
    page.bgcolor = c1
    borderColor=ft.colors.with_opacity(1, '#078b64')
    page.window_center()

    #functions
    def evaluateFields(destination,sender,object,subject,password):
        if(destination=="" or sender=="" or object=="" or subject =="" or password==""):
            return True
        else: return False

    def getTeacherFromSubjectName(subjectName):
        if(subjectName==""):
            return ""

        subject_teacher={"Algebra":"aymen.hadjsalem@isimg.tn"
            ,"Calculus":"gamerthe462@gmail.com"
            ,"DataBases":"olfa.jemai@isimg.tn"
            ,"Language theory":"hela.lajmi@isimg.tn"
            ,"Java I":"sofiane.hachicha@isimg.tn"
            ,"C++":"assili.moha@gmail.com"
            ,"Os 2":"ali.othman@isimg.tn"
            ,"Networks":"amani.chaker@isimg.tn"}
        return subject_teacher[subjectName]

    def deleteFields(e:ControlEvent):
        myEmailAdress.value=""
        password.value=""
        object.value=""
        subject.value=""
        ddMenu.value=""
        emailStatus.value=""
        page.update()

    def sendMail(e:ControlEvent):
        # you must unable access to less secure application in your Gmail account
        em=EmailMessage()
        em['From']=myEmailAdress.value
        em['To']=getTeacherFromSubjectName(ddMenu.value)
        em['subject']=object.value
        em.set_content(subject.value)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        if(evaluateFields(getTeacherFromSubjectName(ddMenu.value),myEmailAdress.value,object.value,subject.value,password.value)):
            emailStatus.value="Please Fill The Remaining Fields"
            page.update()
        else:
            try:
                server.login(myEmailAdress.value, password.value)
                server.sendmail(myEmailAdress.value,getTeacherFromSubjectName(ddMenu.value),em.as_string())
                emailStatus.value="Email sent succesfully"
                page.update()
            except smtplib.SMTPAuthenticationError:
                emailStatus.value="Wrong Email Or Password Please Try Again"
                page.update()


    deletedEverythingBTN = ft.ElevatedButton("Clear",on_click=deleteFields,color=borderColor)
    sendEmailBTN = ft.ElevatedButton("Send",on_click=sendMail,color=borderColor)
    myEmailAdress: TextField = ft.TextField(value="", label="Sender", width=300,border_color=borderColor,focused_color="white",bgcolor=borderColor)
    #destination: TextField = ft.TextField(value="", label="Destination", width=300)
    object: TextField = ft.TextField(value="", label="Object", width=300,border_color=borderColor,focused_color="white",bgcolor=borderColor)
    subject: TextField = ft.TextField(value="", label="Subject", width=300, multiline=True, max_lines=5,border_color=borderColor,focused_color="white",bgcolor=borderColor)
    password: TextField = ft.TextField(value="", label="Password", width=300, password=True, can_reveal_password=True,border_color=borderColor,focused_color="white",bgcolor=borderColor)
    emailStatus: TextField = ft.TextField(value="", border=None, read_only=True, border_width=0,width=500)
    ddMenu=ft.Dropdown(
            label="Course",
            hint_text="Choose your Course?",
            options=[
                ft.dropdown.Option("Algebra"),
                ft.dropdown.Option("Calculus"),
                ft.dropdown.Option("DataBases"),
                ft.dropdown.Option("Language theory"),
                ft.dropdown.Option("Java I"),
                ft.dropdown.Option("C++"),
                ft.dropdown.Option("Os 2"),
                ft.dropdown.Option("Networks"),
            ],width=300,color=borderColor,border=None,bgcolor=borderColor,focused_border_color=borderColor,border_color=borderColor,value="")
    page.add(ft.Column([myEmailAdress, password,ddMenu, object, subject,ft.Row([deletedEverythingBTN,sendEmailBTN]),ft.Row([emailStatus])]))


ft.app(target=main,assets_dir="icons")
