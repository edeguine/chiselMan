
# Workflow
## Mastering the app's concepts

* [Brush handling](1_brush_handling.md): learn how to attach / detach the brush and how to pick the right vertices when sculpting.
* [Dynamic topology](2_dyntopo.md): learn more about this key feature.
* [File management](3_file_management.md): learn how to export, sync and make some space when finished sculpting.
* [Performance](4_performance.md): learn how to keep the app running smoothing, keeping the mesh size reasonable, or tips for working with very large meshes (500k+ triangles) or many layers.

## Developer's word

Chisel was designed to be as easy to use as possible and provide a stepping stone to more complex 3D softwares. It is designed for newcomers and hobbyists and is powerful enough to do quality work.

At the core of Chisel is the idea that as a sculpter you should not worry about implementation of the medium (the mesh) and instead focus on shapes, looks, and the feeling of sculpting.

To make that vision manifest, Chisel relies on dynamic topology by default. Dynamic topology means that the mesh triangles (the faces) get automatically subdivided or merged based on the size of your brush. The LOD property controls the level of detail that you get for your brush.

Another interesting aspect of Chisel is that it relies heavily on VR to let you freely move your brush and sculpt as you move your hand. This is different from tablet / stylus style controls where the brush is always applied perpendicular to the surface. With Chisel you can orient your brush in any direction and it will match the angle, furthermore, the controls are continuous, so the longer your press the bigger the bump. These additonal degrees of freedom allow for a more direct and comfortable creative expression.

A particularity of Chisel is that each save is a separate file, given the large storage size of modern devices and modest size of VR sculpts, this is an opportunity for you to easily go back to a previous version. Based on my experience it's always valuable to be able to compare and undo some portions of your work. If you are worried about this, check out the file management section and how to clean up once you are done sculpting.

Finally, Chisel was designed with standalone headsets in mind first. So it aims to be as lightweight as possible and use the hardware to the maximum. Still, it is possible for you to make it lag by using in certain ways (namely Subdivide only dynamic topology mode or many layers). If you have an ambitious project with many layers or very large and detailed meshes, there are still some steps you can take to sculpt comfortably and take full advantage of the topology engine. Head over to the performance section to learn all the tips.
