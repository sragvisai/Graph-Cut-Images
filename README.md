# Graph-Cut-Images

NAME : SAI SRAGVI VIBHUSHAN NIDAMARTI
CAMPUS ID : gt73213@umbc.edu
GL : gt73213@gl.umbc.edu


**Libraries Used and how to install them :**

import math
from skimage import io, util
import heapq
import sklearn

The following moules are not in-built and will be found as python files in the directory
_import Edmon
import Ford
from patchGeneration import_

**Note** : If any by any chance , you encounter a attribute not found error for the above three modules, please restart the jupyter kernel and run the import cells again
 

**How to Run the File**:
It is a Jupyter Notebook and can be run just by pressing the run button / ctrl+enter on ea



**Results Intepreatation:**

The python Notebook consists two sections for the Edmon,Ford algorithms.

Here is the final image for a given input:

-------- Ford algorithm -------------

Input Image  - Size (217 x 291)

![image](https://user-images.githubusercontent.com/47244988/165412535-5aab4136-760c-4d8f-9506-2766cdf6772f.png)

OutPut Image - Size (365 x 365)

![image](https://user-images.githubusercontent.com/47244988/165412607-66f12716-d877-4219-9eb1-b117aa0a2a1e.png)

Intermediatary results :

1. Min Cut representation in the overlap region :

      The following image shows the vertical cut for one of the sequences.
      Here, the green region represents the portion of pixels that are to be taken from the left patch and the white portion represents the pixels that are to be taken from the right patch.
       The following image shows the horizontal cut for one of the sequences.
       Here, the green region represents the portion of pixels that are to be taken from the upper patch and the white portion represents the pixels that are to be taken from the lower patch.
       


![veticalCut](https://user-images.githubusercontent.com/47244988/165413762-eff474a1-2294-4b7f-861d-d1a46c803874.png)



![horizontal](https://user-images.githubusercontent.com/47244988/165413933-661f6e1f-8bf7-470b-87a9-873ed44d04e6.png)

     

2. Overlap region and the cut representaiton for the whole image
      The following image represents the overlap region's that were considered on a whole while in the process of constructing the resultant image.
      The red portion suggests that the pixels were considered from the left/up patch and the white portion suggests that the pixesl were considered from the right/bottom patch.
       
![overlap](https://user-images.githubusercontent.com/47244988/165414010-5619e1d3-2559-4928-af86-c9d781072567.png)

3. Sequential updates of the result image
    
    A snippet of resultant image while its still in the process of being constructed.
    Image Output :


![sequentialUpdate](https://user-images.githubusercontent.com/47244988/165413511-2f4cbff8-dadf-4557-b267-22fcc6831fc4.png)

**Adjancency Matrix** :

Adjancency matrices that were constructed for the formation of the resultant images are stored in the text files with names following the format:
   -> imageName+fileCounter+_Vertical+algoName

**Pixel Vectors**:

These values are represented as x-y , which indicates that there is a cut on the edge between x and y; Stored in text file under /Pixel Vectors directory
File Names are similar to the above represented format.

Sample Inputs and Ouputs:

----------------## FORD ## ---------------------------------------

Input:

![key](https://user-images.githubusercontent.com/47244988/165415668-18968ea1-d8b7-47da-a5db-c8690a081800.png)


Output:

![image](https://user-images.githubusercontent.com/47244988/165415699-5102ff04-6223-4e41-9ea3-246d2771871e.png)


Input : 

  ![todo](https://user-images.githubusercontent.com/47244988/165415767-614d55eb-4d7f-459e-8d5d-205cfc4dc2c4.jpeg)

Output:

![image](https://user-images.githubusercontent.com/47244988/165415794-249cd36b-0974-49a3-9ecd-80f0c1441eb4.png)

-------------------------## Edmond ## --------------------------------------------------

![image](https://user-images.githubusercontent.com/47244988/165415839-94adcc51-bbc4-4504-b57a-2121c6ccfac5.png)

![image](https://user-images.githubusercontent.com/47244988/165415855-b64cdce3-4d83-4723-9fc4-0869270a0d40.png)


    
**References**:
https://www.cc.gatech.edu/cpl/projects/graphcuttextures/
https://www.csee.umbc.edu/~adamb/641/resources/GraphcutTextures.pdf
