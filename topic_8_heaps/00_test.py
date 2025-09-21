from image_converter import convert_image
from priority_queue import PriorityQueue

def main():
    pq = PriorityQueue()

    # Користувачі завантажують свої зображення
    pq.enqueue(("sample1.jpg", "png"), 1)  # Основний користувач
    pq.enqueue(("premium_sample.jpg", "bmp"), 10)  # Преміум-користувач
    pq.enqueue(("sample2.jpg", "tiff"), 1)  # Основний користувач

    while not pq.is_empty():
        file_name, target_format = pq.dequeue()
        output_file = convert_image(file_name, target_format)
        print(f"Зображення було успішно конвертовано і збережено як {output_file}!")

if __name__ == "__main__":
    main()
