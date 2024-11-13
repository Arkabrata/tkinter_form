import tkinter

from tkinter import messagebox

def display_patient_info():  #function
    try:
        Age = int(age_entry.get())
        Name = name_entry.get()
        City= city_entry.get()
        if int(Age) > 15:
            Patent_group = "Adult"
        else: "Pediatric"
        messagebox.showinfo("Patient Info", #showing the output
                            f"Patient Name: {Name}\n"
                            f"Patient Age: {Age}\n"
                            f"Patient Group:{Patent_group}\n"
                            f"Patient City : {City}\n")
    except ValueError:
        messagebox.showerror("Invalid input, please enter valid age")
root= tkinter.Tk()
root.title("Patient Information")
root.geometry("1000x800")
tkinter.Label(root,text="Patient Name").grid(row=0,column=0,padx=10,pady=5)
name_entry=tkinter.Entry(root)
name_entry.grid(row=0,column=1,padx=10,pady=5)

tkinter.Label(root,text="Patient Age").grid(row=1,column=0,padx=10,pady=5)
age_entry=tkinter.Entry(root)
age_entry.grid(row=1,column=1,padx=10,pady=5)

tkinter.Label(root,text="Patient City").grid(row=2,column=0,padx=10,pady=5)
city_entry=tkinter.Entry(root)
city_entry.grid(row=2,column=1,padx=10,pady=5)

submit_button= tkinter.Button(root, text="Submit",command=display_patient_info)
submit_button.grid(row=3,column=0,columnspan=3,pady=10)
root.mainloop()
