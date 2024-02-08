import cv2
def load_image(image_path):.
image = cv2.imread(image_path)
return image

def apply_blur(image, kernel_size=(5, 5)):
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred_image


def save_image(image, save_path):
    cv2.imwrite(save_path, image)
    print(f"Imagem salva em {save_path}")