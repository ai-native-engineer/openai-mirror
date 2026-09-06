<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/bulk-rna-seq-fastq-qc -->

## 善用技能

NGS Analysis 外掛程式包含：

- `ngs-analysis-router`
- `ngs-bulk-rnaseq-counts-qc`
- `ngs-runtime-env`

使用此外掛程式時，ChatGPT 可以運用其中內含的所有技能。

## 逐步指南

1. 請向 ChatGPT 指定內含樣本表、FASTQ、轉錄體 FASTA、基因組 FASTA 及 GTF 的目錄，或直接提供確切的檔案路徑。
2. 執行起始提示詞，讓 ChatGPT 在實際執行前驗證鏈特異性、參考檔案一致性，以及工具是否準備就緒。
3. 在 ChatGPT 中開啟產生的 MultiQC 和矩陣成品，以審查比對率、重複率、文庫類型一致性與資源就緒狀態。
4. 在同一個對話中繼續處理，以排除阻礙因素、使用更新後的中繼資料重新執行，或將產生的基因層級矩陣提供給下游差異表現分析使用。

## 結果

此次執行會傳回經 QC 審查的計數套件，而非單純的量化
輸出。請先查看 MultiQC 報告，找出可能影響
下游判讀的警告。在此範例中，ChatGPT 會顯示 FastQC
序列內容警告與執行摘要，讓團隊判斷
觀察到的模式是否符合文庫製備的預期。

![一併查看 FastQC 序列內容警告與 bulk RNA-seq 執行摘要。](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-1.webp)

接著，請在同一份報告中查看 Salmon 統計資料。比對率、
文庫類型判定結果與重複情形，可用來快速確認是否已準備就緒，
再進行差異表現分析。

![查看產生的 MultiQC 報告中的 Salmon 比對與文庫類型統計資料。](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-2.webp)

產生的基因層級計數矩陣會儲存成可重複使用的成品。請在 ChatGPT 中
開啟該矩陣，確認預期的樣本與特徵皆存在，再將矩陣與執行溯源資訊
一同保留，供下游分析使用。

![開啟產生的基因層級計數矩陣，供後續審查。](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-3.webp)
