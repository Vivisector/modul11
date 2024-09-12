import os, sys
from PIL import Image

print('*'*50)

from PIL import Image
import os

# Путь к папке с изображениями
folder_path = 'd:/Down/imgs/'
path_processed = folder_path + 'processed/'

class ImageProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.image = None

    # метод открытия изображения
    def open_img(self, filename):
        try:
            self.image = Image.open(self.input_file)
            print(f'изображение {filename} успешно открыто')
        except OSError as e:
            print(f'не удалось открыть {self.input_file}: {e}')
            self.image = None

    #метод для перевода в чб
    def convert_bw(self, filename):
        if self.image:
            self.image = self.image.convert('L')
            print(f'Изображение {filename} переведено в чб')

    #метод для изменения размеров
    def resize(self, filename, new_size):
        if self.image:
            self.image = self.image.resize(new_size)
            print(f'Изображение {filename} изменило размер на {new_size}')

    # методе сохранения картинки
    def save_img(self, filename, output_file, format='PNG'):
        if self.image:
            self.image.save(output_file, format=format)
            print(f'Изображение {filename} сохранено как {output_file} в формате {format}')


# Функция для обработки изображений в папке
def process_images_in_folder(folder_path, new_size=(800, 600)):
    for filename in os.listdir(folder_path):
        input_file = os.path.join(folder_path, filename)

        if os.path.isfile(input_file) and filename.lower().endswith(('.jpg', '.png')):
            output_file = os.path.join(path_processed, os.path.splitext(filename)[0] + "_processed.png")

            # Создаём объект класса ImageProcessor и обрабатываем изображение
            img_processor = ImageProcessor(input_file)
            img_processor.open_img(filename)
            img_processor.convert_bw(filename)
            img_processor.resize(filename, new_size)
            img_processor.save_img(filename, output_file)
            print('-'*33)

# Обрабатываем изображения
process_images_in_folder(folder_path)
