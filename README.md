# 🛠️ Automated Software Installer & Validator

A simple **Bash + Python hybrid tool** for **installing and uninstalling software** on Ubuntu. This project automates software setup and logs the process.

## 🚀 Features
✅ **GUI Interface** – Install/Uninstall software with a user-friendly UI.  
✅ **Logging** – Logs all installations and removals for debugging.  
✅ **Hybrid Approach** – Combines Python (Tkinter UI) and Bash (package handling).  
✅ **DEB Packaging** – Easily installable as a `.deb` package.  

## 📂 Project Structure

software_installer/ │── gui_installer.py # Python GUI script (Tkinter) │
── install_validator.sh # Bash script for installation & validation │── install_log.txt # Log file (captures actions) │
── requirements.txt # Dependencies (Python) │── software_installer.deb # Debian package (optional) │
── README.md # Documentation │── .gitignore # Ignore unnecessary files

## 📜 Prerequisites
Make sure you have the following installed:  
- Python 3.8+  
- Bash (default on Linux)  
- `tkinter` for GUI  

To install missing dependencies, run:  
```bash
sudo apt install python3-tk

💻 Installation & Usage
1️⃣ Clone the Repository

git clone https://github.com/yourusername/software_installer.git
cd software_installer

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python3 gui_installer.py

4️⃣ (Optional) Install Using .deb Package
sudo dpkg -i software_installer.deb
```bash```
```
## 🎯 Future Improvements

✅ Add a progress bar for installation.
✅ Improve error handling & validation.
✅ Package it for other Linux distros (RPM for Fedora).


## 📜 License

This project is licensed under the MIT License.

##⭐ Contributing

If you'd like to contribute, fork the repo and submit a PR! 😃

#### **3️⃣ Save and Exit the File**
- **Press** `CTRL + X` to exit the Nano editor.  
- **Press** `Y` to confirm saving the file.  
- **Press** `Enter` to save the file with the same name.  

#### **4️⃣ Verify the README.md File Exists**
Run this command:









if not run use this
Let's debug the issue. Can you provide:

The exact error message you see when running python3 gui_installer.py.
The output of ls -l ~/software_installer/ (to check if all files are correctly placed).
The output of cat ~/software_installer/install_log.txt (to check if logs are being generated).
Try running these and share the output. 🚀

