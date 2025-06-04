import json

def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as fp1, \
         open(file2, 'r', encoding='utf-8') as fp2:
        json1 = json.load(fp1)
        json2 = json.load(fp2)
        print(f'Compare directly using dict: {json1==json2}')
        json1_byte = json.dumps(json1, ensure_ascii=False).encode('utf-8')
        json2_byte = json.dumps(json2, ensure_ascii=False).encode('utf-8')
        print(f'Compare directly using bytes: {json1_byte==json2_byte}')
        line = 0
        fp1.seek(0)
        fp2.seek(0)
        for line1, line2 in zip(fp1, fp2):
            line += 1
            if line1 != line2:
                print(f'{line} is different')
                return
        print('No difference found')

compare_files('output.json', 'extension_api.json')