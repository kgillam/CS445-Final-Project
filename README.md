# CS445-Final-Project
Final project for CS445




# Notes

## Acquire microscope with camera
- microscope did not work well
- micro camera lens is arriving Saturday
  - will mount on tripod with manual focus, then try zooming with it like a microscope to photo a small item
- photos I took on my cannon camera with current lens does capture focal length ()


## Focus stacking
- reference focusstack project https://github.com/cmcguinness/focusstack
  - updated print statements so it can run in python3 (was writing in 2)
  - updated focus_stack algorithm to also return 'mask' matrix used internally - represents which pixels from which image
  - TODO: look into the align_images, see if any adjustments will need to be made for resizing, not just aligning? (since we are zooming, not refocusing)
  - 
- TODO: also look at focus-stack https://github.com/momonala/focus-stack/blob/master/focus_stack/focus_stack.py
  - this is based on cmcguinness's but might have improvements?
- since we want to make modifications, we can't just import the publicly available focus-stack module, we will need to put code in our own project, and modify
  - make sure to cite the reference project(s)


## Depth map generation
- 'mask' returned from updated focus_stack has the knowledge of the distance each pixel was captured at
- reference paper: https://pubs.aip.org/aip/acp/article/2054/1/050001/1023317/Achieving-3D-imaging-through-focus-stacking
    - Depth = I*((Fmax - Fmin)/N)



## 3D reconstruction
- OpenGL? PyOpenGL PyOpenGL_accelerate
- TODO: find good references in python, api docs? 