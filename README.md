# Blender 2.80+ Fortnite Auto .MAT Loader

This automatic .MAT loader creates a Blender material that can be applied to an object.
**Currently** Only works when .MAT files are in the same directory as the textures.

**Textures Supported** - Diffuse, Normal, Specular, Emissive 

# Setup/Installation

1. Download the **[AutoMaterialLoader.py](https://github.com/mr910/BlenderFortniteMaterial/blob/master/FortniteMaterialLoader.py)** file **OR** Click the ilnk --> Click 'Raw' --> 'Copy All' **Ctrl + A** --> 'Paste' **Ctrl + C**
2. Open Blender and in the top right, go to the 'Scripting' tab.
3. Drag **AutoMaterialLoader.py** file into the large text box **OR** Paste the 'Raw' code there.

# How-To Use

1. After importing into 'Scripting', - Collect your exported .MAT file and .TGA textures **(ONLY TGA)**
2. Move the .MAT file(s) into the same folder as the textures
   (Most cosmetics should do this, you can also just drag the textures into the same folder if they are split up)
   This was modified to deal with the most common cases.
![alt text](https://i.imgur.com/msfkUP8.gif)
3. Copy the full path of the .MAT file, this can be done by shift right clicking in 'Windows Explorer' and clicking 'Copy As Path'.
4. From the 'Scripting' tab, paste the full path after "DotMatPath = r" - It should look something like: 

   `DotMatPath = r"C:\PathToUmodelEtc\material.MAT"`
   
5. There are two options available:
   
   * `outputMaterialName` - Determines material name output. Blank matches the filename ex. (`outputMaterialName = ""`)
   * `ApplyMaterialToCurrentlySelectedObject` - Applies material to the currently selected object. `True` or `False` is __case-senitive__.
   
6. Press "Run Script" at the top right.

# Demonstration of usage

https://i.imgur.com/4OMVs4T.mp4

Modified to work with [Blender 2.83 LTS+](https://www.blender.org/download/lts/)
