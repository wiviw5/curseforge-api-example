# CurseForge API Example

A simple example script made in python to make downloading from curseforge API more accessible & open to learn about.

---

### **API Keys:**

API Keys are not given out, as this is only example code and thus does not have an associated API key. Please follow this [link](https://support.curseforge.com/en/support/solutions/articles/9000208346-about-the-curseforge-api-and-how-to-apply-for-a-key) for more information from CurseForge's website on how to obtain an API key for use with this application.

---

### **Installation Requirements:**

This has only been tested to work on [python](https://www.python.org/downloads/) 3.10. Versions **BELOW** this version may not work, versions above should work, please report if it does not.

This uses the pip package [requests](https://pypi.org/project/requests/), and will not work without it. Installation guide can be found below and within the link if you are savy.

This should work on all operating systems, please report if it does not, instructions for MACOS not included.

---

### **Installation Instructions :**

I will have instructions for both Windows and Linux with commands labeled as such. Follow along with the guide for your OS.

**Tip!** The `$` sign indicates a command should be run, it should not be included in the command.

#### Step 1: Making a virtual environment

Part 1:
- On Windows: `Open command prompt within the folder containing main.py`
- On Linux: `Open a terminal session within the folder containing main.py`

Part 2:
- On Windows: `$ python -m venv venv`
- On Linux `$ python3 -m venv venv`


#### Step 2: Using the virtual environment

- On Windows: `$ \venv\Scripts\activate`
- On Linux `$ . venv/bin/activate`

Once done, you should see at the very left of your terminal/command prompt: `(venv) <path>`

#### Step 3: Installing requests

- Same on both: `$ pip install requests`

#### Step 4: Running the program

**If within the virtual environment from earlier steps:**

- On Windows: `$ python main.py`
- On Linux `$ python3 main.py`

**If running from a new command prompt/terminal window:**

Part 1:
- Follow only step 2 again.

Part 2:
- On Windows: `$ python main.py`
- On Linux `$ python3 main.py`

---

## License:

Licensed under [MS-PL](https://opensource.org/licenses/MS-PL) (Microsoft Public License)