
# Materials

In the Mat tab you can find the material settings. They determine how your mesh looks and how it is shaded. Some materials can also help rendering more FPS for large meshes (>500k triangles).
## Material dropdown

Pick a material from the list. You can use paint vertices in Beta > paint vertices to paint it, or the paint bucket for solid color.

For Matcap there is a secondary menu to select a specific matcap.
## Wireframe

Displays the wireframe for a quick topology check. This is resource intensive for large meshes (>500k triangles) and will drop FPS by 2-5 FPS.

If you used the freeze brush, wireframe will be on, play with the toggle to remove it after you unfreeze all vertices.
## Vertex Paint / PBR settings

If you use the Vertex paint material, you can set smoothness (make it shiny or not) and metallic (make it sort of reflective or not).
## Paint bucket

If you use the Vertex paint material, use this button to set a color for the whole material. Will overwrite any color (but you can undo).
## Apply to all children

If you click this checkbox then select a material, use the paint bucket or set smoothness / metallic, the layer and all its children will receive the update. Useful to generate a consistent look across multiple related layers.
# Performance

If you are working on a very large mesh and FPS drop is an issue, you can switch to a less ressource intensive material. Clay, Marble, Matcap are pretty efficient. Vertex Paint is medium efficient. Smooth wireframe or enabling wireframe toggle are the least efficient.
#  How to use the vertex paint in Blender

When you save your sculpture, each layer's color are saved in the FBX file (they are called vertex colors). If you want to see your mesh' s colors in Blender, you can create a simple Principled BSDF and hook Color Attribute to the color socket.
