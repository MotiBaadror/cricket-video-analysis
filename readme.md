## Cricket player and bat and ball detection 
Impact detection 
The results is showing the frame where bat hit the ball. 

src folder have code

![alt Results](results.jpg)




```
git clone https://github.com/MotiBaadror/cricket_video_analysis
cd cricket_video_analysis 
pip install - r requirements.txt
```

Keep the video in data/ folder     

```
cd src 
python image_ai_inference.py
```

image_ai_inference.py to get the json for the cooridinate      
results will be saved in the results dir     
after that to get  the frame where bat hits ball 

```
python generate_results.py
```

download the pretrained model from [here](https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/VIDEO.md#videodetection)

The notebook contain all the helper code which is not organised. 


