# import os
# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.lang import Builder
from kivy.core.window import Window 

from kivymd.app import MDApp

Window.size= (350,550)

KV = '''
MDNavigationLayout:

    MDScreenManager:
        MDScreen:
            MDBoxLayout:
                orientation:'vertical'
            
                MDTopAppBar:
                    title: 'TestApp'
                    left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]


                MDBottomNavigation:

                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'first'
                        icon: 'garage'

                        MDScrollView:
                            MDList:
                                id: scroll

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"

                                ThreeLineAvatarListItem:
                                    text: "Three-line item with avatar"
                                    secondary_text: "Secondary text here----------------------------------------------------------------"
                                    tertiary_text: "fit more text than usual-----------------------------------------------------"

                                    ImageLeftWidget:
                                        source: "image icon.png"



                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'something'
                        icon: 'garage'


                        MDLabel:
                            text: 'page2'
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'screen 3'
                        text: 'third'
                        icon: 'garage'

                        MDLabel:
                            text: 'third page'
                            halign: 'center'
    MDNavigationDrawer:
        id: nav_drawer
        MDLabel:
            text: "Hello, drawer is here"

'''


class TestDemo(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_string(KV)


TestDemo().run()
