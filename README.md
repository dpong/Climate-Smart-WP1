# Climate-Smart-WP1
Working package of Study on E-Infrastructure of Climate-Smart Water Service project

氣象資料繁衍 - 日降水量模擬模式

【目的】
  氣候變遷對水資源衝擊評估過程中，水文模式需要日氣象資料當做輸入值，然而氣候情境透過簡易降尺度至研究區域，只知道研究區域測站之月統計
資料，因此必須利用已知之測站月統計資料，利用氣象資料繁衍方式，合成出日氣象資料，才能進一步應用至水文模擬，進行氣候變遷衝擊評估。本單元目
的即在協助學生了解氣象資料繁衍之原理，並透過實作學習氣象資料繁衍之計算。


【原理與步驟】
  日降雨量之模擬，可分為降雨事件和降雨發生時之降雨量。降雨事件之模擬以歷史資料為演算依據，統計各月中第 I-1 日降雨時，第 I 日降雨的機率，
表示為 P(Wi|Wi-1);各月中第 I-1 日不降雨時，第 I 日降雨的機率，表示為 P(Wi|Di- 1)。降雨量值之模擬，根據洪念民(1996)可知由
指數分佈(Exponential distribution)可模擬出理想的氣候資料。指數分佈方程式如下:

P=μ𝑝 ×[−ln(⁡1−𝑅𝑁)]

  上列方程式中 P 為日降雨量(公分)，P 為對應該月份雨天之平均降雨量，RN 為介於(0, 1)間的隨機亂數。

  降雨資料繁衍流程乃利用蒙地卡羅模擬法(Monte Carlo Simulation)進行降雨資料繁衍，步驟如下:

1. 可藉由MS Excel的函數 “RAND()”來產生(0,1)之間的亂數RN_P。
2. 每月的第一天，若RN_P小於或等於該月降雨機率P(W)時，表示此日為降雨日;
3. 每月除第一日外，其餘日則利用前一日的降雨情形判定為降雨日或非降雨日，依照P(Wi|Wi-1)或P(Wi|Di-1)的歷史資料平均值，若亂數RN_P小於或
   等於P(Wi|Wi-1)或P(Wi|Di-1)時，判定該日為降雨日。其第I天降雨事件判別 式如下:
   
(1)若第 I-1 天降雨量>0 且 RN_P P(Wi|Wi-1)，則第 I 天會降雨;否則， 則第 I 天不會降雨
(2)若第 I-1 天降雨量=0 且 RN_P P(Wi|Di-1)，則第 I 天會降雨;否則， 則第 I 天不會降雨

4. 若已判定第i天會降雨，則利用MS Excel的函數 “RAND()”來產生(0,1)之 間的亂數RN，再利用公式3-3計算該天降雨量P。
5. 反覆操作步驟1~4，直到需要的資料繁衍完畢。
