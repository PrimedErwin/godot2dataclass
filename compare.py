def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as fp1, \
         open(file2, 'r', encoding='utf-8') as fp2:
        line = 0
        for line1, line2 in zip(fp1, fp2):
            line += 1
            if line1 != line2:
                print(f'{line} is different')
                return
        print('No difference found')
            
compare_files('output.json', 'extension_api.json')