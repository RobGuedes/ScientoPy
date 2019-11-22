# !/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

import tkinter.scrolledtext as scrolledtext
from PIL import ImageTk, Image
import globalVar
from PreProcessClass import PreProcessClass
from ScientoPyClass import ScientoPyClass
from generateBibtex import generateBibtex
import webbrowser


class ScientoPyGui:
    def __init__(self):
        self.scientoPy = ScientoPyClass(from_gui=True)

        self.root = Tk()
        self.root.geometry("853x480")
        self.root.resizable(width=False, height=False)
        self.root.title("ScientoPy")

        # Starting the tabs
        self.nb = ttk.Notebook(self.root)
        preprocess_page = Frame(self.nb)
        process_page = Frame(self.nb)

        self.nb.add(preprocess_page, text='1. Pre-processing')
        self.nb.add(process_page, text='2. Analysis')
        self.nb.pack(expand=1, fill="both")
        self.nb.select(preprocess_page)

        # Pre processing tab
        load = Image.open("scientopy_logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(preprocess_page, image=render)
        img.image = render
        img.place(relx=0.5, rely=0.4, anchor=CENTER)

        version_label = Label(preprocess_page, text=("Version %s" % globalVar.SCIENTOPY_VERSION))
        version_label.place(relx=0.5, rely=0.7, anchor=CENTER)

        dataset_button = Button(preprocess_page, text="Select dataset", command=self.select_dataset)
        dataset_button.place(relx=0.9, rely=0.8, anchor=CENTER)
        Label(preprocess_page, text="Dataset folder:").place(relx=0.02, rely=0.8, anchor=W)
        self.datasetLoc = StringVar()
        self.datasetLocEntry = Entry(preprocess_page, width=70, bg='white', textvariable=self.datasetLoc)
        self.datasetLocEntry.place(relx=0.47, rely=0.8, anchor=CENTER)

        run_preprocess_button = Button(preprocess_page, text="Run preprocess", command=self.run_preprocess)
        run_preprocess_button.place(relx=0.9, rely=0.9, anchor=CENTER)

        self.chkValueRemoveDupl = BooleanVar()
        self.chkValueRemoveDupl.set(True)
        Checkbutton(preprocess_page, var=self.chkValueRemoveDupl,
                    text="Remove duplicated documents").place(relx=0.015, rely=0.9, anchor=W)

        # Analysis tab
        Label(process_page, text="").grid(sticky=W, column=0, row=0)
        Label(process_page, text="Criterion:", borderwidth=10).grid(sticky=W, column=0, row=1)
        self.comboCriterion = ttk.Combobox(process_page, values=globalVar.validCriterion, width=15)
        self.comboCriterion.current(3)
        self.comboCriterion.grid(column=1, row=1)

        Label(process_page, text="Graph type:", borderwidth=10).grid(sticky=W, column=0, row=2)
        self.comboGraphType = ttk.Combobox(process_page, values=globalVar.validGrapTypes, width=15)
        self.comboGraphType.current(0)
        self.comboGraphType.grid(column=1, row=2)

        Label(process_page, text="Start Year:", borderwidth=10).grid(sticky=W, column=0, row=3)
        self.spinStartYear = Spinbox(process_page, from_=1900, to=2100, bg='white',
                                     textvariable=DoubleVar(value=globalVar.DEFAULT_START_YEAR), width=15)
        self.spinStartYear.grid(column=1, row=3)

        Label(process_page, text="End Year:", borderwidth=10).grid(sticky=W, column=0, row=4)
        self.spinEndYear = Spinbox(process_page, from_=1900, to=2100, bg='white',
                                   textvariable=DoubleVar(value=globalVar.DEFAULT_END_YEAR), width=15)
        self.spinEndYear.grid(column=1, row=4)

        Label(process_page, text="Topics length:", borderwidth=10).grid(sticky=W, column=0, row=5)
        self.spinTopicsLength = Spinbox(process_page, from_=0, to=1000, bg='white', textvariable=DoubleVar(value=10),
                                        width=15)
        self.spinTopicsLength.grid(column=1, row=5)

        Label(process_page, text="Window (years):", borderwidth=10).grid(sticky=W, column=0, row=6)
        self.spinWindowWidth = Spinbox(process_page, from_=0, to=100, bg='white', textvariable=DoubleVar(value=2),
                                       width=15)
        self.spinWindowWidth.grid(column=1, row=6)

        process_page.grid_columnconfigure(2, pad=50)

        Label(process_page, text="Custom topics:", borderwidth=10).grid(sticky=W, column=2, row=1, padx=15)
        self.entryCustomTopics = scrolledtext.ScrolledText(process_page, undo=True, bg='white', width=70, height=10)
        self.entryCustomTopics.grid(column=2, row=2, rowspan=5)

        self.chkValuePreviusResults = BooleanVar()
        self.chkValuePreviusResults.set(False)
        Checkbutton(process_page, var=self.chkValuePreviusResults,
                    text="Use previous results").place(relx=0.01, rely=0.6, anchor=W)

        self.chkValueTrendAnalysis = BooleanVar()
        self.chkValueTrendAnalysis.set(False)
        Checkbutton(process_page, var=self.chkValueTrendAnalysis,
                    text="Trend analysis").place(relx=0.3, rely=0.6, anchor=W)


        run_button = Button(process_page, text="Run", command=self.scientoPyRun)
        run_button.place(relx=0.95, rely=0.9, anchor=E)

        genbibtex_button = Button(process_page, text="Generate BibTeX", command=self.generate_bibtex)
        genbibtex_button.place(relx=0.02, rely=0.8, anchor=W)

        results_button = Button(process_page, text="Open results table", command=self.open_results)
        results_button.place(relx=0.02, rely=0.9, anchor=W)

        ext_results_button = Button(process_page, text="Open extended results", command=self.open_ext_results)
        ext_results_button.place(relx=0.22, rely=0.9, anchor=W)

    def open_results(self):
        webbrowser.open(self.scientoPy.resultsFileName)

    def open_ext_results(self):
        webbrowser.open(self.scientoPy.extResultsFileName)

    def scientoPyRun(self):
        print(self.chkValuePreviusResults.get())

        self.scientoPy.closePlot()

        self.scientoPy.criterion = self.comboCriterion.get()
        self.scientoPy.graphType = self.comboGraphType.get()
        self.scientoPy.startYear = int(self.spinStartYear.get())
        self.scientoPy.endYear = int(self.spinEndYear.get())
        self.scientoPy.length = int(self.spinTopicsLength.get())
        self.scientoPy.windowWidth = int(self.spinWindowWidth.get())
        self.scientoPy.previousResults = self.chkValuePreviusResults.get()
        self.scientoPy.trend = self.chkValueTrendAnalysis.get()

        if bool(self.entryCustomTopics.get("1.0", END).strip()):
            self.scientoPy.topics = self.entryCustomTopics.get("1.0", END).replace("\n",";")
        else:
            self.scientoPy.topics = ''

        self.scientoPy.scientoPy()

    def select_dataset(self):
        self.root.dir_name = filedialog.askdirectory()
        if not self.root.dir_name:
            return

        self.datasetLoc.set(self.root.dir_name)

    def run_preprocess(self):
        if self.datasetLoc.get():
            preprocess = PreProcessClass(from_gui=True)
            preprocess.dataInFolder = self.root.dir_name
            preprocess.noRemDupl = not self.chkValueRemoveDupl.get()
            totalPapers = preprocess.preprocess()
            if totalPapers == 0:
                messagebox.showinfo("Error", "No valid dataset files found in: %s" % self.root.dir_name)
        else:
            messagebox.showinfo("Error", "No dataset folder defined")

    def generate_bibtex(self):
        latexFileName = filedialog.askopenfilename(initialdir="./", title="Select the LaTeX file",
                                                   filetypes=(("Latex", "*.tex"), ("all files", "*.*")))

        if not latexFileName:
            return

        print(latexFileName)
        outFileName = generateBibtex(latexFileName)
        webbrowser.open(outFileName)


    def runGui(self):
        self.root.mainloop()


if __name__ == '__main__':
    scientoPyGui = ScientoPyGui()
    scientoPyGui.runGui()
