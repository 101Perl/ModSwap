# 📂 ModSwap
App created to change mod packs for Minecraft versions easily

## Screenshot
![image](https://github.com/101Perl/ModSwap/assets/70055689/de2944ca-258f-4946-a24c-e7b0c54f6a71)

## How to use it?
1. Firstly, change the `config.py` file
   - You can open it using Notepad.
   - Then fill in paths as it shown here:
    
    ![image](https://github.com/101Perl/ModSwap/assets/70055689/585dac19-5921-4680-9cc0-fc3caa00d71f)
    
Make sure to use `/` symbol in paths instead of `\`, also there are should be no `/` symbol at the end
   
   - In `path_current_mods` fill in path with `/mods` at the end
   - In `path_available_mods` leave path where your mod packs (folders with different mods) are located
    
2. If you're using Python file to start app you need to install modules
   
   - `pip install shutil PyQt6`
    
3. Open the app
4. Choose one of the folders with mods
5. Use button `Replace` to replace `mods` folder by selected one

+ Use button `Delete current mods folder` to delete `mods` folder which is now located in AppData
