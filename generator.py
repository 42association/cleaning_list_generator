import csv
import random
import json

# CSVファイルを読み込む
with open('2024Q1_cleaning_list.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# ヘッダー行を削除
header = data.pop(0)

# 男性と女性のデータを分ける
male_data = [row for row in data if row[5] == 'male']
female_data = [row for row in data if row[5] == 'female']

# 男性のデータをシャッフル
random.shuffle(male_data)

# 男性と女性のインデックス
male_index = 0
female_index = 0

# 出力する関数
def output_data():
    global male_index, female_index
    
    output_json = []
    
    # 男性を6人出力
    for _ in range(6):
        if male_index < len(male_data):
            row = male_data[male_index]
            output_json.append({
                'login': row[0],
                'level': float(row[3]) if row[3] != '' else None,
                'gender': row[5],
            })
            male_index += 1
    
    # 男性の合計人数が6で割り切れない場合、足りない人数を追加
    if male_index >= len(male_data):
        remaining_count = 6 - (len(male_data) % 6)
        fill_index = 0
        for i in range(remaining_count):
            if fill_index >= len(male_data):
                fill_index = 0
            row = male_data[fill_index]
            if row[0] not in [item['login'] for item in output_json[-6:]]:
                output_json.append({
                    'login': row[0],
                    'level': float(row[3]) if row[3] != '' else None,
                    'gender': row[5]
                })
                fill_index += 1
            else:
                fill_index += 1
                i -= 1
    
    # 女性を1人出力
    if female_index < len(female_data):
        row = female_data[female_index]
        output_json.append({
            'login': row[0],
            'level': float(row[3]) if row[3] != '' else None,
            'gender': row[5]
        })
        female_index += 1
    else:
        female_index = 0
        row = female_data[female_index]
        output_json.append({
            'login': row[0],
            'level': float(row[3]) if row[3] != '' else None,
            'gender': row[5]
        })
        female_index += 1
    
    print(json.dumps(output_json, indent=2, ensure_ascii=False))
    
    return output_json

# メインの処理
last_output_group = []

while True:
    current_output_group = output_data()
    
    # 男性のデータが一巡したらシャッフル
    if male_index >= len(male_data):
        random.shuffle(male_data)
        
        # シャッフル後、前回の最後の出力グループのメンバーが先頭に来ないように調整
        last_output_login = [row['login'] for row in last_output_group]
        for i in range(len(male_data)):
            if male_data[i][0] not in last_output_login:
                male_data = male_data[i:] + male_data[:i]
                break
        
        male_index = 0
    
    last_output_group = current_output_group
    
    input("Press Enter to continue...")
