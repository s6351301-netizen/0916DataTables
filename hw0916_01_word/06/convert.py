import csv
import json

input_csv = 'ecdict.csv'
output_json = 'data.json'
word_list = []

with open(input_csv, mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    count = 1
    for row in csv_reader:
        word = row.get('word', '').strip()
        translation = row.get('translation', '').strip()
        phonetic = row.get('phonetic', '').strip()
        
        # 取得單字頻率標籤
        oxford = row.get('oxford', '').strip()
        collins = row.get('collins', '').strip()
        
        # 【關鍵過濾條件】：只要「牛津 3000 核心單字(1)」或「柯林斯 4~5 星常用字」
        if oxford != '1' and collins not in ['4', '5']:
            continue
            
        # 排除沒有翻譯，或是太短(單個字母)、包含特殊符號的字
        if not word or not translation or len(word) < 2 or not word.isalpha():
            continue
            
        formatted_translation = translation.replace('\n', ' / ')
        
        word_data = {
            "id": count,
            "word": word,
            "meaning": formatted_translation,
            "pronunciation": f"/{phonetic}/" if phonetic else "無音標",
            "sentence": "No example sentence available.",
            "sentence_meaning": "無例句翻譯"
        }
        
        word_list.append(word_data)
        count += 1
        
        # 抓取最常用的 2000 個單字做為前端資料庫就很豐富了
        if count > 2000:
            break

with open(output_json, mode='w', encoding='utf-8') as json_file:
    json.dump(word_list, json_file, ensure_ascii=False, indent=4)

print(f"轉換成功！透過頻率篩選，共輸出了 {len(word_list)} 筆【常用】單字資料至 {output_json}")