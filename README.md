# word-generator

音節（母音・子音の組み合わせ）のパターンに沿った語を生成するアプリです。

## 使い方

1. `src/config.json` で定義される設定をいじる
2. `src/generate.py` を実行する

## `config.json`

### `sounds`

`sounds` ではパターンで用いる音を構成します。`sounds`は辞書で宣言されます。

辞書のキーは音のラベルであり、値は音の取りうる文字の配列（スペース区切り）です。

```json5
{
    "sounds": {
        "C": "c d f g h",
        "V": "a e i o u",
        "C_CLUSTER": "sk pf tr" // 辞書の
    }
}
```

### `patterns`

`patterns` では生成する語彙の音節パターンを設定します。`patterns` は音節パターンの構成の配列です。

音節パターンの構成は辞書であり、`syllable`（必須）、`label`（任意）、`count`（任意）で構成されます。`syllable` で用いる音に先述の `sounds` で宣言されたもの以外を用いた場合、スクリプトの実行時にエラーが発生します。

```json5
{
    "patterns": [{
        // Required:
        // "syllable": [音節を一つずつ区切った配列]
        // "sounds" に対応する音節の音がない場合エラーになります
        "syllable": ["C", "V", "C"],
    
        // Optional:
        // 生成する文字列の説明
        "label": "適当な語彙を生成する",
    
        // Optional:
        // 生成する語の個数
        // デフォルト値: 5
        "count": 3
    }]
}
```
