import tkinter
from tkinter import *
import os
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#main screen
win = customtkinter.CTk() 
win.title("E-Wallet Manager")
#Untuk ukuran halaman
win.geometry("700x500+500+120")
win.resizable()


#Function
def register():
    regis = customtkinter.CTk()
    regis.geometry("320x500")
    regis.title("Register")
    regis.resizable(False, False)
    t1 = customtkinter.CTkLabel(master = regis, text = "Register", font = ('Century Gothic', 20))
    t1.place(x = 155, y = 20, anchor=tkinter.CENTER)

    def cancel_register():
        regis.destroy()

    global first_name
    global last_name
    global username
    global email
    global password
    global confirm_password
    global first_name_entry
    global last_name_entry
    global username_entry
    global email_entry
    global password_entry
    global confirm_password_entry
    global harian
    global notif

    first_name = StringVar()
    last_name = StringVar()
    username = StringVar()
    email = StringVar()
    password = StringVar()
    confirm_password = StringVar()
    harian = StringVar()

    first_name_lable = customtkinter.CTkLabel(master = regis, text = "First Name", font = ('Times New Roman', 15))
    first_name_lable.place(x = 65, y = 50)
    first_name_entry = customtkinter.CTkEntry(master = regis, width = 200, placeholder_text='First Name')
    first_name_entry.place(x = 60, y = 80)
    first_name = first_name_entry

    last_name_lable = customtkinter.CTkLabel(master = regis, text = "Last Name", font = ('Times New Roman', 15))
    last_name_lable.place(x = 65, y = 110)
    last_name_entry = customtkinter.CTkEntry(master = regis, width = 200, placeholder_text='Last Name')
    last_name_entry.place(x = 60, y = 140)
    last_name = last_name_entry

    username_lable = customtkinter.CTkLabel(master = regis, text = "Username", font = ('Times New Roman', 15))
    username_lable.place(x = 65, y = 170)
    username_entry = customtkinter.CTkEntry(master = regis, width = 200, placeholder_text='Username')
    username_entry.place(x = 60, y = 200)
    username = username_entry

    email_lable = customtkinter.CTkLabel(master = regis, text = "Email", font = ('Times New Roman', 15))
    email_lable.place(x = 65, y = 230)
    email_entry = customtkinter.CTkEntry(master = regis, width = 200, placeholder_text='Email')
    email_entry.place(x = 60, y = 260)
    email = email_entry

    password_lable = customtkinter.CTkLabel(master = regis, text = "Password", font = ('Times New Roman', 15))
    password_lable.place(x = 65, y = 290)
    password_entry = customtkinter.CTkEntry(master = regis, width = 200, placeholder_text='Password', show = "*")
    password_entry.place(x = 60, y = 320)
    password = password_entry

    confirm_password_lable = customtkinter.CTkLabel(master = regis, text = "Confirm Password", font = ('Times New Roman', 15))
    confirm_password_lable.place(x = 65, y = 350)
    confirm_password_entry = customtkinter.CTkEntry(master = regis, width = 200, placeholder_text='Confirm Password', show = "*")
    confirm_password_entry.place(x = 60, y = 380)
    confirm_password = confirm_password_entry

    cancel_button = customtkinter.CTkButton(master = regis, width = 50, text = "Cancel", command = cancel_register)
    cancel_button.place(x = 60, y = 470)


    regis_button = customtkinter.CTkButton(master = regis, width = 100, text = "Register", command = finish_reg)
    regis_button.place(x = 160, y = 440)

    notif = Label(master = regis, font = ('Times New Roman', 15))
    notif.place(x = 110, y = 510)

    regis.mainloop()

def finish_reg():
    global first_name_ingfo
    global last_name_ingfo
    global username_ingfo
    global email_ingfo
    global password_ingfo
    global all_account

    first_name_ingfo = first_name.get()
    last_name_ingfo = last_name.get()
    username_ingfo = username.get()
    email_ingfo = email.get()
    password_ingfo = password.get()
    all_account = os.listdir()

    if first_name_ingfo == "" or last_name_ingfo == "" or username_ingfo == "" or email_ingfo == "" or password_ingfo == "":
        notif.config(fg="red",text="All fields are required")
        return
    
    for name_check in all_account:
        if username_ingfo == name_check:
            notif.config(fg="red",text="Account Already exists")
            return
        else:
            file = open(username_ingfo, "w")
            file.write(first_name_ingfo + " " + last_name_ingfo +"\n")
            file.write(username_ingfo + "\n")
            file.write(email_ingfo + "\n")
            file.write(password_ingfo + "\n")
            file.write("100000")
            file.close()
            notif.config(fg='green',text="Account has been created")
    

    first_name_entry.delete(0, END)
    last_name_entry.delete(0,END)
    username_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)
 


def login_verify():
    all_accounts = os.listdir()
    global username_verify
    global password_verify
    global username1

    username1 = username_verify.get()
    password1 = password_verify.get()

    if username1 in all_accounts:
        file = open(username1, "r")
        file_data = file.read()
        file_data = file_data.split('\n')




        if password1 in file_data:
            #win.destroy()
            file = open (username1, "r")
            file_data =  file.read()
            user_details = file_data.split("\n")
            details_balance = user_details[4]
            customtkinter.set_appearance_mode("System")

            global main

            main = customtkinter.CTk()
            main.title("Dashboard")
            main.geometry("520x680+450+20")
            main.resizable(False,False)
            main.configure(bg = '#F5FEFD')

            #back = Canvas(master = main, width = 520, height = 680)
            #back.pack(side = LEFT, expand = True, fill = BOTH)

            #img = (Image.open("grd.jpg"))
            #back.create_image(10, 10, anchor = NW, image = img)
            f = tkinter.Frame(main, width = 650, height = 690, bg = '#F5FEFD')
            f.place(x = 0, y = 60)

            welcome = tkinter.Frame(master = main, width = 650, height = 60, bg = '#2D85C4')
            welcome.place(x = 0, y = 0)

            menu_bar = tkinter.Frame(master = main, width = 650, height = 100, bg = '#2576AF')
            menu_bar.place(x = 0, y = 750)

            wallet = tkinter.Frame(master = f, width = 450, height = 60, bg = '#F47B11')
            wallet.place(x = 100, y = 120)


            wallet.place(x = 100, y = 120)
            bal = customtkinter.CTkLabel(master = wallet, text = ("Welcome " + username1), font = ('Century Gothic', 25))
            bal.place(x = 0, y = 7)

            deposit_button = customtkinter.CTkButton(master = f, width = 60, height = 50, text = "Top Up",command=top_up, fg_color = '#F47B11')
            deposit_button.place(x = 130, y = 200)

            withdraw_button = customtkinter.CTkButton(master = f, width = 60, height = 50, text = "Withdraw",command=withdraw, fg_color = '#F47B11')
            withdraw_button.place(x = 240, y = 200)

            transfer_button = customtkinter.CTkButton(master = f, width = 60, height = 50, text = "Transfer", command = transfer, fg_color = '#F47B11')
            transfer_button.place(x = 350, y = 200)

 

            def home():

                welcome = tkinter.Frame(master = main, width = 650, height = 60, bg = '#2D85C4')
                welcome.place(x = 0, y = 0)


                global f1
                f1 = tkinter.Frame(master = main, width = 650, height = 690, bg = '#F5FEFD')
                f1.place(x = 0, y = 60)

                wallet = tkinter.Frame(master = f1, width = 450, height = 60, bg = '#F47B11')
                wallet.place(x = 100, y = 120)
                bal = customtkinter.CTkLabel(master = wallet, text = ("Welcome :" + username1), font = ('Century Gothic', 25))
                bal.place(x = 0, y = 7)

                deposit_button = customtkinter.CTkButton(master = f1, width = 60, height = 50, text = "Top Up",command=top_up, fg_color = '#F47B11')
                deposit_button.place(x = 130, y = 200)

                withdraw_button = customtkinter.CTkButton(master = f1, width = 60, height = 50, text = "Withdraw",command=withdraw, fg_color = '#F47B11')
                withdraw_button.place(x = 240, y = 200)

                transfer_button = customtkinter.CTkButton(master = f1, width = 60, height = 50, text = "Transfer", command = transfer, fg_color = '#F47B11')
                transfer_button.place(x = 350, y = 200)

                quote = tkinter.Frame(master = f1, width = 450, height = 200, bg = '#3995D7')
                quote.place( x= 100, y = 380)

                bal = customtkinter.CTkLabel(master = quote, text = ("The art is not in making money"), font = ('Century Gothic', 23))
                bal.place(x = 2, y = 37)
                bal = customtkinter.CTkLabel(master = quote, text = ("but in keeping it"), font = ('Century Gothic', 23))
                bal.place(x = 90, y = 70)


            home_menu = customtkinter.CTkButton(master = menu_bar, width = 90, height = 70, text = "Home", command = home, fg_color = '#F47B11')
            home_menu.place(x = 10, y = 5)

            def profile():
                file = open(username1, "r")

                nama_lengkap = file.readline()
                user = file.readline()
                gmail = file.readline()

                f4 = tkinter.Frame(main, width = 650, height = 750, bg = '#F5FEFD')
                f4.place(x = 0, y = 0)

                ff = tkinter.Frame(master = f4, width = 650, height = 80, bg = '#2D85C4')
                ff.place(x = 0, y = 0)
                pp = customtkinter.CTkLabel(master = ff, text = "Profile", font = ("Times New Roman", 50))
                pp.place(x = 200, y = 10)
                frame_nama = tkinter.Frame(master = main, width = 550, height = 120, bg = '#2D85C4')
                frame_nama.place(x = 50, y = 100)
                nama = customtkinter.CTkLabel(master = frame_nama, text = nama_lengkap, font = ('Times New Roman', 30))
                nama.place(x = 140, y = 10)
                mail = customtkinter.CTkLabel(master = frame_nama, text = gmail, font = ("Times New Roman", 30))
                mail.place(x = 80, y = 45)
                frame_info = tkinter.Frame(master = f4, width = 550, height = 300, bg = '#2D85C4')
                frame_info.place(x = 50, y = 250)

                def limitset():
                    limits = limit_entry.get()
                    if limits == '':
                        limit_notif = Toplevel()
                        limit_notif.geometry("250x250")
                        limit_notif.title("error!")
                        limit_notif.resizable(False, False)
                        limit_notif.mainloop()
                        limit_bel.config(text="Limit Required",fg='red')

                    elif float(limits) <= 0:
                        print(limits)
                    file = open("Limit" + " " + username1, "w")
                    file.write(limits)
                    file.close()

                check = os.listdir()
                limit_check = ("Limit" + " " + username1)

                if limit_check in check:
                    file1 = open("Limit" + " " + username1)
                    limits = file1.readlines()[0]
                    
                    limit = customtkinter.CTkLabel(master = frame_info, text = "Limit : " + limits, font = ("Times New Roman", 30))
                    limit.place(x = 10, y = 150)                   
                elif limit_check not in check:
                    limit = customtkinter.CTkLabel(master = frame_info, text = "Limit : ", font = ("Times New Roman", 30))
                    limit.place(x = 10, y = 150)
                    limit_entry = customtkinter.CTkEntry(master = frame_info, width = 220, placeholder_text = "enter limit",)
                    limit_entry.place(x = 100, y = 155)
                    limit_button = customtkinter.CTkButton(master = frame_info, width = 100, text = "set limit", command = limitset, fg_color = '#F47B11')
                    limit_button.place(x = 330, y = 155)
                    limit_bel =Label(frame_info,font=('Arial',10))
                    limit_bel.place(x=100,y=230)
                    

                stats = customtkinter.CTkLabel(master = frame_info, text = "Status akun : active", font = ("Times New Roman", 30))
                stats.place(x = 10, y = 80)
                usern = customtkinter.CTkLabel(master = frame_info, text = ("Username : " + user), font = ("Times New Roman", 30))
                usern.place(x = 10, y = 10)

            profile_menu = customtkinter.CTkButton(master = menu_bar, width = 90, height = 70, text = "Profile",command=profile, fg_color = '#F47B11')
            profile_menu.place(x = 420, y = 5)

            quote = tkinter.Frame(master = f, width = 450, height = 200, bg = '#3995D7')
            quote.place(x = 100, y = 380)

            bal = customtkinter.CTkLabel(master = quote, text = ("The art is not in making money"), font = ('Century Gothic', 23))
            bal.place(x = 2, y = 37)
            bal = customtkinter.CTkLabel(master = quote, text = ("but in keeping it"), font = ('Century Gothic', 23))
            bal.place(x = 90, y = 70)

            main.mainloop()
        
    else:
        login_notif.config(text="No Account found",fg="red")
        return
    login_notif.config(fg='red',text='Username or Password ')


def top_up():
    global deposit_entry
    global deposit_notif
    global current_balance_label1
    global amount
    amount = StringVar()
    file = open(username1, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    deposit_screen = customtkinter.CTk()
    deposit_screen.title("Top Up")
    deposit_screen.geometry("270x300+450+100")
    deposit_screen.resizable(False, False)

    topup_label = customtkinter.CTkLabel(deposit_screen, text = "Top Up", font = ("Arial", 20))
    topup_label.pack(pady = 10)
    current_balance_label1 = customtkinter.CTkLabel(deposit_screen, text = "Current Balance : Rp." + details_balance, font = ("Arial", 20))
    current_balance_label1.pack(pady = 15)

    tp_label = customtkinter.CTkLabel(deposit_screen,text='Masukkan Nominal')
    tp_label.pack(pady=5)

    deposit_entry = customtkinter.CTkEntry(deposit_screen)
    deposit_entry.pack(pady = 10)

    deposit_notif =Label(deposit_screen, font = ("Arial", 20))
    deposit_notif.pack(pady= 10)

    deposit_button = customtkinter.CTkButton(master = deposit_screen, text = "Finish", command = finish_deposit, font = ("Arial", 10))
    deposit_button.pack(pady = 10)

    deposit_screen.mainloop()

def finish_deposit():
    jumlah = deposit_entry.get()
    if jumlah == '':
        deposit_notif.config(text="Amount is required",fg="Red")
    if float(jumlah) <= 0:
        deposit_notif.config(text="Negative currency is not accepted",fg="Red")
        return
                                
    file = open(username1,"r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]
    update_balance = current_balance
    update_balance = float(update_balance) + float(jumlah)
    file_data      = file_data.replace(current_balance, str(update_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label1.configure(text="Current Balance : Rp."+str(update_balance))
    deposit_notif.config(text="Balance Updated",fg="green")

    f = tkinter.Frame(main, width = 650, height = 690, bg = '#F5FEFD')
    f.place(x = 0, y = 60)

    welcome = tkinter.Frame(master = main, width = 650, height = 60, bg = '#2D85C4')
    welcome.place(x = 0, y = 0)


    menu_bar = tkinter.Frame(master = main, width = 650, height = 100, bg = '#2576AF')
    menu_bar.place(x = 0, y = 750)

    wallet = tkinter.Frame(master = f, width = 450, height = 60, bg = '#F47B11')
    wallet.place(x = 100, y = 120)
    bal = customtkinter.CTkLabel(master = wallet, text = ("Welcome :" + username1), font = ('Century Gothic', 25))
    bal.place(x = 0, y = 7)



def withdraw():
    global withdraw_amount
    global withdraw_notif
    global current_balance_label2
    global withdraw_entry
    global deposit_notif
    withdraw_amount = StringVar()
    file = open(username1, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    withdraw_screen = customtkinter.CTk()
    withdraw_screen.title("Top Up")
    withdraw_screen.geometry("270x300+450+100")
    withdraw_screen.resizable(False, False)

    withdraw_label = customtkinter.CTkLabel(withdraw_screen, text = "withdraw", font = ("Arial", 20))
    withdraw_label.pack(pady = 10)
    current_balance_label2 = customtkinter.CTkLabel(withdraw_screen, text = "Current Balance : Rp." + details_balance, font = ("Arial", 20))
    current_balance_label2.pack(pady = 15)
    nominal_label = customtkinter.CTkLabel(withdraw_screen,text='Masukkan Nominal')
    nominal_label.pack(pady=10)

    withdraw_entry = customtkinter.CTkEntry(withdraw_screen)
    withdraw_entry.pack(pady = 10)

    withdraw_notif =Label(withdraw_screen, font = ("Arial", 20))
    withdraw_notif.pack(pady= 10)

    withdraw_button = customtkinter.CTkButton(master = withdraw_screen, text = "Finish", command = finish_withdraw, font = ("Arial", 10))
    withdraw_button.pack(pady = 10)

    withdraw_screen.mainloop()

def finish_withdraw():
    check = os.listdir()
    jumlah = withdraw_entry.get()
    file1 = open("Limit" + " " + username1)
    limits = file1.readlines()[0]

    if jumlah == '':
        withdraw_notif.config(text="Amount is required",fg="Red")
    if float(jumlah) <= 0:
        withdraw_notif.config(text="Negative currency is not accepted",fg="Red")
        return
    elif jumlah >= limits:
        withdraw_notif.config(text = "Amount cant be higher than limits")
    else:

                                
        file = open(username1,"r+")
        file_data = file.read()
        details = file_data.split("\n")
        current_balance = details[4]
        update_balance = current_balance
        update_balance = float(update_balance) - float(jumlah)
        file_data      = file_data.replace(current_balance, str(update_balance))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()
        file3 = open("Limit" + " " + username1, "r+")
        file_data3 = file3.read()
        detail3 = file_data3.split()
        current_limit = detail3[0]
        update3 = current_limit
        update3 = float(update3) - float(jumlah)
        file_data3 = file_data3.replace(current_limit, str(update3))
        file3.seek(0)
        file3.truncate(0)
        file3.write(file_data3)
        file3.close()

    current_balance_label2.configure(text="Current Balance : Rp."+str(update_balance))
    withdraw_notif.config(text="Balance Updated",fg="green")

def transfer():
    global trf_amount
    global trf_notif
    global trf_entry
    global target_entry
    global current_balance_label3


    trf_amount = StringVar()
    file = open(username1, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    trf_screen = customtkinter.CTk()
    trf_screen.title("Transfer")
    trf_screen.geometry("300x400+450+100")
   # trf_screen.resizable(False, False)

    trf_label = customtkinter.CTkLabel(trf_screen, text = "Transfer", font = ("Arial", 20))
    trf_label.pack(pady = 10)
    current_balance_label3 = customtkinter.CTkLabel(trf_screen, text = "Current Balance : Rp." + details_balance, font = ("Arial", 20))
    current_balance_label3.pack(pady = 15)

    traf_label = customtkinter.CTkLabel(trf_screen,text='Masukan Nominal')
    traf_label.pack(pady = 5)

    trf_entry = customtkinter.CTkEntry(trf_screen)
    trf_entry.pack(pady = 10)

    tref_label = customtkinter.CTkLabel(trf_screen,text='Masukan Username Tujuan')
    tref_label.pack(pady=5)

    target_entry = customtkinter.CTkEntry(trf_screen)
    target_entry.pack(pady = 20)

    trf_notif =Label(trf_screen, font = ("Arial", 20))
    trf_notif.pack(pady= 10)

    trf_button = customtkinter.CTkButton(master = trf_screen, text = "Finish", command = finish_trf, font = ("Arial", 10))
    trf_button.pack(pady = 10)

    trf_screen.mainloop()
    
def finish_trf():
    check = os.listdir()
    jumlah = trf_entry.get()
    username2 = target_entry.get()

    file1 = open("Limit" + " " + username1)
    limits = file1.readlines()[0]

    if jumlah == '':
        trf_notif.config(text = "Amount is required", fg = "Red")
    if float(jumlah) <= 0:
        trf_notif.config(text = "Negative currency is not accepted", fg = "Red")
    elif jumlah >= limits:
        trf_notif.config(text = "Amount cant be higher than limits", fg = "Red")
    else:
        if username2 in check:
            file1 = open(username1, "r+")
            file_data1 = file1.read()
            detail1 = file_data1.split("\n")
            current_balance = detail1[4]
            update1 = current_balance
            update1 = float(update1) - float(jumlah)
            file_data1 = file_data1.replace(current_balance, str(update1))
            file1.seek(0)
            file1.truncate(0)
            file1.write(file_data1)
            file1.close()
            file2 = open(username2, "r+")
            file_data2 = file2.read()
            detail2 = file_data2.split("\n")
            current_balance = detail2[4]
            update2 = current_balance
            update2 = float(update2) + float(jumlah)
            file_data2 = file_data2.replace(current_balance, str(update2))
            file2.seek(0)
            file2.truncate(0)
            file2.write(file_data2)
            file2.close()
            file3 = open("Limit" + " " + username1, "r+")
            file_data3 = file3.read()
            detail3 = file_data3.split()
            current_limit = detail3[0]
            update3 = current_limit
            update3 = float(update3) - float(jumlah)
            file_data3 = file_data3.replace(current_limit, str(update3))
            file3.seek(0)
            file3.truncate(0)
            file3.write(file_data3)
            file3.close()

            current_balance_label3.configure(text="Current Balance : Rp."+str(update1))
            trf_notif.config(text="Balance Updated",fg="green")

username_verify = StringVar()
password_verify = StringVar()

img1 = ImageTk.PhotoImage(Image.open("Bg1.png"))
l1=customtkinter.CTkLabel(master= win,image= img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)

username_login_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
username_login_entry.place(x=50, y=105)
username_verify = username_login_entry

password_login_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
password_login_entry.place(x=50, y=165)
password_verify = password_login_entry

login_notif=Label(master=frame,font=('Century Gothic',12))
login_notif.place(x=75,y=250)

#tombol login
login_button = customtkinter.CTkButton(master=frame, width=220, text="Login",command=login_verify, corner_radius=6)
login_button.place(x= 50, y= 240)

#tombol register
register_button = customtkinter.CTkButton(master=frame, width=220, text="Register", command=register, corner_radius=6)
register_button.place(x= 50, y= 285)


win.mainloop()
