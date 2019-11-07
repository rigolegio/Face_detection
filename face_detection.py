# Для установки face recognition требуется установить библиотеку dlib.
# Корректная установка dlib на win возможна
# только при предварительной установке cmake
# Подключение производим к IP-камере наружного видеонаблюдения.
import cv2
import face_recognition

# Подключаемся к камере
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.66:554/1')
# Если захотим подключиться к компьютерной вебке, то в VideoCapture передаем "0".
face_locations = []
# Далее применим первый метод для преобразования разрешения
d = int(input("Выберите разрешение, от 1 до 6, "
              "где\n 1 - 160x120\n 2 - 320x240\n "
              "3 - 640x480\n 4 - 720x540\n 5 - 800x600\n 6 - 1024x768: "))


def dimensions(d, width=None, height=None):
    dimensions = {1: {'width': 160, 'height': 120},
                  2: {'width': 320, 'height': 240},
                  3: {'width': 640, 'height': 480},
                  4: {'width': 720, 'height': 540},
                  5: {'width': 800, 'height': 600},
                  6: {'width': 1024, 'height': 768}}
    while d != 0:
        if d == 1:
            width = dimensions[1]['width']
            height = dimensions[1]['height']
            return width, height
            break
        elif d == 2:
            width = dimensions[2]['width']
            height = dimensions[2]['height']
            return width, height
            break
        elif d == 3:
            width = dimensions[3]['width']
            height = dimensions[3]['height']
            return width, height
            break
        elif d == 4:
            width = dimensions[4]['width']
            height = dimensions[4]['height']
            print(width, height)
            break
        elif d == 5:
            width = dimensions[5]['width']
            height = dimensions[5]['height']
            return width, height
            break
        elif d == 6:
            width = dimensions[6]['width']
            height = dimensions[6]['height']
            return width, height
            break


if __name__ == '__main__':
    while (cap.isOpened()):
        ret, frame = cap.read()  # считываем кадр
        # А это второй метод, статический
        # Чтобы картинка смотрибельно отображалась, необходимо
        # изменить ее разрешение
        # scale_percent = 30 # ставим процент величины от исходной. Исходная - 100%
        # width = int(cap.get(3) * scale_percent / 100)
        # height = int(cap.get(4) * scale_percent / 100)
        # В dim передаем значения переменных width и height для изменения разрешения
        dim = dimensions(d)  # (width, height)
        resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        # Закончили изменение разрешения кадра

        rgb_frame = resized_frame[:, :, ::-1]  # переделываем в RGB
        face_locations = face_recognition.face_locations(rgb_frame)  # ищем лица
        for top, right, bottom, left in face_locations:
            # Рисуем квадрат вокруг лица
            cv2.rectangle(resized_frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Выводим результат
        cv2.imshow('Video', resized_frame)

        # Для выхода жмем клавишу 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Очищаем переменную cap и закрываем окна.
    cap.release()
    cv2.destroyAllWindows()
