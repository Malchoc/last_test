# camera_basic_upgrade.py
import cv2

# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ 카메라를 열 수 없습니다.")
    exit()

print("✅ 카메라 시작됨! 'q' 키를 누르면 종료됩니다.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 그레이스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 윈도우에 출력
    cv2.imshow("Basic Enhanced Camera (Grayscale)", gray)

    # 'q' 키 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
