#include "HX711.h"

// HX711 接線設定
const int DT_PIN = 6;
const int SCK_PIN = 5;
int stanby = 0,state = 1,sum = 0;

const int sample_weight = 233;  //基準物品（我的手機）的真實重量(公克)
int parameter = 0;  //若已知值請輸入

HX711 scale;

void setup() {
  Serial.begin(9600);
  scale.begin(DT_PIN, SCK_PIN);
  scale.tare();
  if (!parameter){
    scale.set_scale();  // 取得比例參數
    Serial.println("Please put sapmple object on it..."); //放上基準物品（我的手機）
    while (state){
      float current_weight=scale.get_units(10);  // 取得10次數值的平均
      float scale_factor=(current_weight/sample_weight);
      if (scale_factor >= 100){
        stanby++;
        if (stanby >= 3)
          sum += scale_factor;
        if (stanby == 5)
          state = 0;
      }
      Serial.print("Scale number:  ");
      Serial.println(scale_factor);  // 顯示比例參數，要記起來
    }
    parameter = sum/3;
  }
  Serial.print("平均比例參數: ");
  Serial.println(parameter);  // 顯示比例參數，要記起來too
  Serial.println("3秒後開始測量");
  Serial.println("3");
  delay(1000);
  Serial.println("2");
  delay(1000);
  Serial.println("1");
  delay(1000);
  scale.set_scale(parameter);       // 設定比例參數
  Serial.println("python start run");
}

void loop() {

  int data = scale.get_units(1);
  Serial.println(data); //將數值回傳python紀錄
  
}
