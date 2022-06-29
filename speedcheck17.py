from tkinter import*
import matplotlib.pyplot as plt
import speedtest
root=Tk()
root.geometry("600x600")
root.title("Speed Test")
label1=Label(root,text="Internet Speed Check", font=("Lucida Sans Unicode",20,"bold","italic"),fg="#5D6D7E", bg="#dee8f1")
label1.place(relx=0.5, rely=0.1,anchor=CENTER)
label2=Label(root,text="Download Speed", font=("Lucida Sans Unicode",14,"bold","italic"),fg="#82ADA3")
label2.place(relx=0.3, rely=0.6,anchor=CENTER)
label3=Label(root,text="Upload Speed", font=("Lucida Sans Unicode",14,"bold","italic"),fg="#82ADA3")
label3.place(relx=0.7, rely=0.6,anchor=CENTER)
label_download = Labepl(root, font=("Segoe Print", 18, "bold"), fg="#1E8449", bg="#dee8f1")
label_download.place(relx=0.3, rely=0.7,anchor=CENTER)
label_upload = Label(root,font=("Segoe Print", 18, "bold"), fg="#9B59B6", bg="#dee8f1")
label_upload.place(relx=0.7, rely=0.7,anchor=CENTER)
downloadspeed=0
uploadspeed=0
def internetspeed():
    global downloadspeed
    global uploadspeed
    st=speedtest.Speedtest()
    downloadspeed=round(st.download()/1000000,2)
    label_download["text"]=str(downloadspeed)+"mbps"
    uploadspeed=round(st.upload()/1000000,2)
    label_upload["text"]=str(uploadspeed)+"mbps"

button1=Button(root,text="Check Speed", command=internetspeed,bg="#218796", fg="white",relief = FLAT, padx=15,pady=8,  font=("Lucida Sans Unicode", 10))
button1.place(relx=0.5, rely=0.5,anchor=CENTER)
x=[100,200,300,400,500,600,700]
plt.plot(x,downloadspeed,label ="Download Speed")
plt.plot(x,uploadspeed,label ="Upload Speed")
plt.legend()
plt.show()

root.mainloop()