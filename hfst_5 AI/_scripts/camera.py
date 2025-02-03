from threading import Thread
import cv2, os
import matplotlib.pylab as plt

# Klasse (OOP) om een camera in een aparte thread te starten.
class Camera:
    def __init__(self, src=0, fps=60):
        self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.width, self.height =  int(self.stream.get(3)), int(self.stream.get(4))
        self.fps = fps

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:  # Stop de schrijver als de eigenschap stopped = True
                self.stream.release()
                return

            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.grabbed, self.frame

    def stop(self):
        self.stopped = True


# Functie om beschikbare camera-sources te vinden.
def getCamera_src():
    index = 0
    lijst_src = []
    while index < 10:           # Ik ga ervanuit dat 10 camera's wel genoeg zijn.
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        try:
            cap.getBackendName() # Geeft error als camera niet bestaat.
            lijst_src.append(index)
        except:
            pass
        cap.release()
        index += 1
    return lijst_src


# Functie om foto's te trekken.
def getCamera_foto(keuze_camera = 0):
    key = cv2.waitKey(1)
    # Moet 0, 1, 2, ... zijn. Afhankelijk van de gebruikte camera.
    # Maak een camera aan die loopt op een aparte thread
    cam = Camera(fps=60, src=keuze_camera).start()
    pad = os.path.dirname(os.path.abspath(__file__))
    while True:

        try:
            _, afbeelding = cam.read()
            cv2.imshow("Capturing", afbeelding)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename=pad+'/_foto.jpg', img=afbeelding)
                plt_imshow("Genomen foto", afbeelding)
            
            elif key == ord('q'):
                print("Camera uitzetten.")
                cam.stop()
                cv2.destroyAllWindows()
                print("Programma gestopt.")
                break
        
        except(KeyboardInterrupt):
            print("Camera uitzetten.")
            cam.stop()
            cv2.destroyAllWindows()
            print("Programma gestopt.")
            break

# Functie om een afbeelding weer te geven via matplotlib
def plt_imshow(title, image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title(title)
    plt.grid(False)
    plt.show()