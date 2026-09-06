<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/discover-protein-folding-architectures -->

## 探索蛋白質摺疊架構假設

若你的蛋白質摺疊假設需要經過多次
實作才能驗證，請使用 Codex 目標模式。請為 Codex 提供範圍明確的科學方向、
可運作的基準模型，以及可自動評分的基準測試。Codex 可以實作
架構分支版本、追蹤實驗、診斷失敗並繼續
迭代，而你可以審查相關證據。

這個範例從一個具體問題出發：如果 AlphaFold2 風格模型的主幹
不只表示殘基和殘基對，還能表示明確的高階拓撲
物件，模型是否就能更有效率地學習有用的蛋白質幾何
結構？

## 定義範圍明確的實驗

AlphaFold2 的 Evoformer 已運用強大的成對推理和三角形推理。
其三角形運算可改善邊表示，但仍會
寫回成對張量。該科學家提議測試，可持續保留且
由模型學習得到的三角面與四面體胞元表示，是否能
在資料有限的情境下提供實用的歸納偏置。

由此產生的公開程式碼庫 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold)，
新增了稀疏的面狀態 `F_ijk` 與四面體狀態 `U_ijkl`，並保留
傳統的成對表示 `Z_ij`。

```text
MSA representation M
        <-> pair / edge tensor Z_ij
        <-> sparse face tensor F_ijk
        <-> sparse tetra tensor U_ijkl
        -> structure module
        -> recycled geometry
        loops back into the next pass

先從本頁的入門提示詞、最精簡的 AlphaFold2 風格基準模型，
以及公開的 NanoFold 基準測試開始。此基準測試提供小型且經過精選、
採用固定資料並可自動評分的測試平台，適合用於結構生物學
實驗。第一版實作應保持精簡，以便
透過針對性的單元測試和微型基準測試加以驗證，再啟動成本高昂的訓練
作業。

## 使用目標模式進行搜尋

1. 提供一項可證偽的高層次科學假設，而不是要求模型從零開始自行設計整套研究議程。
2. 在 ChatGPT 中使用 GPT-5.5 Pro，將這個研究方向轉化為明列限制條件與消融實驗的實作計畫。
3. 請 Codex 實作最精簡且可執行的 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold) 基準版本，再以針對性的單元測試與微型基準測試進行驗證。
4. 將產生的程式碼庫交給 Codex 目標模式，並指示它透過爬山式搜尋，提高 NanoFold 基準測試驗證集的 `lDDT-Cα` 分數，同時保留實驗紀錄、計畫及產出項目的參照資訊。
5. 讓目標模式持續執行，並運用基準測試回饋，反覆調整架構、訓練方案與實驗任務執行框架。在這個範例中，迴圈執行了超過 150 小時。

使用 `PLAN.md` 記錄目前策略與後續步驟，以 `EXPERIMENTS.md` 來
結構化記錄結果，並以 `EXPERIMENT_NOTES.md` 作為持續更新的隨手筆記。
這些檔案讓長時間執行的搜尋過程可供稽核，並提供穩定的
著力點，方便你引導下一次迭代。

目標模式很適合此處，因為這類搜尋需要反覆實作、
測試、追蹤實驗、診斷失敗，以及依據基準測試結果進行
迭代。未經引導的自動研究通常會逐漸偏向熟悉的局部變更，
例如損失函數、最佳化器與超參數。由科學家提供的精簡
架構假設，為 Codex 界定更有意義的搜尋空間，同時仍保留
測試、診斷和改進實作的餘地。

這套工作流程也適合團隊用來評估科學家參與迴圈
並提供引導時，會如何影響智慧體式科學搜尋的品質。

## 範例結果

這套工作流程的成果是 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold)，
一種具有明確高階單純形狀態的實驗性架構。請一併審查
拓撲與基準測試紀錄，以確認每次迭代仍在
檢驗原始的科學構想。

![1-單純形、2-單純形與 3-單純形蛋白質幾何結構的比較。](/codex/use-cases/discover-protein-folding-architectures-simplex.webp)

值得汲取的重點並不是 Codex 已自主解決蛋白質摺疊問題。這套
工作流程展示了目標模式如何作為持續運作的科學工程
迴圈：科學家提出關鍵的概念轉變，而 Codex 則縮短
實作、實驗、偵錯與後續搜尋的週期。

請將具潛力的診斷結果視為實作路徑可行的證據，
而不是泛化能力的證明。請定期審查智慧體的探索軌跡；若它
流於局部超參數調整，請將其導回具有科學意義的架構問題；並且只在
完成條件相符的公開驗證比較與適當的重複實驗後，
才將結果提升為正式主張。

## 資源

- [SimplexFold 程式碼庫](https://github.com/ChrisHayduk/SimplexFold)
- [SimplexFold 基準測試計畫](https://github.com/ChrisHayduk/SimplexFold/blob/main/BENCHMARK_PLAN.md)
- [NanoFold 競賽](https://github.com/ChrisHayduk/nanoFold-Competition)
- [NanoFold 競賽規則](https://github.com/ChrisHayduk/nanoFold-Competition/blob/main/docs/COMPETITION.md)
- [目標模式持續執行超過 150 小時](https://x.com/ChrisHayduk/status/2055757345506877759?s=20)
- [目標模式文章](https://x.com/ChrisHayduk/status/2053807198870880743?s=20)
