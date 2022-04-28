from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

kv = """

MDScreen:

     MDBoxLayout:
          orientation: "vertical"

          GridLayout:
               cols: 4
               size_hint_y: .2

               MDLabel:
                    id: player
                    text: "O's turn"
                    font_size: dp(25)
                    halign: "center"

               MDLabel:
                    id: player_o_score
                    text: "Player_O_Score = 0"
                    halign: "center"

               MDLabel:
                    id: player_x_score
                    text: "Player_X_Score = 0"
                    halign: "center"

               Button:
                    text: "Restart"
                    on_release: app.restart()

          GridLayout:
               cols: 3
               size_hint_y: .8

               Button:
                    id: btn1
                    text: ""
                    size_hint: .3, .3
                    font_size: dp(150)
                    on_release: app.btn_clicked(btn1)

               Button:
                    id: btn2
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn2)
               
               Button:
                    id: btn3
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn3)

               Button:
                    id: btn4
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn4)

               Button:
                    id: btn5
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn5)
               
               Button:
                    id: btn6
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn6)

               Button:
                    id: btn7
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn7)

               Button:
                    id: btn8
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn8)
               
               Button:
                    id: btn9
                    text: ""
                    size_hint: .3, .3
                    font_size: 150
                    on_release: app.btn_clicked(btn9)

"""

class MainApp(MDApp):

     player_o_score = 0
     player_x_score = 0

     def player_O_win(self):
          if self.root.ids.btn1.text == "O" and self.root.ids.btn2.text == "O" and self.root.ids.btn3.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)
               return True

          elif self.root.ids.btn4.text == "O" and self.root.ids.btn5.text == "O" and self.root.ids.btn6.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)
               return True

          elif self.root.ids.btn7.text == "O" and self.root.ids.btn8.text == "O" and self.root.ids.btn9.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)
               return True

          elif self.root.ids.btn1.text == "O" and self.root.ids.btn4.text == "O" and self.root.ids.btn7.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)
               return True

          elif self.root.ids.btn2.text == "O" and self.root.ids.btn5.text == "O" and self.root.ids.btn8.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)
               return True

          elif self.root.ids.btn3.text == "O" and self.root.ids.btn6.text == "O" and self.root.ids.btn9.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)
               return True

          elif self.root.ids.btn1.text == "O" and self.root.ids.btn5.text == "O" and self.root.ids.btn9.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)
               return True

          elif self.root.ids.btn3.text == "O" and self.root.ids.btn5.text == "O" and self.root.ids.btn7.text == "O":
               self.player_o_score+=1
               self.root.ids.player_o_score.text = "Player_O_Score = "+str(self.player_o_score)
               self.chage_btn_color(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)
               return True

          else:
               return False

     def player_X_win(self):
          if self.root.ids.btn1.text == "X" and self.root.ids.btn2.text == "X" and self.root.ids.btn3.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)
               return True

          elif self.root.ids.btn4.text == "X" and self.root.ids.btn5.text == "X" and self.root.ids.btn6.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)
               return True

          elif self.root.ids.btn7.text == "X" and self.root.ids.btn8.text == "X" and self.root.ids.btn9.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)
               return True

          elif self.root.ids.btn1.text == "X" and self.root.ids.btn4.text == "X" and self.root.ids.btn7.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)
               return True

          elif self.root.ids.btn2.text == "X" and self.root.ids.btn5.text == "X" and self.root.ids.btn8.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)
               return True

          elif self.root.ids.btn3.text == "X" and self.root.ids.btn6.text == "X" and self.root.ids.btn9.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)
               return True

          elif self.root.ids.btn1.text == "X" and self.root.ids.btn5.text == "X" and self.root.ids.btn9.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)
               return True

          elif self.root.ids.btn3.text == "X" and self.root.ids.btn5.text == "X" and self.root.ids.btn7.text == "X":
               self.player_x_score+=1
               self.root.ids.player_x_score.text = "Player_X_Score = "+str(self.player_x_score)
               self.chage_btn_color(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)
               return True

          else:
               return False

     def chage_btn_color(self, btn1, btn2, btn3):
          btn1.color = "red"
          btn2.color = "red"
          btn3.color = "red"
          self.disable_btns()
     
     def disable_btns(self):
          self.root.ids.btn1.disabled = True
          self.root.ids.btn2.disabled = True
          self.root.ids.btn3.disabled = True
          self.root.ids.btn4.disabled = True
          self.root.ids.btn5.disabled = True
          self.root.ids.btn6.disabled = True
          self.root.ids.btn7.disabled = True
          self.root.ids.btn8.disabled = True
          self.root.ids.btn9.disabled = True

     def btn_clicked(self, btn):
          if self.root.ids.player.text == "O's turn":
               btn.text = "O"
               btn.disabled = True
               self.root.ids.player.text = "X's turn"
               self.player_O_win()

          else:
               btn.text = "X"
               btn.disabled = True
               self.root.ids.player.text = "O's turn"
               self.player_X_win()

     def restart(self):
          # making all buttons editable
          self.root.ids.btn1.disabled = False
          self.root.ids.btn2.disabled = False
          self.root.ids.btn3.disabled = False
          self.root.ids.btn4.disabled = False
          self.root.ids.btn5.disabled = False
          self.root.ids.btn6.disabled = False
          self.root.ids.btn7.disabled = False
          self.root.ids.btn8.disabled = False
          self.root.ids.btn9.disabled = False

          # making all buttons text empty
          self.root.ids.btn1.text = ""
          self.root.ids.btn2.text = ""
          self.root.ids.btn3.text = ""
          self.root.ids.btn4.text = ""
          self.root.ids.btn5.text = ""
          self.root.ids.btn6.text = ""
          self.root.ids.btn7.text = ""
          self.root.ids.btn8.text = ""
          self.root.ids.btn9.text = ""

          # setting color of buttons to green
          self.root.ids.btn1.color = "white"
          self.root.ids.btn2.color = "white"
          self.root.ids.btn3.color = "white"
          self.root.ids.btn4.color = "white"
          self.root.ids.btn5.color = "white"
          self.root.ids.btn6.color = "white"
          self.root.ids.btn7.color = "white"
          self.root.ids.btn8.color = "white"
          self.root.ids.btn9.color = "white"

     def build(self):
          self.theme_cls.theme_style = "Dark"
          self.theme_cls.primary_palette = "BlueGray"

          return Builder.load_string(kv)

if __name__ == "__main__":
     MainApp().run()
