<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img alt="LOGO" src="https://cdn.jsdelivr.net/gh/MaaAssistantArknights/design@main/v1/icons/maa-logo_512x512.png" width="256" height="256" />
</p>

<div align="center">

# MaaPCR

基於 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 所提供的項目模板，由[AaronYu0625](https://github.com/AaronYu0625)開發的Maa公主連結小助手。

</div>

## ⚠️免責聲明與風險提示

> [!Note]
> 本項目旨在簡化用户的重複性操作，絕不會修改任何遊戲文件或數據。
> 
> 本項目開源、免費，且僅供學習和交流使用，請勿用於任何商業或營利性目的。
> 
> 開發者擁有本項目的最終解釋權。因使用本軟件而產生的任何問題，均與本項目及開發者無關。
>
> **您應充分了解並自願承擔使用本工具可能帶來的所有風險。**

## 關於Maa公主連結小助手
目前僅支持繁中服(台服)

基於Windows系統下mumu模擬器1280x720,dpi:240 來開發及實測，其他模擬器及系統理論上一樣能用。

開發者原為[Rino公主连结璃乃助手](https://github.com/miaoyu2233/Rino_PCRautomation)的繁中服用家，前段時間大概因MaaFramework更新版本及MFAWPF遷移至MFAAvalonia後便再無更新所以決定自己來開發新版本自用，
當中參考了他的任務流程再用[MaaPipelineEditor](https://github.com/kqcoxn/MaaPipelineEditor)加以優化改良並轉換成Project Interface V2 版本。

當前小助手並未有全舊版的所有功能，現時只有轉換到開發者自用的功能，剩餘功能未定會否補上。

如有任何建議/BUG都可以在[Issues](https://github.com/AaronYu0625/MAA-PCR/issues)上提出，但因本項目為開發者於空閒時用愛發電所研究的，所以不能保證更新時間。

## ✨功能一覽
- 購買一般商店
  - 只買藥水
  - 只買精煉石
  - 全買
>目前暫時只能選擇無限購買或只買一次
>### 無限購買需自行停止任務，不然會一直重複購買至無法購買或用完瑪娜
- 購買商店角色碎片
  - 地下城商店
  - 競技場商店
  - 公主競技場商店
  - 戰隊商店
>目前暫時只能選擇一個角色碎片無限購買或只買一次
>### 無限購買需自行停止任務，不然會一直重複購買至無法購買或用完該商店的硬幣
- EX裝備刷詞條
  - 貫通5
  - 貫通3
  - TP上升3
>需自行進入"究極鍊成"頁面選擇要刷的EX裝備，每當刷出詞條後就會上鎖並停止任務，目前只能上鎖一條詞條如果運氣好一次刷出2條或以上則需自行上鎖其餘詞條，上鎖後再次開始任務即可
>### 開始前請先確定要刷的EX裝備能刷出您所選擇的詞條數值

## 待更新內容
- 自定次數/定時停止商店刷新
- 同一商店選擇多個角色碎片購買
- 跳過主線劇情
- 角色全部強化 & Rank提升
- 自動巡遊 **(因內容龐大待定)**
## 如何使用
### 請先確認模擬器畫面設置為1280x720,DPI:240
<img width="452" height="99" alt="image" src="https://github.com/user-attachments/assets/753b5885-9b51-462d-899e-65a5503560ea" />
以mumu模擬器為例，其他模擬器請自行搜尋如何更改畫面設置

### Windows系統
1. 點擊鏈接下載最新版本[Release](https://github.com/AaronYu0625/MAA-PCR/releases)內帶有win-x86_64的zip檔
    - 內有MFAAvalonia UI版本 或 MXU UI版本可供選擇，初次使用可以點開下方縮圖預覽介面
      
    - MFAAvalonia<img width="320" height="240" alt="image" src="https://github.com/user-attachments/assets/2d35492f-5998-4f1c-91c4-777d334fb48a"  />  MXU<img width="320" height="240" alt="image" src="https://github.com/user-attachments/assets/1df3a90f-531e-46c2-87ee-2187bef7340d" />
2. 選擇MXU 或 MFAA UI版本的win-x86_64下載
3. 解壓後打開`MaaPCR.exe`即可運行 **(解壓不建議使用"解壓縮至此")**
### macOS系統 **(未經實測)**
 - 如果是Intel 處理器的機型，請選擇macos-x86_64下載
 - 如果是M1 處理器往後的機型，請選擇aarch64-x86_64下載
 - 使用方式：
  ```bash
  chmod a+x MaaPiCli
  ./MaaPiCli
  ```
### Linux系統 **(未經實測)**
 - ~~用Linux的都是佬，不用多說吧~~

## ❓常見問題
>彈窗提示To run this application, you must install .NET
  - 前往[下載 .NET 10.0](https://dotnet.microsoft.com/zh-tw/download/dotnet/10.0) 並安裝 `.NET 10.0 Desktop Runtime` （.NET 桌面執行階段）。
>開始任務後無反應或點擊錯位
  - 檢查模擬器畫面設置是否為1280x720,DPI:240

## 嗚謝
### 開源項目
- [MaaFramework](https://github.com/MaaXYZ/MaaFramework)
  基于图像识别的自动化黑盒测试框架
- [MaaPipelineEditor](https://github.com/kqcoxn/MaaPipelineEditor)
  可视化构建 MaaFramework Pipeline 的下一代工作流编辑器
- [MXU](https://github.com/MistEO/MXU)
  MaaFramework Next UI
- [MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia)
  基于 Avalonia UI 构建的 MaaFramework 通用 GUI 解决方案
- [Rino_PCRautomation](https://github.com/miaoyu2233/Rino_PCRautomation)
  Rino公主连结璃乃助手
