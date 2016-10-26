# template
新しくファイルを作った時にテンプレートを挿入してほしいお気持ちになったから作った


## usage
適当にパス通して使って

temp <ファイル名>

## template
temp.pyと同階層にあるtemplates/と、ホームディレクトリの.templates/の中を調べる。
作るファイルと同じ拡張子.tempが存在すればそれを使う。

その際、tempファイル内の<#filename#>をファイル名に、
<#FILENAME#>をファイル名の大文字に置換してくれる。
