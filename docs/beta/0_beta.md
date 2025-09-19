
# Beta

Beta features are still in development but generally work. They will become easier to use as they become mainstream features.
## Decimate by 50%

Divided triangle count by 2. Algorithm is ok but topology will not be perfect. It is instead recommended to do it manually with the subdivide brush and a low LOD.
## Run self-intersect check

If you are going to do 3D printing you can use this to find all self-intersections in your mesh. Generally 3d printing requires you to remove all self-intersections. They will be displayed in green on the mesh. Use the Smooth tool or the remesh tool to try and remove them. Run the check again, repeat until none are left.

Note: there are two versions, quick but imprecise, for a first pass. Then you can use the slow but precise one to really get them all and get a perfect score in Blender 3d print toolbox or equivalent.
## Attempt self-intersect cleaning

Will do a slow check and automatically fix offending triangles by remeshing them. Results not guaranteed, it can easily fail.
## Run manifold check

Chisel needs the mesh to be manifold, or in other words watertight. Each vertex is shared by all incident triangles (no duplicate vertices), each edge must have two neighbors, triangles cannot be duplicated. You can use this check on imported files from other apps to make sure they conform. If your mesh fails this check it's probably a bug and you should send it to me for review at contact@makerscape.info.
## Make manifold

If your mesh fails the manifold check, you can try and run this to fix it. Results not guaranteed.
## Clean inner facets

Sometimes it can happen that your mesh has inner facets (geometry inside larger geometry). This button will do its best to make a mesh that only has outside geometry with no inside geometry. This is an automated fix and best effort, not guaranteed to work.
## Place bone, apply skin, move bone

Will display an additional tab for bone management. Very experimental but useful for moving limbs / fingers etc To use the bone system: - Layers tab > Select the layer you want. - Bones tab > add a bone, move it with the right grip in the right position - Brushes > Freeze , freeze on your mesh the skin for the bone (area of effect) - Beta > apply skin to bone - Beta > move bone, use right grip to very carefully move the bone, the mesh will deform to accomodate the new position - Beta > Place bone, go back to normal mode

The user interaction for this will be greatly improved, on the roadmap.
## Show render tab

Displays an additional experimental Render tab. This tab lets you generate path traced renders of your sculpt. It can be useful to make sure the lights and shadows work well with your sculpt. Very experimental.
## Do a Blender render

For this feature you need a windows PC with Blender. Download the Blender plugin from makerscape.info, create a Blender scene with your FBX and set it up the way you like, make sure the layer names match the FBX layer names. Start the plugin and point to your scene and to your Blender exe, when you request a Blender render from the headset, the plugin will run the render on your computer and return it to the headset. The purpose of this feature is to easily see what the final render will look like and be able to quickly fix geometry to match path tracing shadows and such. Only matching layer names between the scene and the headset will get updated.
