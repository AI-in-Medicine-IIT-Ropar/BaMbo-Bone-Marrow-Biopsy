import os
import cv2
import shutil
import np

def saveimgsandmasks(segclasspath,JPEGimagespath,ExclusionList,finalCompletedir,finalmaskdir,finalimagedir):
    for imgname in os.listdir(JPEGimagespath):
        _,imgNumber=imgname.split('_')
        imgNumber,_=imgNumber.split('.')

        if  int(imgNumber) not in ExclusionList:
            img=cv2.imread(JPEGimagespath+'/'+imgname)
            cv2.imwrite(finalimagedir+'/'+imgname ,img)  

    print('Finished Copying Images')

    for maskname in os.listdir(segclasspath):
        _,maskNumber=maskname.split('_')
        maskNumber,_=maskNumber.split('.')

        if  int(maskNumber) not in ExclusionList:
        
            mask=cv2.imread(segclasspath+'/'+maskname)
            newmask=np.zeros((mask.shape[0],mask.shape[1]),dtype=np.uint8)

            for i,row in enumerate(mask):
                for j,bgr in enumerate(row):
                    rgb=bgr[::-1]    
                    string_rgb=','.join(map(str,rgb))
                    newmask[i][j]=colorvec[string_rgb]
            
            cv2.imwrite(finalmaskdir+'/'+maskname ,newmask)
    print('Finished Copying masks')
    print('Total',len(os.listdir(finalmaskdir)),' masks dataset')


###
colorvec={
"0,0,0":0,#bg
"0,128,0":0,#bg
"128,0,0":1,#fat
"128,128,0":2,#cell
"0,0,128":3#bone
}
segclasspath='PASCALoutput/SegmentationClass/'
JPEGimagespath='PASCALoutput/JPEGImages/'
ExclusionList=[12578,12579,12580,12581,12582] #list of images and masks to exclude in making into integer encoded dataset

finalCompletedir='IE-dataset'
finalmaskdir='IE-dataset/masks'
finalimagedir='IE-dataset/images'

# shutil.rmtree(finalCompletedir)
os.mkdir(finalCompletedir)
os.mkdir(finalmaskdir)
os.mkdir(finalimagedir)
saveimgsandmasks(segclasspath,JPEGimagespath,ExclusionList,finalCompletedir,finalmaskdir,finalimagedir)
