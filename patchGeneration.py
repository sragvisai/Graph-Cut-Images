import numpy as np

class patchGeneration:
    def __init__(self) -> None:
        pass

def getInitialPatch(orgImage, patchLength):
    height, width, _ = orgImage.shape
   
    np.random.seed(1111)
    row = np.random.randint(height - patchLength)
    col = np.random.randint(width - patchLength)

    return orgImage[row:row+patchLength, col:col+patchLength]

def getBestFit(orgImage, patchLength, overlap, res, posY, posX):
    
    height, width, _ = orgImage.shape
    errorList = np.zeros((height - patchLength, width - patchLength))

    for i in range(height - patchLength):
        for j in range(width - patchLength):
            patch = orgImage[i:i+patchLength, j:j+patchLength]
            e = getErrorWithSelection(patch, patchLength, overlap, res, posY, posX)
            errorList[i, j] = e

    i, j = np.unravel_index(np.argmin(errorList), errorList.shape)
    return orgImage[i:i+patchLength, j:j+patchLength]

def getErrorWithSelection(patch, patchLength, overlap, res, posY, posX):
    totalError = 0

    if posX > 0:
        leftError = patch[:, :overlap] - res[posY:posY+patchLength, posX:posX+overlap]
        totalError += np.sum(leftError**2)

    if posY > 0:
        upError   = patch[:overlap, :] - res[posY:posY+overlap, posX:posX+patchLength]
        totalError += np.sum(upError**2)

    if posX > 0 and posY > 0:
        mid = patch[:overlap, :overlap] - res[posY:posY+overlap, posX:posX+overlap]
        totalError -= np.sum(mid**2)

    return totalError

