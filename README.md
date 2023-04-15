# word-generator

音節（母音・子音の組み合わせ）のパターンに沿った語を生成するアプリです。

## 使い方

1. `src/config.json` で定義される設定をいじる
2. `src/generate.py` を実行する

## `config.json`

### `sounds`

```json
"sounds": {
    // "音": "音が取りうる文字の集合　スペース区切り
    // 複数定義可能
    "C": "c d f g h",
    "V": "a e i o u"
}
```

### `patterns`

```json
{
    // "syllable": [音節を一つずつ区切った配列]
    // "sounds" に対応する音節の音がない場合エラーになります
    "syllable": ["C", "V", "C"],

    // 生成する語の個数
    "count": 3
}
```
