import cv2 as cv
import mediapipe as mp
import time



class handDetector():
    def __init__(self, mode=False, maxHands=2, model_complexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # Get hands
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.model_complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # If camara detects a hand
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(
                        img,
                        handLms, 
                        self.mpHands.HAND_CONNECTIONS
                    )
        return img
    
    def findPosition(self, img, handId = 0, draw = True):
        landmarkList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmark[handId]

            for id, lm in enumerate(myHand.landmark):
                h , w , c = img.shape
                # get coordinates of each 20 landmarks
                cx, cy = int(lm.x*w), int(lm.y*h)
                list.append([id, cx, cy])
                if draw:
                    cv.circle(img,(cx,cy), 15, (255,0,255), cv.FILLED)
                
                return landmarkList

def main():


    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector = handDetector()
    while True:
        sucess, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)


        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(img, f'FPS: {int(fps)}', (40,50), cv.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)



        cv.imshow("Image", img)
        cv.waitKey(1)
if __name__ == "__main__":
    main()