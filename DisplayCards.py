
from kivymd.app import MDApp

from kivymd.uix.list import MDList, ThreeLineAvatarListItem, ImageLeftWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView

from kivy.core.window import Window

Window.size= (350,550)


class testcard(MDApp):
    def build(self):

        screener = MDScreen()
        
        #list
        listcontainer = MDScrollView()
        
        listcontainer.add_widget(
            MDList(
                ThreeLineAvatarListItem(
                    ImageLeftWidget(source="./modified_assets/150w flood light led.png"),
                    text="led lamp",
                    secondary_text= "100PCS/CTN"
                    )
                )
            )
        

        

        screener.add_widget(listcontainer)
        return screener 

testcard().run()



