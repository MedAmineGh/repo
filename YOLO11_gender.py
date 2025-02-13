from ultralytics import YOLO

def train_yolo(model_path='relu6-yolov11-cls.yaml', data_path='data.yaml', epochs=50, batch_size=16, img_size=640):
    """
    Function to train YOLOv8 model.
    
    :param model_path: Path to the YOLO model (pretrained or custom YAML for scratch training)
    :param data_path: Path to dataset YAML file
    :param epochs: Number of training epochs
    :param batch_size: Training batch size
    :param img_size: Input image size
    """
    # Load model (pretrained or new)
    model = YOLO(model_path)
    model = YOLO("relu6-yolov11-cls.yaml")
    # Train model
    model.train(
        data=data_path,
        epochs=epochs,
        batch=batch_size,
        imgsz=img_size
    )
    
    print("Training complete.")

if __name__ == "__main__":
    train_yolo()


