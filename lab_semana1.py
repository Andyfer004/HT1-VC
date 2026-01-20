import os
import cv2
import numpy as np


# ------------------ Utils ------------------
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


# ------------------ Transformaciones ------------------
def contrast_brightness(image, alpha, beta):
    img = image.astype(np.float32) / 255.0
    out = alpha * img + (beta / 255.0)
    out = np.clip(out, 0.0, 1.0)
    return (out * 255).astype(np.uint8)


def gamma_correction(image, gamma):
    img = image.astype(np.float32) / 255.0
    out = np.power(img, gamma)
    return (np.clip(out, 0.0, 1.0) * 255).astype(np.uint8)


# ------------------ Segmentación HSV ------------------
def hsv_segment(image, color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if color == "verde":
        lower = np.array([35, 60, 40])
        upper = np.array([85, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)

    elif color == "azul":
        lower = np.array([90, 60, 40])
        upper = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)

    else:  # rojo
        lower1 = np.array([0, 60, 40])
        upper1 = np.array([10, 255, 255])
        lower2 = np.array([170, 60, 40])
        upper2 = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, lower1, upper1) | cv2.inRange(hsv, lower2, upper2)

    return cv2.bitwise_and(image, image, mask=mask)


# ------------------ Main ------------------
def main():
    input_dir = "ejemplos"
    output_dir = "resultados"
    ensure_dir(output_dir)

    colors = ["rojo", "verde", "azul"]

    files = sorted([
        f for f in os.listdir(input_dir)
        if f.lower().endswith((".jpg", ".png", ".jpeg"))
    ])

    for i, fname in enumerate(files):
        img = cv2.imread(os.path.join(input_dir, fname))
        if img is None:
            continue

        base = os.path.splitext(fname)[0]
        out_dir = os.path.join(output_dir, base)
        ensure_dir(out_dir)

        contrast = contrast_brightness(img, alpha=1.2, beta=10)
        gamma = gamma_correction(img, gamma=0.6)
        segmented = hsv_segment(img, colors[i % 3])

        cv2.imwrite(os.path.join(out_dir, "contraste.png"), contrast)
        cv2.imwrite(os.path.join(out_dir, "gamma.png"), gamma)
        cv2.imwrite(os.path.join(out_dir, "segmentacion.png"), segmented)

        print(f"{fname} -> segmentación {colors[i % 3]}")


if __name__ == "__main__":
    main()