#!/usr/bin/python 
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from template import model
import re

def main():
    summary, records  = result[0], result[1:]
    words = summary['description'].split('\n')
    keywords = {'发票类型':'title', '发票编号':'number', '开票日期':'date', '付款方':'taxpayer', '纳税人识别号':'taxpayer_number', '地址、电话':'contact_info', '开户行账户':'bank_info', '服务项':'service', '规格型号':'related_info', '单位':'unit', '数量':'amount', '金额':'price', '税率':'tax_rate', '税额':'tax_pay', '合计金额':'total_price', '合计税额':'total_tax', '销售方名称':'provider_name', '纳税人识别号':'identification', '地址电话':'pcontact_info', '开户及账户':'pbank_infor', '收款人':'payee', '复核':'reviewer', '开票人':'drawer' }

    match = {}
    for word in words:
        if ':' in word or '¥' in word:
            pair = word.split(':')
            for key in keywords.keys():
                if pair[0] in key:
                    match[keywords[key]] = pair[1].strip()
    return match


# 将两个record合并为一个
def merge(pointA, pointB, horizontal, distance):
    combination = {}
    if horizontal:
        if abs(pointA['boundingPoly']['vertices'][1]['x']-pointB['boundingPoly']['vertices'][0]['x']) < distance:
            combination['description'] = pointA['description'].strip() + pointB['description'].strip()
            vertices = pointA['boundingPoly']['vertices']
            vertices[1] = pointB['boundingPoly']['vertices'][1]
            vertices[2] = pointB['boundingPoly']['vertices'][2]
            vertices = {'vertices':vertices}
            combination['boundingPoly'] = vertices
    else:
        pointA['desription'] = pointA['description'].strip()
        pointB['desription'] = pointB['description'].strip()
    #else:
    #    if abs(pointA['boundingPoly']['vertices'][0]['y']-pointB['boundingPoly']['vertices'][3]['y']) < distance:
    #        combination['description'] = pointA['description'] + pointB['description']
    #        vertices = pointA['boundingPoly']['vertices']
    #        vertices[0] = pointB['boundingPoly']['vertices'][0]
    #        vertices[1] = pointB['boundingPoly']['vertices'][1]
    #        vertices = {'vertices':vertices}
    #        combination['boundingPoly'] = vertices
    return combination

# 这个函数将records离得近的元素合并为一个函数
# 这个函数将会修改records中相关内容
def rearrange(records, horizontal=True, distance=0.0):
    result = []
    for index in range(len(records)-1):
        combine = merge(records[index], records[index+1], horizontal, distance)
        if combine:
            records[index+1] = combine
        else:
            result.append(records[index])
    return result

# 在原图上进行画图  查看相关的结果
def draw_text(image, records):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for record in records:
        box = [(v.get('x', 0.0), v.get('y', 0.0)) for v in record['boundingPoly']['vertices']]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
    im.show()

if __name__ == '__main__':
    records = model[1:]
    #result = rearrange(records, distance=60)
    for record in records:
        if '日期' in record['description']:
            print('Desciption： ' + record['description'])
            print(record['boundingPoly']['vertices'])
    #filename = '2.pic_hd.jpg'
    #with open(filename, 'rb') as image:
    #    draw_text(image, result)

    #match = main()
    #print(match)
    #for record in records:
    #    description = record['description']
    #    vertices = record['boundingPoly']['vertices']

