# Configuration for Call Of Duty Warzone
# Texture map types will be defined here

import bpy
import os
from mathutils import Vector

# Input Configuration
# Enter the path to the .MAT file and textures.
# Texture(s) and .MAT file(s) MUST be in the same folder.
# Shift + right click a selected folder/file in Windows Explorer 
# Click "Copy As Path" and then paste it in bewtween the quotation marks (after the r)

DotMatPath = r""

# Material Output Name
# Change to just "" to use the .MAT filename
outputMaterialName = "" 

# Apply Switch
# Disable if the object has multiple materials and apply manually from "Shading' tab in Blender
ApplyMaterialToCurrentlySelectedObject = False 
# Input Configuration End
# DO NOT TOUCH ANY CODE BELOW

# Material Creation
if not outputMaterialName:
    outputMaterialName = os.path.basename(DotMatPath)

mat = bpy.data.materials.new(name=outputMaterialName)
mat.use_nodes = True
materialOutput = mat.node_tree.nodes.get('Material Output')
principleBSDF = mat.node_tree.nodes.get('Principled BSDF')

# Remove Inital Link
mat.node_tree.links.remove(principleBSDF.outputs[0].links[0]) 

addShader = mat.node_tree.nodes.new("ShaderNodeAddShader")
mat.node_tree.links.new(principleBSDF.outputs[0], addShader.inputs[0])
mat.node_tree.links.new(addShader.outputs[0], materialOutput.inputs[0])
addShader.location = Vector((400, -250))
materialOutput.location = Vector((650, -250))

textureBasePath = os.path.dirname(DotMatPath)

with open(DotMatPath) as f:
    for l in f:
        line = l.rstrip()
        if line.startswith("Diffuse="):
            diffuseImgPath = textureBasePath + r"/" + line.replace("Diffuse=", "") + ".tga"
            print(diffuseImgPath)
            #Diffuse Texture
            diffuseTex = mat.node_tree.nodes.new("ShaderNodeTexImage")
            diffuseImg = bpy.data.images.load(filepath = diffuseImgPath)
            diffuseTex.image = diffuseImg
            diffuseTex.location = Vector((-400,450))
            #diffuseTex.hide = True

            #Connect diffuse texture to 'PrincipleBSDF'
            mat.node_tree.links.new(diffuseTex.outputs[0], principleBSDF.inputs[0])
            #Diffuse End
        elif line.startswith("Normal="):
            normalImgPath = textureBasePath + r"/" + line.replace("Normal=", "") + ".tga"
            print(normalImgPath)
            
            #Normal Start
            normY = -125
            normTex = mat.node_tree.nodes.new("ShaderNodeTexImage")
            normCurve = mat.node_tree.nodes.new("ShaderNodeRGBCurve")
            normMap = mat.node_tree.nodes.new("ShaderNodeNormalMap")
            normImage = bpy.data.images.load(filepath = normalImgPath)
            
            #Location
            normTex.location = Vector((-800, normY))
            normCurve.location = Vector((-500, normY))
            normMap.location = Vector((-200, normY))

            normImage.colorspace_settings.name = 'Non-Color'
            normTex.image = normImage
            #normTex.hide = True

            #Setup 'RGB Curve'
            normCurve.mapping.curves[1].points[0].location = (0,1)
            normCurve.mapping.curves[1].points[1].location = (1,0)

            #Connect Everything
            mat.node_tree.links.new(normTex.outputs[0], normCurve.inputs[1])
            mat.node_tree.links.new(normCurve.outputs[0], normMap.inputs[1])
            mat.node_tree.links.new(normMap.outputs[0], principleBSDF.inputs['Normal'])
            #Normal End
        elif line.startswith("Specular="):
            specularImgPath = textureBasePath + r"/" + line.replace("Specular=", "") + ".tga"
            print (specularImgPath)
            
            #Specular Start
            specY = 140
            specTex = mat.node_tree.nodes.new("ShaderNodeTexImage")
            specSeperateRGB = mat.node_tree.nodes.new("ShaderNodeSeparateRGB")
            specSeperateRGB.location = Vector((-250, specY))
            #specSeperateRGB.hide = True

            specImage = bpy.data.images.load(filepath = specularImgPath)
            specImage.colorspace_settings.name = 'Non-Color'

            specTex.image = specImage
            specTex.location = Vector((-600, specY))
            #specTex.hide = True

            #Connect specular texture to 'Seperate RGB'
            mat.node_tree.links.new(specTex.outputs[0], specSeperateRGB.inputs[0])
            #Connect 'Seperate RGB' to 'PrincipleBSDF'
            mat.node_tree.links.new(specSeperateRGB.outputs[0], principleBSDF.inputs['Specular'])
            mat.node_tree.links.new(specSeperateRGB.outputs[1], principleBSDF.inputs['Metallic'])
            mat.node_tree.links.new(specSeperateRGB.outputs[2], principleBSDF.inputs['Roughness'])
            #Specular End
        elif line.startswith("Emissive="):
            emissiveImgPath = textureBasePath + r"/" + line.replace("Emissive=", "") + ".tga"
            print (emissiveImgPath)
            #Emission Start
            emiTex = mat.node_tree.nodes.new("ShaderNodeTexImage")
            emiShader = mat.node_tree.nodes.new("ShaderNodeEmission")
            emiImage = bpy.data.images.load(filepath = emissiveImgPath)
            emiTex.image = emiImage
            #Emission - location
            emiTex.location = Vector((-200, -425))
            emiShader.location = Vector((100, -425))
            #Connecting
            mat.node_tree.links.new(emiTex.outputs[0], emiShader.inputs[0])
            mat.node_tree.links.new(emiShader.outputs[0], addShader.inputs[1])
            #Emission End           

            
           #END
if ApplyMaterialToCurrentlySelectedObject:
    bpy.context.active_object.data.materials[0] = mat
