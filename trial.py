#-*- coding: utf-8 -*-
import numpy as np
#from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import cv2
import matplotlib.pyplot as plt

# 导出获得google的数据
from temp import result
# 导出相关的模板数据
from pinpoint import pinpoint, target


#font_name = 'stsong.tff'
#fontSize = 20
def get_match():
    global result
    #keywords = {'发票类型':'title', '发票编号':'number', '开票日期:':'date', '付款方名称':'taxpayer', '納稅人识别号:':'taxpayer_number', '付款人地址、电话':'contact_info', '开户行账户':'bank_info', '服务项':'service', '规格型号':'related_info', '单位':'unit', '数量':'amount', '金额':'price', '税率':'tax_rate', '税额':'tax_pay', '合计金额':'total_price', '合计税额':'total_tax', '销售方名称':'provider_name', '纳税人识别号':'identification', '地址、电话':'pcontact_info', '开户及账户':'pbank_infor', '收款人':'payee', '复核':'reviewer', '开票人':'drawer' }
    #keywords = {'date':'日期', 'price':'金额', 'payee':'收款人', 'reviewer':'复核', 'unit':'单位','amount':'数量', 'capital':'大写', 'lower':'小写', 'service':'服务', 'proof':'凭证'}
    keywords = {'price':'金额', 'payee':'收款人', 'lower':'小写', 'service':'服务'}
    match = []
    match_keyword = {}
    for record in result:
        for key,value in keywords.items():
            if record['description'].strip() == value:
                match.append(record)
                match_keyword[key] = record['boundingPoly']['vertices'][0]
    return match_keyword

    #result = [record for record in result if record['description'].strip() in keywords.values()]

    # 构造相关的对齐点的数组
    #print(len(match))
    #return match
    
def process_image(filename, match_keyword, points):
    img = cv2.imread(filename)
    rows, cols, ch = img.shape

    listA = []
    listB = []
    for key in match_keyword:
        listA.append((match_keyword[key]['x'], match_keyword[key]['y']))
        listB.append((points[key]['x'], points[key]['y']))
    pts1 = np.float32(listA)
    pts2 = np.float32(listB)

    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (976, 544))
    a = (30, 170)
    point = cv2.warpPerspective(a, M, (976, 544))
    print(point)

    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Ouput')
    plt.show()

def draw_text(image, text_response, output_filename):
    im = Image.open(image)
    new_im = Image.new(im.mode, im.size)
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
        #myfont = ImageFont.truetype(font_name, fontSize)
        #draw2.text(box[0], description, fill = (255,255,255))

    del draw1
    #del draw2
    im.save(output_filename+'ing.jpg')

def main(input_filename, output_filename):
    match = get_match()
    #with open(input_filename, 'rb') as image:
    #    draw_text(image, text_response, output_filename)
    global pinpoint
    process_image(input_filename, match, pinpoint)



if __name__ == '__main__':
    photo_file = '2.pic_hd.jpg'
    main(photo_file, photo_file+'text')
