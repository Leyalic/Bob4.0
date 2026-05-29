"""Bob tkinter UI — delegates all file I/O to FileProcessor."""
import os
import tkinter as tk
from pathlib import Path
from tkinter import ttk, Toplevel, filedialog

import Files.processor as _processor
from Files import config
from Files.processor import FileProcessor

# ── Design tokens ──────────────────────────────────────────────────────────
_NAVY   = "#1E3A5F"
_NAVY_H = "#2A4F80"
_WHITE  = "#FFFFFF"
_BG     = "#F4F6F9"
_RED    = "#C62828"
_BLUE   = "#1565C0"
_GREEN  = "#2E7D32"
_MUTED  = "#546E7A"
_LINE   = "#DDE3ED"
_FONT   = "Segoe UI"


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

        root.title("Bob — Financial Aid File Processor")
        root.geometry("860x480")
        root.configure(bg=_BG)
        root.resizable(False, False)
        self._setup_styles(root)

        # ── Header bar ────────────────────────────────────────────────────
        hdr = tk.Frame(root, bg=_NAVY, height=64)
        hdr.pack(fill=tk.X)
        hdr.pack_propagate(False)
        try:
            try:
                from PIL import Image, ImageTk
                _pil = Image.open("uosfa.png")
                _h = 48
                _w = int(_pil.width * _h / _pil.height)
                _resample = getattr(Image, "Resampling", Image).LANCZOS
                _pil = _pil.resize((_w, _h), _resample)
                self._img = ImageTk.PhotoImage(_pil)
            except ImportError:
                self._img = tk.PhotoImage(file="uosfa.png")
            tk.Label(hdr, image=self._img, bg=_NAVY).pack(side=tk.LEFT, padx=16, pady=8)
        except Exception:
            pass
        title_col = tk.Frame(hdr, bg=_NAVY)
        title_col.pack(side=tk.LEFT, pady=12)
        tk.Label(title_col, text="Bob  —  Financial Aid File Processor",
                 bg=_NAVY, fg=_WHITE, font=(_FONT, 13, "bold")).pack(anchor="w")
        tk.Label(title_col, text="Hello, my name is Bob.  I do queries.",
                 bg=_NAVY, fg="#A8BFCF", font=(_FONT, 9)).pack(anchor="w")

        # ── Footer (packed before content so content fills the middle) ────
        footer = tk.Frame(root, bg=_BG)
        footer.pack(side=tk.BOTTOM, fill=tk.X)

        # Mode row: Run Mode label | checkbox | Reset Test Folders (when visible)
        tk.Frame(footer, bg=_LINE, height=1).pack(fill=tk.X)
        mode_row = tk.Frame(footer, bg=_BG)
        mode_row.pack(fill=tk.X, padx=16, pady=6)
        tk.Label(mode_row, text="Run Mode:", bg=_BG, fg=_MUTED,
                 font=(_FONT, 10, "bold")).pack(side=tk.LEFT, padx=(0, 10))
        self._test_var = tk.BooleanVar(value=False)
        self._test_check = ttk.Checkbutton(
            mode_row,
            text="PRODUCTION MODE  —  files will be moved for real!",
            variable=self._test_var,
            command=self._toggle_test_mode,
            style="Prod.TCheckbutton",
        )
        self._test_check.pack(side=tk.LEFT)
        self._reset_btn = ttk.Button(mode_row, text="Reset Test Folders",
                                     style="Ghost.TButton",
                                     command=self._reset_test_folder)
        # reset button starts hidden — shown via pack(side=RIGHT) in test mode

        # Action bar: View Log (left) | Exit (right)
        tk.Frame(footer, bg=_LINE, height=1).pack(fill=tk.X)
        bar = tk.Frame(footer, bg=_BG)
        bar.pack(fill=tk.X, padx=16, pady=8)
        ttk.Button(bar, text="View Log", style="Ghost.TButton",
                   command=self._open_log).pack(side=tk.LEFT)
        self._exit_btn = ttk.Button(bar, text="Exit", style="Ghost.TButton",
                                    command=root.destroy)
        self._exit_btn.pack(side=tk.RIGHT)

        # ── Content (fills remaining vertical space) ──────────────────────
        content = tk.Frame(root, bg=_BG)
        content.pack(fill=tk.BOTH, expand=True)

        # Center frame — expand=True without fill keeps it at natural size,
        # centered in whatever vertical space is available.
        center = tk.Frame(content, bg=_BG)
        center.pack(expand=True)

        year_frame = tk.Frame(center, bg=_BG)
        year_frame.pack()
        tk.Label(year_frame, text="Enter Default Aid Year:", bg=_BG, fg=_MUTED,
                 font=(_FONT, 11, "bold")).pack(side=tk.LEFT, padx=(0, 12))
        vcmd = (root.register(self._validate_year),
                "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W")
        self._year_entry = ttk.Entry(year_frame, width=8, font=(_FONT, 11),
                                     validate="all", validatecommand=vcmd)
        self._year_entry.pack(side=tk.LEFT)

        self._warn_label = tk.Label(center, text="", bg=_BG, fg=_RED,
                                    font=(_FONT, 10))
        self._warn_label.pack(pady=(6, 0))

        self._run_btn = ttk.Button(center, text="Locate Files",
                                   style="Primary.TButton",
                                   command=self._open_popup)
        self._run_btn.pack(pady=(18, 0))

        self._run_label = tk.Label(center, text="", bg=_BG, fg=_MUTED,
                                   font=(_FONT, 10))
        self._run_label.pack(pady=(10, 0))

    # ── Styles ─────────────────────────────────────────────────────────────

    def _setup_styles(self, root: tk.Tk) -> None:
        s = ttk.Style(root)
        s.theme_use("clam")
        s.configure(".", font=(_FONT, 10))

        s.configure("Primary.TButton",
                    background=_NAVY, foreground=_WHITE,
                    font=(_FONT, 12, "bold"), padding=(32, 10),
                    relief="flat", borderwidth=0)
        s.map("Primary.TButton",
              background=[("active", _NAVY_H), ("disabled", "#B0BEC5")],
              foreground=[("disabled", _WHITE)])

        s.configure("Ghost.TButton",
                    background=_BG, foreground=_NAVY,
                    font=(_FONT, 10), padding=(10, 5),
                    relief="flat", borderwidth=0)
        s.map("Ghost.TButton",
              background=[("active", "#E8EEF7")],
              foreground=[("active", _NAVY)])

        s.configure("Prod.TCheckbutton",
                    background=_BG, foreground=_RED,
                    font=(_FONT, 10, "bold"))
        s.map("Prod.TCheckbutton", background=[("active", _BG)])

        s.configure("Test.TCheckbutton",
                    background=_BG, foreground=_BLUE,
                    font=(_FONT, 10, "bold"))
        s.map("Test.TCheckbutton", background=[("active", _BG)])

        s.configure("TRadiobutton", background=_BG, foreground="#212121",
                    font=(_FONT, 10))
        s.map("TRadiobutton", background=[("active", _BG)])

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
        return True

    # ── Mode toggle ────────────────────────────────────────────────────────

    def _toggle_test_mode(self) -> None:
        if self._test_var.get():
            self._test_check.config(text="Test Mode  —  files go to Testing folder",
                                    style="Test.TCheckbutton")
            self._reset_btn.pack(side=tk.RIGHT)
        else:
            self._test_check.config(text="PRODUCTION MODE  —  files will be moved for real!",
                                    style="Prod.TCheckbutton")
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
        self._process_directory(directory)

    def _process_directory(self, directory: str) -> None:
        year = self._year_entry.get()
        is_test = self._test_var.get()

        self._exit_btn["state"] = "disabled"
        self._year_entry["state"] = "disabled"
        self._run_btn["state"] = "disabled"
        self._run_label.config(text="Processing — please do not close the window", fg=_MUTED)
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

        self._run_label.config(text="Processing complete!", fg=_GREEN)
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
            if self._folder_option == "__ignore__":
                self._processor.ignore_file(filename)
            elif self._folder_option:
                renamed = self._processor.new_name(filename, self._processor.year)
                self._processor.do_query_unknown(filename, renamed, self._folder_option, learn=True)
            self._unknown_list.remove(filename)

    def _folder_select_popup(self, filename: str) -> Toplevel:
        win = Toplevel(self._root)
        win.title("Select Destination Folder")
        win.configure(bg=_BG)
        win.resizable(False, False)
        x, y = self._root.winfo_x(), self._root.winfo_y()
        win.geometry(f"+{x + 30}+{y + 30}")
        self._select_window = win

        tk.Label(win, text="This file could not be sorted automatically.",
                 bg=_BG, fg=_MUTED, font=(_FONT, 10)).pack(padx=24, pady=(18, 2))
        tk.Label(win, text="Select a destination folder, or close this window to skip.",
                 bg=_BG, fg=_MUTED, font=(_FONT, 10)).pack(padx=24)
        tk.Label(win, text=filename, bg=_BG, fg=_NAVY,
                 font=(_FONT, 10, "bold")).pack(padx=24, pady=(8, 12))
        tk.Frame(win, bg=_LINE, height=1).pack(fill=tk.X)

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

        v = tk.IntVar(value=12)
        rb_frame = tk.Frame(win, bg=_BG)
        rb_frame.pack(padx=24, pady=8, fill=tk.X)
        for i, opt in enumerate(options):
            ttk.Radiobutton(rb_frame, text=opt, variable=v, value=i).pack(anchor="w", pady=1)

        tk.Frame(win, bg=_LINE, height=1).pack(fill=tk.X)
        btn_frame = tk.Frame(win, bg=_BG)
        btn_frame.pack(pady=14)
        ttk.Button(btn_frame, text="Submit", style="Primary.TButton",
                   command=lambda: self._handle_folder_selection(options[v.get()])
                   ).pack(side=tk.LEFT, padx=8)
        ttk.Button(btn_frame, text="Ignore (always skip)", style="Ghost.TButton",
                   command=self._handle_ignore).pack(side=tk.LEFT, padx=8)

        return win

    def _handle_folder_selection(self, option: str) -> None:
        self._folder_option = option
        if self._select_window:
            self._select_window.destroy()

    def _handle_ignore(self) -> None:
        self._folder_option = "__ignore__"
        if self._select_window:
            self._select_window.destroy()

    # ── Origination file prompts ───────────────────────────────────────────

    def _create_orig_window(self, filename: str, pathname: str) -> Toplevel:
        self._orig_path = None
        win = Toplevel(self._root)
        win.configure(bg=_BG)
        win.resizable(False, False)
        self._orig_window = win

        tk.Label(win, text="Could not locate the following file:",
                 bg=_BG, fg=_MUTED, font=(_FONT, 10)).pack(padx=28, pady=(22, 4))
        tk.Label(win, text=filename, bg=_BG, fg=_NAVY,
                 font=(_FONT, 11, "bold")).pack(padx=28)
        tk.Label(win, text="Expected location:", bg=_BG, fg=_MUTED,
                 font=(_FONT, 10)).pack(padx=28, pady=(14, 4))
        tk.Label(win, text=pathname, bg=_BG, fg=_NAVY,
                 font=(_FONT, 10)).pack(padx=28)
        tk.Label(win, text="Please select the file manually, or click Skip.",
                 bg=_BG, fg=_MUTED, font=(_FONT, 10)).pack(padx=28, pady=(14, 0))
        tk.Frame(win, bg=_LINE, height=1).pack(fill=tk.X, pady=(16, 0))

        btn_frame = tk.Frame(win, bg=_BG)
        btn_frame.pack(pady=16)
        ttk.Button(btn_frame, text="Select File", style="Primary.TButton",
                   command=self._handle_orig_select).pack(side=tk.LEFT, padx=8)
        ttk.Button(btn_frame, text="Skip", style="Ghost.TButton",
                   command=win.destroy).pack(side=tk.LEFT, padx=8)

        return win

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
