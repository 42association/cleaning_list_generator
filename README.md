# Cleaning List Generator

このプロジェクトは、CSVファイルから掃除当番のリストを生成するPythonスクリプトです。男性6人と女性1人のグループを作成し、ランダムな順序で出力します。

## 仕様

- CSVファイル (`2024Q1_cleaning_list.csv`) から掃除当番のデータを読み込みます。
- 男性と女性のデータを分けます。
- 男性のデータをシャッフルします。
- 男性6人と女性1人のグループを作成します。
- 男性のデータが一巡したら再度シャッフルします。
- 前回の最後の出力グループのメンバーが次回の先頭に来ないように調整します。
- 出力はJSONフォーマットで行います。

## 使用方法

1. `2024Q1_cleaning_list.csv` ファイルを用意します。以下の列を含むようにしてください:
  - intra
  - first_name
  - last_name
  - level
  - gender
  - affiliation

2. スクリプトを実行します:
```
$ python generator.py
```

3. Enterキーを押すと、次のグループが出力されます。

## 出力フォーマット

出力はJSONフォーマットで行われます。各メンバーは以下の情報を含みます:

- `login`: メンバーのイントラID
- `first_name`: 名
- `last_name`: 姓
- `level`: レベル (浮動小数点数 または null)
- `closed`: null
- `gender`: 性別 ("male" または "female")
- `campus_name`: 所属
- `groups_name`: ("" または "online")

例:

```json
[
  {
    "intra": "ymatsui",
    "first_name": "yushi",
    "last_name": "matsui",
    "level": 100,
    "gender": "male",
    "affiliation": "42 Tokyo"
  }
  ...
]
