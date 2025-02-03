from ultralytics import YOLO
import cv2, time, random
import matplotlib.pylab as plt

try: # Afhankelijk van waar het script wordt uitgevoerd, is het pad naar camera anders.
    from camera import Camera
except ModuleNotFoundError:
    from _scripts.camera import Camera

# Functie om objecten op realtime te detecteren.
def detect_foto(foto_pad=r"_scripts/_foto.jpg", yolo_model="yolov8m.pt", accuraatheid=0.6):
    
    # Inladen model & foto.
    yolo = YOLO(yolo_model)
    foto = cv2.imread(foto_pad)
    foto = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
    kleuren = [random.choices(range(256), k=3) for _ in range(len(yolo.names))]

    # Detecteer objecten & teken rechthoeken.
    objecten = yolo(foto, verbose=False)[0]
    for object in objecten.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = object
        x1, y1, x2, y2, class_id = int(x1), int(y1), int(x2), int(y2), int(class_id)
        if score > accuraatheid:
            cv2.rectangle(foto, (x1,y1), (x2,y2), kleuren[class_id], 2)
            cv2.putText(foto, f"{yolo.names[class_id]}:{round(score,2)}", (x1+5, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 1, kleuren[class_id], 2)

    # Tonen verwerkte foto.
    plt_imshow("Verwerkte foto", foto)



# Functie om objecten in realtime te detecteren (+ FPS).
def detect_realtime(keuze_camera=0, yolo_model="yolov8m.pt", accuraatheid=0.6):

    # Inladen camera & model.
    yolo = YOLO(yolo_model)
    cam = Camera(fps=60, src=keuze_camera).start()
    kleuren = [random.choices(range(256), k=3) for _ in range(len(yolo.names))]

    vorige_tijd, huidige_tijd = 0, time.time()
    while True:
        # Inladen volgende frame van video (tot video klaar is).
        ret, frame = cam.read()
        if not ret:
            break

        # Verwerken frame.
        frame = cv2.resize(frame, (780, 540), interpolation = cv2.INTER_LINEAR) 
        objecten = yolo(frame, verbose=False)[0]
        for object in objecten.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = object
            x1, y1, x2, y2, class_id = int(x1), int(y1), int(x2), int(y2), int(class_id)
            if score > accuraatheid:
                cv2.rectangle(frame, (x1,y1), (x2,y2), kleuren[class_id], 2)
                cv2.putText(frame, f"{yolo.names[class_id]}:{round(score,2)}", (x1+5, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 1, kleuren[class_id], 2)

        # Toevoegen fps-counter.
        vorige_tijd, huidige_tijd = huidige_tijd, time.time()
        fps = round( (1/(huidige_tijd-vorige_tijd)), 2)
        cv2.putText(frame, f"FPS:{fps}", (7,70),  cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

        # Tonen resultaat frame. (Druk 'q' om te stoppen).
        cv2.imshow("Real-Time", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cam.stop()
    cv2.destroyAllWindows()


# Functie om een afbeelding weer te geven via matplotlib.
def plt_imshow(title, image):
    plt.imshow(image)
    plt.title(title)
    plt.grid(False)
    plt.show()