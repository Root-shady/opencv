#-*- coding: utf-8 -*-
'''
Created on 30 Jun 2016

@author: mozat
'''

import base64
from CloudVisionAPI import CloudVision
from PIL import Image, ImageDraw, ImageFont

#font_name = 'simsun-win.ttc'
font_name = 'stsong.ttf'
fontSize = 20

def detect_text(image, num_retries = 3, max_results = 6):
    image_content = image.read()
    batch_request = [{
                'image': {
                    'content': base64.b64encode(image_content).decode('UTF-8')
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': max_results,
                }]
            }]

    vision_cloud = CloudVision()
    service = vision_cloud.get_api_service()
    
    request = service.images().annotate(
        body={'requests': batch_request})
    
    responses = request.execute(num_retries=num_retries)
    if 'responses' not in responses:
        return []
    response = responses['responses']
    if 'error' in response:
        return []
    if 'textAnnotations' in response[0]:
        text_response = response[0]['textAnnotations']
    else:
        text_response = []

    return text_response

def draw_text(image, text_response, output_filename):
    im = Image.open(image)
    new_im = Image.new(im.mode, im.size, )
    draw1 = ImageDraw.Draw(im)
    draw2 = ImageDraw.Draw(new_im)
    
    for text in text_response[1:]:
        box = [(v.get('x', 0.0), v.get('y', 0.0)) for v in text['boundingPoly']['vertices']]
        draw1.line(box + [box[0]], width=5, fill='#00ff00')
        
        description = text['description']
#         num_word = len(description)
#         width = box[1][0] - box[0][0]
#         height = box[3][1] - box[0][1]
#         fontSize = min(height, width/num_word)
        myfont = ImageFont.truetype(font_name, fontSize)
        draw2.text(box[0], description, fill = (255,255,255), font = myfont)

    del draw1
    del draw2
    im.save(output_filename+'bounding.jpg')
    new_im.save(output_filename+'text.jpg')

def main(input_filename, output_filename, num_retries, max_results):
    with open(input_filename, 'rb') as image:
        text_response = detect_text(image, num_retries, max_results)
        image.seek(0)
        draw_text(image, text_response, output_filename)
    
if __name__ == '__main__':
    photo_file = '2.pic_hd.jpg'
    import time
    start = time.time()
    main(photo_file, photo_file+'.google.', 3, 6)
    finish = time.time()
    print(finish-start)
