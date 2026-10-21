# Python from zero

A first Python course for someone who has not programmed before. The lessons are Jupyter notebooks. Each one explains a word the first time it appears, then asks you to try one small step.

You start by learning what Jupyter is and how a notebook runs. Then you store values, work with text, keep several values together, make choices, repeat steps, and name a group of steps. You build a contact list, then learn files, errors, and modules so that list can be saved and opened again.

## Read this before you type anything

A **terminal** is a window where you type a line and press Enter to run it. A **command** is one of those lines. A **folder** is a place on the computer that holds files. A **file** is one saved document, such as this README.

These steps start from the course folder, the folder that already contains this `README.md` file, a `requirements.txt` file, and a `lessons` folder. You can read this README on the project page, or open the file in any text editor.

After you type or paste a command, press Enter to run it. To paste into the terminal, click the terminal window first. Then press Ctrl+Shift+V on Linux, Ctrl+V in Windows PowerShell, or Command+V on a Mac.

You need an internet connection for the install step. You do not need an account.

## 1. Open a terminal

- **Windows:** Click Start, type `PowerShell`, and open **Windows PowerShell**. The window that appears is the terminal.
- **Mac:** Press Command and the space bar together, type `Terminal`, and press Enter.
- **Linux:** Open your applications menu, search for Terminal, and open it.

The terminal is ready when you see a blinking cursor at the end of a line. A **cursor** is the mark that shows where the next thing you type will appear.

## 2. Move into the course folder

`cd` means change directory. It moves the terminal into a folder. A **path** is the list of folder names that leads to a place, separated by `/` on Mac and Linux and by `\` on Windows. Use the path to your course folder in place of the example.

**Mac or Linux**

```bash
cd /path/to/your/course/folder
```

This moves the terminal into the course folder.

**Windows PowerShell**

```powershell
cd C:\path\to\your\course\folder
```

This moves the terminal into the course folder.

Check the move:

```bash
ls
```

This lists the names in the current folder. You should see `README.md`, `requirements.txt`, and `lessons`. The same `ls` command works in Windows PowerShell.

## 3. Check that Python 3 is installed

**Mac or Linux**

```bash
python3 --version
```

This prints the Python version on your computer. You want a line that starts with `Python 3`.

**Windows PowerShell**

```powershell
python --version
```

This prints the Python version on your computer. You want a line that starts with `Python 3`.

If the terminal says the command was not found, try the other name, `python3` or `python`. If that prints `Python 3`, use that name in place of `python3` or `python` in the next command. If the version starts with `Python 2`, or Python is missing, install Python 3 from [python.org/downloads](https://www.python.org/downloads/) and open a new terminal. On the Windows installer, turn on **Add python.exe to PATH** before you click Install. PATH is the list of places the terminal looks for programs.

## 4. Create a private Python for this course

A **virtual environment** is a private Python setup stored in a folder for this course. The tools you install next go there.

**Mac or Linux**

```bash
python3 -m venv .venv
```

This creates a new folder named `.venv` inside the course folder. A leading dot means some file windows hide that folder. You do not need to open it.

**Windows PowerShell**

```powershell
python -m venv .venv
```

This creates the same `.venv` folder.

## 5. Turn on that private Python

**Mac or Linux**

```bash
source .venv/bin/activate
```

This points the terminal at the private Python. If it worked, the start of the line shows `(.venv)`.

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

This points the terminal at the private Python. If it worked, the start of the line shows `(.venv)`.

If PowerShell stops you with an error about running scripts, run this command, then try the activate command again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

This lets scripts run in this window only. Closing the window clears the setting.

## 6. Install Jupyter

```bash
pip install -r requirements.txt
```

This uses `pip`, Python's installer, to read `requirements.txt` and install JupyterLab and the notebook kernel. A **kernel** is the part of Jupyter that runs the code in a notebook. The first lesson explains the kernel again, more slowly. The same command works in Windows PowerShell. The installer prints many lines. When it finishes, you get a fresh line starting with `(.venv)`.

## 7. Start JupyterLab

```bash
jupyter lab
```

This starts JupyterLab and opens it in your browser. A **browser** is the program you use for websites, such as Chrome, Firefox, Edge, or Safari.

Leave the terminal window open while you study. Jupyter keeps running there. To stop it, click the terminal and press Ctrl+C. On a Mac that is also Ctrl+C. If the terminal asks you to confirm the shutdown, type `y` and press Enter.

If the browser does not open, look in the terminal for a line that starts with `http://localhost:` or `http://127.0.0.1:`. Paste that whole address into the browser's address bar and press Enter.

## 8. Open the first lesson

In the JupyterLab window, double-click the `lessons` folder in the file list on the left. Then double-click `01-your-first-notebook.ipynb`.

If Jupyter asks you to pick a kernel, choose **Python 3**.

Work in this order:

1. `01-your-first-notebook.ipynb` — what Jupyter is, what a cell is, how to run a cell, and how to read the output, then a check that the kernel runs
2. `02-variables-and-types.ipynb` — names that store values, and the kinds of values
3. `03-strings.ipynb` — text: length, positions, slices, and building new text
4. `04-lists-and-dicts.ipynb` — several values in order, and labeled pairs
5. `05-conditionals-and-loops.ipynb` — choices and repetition
6. `06-functions.ipynb` — naming a group of lines so you can run it again
7. `07-contact-list.ipynb` — a small contact list you finish one cell at a time
8. `08-files.ipynb` — read a text file, write a text file, and close it with `with`
9. `09-errors.ipynb` — `try` and `except` when a file is missing or a value is wrong
10. `10-modules.ipynb` — `import`, and `pathlib` and `datetime` from the standard library
11. `11-csv.ipynb` — save and load the contact list with the `csv` module
12. `12-saved-contacts.ipynb` — files, errors, and the contact list in one small project

Inside a lesson, run code cells with Shift+Enter and read the output under the cell. Sample answers are folded cells under the heading **Solution**. Try the step before you unfold the answer. The first notebook shows how to unfold one.

## The next time you study

On a later day, open a terminal, move into the course folder with `cd`, run the activate command from step 5, then run `jupyter lab`. The `.venv` folder and the installed tools stay on your computer.
