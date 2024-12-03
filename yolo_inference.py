from ultralytics import YOLO

model = YOLO('models/best.pt')

results = model.predict('input_videos/08fd33_4.mp4', save=True)

for result in results:  # Loop through inference results for each frame
    print(result)
    print('=====================================')
    for box in result.boxes:
        print(box)