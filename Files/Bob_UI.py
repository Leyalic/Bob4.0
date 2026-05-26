#Created by Iman Essaghir and Joshua Hardy
import sys
sys.path.insert(1, '../Files/')
from Files import Do_Queries_Functions

from fileinput import filename
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from pathlib import Path
import time

###############################
import os
import shutil
###############################

year_valid = False
term_valid = False

rootWindow = Tk()

titleLabel = Label(rootWindow, text="Welcome to the Do Queries Process")

titleLabel.pack()

img=PhotoImage(file='uosfa.png')
Label(rootWindow,image=img).pack()

rootWindow.geometry("850x550")

# Return values of Do_Queries_FUnctions
direct_loan_flag = False
alt_loan_flag = False
unknown_list = []

select_window = None
folder_option = ""

orig_window = None
orig_path = None
myWin = None

aid_year = ""
date = time.strftime("%x").replace("/", "-")

running_text = "Program running, please do not close the window"

test = False

#Adding widgets

class BobWindow(tk.Frame):
    
    # Handler for orig window popup
    def handle_orig_window():
        global orig_window
        global orig_path
        orig_path = Path(filedialog.askopenfilename())
        orig_window.destroy()

    # Prompt user to select origination file
    def create_orig_window(filename, pathname):
        global orig_window
        global orig_path
        orig_path = None
        orig_window = Toplevel(rootWindow)
        #orig_window.grab_set(); # Disable interacting with root

        prompt1 = "Could not locate the following file:"
        prompt2 = filename
        prompt3 = "in the following location:"
        prompt4 = pathname
        prompt5 = "Please select origination file"
        tk.Label(orig_window, text=prompt1, padx=10, pady=5).pack()
        tk.Label(orig_window, text=prompt2, fg='#00f', padx=10, pady=5).pack()
        tk.Label(orig_window, text=prompt3, padx=10, pady=5).pack()
        tk.Label(orig_window, text=prompt4, fg='#00f', padx=10, pady=5).pack()
        tk.Label(orig_window, text=prompt5, padx=10, pady=5).pack()

        select_button = Button(orig_window, text="Select File", bd="2", command=lambda: BobWindow.handle_orig_window(), height="2", width="15")
        skip_button = Button(orig_window, text="Skip", bd="2", command=lambda: orig_window.destroy(), height="2", width="15")

        select_button.pack(side="left", anchor="e",padx=18, pady=18)
        skip_button.pack(side="right", anchor="w",padx=18, pady=18)

        return orig_window   

    # Copy direct loan origination file into UOSFA folder
    def run_direct_orig():
        success = Do_Queries_Functions.move_direct_orig("", True)
        if not success:
            # Prompt user for orig file
            filename = date + " DL ORIG " + aid_year + ".doc"
            pathname = "O:/Systems/Direct Loans/Origination/\n\n"
            
            # Stores user submitted filepath in global 'orig_path'
            wind = BobWindow.create_orig_window(filename, pathname)
            rootWindow.wait_window(wind)

            if orig_path is None:
                pass
            else:
                Do_Queries_Functions.move_direct_orig(orig_path, False)
    
    # Copy alt loan origination file into UOSFA folder
    def run_alt_orig():
        success = Do_Queries_Functions.move_alt_orig("", True)
        if not success:
            # Prompt user for orig file
            filename = date + " ALT Loan ORIG " + aid_year + ".doc"
            pathname = "O:/Systems/QUERIES/ALT Loans/\n\n"
            
            # Stores user submitted filepath in global 'orig_path'
            wind = BobWindow.create_orig_window(filename, pathname)
            rootWindow.wait_window(wind)

            if orig_path is None:
                pass
            else:
                Do_Queries_Functions.move_alt_orig(orig_path, False)

    # Handler for folder select popup
    def handle_selection(option):
        global folder_option
        global select_window

        folder_option = option
        select_window.destroy()

    # Prompt user to select folder for unknown file
    def folder_select_popup(filename):
        global select_window
        select_window = Toplevel(rootWindow)
        
        #select_window.grab_set(); # Disable interacting with root

        x_loc = rootWindow.winfo_x()
        y_loc = rootWindow.winfo_y()
        select_window.geometry('+%d+%d' % (x_loc + 10, y_loc +10))
        prompt = "The following file could not be sorted. Please select a destination folder."
        options = [
                    "Alternative Loan Reports",
                    "Budget Reports",
                    "Daily Reports",
                    "Direct Loan Reports",
                    "External Award Reports",
                    "Financial Aid Reports",
                    "Monthly Reports",
                    "Other Reports",
                    "Packaging Reports",
                    "Pell Reports",
                    "SAP Reports",
                    "Scholarship Reports",
                    "Unknown Reports",
                    "Weekly Reports"              
                  ]
        tk.Label(select_window, text=prompt, padx=10, pady=5).pack()
        tk.Label(select_window, text=filename, fg='#00f', padx=10).pack()
        v = tk.IntVar()
        for i, option in enumerate(options):
            tk.Radiobutton(select_window, text=option, variable=v, value=i).pack(anchor="w")
        tk.Button(select_window, text="Submit", command=lambda: BobWindow.handle_selection(options[v.get()])).pack()
        v.set(12)
        select_window.title("Select Folder")
        return select_window


    # Prompt user to select folder for unknown files
    def handle_unknown_files():
        global unknown_list
        global folder_option

        done = True
        while len(unknown_list) > 0:
            done = False
            folder_option = ""

            # Ask user to select folder
            filename = unknown_list[0]                     
            wind = BobWindow.folder_select_popup(filename)
            rootWindow.wait_window(wind)

            if folder_option == "":
                unknown_list.remove(filename)
                continue

            #("Moved to " + folder_option)

            # Move file to selected folder
            #year = Do_Queries_Functions.find_aid_year(Path(filename))
            renamed = Do_Queries_Functions.new_name(filename, aid_year)           
            Do_Queries_Functions.do_query_unknown(filename, renamed, folder_option, aid_year, True)
            unknown_list.remove(filename)

        #print("All Unknown Files Handled")

        return done

    # Runs Do_Queries on all files
    def open_popup(self):       
        global aid_year
        global direct_loan_flag
        global alt_loan_flag
        global unknown_list

        direct_loan_flag = False
        alt_loan_flag = False
        unknown_list = []

        if year_valid:

            self.exit_Button["state"] = "disabled"
            self.t1["state"] = "disabled"
            self.b1["state"] = "disabled"
            self.run_label["text"] = running_text

            aid_year = self.t1.get()           
            direct_loan_flag, alt_loan_flag, unknown_list = Do_Queries_Functions.run(self.t1.get(), test)

            if len(unknown_list) > 0:
                # Disable all window input here
                
                BobWindow.handle_unknown_files()
                # Re-enable all window input here
                
                #print("Process Completed")

            if direct_loan_flag:
                BobWindow.run_direct_orig()

            if alt_loan_flag:
                BobWindow.run_alt_orig()

            self.run_label["text"] = ""
            self.b1["state"] = "normal"
            self.t1["state"] = "normal"
            self.exit_Button["state"] = "normal"
            
        else:
            rootWindow.bell()
            prev = self.focus_get()
            self.b1.focus()
            prev.focus()
            self.aid_warn_label.config(text = "Aid Year must be provided")


    # Checks if aid year is a 4-digit number
    def validate_aid_year(self, d, i, P, s, S, v, V, W):     
        global year_valid
        global term_valid
        if V == "key":
            if P.isnumeric():
                if len(P) == 4:
                    year_valid = True
                else:
                    year_valid = False
            else:
                year_valid = False
            return True
        elif V == "focusout":
            if P.isnumeric():
                if len(P) == 4:
                    self.aid_warn_label.config(text = "")
                    year_valid = True
                    return True
                else:
                    self.aid_warn_label.config(text = "Aid Year must have 4 digits")
                    year_valid = False
                    return False
            else:
                self.aid_warn_label.config(text = "Aid Year must be a number")
                year_valid = False
                return False
        elif V == "focusin":
            return True
    
#############################################################################################
    def reset_test_folder(self):
        #direct = Path("C:/Users/JHARDY/Documents/DoQueries/Destination Folders")
        #direct = Path("C:/Users/iessaghir/Documents/DoQueries/Destination Folders")
        direct = Path("O:/UOSFA Reports/Testing/Destination Folders")

        for folder in os.listdir(direct):
            path = direct / Path(folder)
            for old_file in os.listdir(path):
                os.remove(path / Path(old_file))
        print("Done Resetting")
#############################################################################################


    def __init__(self, win):
        tk.Frame.__init__(self, win)
        self.lbl1=Label(win, text='Please enter the aid year', fg='black', font=("Times New Roman bold", 13))
       
        aid_valid = (self.register(self.validate_aid_year),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.t1=Entry(bd=10, validate="all", validatecommand=aid_valid)
        
        self.aid_warn_label = Label(win, text="", fg='blue', font=("Times New Roman bold", 13))
        self.aid_warn_label.place(x=570, y=340)


        self.lbl1.place(x=200, y=300)
        self.t1.place(x=600, y=300)
        
        self.run_label = Label(win, text="", fg='red', font=("Times New Roman bold", 13)) 
        self.run_label.place(x=260, y=375)

        
        #################################################################
        #################################################################
        if test:
            self.reset_button = Button(rootWindow, text="Reset Test Folders", command=self.reset_test_folder)
            self.reset_button.pack(side=BOTTOM, anchor="s", padx=8, pady=8)
        #################################################################
        #################################################################


        #Create a button in the main Window to open the popup
        self.b1=Button(win, text="Run", font=('Helvatical bold',12), bd="4", command=self.open_popup, height=2, width=10)
        self.b1.pack(side=BOTTOM, anchor="center",padx=18, pady=18)
    
        self.exit_Button = Button(rootWindow, text="Exit Program", command=rootWindow.destroy)
        self.exit_Button.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

        

        self.winfo_toplevel().title("Bob Window")
   
def main():
    global myWin
    global rootWindow
    myWin=BobWindow(rootWindow)
    rootWindow.mainloop()

if __name__ == "__main__":
    main()
