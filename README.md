# 說明 #
本專案為MAC的輸入法開源專案"香草輸入法"（OpenVanilla）的輔助程式，
用來轉內建行列輸入法的cin檔，使其變為dvorak英文鍵盤 + 行列中文。

## 問題描述 ##
香草輸入法中的行列，英文鍵位綁定qwerty鍵盤。
即使在香草輸入法中的「偏好設定」->「一般設定」->「數字鍵盤配置」中，設定dvorak鍵盤，
在行列中使用「caps lock」鍵一樣會對應qwerty鍵盤。
我想這應該是因為行列的規格特別，需要另外處理。

本專案提供一個解決方案，讓dvorak + 行列的使用者，可以使用香草輸入法搭配使用。

## 以知問題 ##
* 一級簡碼中，「2^」對應的符號鍵位無法使用；同時，「8v」對應的一級簡碼無法使用。猜測應該是香草的「2^」對應符號鍵位是special case，所以將其mapping table改掉會產生問題。「8v」在dvorak的對應鍵是「w」，剛好是qwerty鍵盤的「2^」，應該是因此出了問題。

## 環境 ##
本專案測試時的香草輸入法採當時的最新版。（1.4.0）
python 使用 3.7.4版。
程式只是簡單的轉碼程式，照理說應該不會有問題。

## 使用說明 ##
將此專案clone回家目錄資料夾

```bash
cd ~
git clone https://github.com/idhowardgj94/OpenVanilla_Dvorak_Array
```

首先先將行列的英文鍵位從qwerty轉為dvorak鍵位：

```bash
defaults write org.openvanilla.OVIMArray AlphanumericKeyboardLayout com.apple.keylayout.Dvorak
```

之後若要改回qwerty鍵盤對應，執行以下指令即可：
```bash
defaults write org.openvanilla.OVIMArray AlphanumericKeyboardLayout com.apple.keylayout.US
```

可以直接使用轉換出來的cin檔，也可以手動將香草內鍵的行列cin檔抓出來mapping。

若要使用轉換出來的mapping檔：

```bash
cd OpenVanilla_Dvorak_Array/new # into new directory
cp * ~/Library/Input\ Methods/OpenVanilla.app/Contents/Resources/DataTables/Array
# copy new table to openVanilla's folder
sudo reboot # reboot to let OpenVanilla read new table.
```

如果要自行轉換cin檔，請照著以下步驟操作：

1、將香草輸入法中的行列cin烤貝回專案根目錄。

```bash
cd ~/OpenVanilla_Dvorak_Array
cp ~/Library/Input\ Methods/OpenVanilla.app/Contents/Resources/DataTables/Array .
```

2、打開`transform.py`，修改`FILES` 變數，將烤貝回來、需要轉檔的檔案名稱填入陣列中。

```python
FILES = ["array30.cin", "array-shortcode.cin", "array-special.cin"]
```

3、執行程式，輸出會存在`new`資料夾中

```bash
python transform.py
```

4、將new資料夾中的檔案copy回OpenVanilla資料夾、重新開機。

```bash
cd new # into new directory
cp * ~/Library/Input\ Methods/OpenVanilla.app/Contents/Resources/DataTables/Array
# copy new table to openVanilla's folder
sudo reboot # reboot to let OpenVanilla read new table.
```
