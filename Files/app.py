"""Bob tkinter UI — delegates all file I/O to FileProcessor."""
import os
import tkinter as tk
from pathlib import Path
from tkinter import Button, Checkbutton, Entry, Label, Radiobutton, Toplevel, filedialog

import Files.processor as _processor
from Files import config
from Files.processor import FileProcessor


class BobApp(tk.Frame):
    """Main application window."""

    def __init__(self, root: tk.Tk) -> None:
        super().__init__(root)
        self._root = root
        self._processor: FileProcessor | None = None
        self._unknown_list: list[str] = []
        self._folder_option = ""
        self._orig_path: Path | None = None
        self._select_window: Toplevel | None = None
        self._orig_window: Toplevel | None = None
        self._year_valid = False

        root.title("Bob Window")
        root.geometry("850x550")

        # ── Header ────────────────────────────────────────────────────────
        Label(root, text="Hello, my name is Bob. I do queries.").pack(pady=(10, 0))
        try:
            self._img = tk.PhotoImage(file="uosfa.png")
            Label(root, image=self._img).pack()
        except tk.TclError:
            pass

        # ── Aid year row ──────────────────────────────────────────────────
        year_frame = tk.Frame(root)
        year_frame.pack(pady=(20, 0))
        Label(year_frame, text="Please enter the aid year",
              font=("Times New Roman bold", 13)).pack(side=tk.LEFT, padx=(0, 10))

        vcmd = (root.register(self._validate_year),
                "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")
        self._year_entry = Entry(year_frame, bd=10, validate="all", validatecommand=vcmd)
        self._year_entry.pack(side=tk.LEFT)

        self._warn_label = Label(root, text="", fg="blue", font=("Times New Roman bold", 13))
        self._warn_label.pack()

        self._run_label = Label(root, text="", fg="red", font=("Times New Roman bold", 13))
        self._run_label.pack(pady=(5, 0))

        # ── Bottom controls ───────────────────────────────────────────────
        # pack order: first packed sits at absolute bottom; visually bottom→top:
        #   bottom_bar (View Log | Exit) → run → test checkbox → reset (when visible)
        bottom_bar = tk.Frame(root)
        bottom_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=8)
        Button(bottom_bar, text="View Log",
               command=self._open_log).pack(side=tk.LEFT)
        self._exit_btn = Button(bottom_bar, text="Exit Program", command=root.destroy)
        self._exit_btn.pack(side=tk.RIGHT)

        self._run_btn = Button(root, text="Run", font=("Helvetica bold", 12), bd=4,
                               command=self._open_popup, height=2, width=10)
        self._run_btn.pack(side=tk.BOTTOM, anchor="center", padx=18, pady=18)

        mode_frame = tk.Frame(root)
        mode_frame.pack(side=tk.BOTTOM, anchor="center", padx=8, pady=4)
        Label(mode_frame, text="Run Mode:",
              font=("Times New Roman bold", 11)).pack(side=tk.LEFT, padx=(0, 8))
        self._test_var = tk.BooleanVar(value=False)
        self._test_check = Checkbutton(mode_frame,
                                       text="PRODUCTION MODE  (files will be moved for real!)",
                                       variable=self._test_var,
                                       command=self._toggle_test_mode,
                                       fg="red",
                                       font=("Times New Roman bold", 11))
        self._test_check.pack(side=tk.LEFT)

        self._reset_btn = Button(root, text="Reset Test Folders",
                                 command=self._reset_test_folder)
        # reset button starts hidden — only shown when test mode is on

    # ── Validation ─────────────────────────────────────────────────────────

    def _validate_year(self, d, i, P, s, S, v, V, W) -> bool:
        if V == "key":
            self._year_valid = P.isnumeric() and len(P) == 4
            return True
        if V == "focusout":
            if P.isnumeric() and len(P) == 4:
                self._warn_label.config(text="")
                self._year_valid = True
                return True
            self._warn_label.config(
                text="Aid Year must have 4 digits"
                if P.isnumeric() else "Aid Year must be a number"
            )
            self._year_valid = False
            return False
        return True  # focusin or forced

    # ── Mode toggle ────────────────────────────────────────────────────────

    def _toggle_test_mode(self) -> None:
        if self._test_var.get():
            self._test_check.config(text="Test Mode  (files go to Testing folder)", fg="blue")
            self._reset_btn.pack(side=tk.BOTTOM, anchor="s", padx=8, pady=8)
        else:
            self._test_check.config(text="PRODUCTION MODE  (files will be moved for real!)", fg="red")
            self._reset_btn.pack_forget()

    def _reset_test_folder(self) -> None:
        direct = Path("C:/UOSFA Reports/Testing/Destination Folders")
        for folder in os.listdir(direct):
            path = direct / folder
            if path.is_dir():
                for old_file in os.listdir(path):
                    (path / old_file).unlink(missing_ok=True)
        print("Done Resetting")

    def _open_log(self) -> None:
        os.startfile(str(_processor.LOG_FILE))

    # ── Main run ───────────────────────────────────────────────────────────

    def _open_popup(self) -> None:
        if not self._year_valid:
            self._root.bell()
            self._warn_label.config(text="Aid Year must be provided")
            return

        directory = filedialog.askdirectory(title="Select source folder")
        if not directory:
            return

        year = self._year_entry.get()
        is_test = self._test_var.get()

        self._exit_btn["state"] = "disabled"
        self._year_entry["state"] = "disabled"
        self._run_btn["state"] = "disabled"
        self._run_label.config(text="Program running, please do not close the window", fg="red")
        self._root.update()

        self._processor = FileProcessor(year, is_test)
        self._processor.set_source_folder(directory)
        direct_loan_flag, alt_loan_flag, dlout_flag, unknown_list = self._processor.run()

        if unknown_list:
            self._unknown_list = list(unknown_list)
            self._handle_unknown_files()

        if direct_loan_flag:
            self._run_direct_orig()

        if direct_loan_flag or dlout_flag:
            self._run_dlout_orig()

        if alt_loan_flag:
            self._run_alt_orig()

        self._run_label.config(text="Processing complete!", fg="green")
        self._run_btn["state"] = "normal"
        self._year_entry["state"] = "normal"
        self._exit_btn["state"] = "normal"

    # ── Unknown file handling ──────────────────────────────────────────────

    def _handle_unknown_files(self) -> None:
        while self._unknown_list:
            self._folder_option = ""
            filename = self._unknown_list[0]

            wind = self._folder_select_popup(filename)
            self._root.wait_window(wind)

            if not self._folder_option:
                self._unknown_list.remove(filename)
                continue

            renamed = self._processor.new_name(filename, self._processor.year)
            self._processor.do_query_unknown(filename, renamed, self._folder_option, learn=True)
            self._unknown_list.remove(filename)

    def _folder_select_popup(self, filename: str) -> Toplevel:
        self._select_window = Toplevel(self._root)
        self._select_window.title("Select Folder")
        x, y = self._root.winfo_x(), self._root.winfo_y()
        self._select_window.geometry(f"+{x + 10}+{y + 10}")

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
            "Weekly Reports",
        ]

        Label(self._select_window,
              text="The following file could not be sorted. Please select a destination folder or click the x in top right corner to skip.",
              padx=10, pady=5).pack()
        Label(self._select_window, text=filename, fg="#00f", padx=10).pack()

        v = tk.IntVar(value=12)  # default: Unknown Reports
        for i, opt in enumerate(options):
            Radiobutton(self._select_window, text=opt, variable=v, value=i).pack(anchor="w")

        Button(self._select_window, text="Submit",
               command=lambda: self._handle_folder_selection(options[v.get()])).pack()

        return self._select_window

    def _handle_folder_selection(self, option: str) -> None:
        self._folder_option = option
        if self._select_window:
            self._select_window.destroy()

    # ── Origination file prompts ───────────────────────────────────────────

    def _create_orig_window(self, filename: str, pathname: str) -> Toplevel:
        self._orig_path = None
        self._orig_window = Toplevel(self._root)

        Label(self._orig_window, text="Could not locate the following file:",
              padx=10, pady=5).pack()
        Label(self._orig_window, text=filename, fg="#00f", padx=10, pady=5).pack()
        Label(self._orig_window, text="in the following location:",
              padx=10, pady=5).pack()
        Label(self._orig_window, text=pathname, fg="#00f", padx=10, pady=5).pack()
        Label(self._orig_window, text="Please select origination file",
              padx=10, pady=5).pack()

        btn_frame = tk.Frame(self._orig_window)
        btn_frame.pack(pady=18)
        Button(btn_frame, text="Select File", bd=2, height=2, width=15,
               command=self._handle_orig_select).pack(side=tk.LEFT, padx=18)
        Button(btn_frame, text="Skip", bd=2, height=2, width=15,
               command=self._orig_window.destroy).pack(side=tk.RIGHT, padx=18)

        return self._orig_window

    def _handle_orig_select(self) -> None:
        path = filedialog.askopenfilename()
        if path:
            self._orig_path = Path(path)
        if self._orig_window:
            self._orig_window.destroy()

    def _run_direct_orig(self) -> None:
        if self._processor.move_direct_orig():
            return
        p = self._processor
        filename = f"{p.date} DL ORIG {p.year}.doc"
        src_dir = config.TEST_DL_ORIG_DIR if p.is_test else config.DL_ORIG_DIR
        wind = self._create_orig_window(filename, str(src_dir))
        self._root.wait_window(wind)
        if self._orig_path:
            self._processor.move_direct_orig(self._orig_path)

    def _run_alt_orig(self) -> None:
        if self._processor.move_alt_orig():
            return
        p = self._processor
        filename = f"{p.date} ALT Loan ORIG {p.year}.doc"
        src_dir = config.TEST_ALT_ORIG_DIR if p.is_test else config.ALT_ORIG_DIR
        wind = self._create_orig_window(filename, str(src_dir))
        self._root.wait_window(wind)
        if self._orig_path:
            self._processor.move_alt_orig(self._orig_path)

    def _run_dlout_orig(self) -> None:
        if self._processor.move_dlout_orig():
            return
        p = self._processor
        filename = f"{p.date} DLOUT {p.year}.doc"
        src_dir = config.TEST_DL_ORIG_DIR if p.is_test else config.DL_ORIG_DIR
        wind = self._create_orig_window(filename, str(src_dir))
        self._root.wait_window(wind)
        if self._orig_path:
            self._processor.move_dlout_orig(self._orig_path)


def main() -> None:
    root = tk.Tk()
    BobApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
