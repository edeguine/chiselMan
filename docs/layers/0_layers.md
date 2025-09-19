
# Layers

Layers can be accessed in the Layers tab. They work just like in Procreate or Photoshop, each layer is an independent mesh. You need to have at least one layer in your sculpture, even if it is empty.
## Organizing layers

You can drag and drop a layer B onto another layer A to make layer B a child of layer A. When layer A is moved, layer B will be moved to. This is useful to represent hierachy, typically you if you are making a head for instance, you would make each eye a child of the head, the mustache a child of the head etc.

If you need to bring a layer to the top level, select it then press "Root", this will bring the layer all the way to the top of the hierarchy and unparent it.
## Layer operations
### Add Layer

Adds a layer with the default ball mesh.
### Add empty layer

Adds a layer with no mesh. You can use the boolean Add brush to add a mesh. After you add it you can wait 12 seconds for the center of mass to be updated (it will make moving the layer easier) or Misc > Origin at center of mass.
### Delete

!!! warning
    Deletes the layer and all children. This operation is permanent.

The only way to undo is to load a previous save or autosave.
Rename

You can rename layers for better organization. Two layers cannot share the same name, so the rename will not work if the name is already taken.
### Copy layer

Copies a layer and all children, the layer names will have a suffix to indicate it's a copy.
### Root layer

Bring the layer to the top of the hierarchy, above any parent.
### Merge layers

If you want to 3d print your sculpt or need it as a single mesh, you can use the merge system. Press merge layer then click on the empty space (checkbox) near each layer you want to merge then confirm. This will preform a boolean add for each layer selected and put the result into a new layer. The original layers are not deleted. It sometimes fails if the geometry is too complex.
### Flip X / Y / Z

This will flip the layer and its children along one of the cardinal axes. Useful to do symmetry, like hands of a character.
