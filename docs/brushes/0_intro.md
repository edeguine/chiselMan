
# Brushes

Brushes are the core concept used for sculpting. They provide a way to manipulate the mesh.
## Styles of brushes

The brushes can be broken up roughly along these categories:

* Displacement: these brushes move the vertices to create shapes.
* Smoothing: these brushes help make the mesh look more regular.
* Movement brushes: these brushes provide some movement based interaction.
* Booleans: these brushes let you add brand new shapes.
* Special brushes: these brushes have one specific function.

## Properties and Alt tab

Almost all brushes can be customized in the [Props](1_properties.md) tab for basic settings like strength, flow and shape. These settings are shared by all brushes.

In the [Props](1_properties.md) tab you will also find the setting related to the [handling](../workflow/1_brush_handling.md) of the brush (attached / detached, follow hand movement, etc).

Some brushes have additional setting specific to them in the [Alt](2_alt_props.md) tab, things like boolean base shape, sharpness for Crease or other specialy settings.
## Displacement brushes
### Round

Makes a simple round elongated bump. Great for organic shapes, sculpting faces.
### Flat

Makes a simple flat bump.
### Triangle

Makes a simple triangle bump. Great for sharper details, more angular features.
### Move

Grab and move the mesh orgagnically. Sharpness can be customized in Alt. Great for bringing some flowy feeling to your sculpts.
### Shave

Pushes the mesh against the normal. Useful for refining a shape, "sanding it down". In the Alt settings you can use a slower mode that tries to prevent the mesh from going inside out - not perfect though. (You will see if it happens, it looks glitchy)
### Dilate

Dilates the mesh following the normal. Good for making appendages, nose or cheeks.
### Expand

Expand the mesh away from brush center (ignores normal). Similar to Dilate, but uses the brush center and not the mesh. It radiates out.
### Pinch

Contracts the mesh towards brush center (ignores normal). Great for making terrain texture.
### Twist

Spins the mesh around the brush center in a spiral. Great for making random / noisy surfaces.
### Crease

Make a rim or an indent into the mesh. Sharpness and curve style can be customized in Alt. Point is the default shape, point variant is more frank, point tangent also pulls in the sides of the brush, line is a straight crease line.
### Carve

Carves the mesh, pushes the mesh outwards from within the blue shape. Shape can be customized in Alt. Can be slow.
### Extrude

Extrudes the mesh, pushes the mesh inwards into the blue shape. Shape can be customized in Alt. Can be slow.
## Smoothing
### Smooth

Laplacian smoothing, moves the vertices to make the mesh more uniform. Can make the mesh a bit flat.
### Smooth+

Moves the vertices to remove sharp angles, makes the mesh softer and rounder.
### Smooth curve

Tries to smooth the mesh while preserving curvature, for instance useful for smoothing a vase or a flower petal.
### Smooth flatten

Aligns the vertices to make a flat surface. Great for bringing in line glitchy vertices / spikes (e.g. after a boolean subtract, or a shave brush on a sharp edge).
### Smooth align

Aligns the vertices, with more control. Alt tab lets you specify which vertices to pick (above / below / both sides).
## Movement based

These brushes work based on controller movement. They are the most "VR native" brushes of the bunch.
### Move

Grab and move the mesh orgagnically. Sharpness can be customized in Alt. Great for bringing some flowy feeling to your sculpts.
### Pull

Put your brush on the surface of the mesh, hold sculpt and move your brush to pull out the mesh to follow your brush. Great for making branches, horns, fingers etc. Don't go too fast or the program won't be able to keep up.
### Flow

Hold sculpt and move your hand around to make a tube. Alt lets you customize tube shape and density. Can be used to write "Hello" for instance.
## Booleans
### Add

Adds a shape to your sculpture and merge it with the existing mesh. If you want the shape alone, creat an empty layer first. Alt tab lets you customize shape (preset or your own).
### Subtract

Removes a shape from your sculpture. Alt tab lets you customize shape (preset or your own).
### Cut

Cuts a piece from your mesh and lets you add it elsewhere (it becomes your brush).
### Copy

Copies a piece of your mesh, without removing it, and lets you add it elsewhere (it becomes your brush).
### Alt sub

Cuts a piece of your brush (brush minus mesh) and updates the brush. Use it to quickly cut out parts of your brush when using booleans.
## Special brushes
### Subdivide

Applies dynamic topology without moving vertices. Useful for increasing or reducing triangle count.
### Paint

Lets your paint your mesh (vertex painting). Material needs to be set to Vertex Paint. If you use it with dynamic topology, the paint will match the size of your brush. If you use it with dynamic topology turned-off, the closest vertices inside your brush will be painted (less detail). You can press the Y button to bring in the color picker. You can press left trigger + Y button to go into "sample color" mode then do a sculpt action to sample the color at the brush location (brush will collect one sample then revert back to painting)
### Remesh

Remesh a part of your mesh, useful to remove snags, glitches and high incidence parts of the mesh. Can be slow on larger meshes. Does not preserve detail too well.
### Deform

Lets you deform your mesh with a lattice. Grab the blue control points with your right grip (middle finger) to move them. Move the brush and press the sculpt button to reposition the lattice, you will see new blue control points at the brush location.
### Freeze / Unfreeze

Freeze or unfreeze some vertices to lock them in place. Useful when you want to edit close or touching surfaces. When you are done, unfreeze your vertices.
### Show sym

Lets you adjust the "origin of symmetry" and its orientation compared to your layer with right grip trigger. After that, switch to another brush and turn on Ox / Oy / Oz symmetry in the props tab to use symmetry. The symmetry will be based on the location of the "origin of symmetry".
