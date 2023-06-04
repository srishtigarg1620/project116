
import cv2

img = cv2.imread("./PRO-C116-project-image-main-main/solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Mercury",
            (120,240),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )
cv2.putText(img,
            "Venus",
            (190,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )
cv2.putText(img,
            "Earth",
            (290,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )
cv2.putText(img,
            "Mars",
            (380,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )
cv2.putText(img,
            "Jupiter",
            (540,340),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )
cv2.putText(img,
            "Saturn",
            (740,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (255,255,255)
            )
cv2.putText(img,
            "Uranus",
            (970,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "Neptune",
            (1099,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )


cv2.imshow("Solar system", img)

cv2.waitKey(0)