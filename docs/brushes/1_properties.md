
# Brush properties

The brush properties control how the brush behaves.
# Basic settings

These settings are shared by almost all brushes.
### Size

The overall size (green bubble) of the brush.
### Strength

Simple, the stronger the brush the bigger the displacement. Typically this controls the height of the bump (e.g. round brush or crease brush).
### FlowSpeed

Keep the same displacement but make it happen faster or slower.
### Inner size

The inner radius (blue bubble) of the brush
### Relative X

The retangular size of the brush along the left / right axis.
### Relative Z

The rectangular size of the brush along the forward / bacwkard axis.

By combining Inner size, relative X, relative Z you can get any shape you want for the blue brush.
### LOD

Level of detail, how much detail to put into each brush stroke. 10 is a good value. See [Dynamic topology](../workflow/2_dyntopo.md)
## Interaction settings

These settings control the interaction between you and the brush.
### Use hand movement for direction (experimental)

In this mode you need to hold sculpt and move your hand to make a bump, the bump will be in the direction of the movement, it feels fun but can be tiresome after a while. When it is turned off, the orientation of the brush is all that matters, no need to move the brush to sculpt.
### Lock brush to controller

Keep the brush at the position of your controller. Turn-it off for a more comfortable experience where you sculpt from further away (right grip to move the brush).
### Use surface vertices

A crucial feature that will be turned on / off constantly. It decided whether to use only the vertices in the same direction as the brush (surface), or any vertex in the green bubble. See [Brush handling](../workflow/1_brush_handling.md) for illustration and explanation.
### Symmetry

Turn-on or off Ox (left / right), Oy (up / down), Oz (forward / backward) symmetry. Make sure you adjust the origin of symmetry if needed Brushes > Show sym.
### Dynamic topology

Which style of dynamic topology to do. None: no new triangles created or merged, Subdivide: only creates triangles, Merge: only merges triangles. See [Dynamic topology](../workflow/2_dyntopo.md).
