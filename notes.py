import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("600x400")
        self.file_path = None

        # Setup menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File menu
        file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Text area
        self.text_area = tk.Text(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=1, fill=tk.BOTH)
        self.text_area.focus_set()

    def new_file(self):
        if self._confirm_discard_changes():
            self.text_area.delete(1.0, tk.END)
            self.file_path = None
            self.root.title("Simple Notepad")

    def open_file(self):
        if not self._confirm_discard_changes():
            return
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.file_path = path
                self.root.title(f"Simple Notepad - {self.file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        if self.file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(content.rstrip('\n'))
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content.rstrip('\n'))
                self.file_path = path
                self.root.title(f"Simple Notepad - {self.file_path}")
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def _confirm_discard_changes(self):
        # Naive implementation: always return True (no unsaved change tracking)
        # For improvement: can add tracking for unsaved changes
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleNotepad(root)
    root.mainloop()

