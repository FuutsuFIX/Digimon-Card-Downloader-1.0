# Digimon Card Downloader 1.0
 Mass download Digimon TCg card arts using python and Digiprintmon as a source, downloaded images are named according to their card identifier. You can choose the folder you want to download cards in and keep it update with a download missing card features (obviously requires internet connection)
# Legal Disclaimer Regarding the Downloaded Images

Please be aware that the images downloaded using this software are copyrighted material and are the exclusive property of the Digimon Card Game, Bandai, and Toei. The use of these images is strictly for personal, non-commercial purposes only. Any reproduction, distribution, transmission, modification, or use of these images for commercial purposes, including but not limited to the sale, resale, or distribution of the images in any format, is strictly prohibited and may infringe upon the copyrights held by the respective owners.

This software is provided for educational and personal use only, and it must not be used to circumvent or violate any copyright laws. The users of this software are solely responsible for ensuring their actions comply with applicable copyright laws and regulations. The creator of this software does not endorse, support, or encourage any form of copyright infringement.

By using this software, users acknowledge that they are aware of the copyright restrictions and agree to use the images in compliance with all applicable laws and regulations. The creator of this software bears no responsibility for any illegal use or misuse of the images obtained through this software.

# Malware Identification
DigimonCardDownloader, may currently trigger false positive alerts from some antivirus software due to the nature of the PyInstaller packaging method. PyInstaller bundles Python scripts into a standalone executable, and this process can sometimes resemble the behavior of certain malware. If you have concerns about the executable, you can choose to compile the .py file manually. Here's a guide on how to do it and an overview of using PyInstaller:

# Manual Compilation:
To compile the DigimonCardDownloader.py file manually, you'll need to have Python installed on your system. Follow these steps:

Install Python: If you don't already have Python installed, download and install the latest version from the official website (https://www.python.org/downloads/).

Install Required Libraries: Open a command prompt or terminal and navigate to the directory containing DigimonCardDownloader.py. Use the following command to install any required libraries: pip install requests.

Run the Script: To run the script, use the command python DigimonCardDownloader.py. This method allows you to execute the code directly from the Python interpreter.

# Using PyInstaller:
If you still prefer to use the PyInstaller-generated executable, follow these steps:

Install PyInstaller: If you haven't already, install PyInstaller using pip: pip install pyinstaller.

Navigate to the Script Directory: Open a command prompt or terminal and navigate to the directory containing DigimonCardDownloader.py.

Create the Executable: Run the following command to create an executable from the Python script: pyinstaller --onefile DigimonCardDownloader.py.

Locate the Executable: PyInstaller will create a 'dist' directory within the script directory. Inside the 'dist' directory, you'll find the standalone executable.

By compiling the script manually or using PyInstaller, you can have more control over the process and alleviate concerns related to false positives triggered by antivirus software.
