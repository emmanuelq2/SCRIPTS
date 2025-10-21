import sys
sys.stdout.reconfigure(encoding="utf-8")
import difflib

def simple_diff(mt: str, pe: str):
    diff = difflib.ndiff(mt, pe)
    for d in diff:
        print(d)

# Example usage (Japanese)
mt_ja = "クラリティは、クリスタルの純度とインクルージョンの見えやすさを表します。"
pe_ja = "ククラリティは、結晶の純度やインクルージョン（内包物）の見え方を評価するものです。"

print("\n=== Diff (JA) ===")
simple_diff(mt_ja, pe_ja)

# Example usage (Chinese)
mt = "这些鞋子以扁平设计展现出简约的优雅。"
pe = "这些鞋子以平底设计展现出简约的优雅。"

print("=== Diff (ZH) ===")
simple_diff(mt, pe)





