import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
from tkinter import filedialog

# Define color constants
BACKGROUND_COLOR = "#FFFF00"  # Yellow
TEXT_COLOR = "#000000"  # Black
HIGHLIGHT_COLOR = "#000000"  # Black

class ClassListGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Class List Generator")
        self.geometry("800x600")
        self.configure(background=BACKGROUND_COLOR)

        # Bootstrap style
        style = Style(theme='flatly')
        style.configure('.', font=('Helvetica', 12), background=BACKGROUND_COLOR, foreground=TEXT_COLOR)
        style.configure('TButton', font=('Helvetica', 12), background=BACKGROUND_COLOR, foreground=TEXT_COLOR)
        style.configure('TFrame', background=BACKGROUND_COLOR)
        style.configure('TLabel', background=BACKGROUND_COLOR, foreground=TEXT_COLOR)
        style.configure('TEntry', background=BACKGROUND_COLOR, foreground=TEXT_COLOR)

        # Header image
        header_image = tk.PhotoImage(file="header_image.png")
        header_label = tk.Label(self, image=header_image, bg=BACKGROUND_COLOR)
        header_label.image = header_image
        header_label.grid(row=0, columnspan=4, pady=10)

        # Input frame
        input_frame = ttk.Frame(self, style='TFrame', padding=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10)

        self.create_label("Course Code:", input_frame, 0, 0)
        self.entry_course_code = self.create_entry(input_frame, 0, 1)

        self.create_label("Section:", input_frame, 1, 0)
        self.entry_section = self.create_entry(input_frame, 1, 1)

        self.generate_button = ttk.Button(input_frame, text="Generate Class List", command=self.generate_class_list)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Output frame
        output_frame = ttk.Frame(self, style='TFrame', padding=10)
        output_frame.grid(row=1, column=1, padx=10, pady=10)

        # Class list display
        self.class_list_text = tk.Text(output_frame, height=10, width=70, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        self.class_list_text.pack(side=tk.LEFT)

        # Print button
        self.print_button = ttk.Button(output_frame, text="Print", command=self.print_class_list)
        self.print_button.pack(side=tk.RIGHT, padx=10)

    def create_label(self, text, parent, row, column):
        label = ttk.Label(parent, text=text, style='TLabel')
        label.grid(row=row, column=column, padx=5, pady=5, sticky="w")
        return label

    def create_entry(self, parent, row, column):
        entry = ttk.Entry(parent, style='TEntry')
        entry.grid(row=row, column=column, padx=5, pady=5, sticky="w")
        return entry

    def generate_class_list(self):
        course_code = self.entry_course_code.get()
        section = self.entry_section.get()

        # Dummy data for demonstration
        class_list = [
            {"STUDENT NO": "2110392", "STUDENT NAME": "ALAO, GENN REY PIAO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110015", "STUDENT NAME": "ALONSAGAY, EDRALIN FROILAN DOMINGO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110486", "STUDENT NAME": "AMEGLEO, JOHN PAUL BOLVIDER", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2113184", "STUDENT NAME": "ASGAR, CLYDE DENZEL RADO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110946", "STUDENT NAME": "AUSTRIA, KAYLA MAE SALUCOP", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2111177", "STUDENT NAME": "BAUTISTA, NINA FRANCESCA ALDON", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2113508", "STUDENT NAME": "BIÑAS, ANDRIAN BONEO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110600", "STUDENT NAME": "CAPUCION, ARJOHN VERDERA", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2112385", "STUDENT NAME": "CAYUBE, ADRIANA EMERY ESCUETA", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110539", "STUDENT NAME": "COMIA, JASMINE ROGELIO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2113507", "STUDENT NAME": "CONDOLON, CHARLES JUSTIN LEE ALAJAR", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2112771", "STUDENT NAME": "CORTEZANO, ELIJAH DAVID DELA CRUZ", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2120050", "STUDENT NAME": "DE JOYA, JALEN JOHN DIMAANO", "YEAR": "2", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2111629", "STUDENT NAME": "DE VERA, BARON MORALES", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2111494", "STUDENT NAME": "DELA CRUZ, JOVINEIL VILLAMAYOR", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2112965", "STUDENT NAME": "ENCELA, JOSHUA CORTEZ", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110494", "STUDENT NAME": "ESCONDE, KHIEL IAN VIGO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2113143", "STUDENT NAME": "ESPINOSA, RONWALDO CHAVEZ", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2113481", "STUDENT NAME": "GALLEGO, REIGN MARIELLE TAMAYO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110081", "STUDENT NAME": "HIJE, JERICHO AMIO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110366", "STUDENT NAME": "JABAT, JOSHUA IVAN MONTANO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2111012", "STUDENT NAME": "LAHOZ, KRISIA JOVAN CAPINPIN", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110281", "STUDENT NAME": "POSTRERO, RAYMOND SINUGBUHAN", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2112757", "STUDENT NAME": "REYES, DAN BALICHA", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2110119", "STUDENT NAME": "RONQUILLO, RAFAEL DELFIN", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2120033", "STUDENT NAME": "SANTILLAN, KRIZZIA PEARL EVANGELISTA", "YEAR": "2", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2111412", "STUDENT NAME": "SANTOS, GEOMAR VELASCO", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2120103", "STUDENT NAME": "TAN, KIM MICHAEL LIM", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2112280", "STUDENT NAME": "TORRIANA, KESHA NACIONALES", "YEAR": "3", "PROGRAM": "BSCS"},
            {"STUDENT NO": "2112367", "STUDENT NAME": "VARDE, KIAN DENNIEL RIVERA", "YEAR": "3", "PROGRAM": "BSCS"}
        ]
        # Display the class list in the text widget
        self.class_list_text.delete("1.0", tk.END)
        self.class_list_text.insert(tk.END, f"Class List for {course_code} - Section {section}\n")
        for student in class_list:
            self.class_list_text.insert(tk.END, f"Student ID: {student['STUDENT NO']}, Name: {student['STUDENT NAME']}\n")

        # Display confirmation message
        messagebox.showinfo("Class List Generated", f"Class list for {course_code} - Section {section} has been generated.")

    def print_class_list(self):
        class_list_text = self.class_list_text.get("1.0", tk.END)
        # Print the class list text
        print(class_list_text)

if __name__ == "__main__":
    app = ClassListGeneratorApp()
    app.mainloop()
