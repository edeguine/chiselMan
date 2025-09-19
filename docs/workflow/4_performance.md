
# Performance

The app is designed to stay responsive even on larger meshes, but there are ways to make it lag, generally related to having too many triangles or too many layers on screen. There are ways though to tackle on more ambitious projects and work with large meshes.
## Triangle count / Vertex count

You can see the triangle count of your current mesh as well as the whole scene (all layers) by setting Prefs > show system UI. The Quest 3 can render up to 800k triangles without too many issues, higher than that the material will influence if there is a frame drop or not.

## Layers visibility

Layers can be hidden or displayed in your scene. A hidden layer does not impact framerate and rendering (but it uses memory - RAM). To boost performance hide the layers you are not currently working on or that you don't need to see right now. Layers > hide (next to the layer's name)

## Break down your sculpt into layers

This should be obvious, but the easiest way to work without compromises it to use multiple layers and selectively show them. One for the hands, on for the head, one for the body and so forth.

## Mesh size and material

If you have a large mesh (let's say >500k triangles), some materials are more expensive than other computation-wise. The cheapest materials are the matcap / clay / marble because they have very basic shading. After that the vertex paint material (PBR shading) is a bit more expensive but still decent. The slowest of all is when you activate wireframe or use the Smooth wireframe material. Computing and displaying the wires (each triangle outline) is very expensive, so use it sparingly to check your topology then turn it off.
## Working with larger meshes

### Locality

At the core of its design, the app uses locality, so that only the triangles around the brush are picked up for computation. So if you want to make a high poly mesh (>500k triangles), you will get the best performance by working from large detail to small detail. First figure out the general shape of your sculpt when the poly count is low and block out the main shapes. Then once you start having a lot of triangles, zoom in and work on small areas of the sculpt at a time. If you keep your brush at a decent size compared to triangle density you will be fine. To make it lag, make the brush the size of you whole sculpt and try to sculpt, you will see the struggle.

Still related to locality, the number of polys visible on screen impacts rendering framerate. If you can, try to position your sculpt so that you only see the necessary surface, everything off screen does not count for rendering.

### LOD and dynamic topology

To boost performance you can activate Experimental > large mesh mode. In this mode the dynamic topology is not applied every frame, instead only a few times per second, this boosts performance.

To boost more you can reduce the LOD (level of detail) so that your brush generates less triangles.

Finally, the ultimate performance trick, but a bit inconvenient is to turn off dynamic topology ( Props > dynamic topology > None). In this mode no new triangles are created or deleted and your are just moving the vertices.

### Reducing triangle count and decimate

Finally a last resort is to reduce the triangle count of your mesh. There are two ways to do it: - Use the subdivide brush with a lower LOD and apply it around the mesh, namely on the parts with too many triangles and not too much detail. For instance you might have a mostly flat skin surface (e.g. the neck of your character) and it does not need that many triangles, make the LOD low (e.g 3.5) and the brush a decent size and apply it on the neck surface to reduce poly count. This method is preferred because it interactive and you can fine tune the look and feel of your sculpt when reducing triangle count.

* Use Experimental > Decimate by 50%. This is more automated, it uses an algorithm to find flat surfaces or low detail surfaces and reduce poly count but it can lead to some weird topolgy, use at your own risks.

