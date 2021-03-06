# pyTimelapse

## Abstract

* An Extra-long Timelapse Solution Using Python and ADB

* Overview

  ```mermaid
  graph LR
  A(pyTimelapse)
  	A --> B(Hardware)
    	B --> C(Fixed Tripod)
    	B --> D(Water Proof)
    	B --> E(Power Line)
   	A --> F(Software)
   		F --> K(Python Scripts)
   			K --> L(pyTimelapse: Main Function)
   			K --> M(copyfiles.py)
   		F --> N(Robust Utilities)
   			N --> O(Autostart)
   			N --> P(Restart Host Computer After Power Failure)
   		F --> G(Dependencies)
   			G --> H(ADB)
   			G --> I(scrcpy)
   			G --> J(Python Modules)
  ```

  > Typora graph LR

## Installing Dependencies

1. Android Debug Bridge: https://developer.android.google.cn/studio/releases/platform-tools
2. scrcpy: https://github.com/Genymobile/scrcpy
3. Python packages: use pip to install whatever is missing

## Usage

1. Main function: `python3 timelapse.py`
   * This file is highly mobile-device dependent
   * Please **read through the code and customize it according to your needs** before you put it into work 
2. Select & copy files: `python3 copyfiles.py`
   * Again, you may need to **configure paths** before it can work properly

## Auto Startup Scripts

1. `start.sh` is for linux/macos and `start_win.bat` is for windows
2. Specify values of `<IP>` and `<REPO PATH>` in these files
3. Add the execution of the script to your OS startup application list
4. In BIOS settings, set your computer to "reboot after a power failure"
   * windows users may find autologon helpful: https://docs.microsoft.com/zh-cn/sysinternals/downloads/autologon





