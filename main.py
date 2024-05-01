import customtkinter
import random
from bubble_sort import bubble_sort

class Sorting_Algorithm():
    def __init__(self) -> None: 
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        
        self.root.geometry("1000x550")
        self.root.resizable(False,False)
        self.root.title("Sorting Algorithm")
        
        self.title = customtkinter.CTkLabel(self.root, text="Sorting Algorithm Processor", font=("Times New Roman", 40),anchor="center")
        self.title.grid(row=0,column=0,pady=20,padx=(300,0))
        
        self.input_tab = customtkinter.CTkTabview(self.root,width=450,height=400)
        self.input_tab.grid(row=1,column=0,pady=20,padx=(0,200))
        self.input_tab1 = self.input_tab.add("Number Sort")
        
        self.labelAlgo = customtkinter.CTkLabel(master=self.input_tab1, text="Algorithm :", font=("Times New Roman", 20),anchor="center")
        self.labelAlgo.grid(row=0,column=0,padx=(40,20),pady=20)
        
        self.choose_algorithm = customtkinter.CTkComboBox(master=self.input_tab1,state="readonly",values=["Bubble Sort"],width=200)
        self.choose_algorithm.grid(row=0,column=1,padx=(40,20),pady=20)

        self.labelMode =  customtkinter.CTkLabel(master=self.input_tab1, text="Mode :", font=("Times New Roman", 20))
        self.labelMode.grid(row=1,column=0,padx=(40,20),pady=20)

        self.choose_mode = customtkinter.CTkComboBox(master=self.input_tab1,state="readonly",values=["Ascending","Descending"],width=200)
        self.choose_mode.grid(row=1,column=1,padx=(40,20),pady=20)
        
        self.Labelinput = customtkinter.CTkLabel(master=self.input_tab1, text="Input (coma seperated):", font=("Times New Roman", 20))
        self.Labelinput.grid(row=2,column=0,padx=(40,20),pady=20)
        
        self.input = customtkinter.CTkEntry(master=self.input_tab1,width=200)
        self.input.grid(row=2,column=1,padx=(40,20),pady=20)
        
        self.generate = customtkinter.CTkButton(master=self.input_tab1,text="Generate Array ⚡️", font=("Times New Roman", 25), width=400,height=40, fg_color="#d24e00", command=self.generate_array)
        self.generate.grid(row=3,column=0,columnspan=2,padx=(40,20),pady=20)
        
        self.submit = customtkinter.CTkButton(master=self.input_tab1,text="Sort!",command=self.sort)
        self.submit.place(relx=0.5,rely=0.9,anchor="center")
        
        self.resultLabel = customtkinter.CTkLabel(master=self.root, text="Result:", font=("Times New Roman", 30))
        self.resultLabel.grid(row=1,column=1,pady=(0,350),padx=(0,20))
        
        self.result = customtkinter.CTkTextbox(master=self.root,font=("Times New Roman",20),state="disable",width=430,height=70)
        self.result.place(relx=0.988,rely=0.37,anchor="e")
        
        self.step = customtkinter.CTkTextbox(master=self.root,width=430,height=250,font=("Times New Roman",20),state="disable")
        self.step.place(relx=0.988,rely=0.69,anchor="e")
        self.root.mainloop()
    
    def generate_array(self):
        array = ""
        length = random.randint(10,20)
        for i in range(length):
            if i == length-1:
                string = f"{random.randint(1,100)}"
                array = array + string
            else:
                string = f"{random.randint(1,100)},"
                array = array + string

        self.input.delete(0,"end")
        self.input.insert(0,array)
    
    def error(self,error_message):
        error_popup = customtkinter.CTkToplevel(self.root)
        error_popup.grab_set()
        error_popup.geometry("400x130")
        error_popup.resizable(False,False)
        error_popup.title("Error")
        
        error_label = customtkinter.CTkLabel(master=error_popup,wraplength=330,text=error_message,font=("Times New Roman",20),text_color="White")
        error_label.pack(pady=(30,0))
        
        ok_button = customtkinter.CTkButton(master=error_popup,text="OK",width=50,height=30,font=("Times New Roman",20),command=error_popup.destroy)
        ok_button.pack(pady=10)
    
    def sort(self):
        algorithm = self.choose_algorithm.get()
        order = self.choose_mode.get()
        array = self.input.get()
           
        if array == "":
            self.error("Input is empty! Please enter some numbers.")
            return None
        elif algorithm == "":
            self.error("Algorithm is empty! Please choose an algorithm.")
            return None
        elif order == "":
            self.error("Mode is empty! Please choose a mode.")
            return None
        
        array = array.replace(" ","")
        array = array.split(",")
        
        try:
            array = [int(i) for i in array if i != ""]
        except ValueError:
            self.error("Invalid input! Please enter only numbers.")
            return None
        
        if algorithm == "Bubble Sort":
            array , process = bubble_sort(array,order)
            self.result.configure(state="normal")
            
        self.result.delete("0.0","end")
        self.result.insert("0.0",f"{array}")
        self.result.configure(state="disable")
        self.step.configure(state="normal")
        self.step.delete("0.0","end")
        self.step.insert("0.0",f"{process}")
        self.step.configure(state="disable")
        
if __name__ == "__main__":
    Sorting_Algorithm()