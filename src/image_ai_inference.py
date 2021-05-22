from imageai.Detection import VideoObjectDetection
import os

boxes = []
def forFrame(frame_number, output_array, output_count):
    boxes.append(output_array)
    print("FOR FRAME " , frame_number)
    print("Output for each object : ", output_array)
    print("Output count for unique objects : ", output_count)
    print("------------END OF A FRAME --------------")

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "checkpoints/resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()

custom_objects = detector.CustomObjects(sports_ball=True,baseball_bat=True)

video_path = detector.detectCustomObjectsFromVideo(
                custom_objects=custom_objects,
                input_file_path=os.path.join(execution_path, "data/red_cricket.avi"),
                output_file_path=os.path.join(execution_path, "results/bat_ball_det"),
                frames_per_second=2, log_progress=True,
                per_frame_function = forFrame
                )
print(video_path)