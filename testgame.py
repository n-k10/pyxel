#https://kitao.github.io/pyxel/web/launcher/?run=n-k10/pyxel/main/testgame&gamepad=enabled
import pyxel
import random

class App:
    def __init__(self):
        # 画面サイズの設定 (幅160 x 高さ120)
        pyxel.init(160, 120, title="Apple Catcher")

        # プレイヤー（カゴ）の初期設定
        self.player_w = 20  # カゴの幅
        self.player_h = 4   # カゴの高さ
        self.player_x = 70  # X座標（横）
        self.player_y = 105 # Y座標（縦）

        # りんごの初期設定
        self.apple_r = 4    # りんごの半径
        self.apple_x = random.randint(10, 150)
        self.apple_y = 0

        # スコア
        self.score = 0

        # ゲームループの開始
        pyxel.run(self.update, self.draw)

    def update(self):
        # Qキーでゲーム終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # プレイヤーの移動（左右キー）
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 3, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 3, 160 - self.player_w)

        # りんごを落とす（スピード）
        self.apple_y += 2

        # 当たり判定（キャッチ成功！）
        # カゴの範囲にりんごが入っているかチェック
        if (self.player_y <= self.apple_y + self.apple_r <= self.player_y + self.player_h) and \
           (self.player_x - self.apple_r <= self.apple_x <= self.player_x + self.player_w + self.apple_r):
            self.score += 10
            self.reset_apple()

        # 画面の下まで落ちた場合（ミス）
        if self.apple_y > 120:
            self.score = max(self.score - 5, 0) # スコアを減らす（0以下にはしない）
            self.reset_apple()

    def reset_apple(self):
        # りんごの位置を上にリセット
        self.apple_x = random.randint(10, 150)
        self.apple_y = 0

    def draw(self):
        # 画面を水色(12)でクリア
        pyxel.cls(12)

        # スコアの表示 (色: 7=白)
        pyxel.text(5, 5, f"SCORE: {self.score}", 7)

        # プレイヤー（カゴ）を描画 (色: 11=緑)
        pyxel.rect(self.player_x, self.player_y, self.player_w, self.player_h, 11)

        # りんごを描画 (色: 8=赤)
        pyxel.circ(self.apple_x, self.apple_y, self.apple_r, 8)

        # 操作説明
        pyxel.text(5, 112, "LEFT/RIGHT: Move  Q: Quit", 7)

# アプリを実行
App()
