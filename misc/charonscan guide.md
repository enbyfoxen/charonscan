# Guide to setting up ShareX for charonscan

 1. Download and install ShareX: [https://getsharex.com/](https://getsharex.com/)
2. Download the config file: [charonscan.sxcu](https://scan.ripcharon.space/data/charonscan.sxcu)
3. Open ShareX, select `Destinations` then `Custom uploader settings...`
![Custom uploader settings](https://i.imgur.com/GM3O3uJ.png)

4. Select `import` then `From file...`
![import custom uploader](https://i.imgur.com/pxQc6Ab.png)

5. Navigate to the `charonscan.sxcu` file that you downloaded earlier and open it.
![import custom uploader](https://i.imgur.com/LOrsd96.png)

6. Ensure `Text Uploader` is set to `Charonscan`
![set text uploader](https://i.imgur.com/ICNwicz.png)

7. Close the `Custom uploader settings` and select `Hotkey settings...` in the main window.
![hotkey settings](https://i.imgur.com/L2wzE2Q.png)

8. In the window that opens, select `Add...`
![add shortcut](https://i.imgur.com/5V2Hs3x.png)

9. In the window that opens, open the `Task` Drop down menu, select `Upload` then `Upload from clipboard`
![set task](https://i.imgur.com/zxvD9xV.png)

10.  Enable the `Override destinations` checkbox, then open the `Destinations...` dropdown.
Select `Text uploader` then select `Custom text uploader`.
![set destination](https://i.imgur.com/WmEkunM.png)

11. Enable the `Override after upload settings` checkbox.
Open the `After upload:` dropdown menu.
Then enable `Copy URL to clipboard` and/or `Open URL` depending on your preferences.
![after upload settings](https://i.imgur.com/SJsNH8t.png)

12. Close the `Task settings for Upload from clipboard window` to return to the `Hotkey settings` window.
Click on the button next to the custom hotkey you created, and set a shortcut of your choosing.
![set shortcut](https://i.imgur.com/SkEcCye.png)

13. Close the `Hotkey settings` window. Your shortcut is now configured. 
To upload a D-Scan to charonscan, copy it to your clipboard, then hit your shortcut.
It will upload the D-Scan. After the second or two, depending on what you set earlier, a browser window with the D-Scan will open, the D-Scan link be copied to your clipboard, or both.
ShareX will also give you a pop-up telling you `Task completed`
![success](https://i.imgur.com/5BT5erp.png)
***
Should your clipboard not contain a valid D-Scan, or a server issue occurs, ShareX will instead serve you an error pop-up.
![enter image description here](https://i.imgur.com/lougBvL.png)


