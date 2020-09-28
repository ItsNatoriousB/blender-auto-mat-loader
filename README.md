# Blender 2.80 Fortnite .mat Auto Loader

This automatic .MAT loader creates a Blender material that you apply to a object.
**CurRENTLY** Only works when .MAT files re in the samedirectory as the textures

Supports Diffuse, Normal, Specular & Emissive textures

# Setup/Installation

1. Download the .py file (or click it, then click raw and ctrl+a -> ctrl+c it)
2. Open Blender
3. Go to the scripting tab, and drag the .py file into the large text box (or paste the code into there from earlier)

# How to use
1. Once you have it imported into the scripting tab, you should setup your exported .mat and exported .tga textures (you must use tga at the moment)
2. Move the .mat file you want to import to the same folder as the textures (Majority of cosmetics should do this, you can also just drag the textures into the same folder if they are split up, but this is made to deal with the most common case)
![alt text](https://i.imgur.com/msfkUP8.gif)
3. Copy the full path of the .mat file, this can be done by shift right clicking in windows explorer and clicking "Copy As Path"
4. In the scripting tab in blender, past the full path after "DotMatPath = r", It should look something like: 

   `DotMatPath = r"C:\PathToUmodelEtc\material.mat"`
   
5. There are two other options available:
   
   `outputMaterialName` Used to determine the output material name. Leave blank (`outputMaterialName = ""`) to match the filename
   
   `ApplyMaterialToCurrentlySelectedObject` - Applies material to the currently selected object. `True` or `False` is case-senitive.
   
6. Press "Run Script" at the top right

# Demonstration of usage
https://i.imgur.com/4OMVs4T.mp4

Created on blender 2.80, other versions not verified.
