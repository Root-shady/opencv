code = {'description':'code','vertices':[{'y': 36, 'x': 175}, {'y': 42, 'x': 313}, {'y': 63, 'x': 312}, {'y': 57, 'x': 174}]}
title = {'description':'title', 'vertices': [{'y': 26, 'x': 365}, {'y': 26, 'x': 586}, {'y': 47, 'x': 586}, {'y': 48, 'x': 365}]}
number = {'description':'number', 'vertices': [{'y': 62, 'x': 791}, {'y': 59, 'x': 861}, {'y': 71, 'x': 862}, {'y': 74, 'x': 792}]}
date = {'description':'date', 'vertices': [{'y': 89, 'x': 748}, {'y': 81, 'x': 849}, {'y': 94, 'x': 849} ,{'y': 98, 'x': 748}]}
taxpayer = {'description':'taxpayer', 'vertices': [{'y': 123, 'x': 219},  {'y': 124, 'x': 399}, {'y': 135, 'x': 399},{'y': 134, 'x': 219}]}
taxpayer_number = {'description':'taxpayer_number', 'vertices': [{'y': 142, 'x': 233}, {'y': 144, 'x': 399}, {'y': 157, 'x': 399}, {'y': 155, 'x': 233}]} 

contact_info = {'description':'contact_info', 'vertices': [{'y': 165, 'x': 219},  {'y': 167, 'x': 495}, {'y': 173, 'x': 495}, {'y': 173, 'x': 219}]} 
bank_info = {'description':'bank_info', 'vertices': [{'y': 188, 'x': 202}, {'y': 185, 'x': 439}, {'y': 195, 'x': 439}, {'y': 192, 'x': 202}]} 
service = {'description':'service', 'vertices': [{'y': 350, 'x': 95}, {'y': 350, 'x': 270}, {'y': 220, 'x': 270 }, {'y': 220, 'x': 95}]} 
related_info = {'description':'related_info', 'vertices': [{'y': 350, 'x': 295}, {'y': 350, 'x': 380}, {'y': 220, 'x': 380 }, {'y': 220, 'x': 295}]} 
unit = {'description':'unit', 'vertices': [{'y': 350, 'x': 395}, {'y': 350, 'x': 425}, {'y': 220, 'x': 425 }, {'y': 220, 'x': 395}]} 
amount = {'description':'amount', 'vertices': [{'y': 350, 'x': 445}, {'y': 350, 'x': 515}, {'y': 220, 'x': 515 }, {'y': 220, 'x': 445}]} 
unit_price = {'description':'unit_price', 'vertices': [{'y': 350, 'x': 525}, {'y': 350, 'x': 590}, {'y': 220, 'x': 590 }, {'y': 220, 'x': 525}]} 
price = {'description':'price', 'vertices': [{'y': 350, 'x': 605}, {'y': 350, 'x': 715}, {'y': 220, 'x': 715 }, {'y': 220, 'x': 605}]} 
tax_rate = {'description':'tax_rate', 'vertices': [{'y': 350, 'x': 726}, {'y': 350, 'x': 765}, {'y': 220, 'x': 765 }, {'y': 220, 'x': 726}]} 
tax_pay = {'description':'tax_pay', 'vertices': [{'y': 350, 'x': 780}, {'y': 350, 'x': 890}, {'y': 220, 'x': 890 }, {'y': 220, 'x': 780}]} 
#tax_pay = {'description': 'number', 'vertices': [{'y': 201, 'x': 795}, {'y': 201, 'x': 847}, {'y': 212, 'x': 847}, {'y': 212, 'x': 795}]}
net_price = {'description': 'net_price', 'vertices': [{'y': 357, 'x': 637},  {'y': 356, 'x': 714}, {'y': 366, 'x': 714}, {'y': 367, 'x': 637}]}
tax_price = {'description': 'tax_price', 'vertices': [{'y': 354, 'x': 815}, {'y': 356, 'x': 879}, {'y': 368, 'x': 878}, {'y': 366, 'x': 815}]}

total_price = {'description': 'total_price', 'vertices': [{'y': 383, 'x': 721},  {'y': 383, 'x': 807}, {'y': 394, 'x': 807}, {'y': 396, 'x': 721}]}

provider_name = {'description': 'provider_name', 'vertices': [{'y': 415, 'x': 217}, {'y': 414, 'x': 373}, {'y': 425, 'x': 373}, {'y': 427, 'x': 217}]}
identification = {'description': 'identification', 'vertices':[{'y': 434, 'x': 234}, {'y': 434, 'x': 406}, {'y': 447, 'x': 406}, {'y': 447, 'x': 234}]}
pcontact_info = {'description': 'pcontact_info', 'vertices': [{'y': 456, 'x': 216},  {'y': 455, 'x': 434}, {'y': 465, 'x': 434}, {'y': 467, 'x': 216}]}
pbank_info = {'description': 'pbank_info', 'vertices': [{'y': 475, 'x': 216},  {'y': 475, 'x': 503}, {'y': 484, 'x': 503}, {'y': 485, 'x': 216}]}

payee = {'description': 'payee', 'vertices': [{'y': 496, 'x': 150}, {'y': 495, 'x': 176}, {'y': 506, 'x': 176}, {'y': 507, 'x': 150}]}
reviewer = {'description': 'reviewer', 'vertices': [{'y': 493, 'x': 556},  {'y': 491, 'x': 596}, {'y': 503, 'x': 596}, {'y': 505, 'x': 556}]}


target = [code, title, number, date, taxpayer, taxpayer_number, contact_info, bank_info, service, related_info, unit, amount, unit_price, price, tax_rate, tax_pay, net_price, tax_price, total_price, provider_name, identification, pcontact_info, pbank_info, payee, reviewer]

pinpoint = {'service':{'y':205, 'x': 211}, 'unit':{'y': 204, 'x': 402}, 'amount':{'y': 204, 'x': 462}, 'tax_pay':{'y': 201, 'x': 795}, 'capital':{'y': 387, 'x': 201}, 'lower':{'y': 383, 'x': 671},'payee':{'y': 499, 'x': 89},'reviewer':{'y': 496, 'x': 318}, 'proof':{'y': 372, 'x': 896}, 'price':{'y': 203, 'x': 633}, 'date':{'y': 87, 'x': 699}}
