# Gemini created this on Jan 16, 2026
# Updated July 2026

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from tkinter.colorchooser import askcolor

class TKWindow:
    def __init__(self):
        """Initializes a hidden root window to prevent 'ghost' windows."""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main tkinter window
        self.root.attributes("-topmost", True)  # Keep pop-ups on top

    # ==========================================
    # 1. MESSAGE & NOTIFICATION BOXES
    # ==========================================
    def info(self, title, message, **kwargs):
        """Displays a standard info box. Returns 'ok'."""
        return messagebox.showinfo(title, message, **kwargs)

    def warning(self, title, message, **kwargs):
        """Displays a warning box. Returns 'ok'."""
        return messagebox.showwarning(title, message, **kwargs)

    def error(self, title, message, **kwargs):
        """Displays an error box. Returns 'ok'."""
        return messagebox.showerror(title, message, **kwargs)

    # ==========================================
    # 2. QUESTION & CONFIRMATION BOXES
    # ==========================================
    def ask_yes_no(self, title, message, **kwargs):
        """Returns True for 'Yes', False for 'No'."""
        return messagebox.askyesno(title, message, **kwargs)

    def ask_ok_cancel(self, title, message, **kwargs):
        """Returns True for 'OK', False for 'Cancel'."""
        return messagebox.askokcancel(title, message, **kwargs)

    def ask_retry_cancel(self, title, message, **kwargs):
        """Returns True for 'Retry', False for 'Cancel'."""
        return messagebox.askretrycancel(title, message, **kwargs)

    def ask_question(self, title, message, **kwargs):
        """Returns string 'yes' or 'no'."""
        return messagebox.askquestion(title, message, **kwargs)

    def ask_yes_no_cancel(self, title, message, **kwargs):
        """Returns True for 'Yes', False for 'No', and None for 'Cancel'."""
        return messagebox.askyesnocancel(title, message, **kwargs)

    # ==========================================
    # 3. USER INPUT PROMPTS
    # ==========================================
    def get_string(self, title, prompt, **kwargs):
        """Prompts for a string. Returns string or None."""
        return simpledialog.askstring(title, prompt, parent=self.root, **kwargs)

    def get_password(self, title, prompt, **kwargs):
        """Prompts for a string but masks the text with asterisks (*). Returns string or None."""
        return simpledialog.askstring(title, prompt, show="*", parent=self.root, **kwargs)

    def get_integer(self, title, prompt, min_val=None, max_val=None, **kwargs):
        """Prompts for an integer. Can use minvalue/maxvalue in kwargs or direct arguments."""
        minvalue = min_val if min_val is not None else kwargs.pop('minvalue', None)
        maxvalue = max_val if max_val is not None else kwargs.pop('maxvalue', None)
        return simpledialog.askinteger(title, prompt, minvalue=minvalue, maxvalue=maxvalue, parent=self.root, **kwargs)

    def get_float(self, title, prompt, min_val=None, max_val=None, **kwargs):
        """Prompts for a float. Can use minvalue/maxvalue in kwargs or direct arguments."""
        minvalue = min_val if min_val is not None else kwargs.pop('minvalue', None)
        maxvalue = max_val if max_val is not None else kwargs.pop('maxvalue', None)
        return simpledialog.askfloat(title, prompt, minvalue=minvalue, maxvalue=maxvalue, parent=self.root, **kwargs)

    # ==========================================
    # 4. FILE & DIRECTORY DIALOGS
    # ==========================================
    def select_file(self, title="Select File", **kwargs):
        """Opens a file selector. Returns selected file path (str) or empty string."""
        return filedialog.askopenfilename(title=title, **kwargs)

    def select_multiple_files(self, title="Select Files", **kwargs):
        """Opens a file selector allowing multiple selections. Returns a tuple of paths."""
        return filedialog.askopenfilenames(title=title, **kwargs)

    def save_file_as(self, title="Save As", default_ext="", **kwargs):
        """Opens a 'Save As' dialog. Returns selected file path (str) or empty string."""
        return filedialog.asksaveasfilename(title=title, defaultextension=default_ext, **kwargs)

    def select_folder(self, title="Select Folder", **kwargs):
        """Opens a directory selector. Returns directory path (str) or empty string."""
        return filedialog.askdirectory(title=title, **kwargs)

    # ==========================================
    # 5. SPECIAL DIALOGS
    # ==========================================
    def select_color(self, title="Choose Color", initial_color=None, **kwargs):
        """Opens a color picker. Returns tuple: ((R, G, B), '#hexcode') or (None, None)."""
        return askcolor(color=initial_color, title=title, **kwargs)

    # ==========================================
    # CLEANUP
    # ==========================================
    def __del__(self):
        """Clean up the root window when the object is destroyed."""
        try:
            self.root.destroy()
        except Exception:
            pass