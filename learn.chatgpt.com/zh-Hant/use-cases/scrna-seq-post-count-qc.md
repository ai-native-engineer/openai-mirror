<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/scrna-seq-post-count-qc -->

## 善用技能

NGS Analysis 外掛程式包含：

- `ngs-analysis-router`
- `scrna-seq-qc`
- `ngs-scrna-seq`

使用此外掛程式時，ChatGPT 可以使用其中封裝的所有技能。

## 逐步指南

1. 向 ChatGPT 指明要使用的矩陣、條碼、基因或特徵、資訊清單和資料集的中繼資料，或提供確切的檔案參照資訊。
2. 執行起始提示詞，讓 ChatGPT 根據觀察到的分布選擇 QC 閾值，並將選擇依據記錄在此次執行的產物中。
3. 開啟視覺化索引，以及審查用的筆記本或應用程式，查看通過或未通過 QC 的細胞數、UMAP 圖和註釋信賴度。
4. 在同一對話中繼續操作，以微調閾值、提供相符的參考圖譜，或在解除雙細胞偵測的阻礙後重新執行。

## 結果

這次執行會產生用於審查篩選決策的介面，而不只是
經篩選的矩陣。請先查看閾值選擇依據圖和 QC
摘要，瞭解每項篩選條件移除或標記了多少細胞，並
判斷選定的閾值是否符合觀察到的分布。

![審查單細胞分析的閾值選擇依據圖，以及通過或未通過 QC 的細胞數。](/codex/use-cases/scrna-seq-post-count-qc-screenshot-1.webp)

接著，依粗略標籤和 Leiden 叢集檢視產生的 UMAP 圖。這些
檢視畫面能幫助你找出註釋缺漏、可疑叢集，或
需要重新檢視的閾值設定。

![依粗略標籤和 Leiden 叢集檢視 UMAP 圖。](/codex/use-cases/scrna-seq-post-count-qc-screenshot-2.webp)

最後，審查細胞層級的指標和篩選結果。ChatGPT 會保留
這份表格，以及經篩選的 `.h5ad` 和視覺化產物，讓你能夠
在同一對話中修改閾值，而不會遺失
第一輪篩選的決策依據。

![開啟細胞層級的 QC 指標和篩選結果以供審查。](/codex/use-cases/scrna-seq-post-count-qc-screenshot-3.webp)
