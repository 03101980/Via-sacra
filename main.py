from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from via_sacra_texts import STATIONS_TEXT  # Importar os textos

Window.size = (360, 640)

class MainScreen(MDScreen):
    def update_theme(self):
        self.md_bg_color = app.theme_cls.bg_normal
        # Adicione aqui a lógica para atualizar o tema da tela, se necessário.
        pass

class IntroScreen(MDScreen):
    def update_theme(self):
        self.md_bg_color = app.theme_cls.bg_normal
    pass

class EstacaoScreen(MDScreen):
    station_number = NumericProperty(None)
    station_station = StringProperty("")
    station_titre = StringProperty("")
    station_image = StringProperty("")
    station_text_texto_moderador = StringProperty("")
    station_text_texto_resp = StringProperty("")
    station_text_texto_um = StringProperty("")
    station_text_texto_dois= StringProperty("")
    station_text_texto_tres = StringProperty("")
    station_text_texto_oration= StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_station_number(self, instance, value):
        viaSacra = ViaSacraApp()
        station_data = viaSacra.stations_data[value]
        self.station_station = station_data['station']
        self.station_titre = station_data['titre']
        self.station_image = station_data['image']
        self.station_text_texto_moderador= station_data['text_mod']
        self.station_text_texto_resp = station_data['text_resp']
        self.station_text_texto_um = station_data['text_um']
        self.station_text_texto_dois = station_data['text_dois']
        self.station_text_texto_tres = station_data['text_tres']
        self.station_text_texto_oration = station_data['text_oration']
    
    def update_theme(self):
        self.md_bg_color = app.theme_cls.bg_normal

class ConclusaoScreen(MDScreen):
    def update_theme(self):
        self.md_bg_color = app.theme_cls.bg_normal
    pass

class ViaSacraApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Blue"         # Azul suave
        self.theme_cls.primary_hue = "400"              # Tom médio-suave
        self.theme_cls.accent_palette = "LightBlue"     # Azul claro/accent
        self.theme_cls.accent_hue = "200"
        self.theme_cls.theme_style = "Dark"
        self.stations_data = {
            1: {'station':'1ª Estação','titre':'Jesus é condenado à morte', 'image': 'assets/1estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[1]['text_um'],
                'text_dois': STATIONS_TEXT[1]['text_dois'],
                'text_tres': STATIONS_TEXT[1]['text_tres'],
                'text_oration': STATIONS_TEXT[1]['text_oration']},
            2: {'station':'2ª Estação','titre':'Jesus carrega a cruz', 'image': 'assets/2estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[2]['text_um'],
                'text_dois': STATIONS_TEXT[2]['text_dois'],
                'text_tres': STATIONS_TEXT[2]['text_tres'],
                'text_oration': STATIONS_TEXT[2]['text_oration']},
            3: {'station':'3ª Estação','titre':'Jesus cai pela primeira vez', 'image': 'assets/3estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[3]['text_um'],
                'text_dois': STATIONS_TEXT[3]['text_dois'],
                'text_tres': STATIONS_TEXT[3]['text_tres'],
                'text_oration': STATIONS_TEXT[3]['text_oration']},
            4: {'station':'4ª Estação','titre':'Jesus encontra sua mãe', 'image': 'assets/4estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[4]['text_um'],
                'text_dois': STATIONS_TEXT[4]['text_dois'],
                'text_tres': STATIONS_TEXT[4]['text_tres'],
                'text_oration': STATIONS_TEXT[4]['text_oration']},
            5: {'station':'5ª Estação','titre':'Simão ajuda Jesus a carregar a cruz', 'image': 'assets/5estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[5]['text_um'],
                'text_dois': STATIONS_TEXT[5]['text_dois'],
                'text_tres': STATIONS_TEXT[5]['text_tres'],
                'text_oration': STATIONS_TEXT[5]['text_oration']},
            6: {'station':'6ª Estação','titre':'Verônica limpa o rosto de Jesus', 'image': 'assets/6estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[6]['text_um'],
                'text_dois': STATIONS_TEXT[6]['text_dois'],
                'text_tres': STATIONS_TEXT[6]['text_tres'],
                'text_oration': STATIONS_TEXT[6]['text_oration']},
            7: {'station':'7ª Estação','titre':'Jesus cai pela segunda vez', 'image': 'assets/7estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[7]['text_um'],
                'text_dois': STATIONS_TEXT[7]['text_dois'],
                'text_tres': STATIONS_TEXT[7]['text_tres'],
                'text_oration': STATIONS_TEXT[7]['text_oration']},
            8: {'station':'8ª Estação','titre':'Jesus encontra as mulheres de Jerusalém', 'image': 'assets/8estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[8]['text_um'],
                'text_dois': STATIONS_TEXT[8]['text_dois'],
                'text_tres': STATIONS_TEXT[8]['text_tres'],
                'text_oration': STATIONS_TEXT[8]['text_oration']},
            9: {'station':'9ª Estação','titre':'Jesus cai pela terceira vez', 'image': 'assets/9estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[9]['text_um'],
                'text_dois': STATIONS_TEXT[9]['text_dois'],
                'text_tres': STATIONS_TEXT[9]['text_tres'],
                'text_oration': STATIONS_TEXT[9]['text_oration']},
            10: {'station':'10ª Estação','titre':'Jesus é despojado de suas vestes', 'image': 'assets/10estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[10]['text_um'],
                'text_dois': STATIONS_TEXT[10]['text_dois'],
                'text_tres': STATIONS_TEXT[10]['text_tres'],
                'text_oration': STATIONS_TEXT[10]['text_oration']},
            11: {'station':'11ª Estação','titre':'Jesus é pregado na cruz', 'image': 'assets/11estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[11]['text_um'],
                'text_dois': STATIONS_TEXT[11]['text_dois'],
                'text_tres': STATIONS_TEXT[11]['text_tres'],
                'text_oration': STATIONS_TEXT[11]['text_oration']},
            12: {'station':'12ª Estação','titre':'Jesus morre na cruz', 'image': 'assets/12estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[12]['text_um'],
                'text_dois': STATIONS_TEXT[12]['text_dois'],
                'text_tres': STATIONS_TEXT[12]['text_tres'],
                'text_oration': STATIONS_TEXT[12]['text_oration']},
            13: {'station':'13ª Estação','titre':'Jesus é descido da cruz', 'image': 'assets/13estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[13]['text_um'],
                'text_dois': STATIONS_TEXT[13]['text_dois'],
                'text_tres': STATIONS_TEXT[13]['text_tres'],
                'text_oration': STATIONS_TEXT[13]['text_oration']},
            14: {'station':'14ª Estação','titre':'Jesus é colocado no sepulcro', 'image': 'assets/14estacao.jpg', 
                'text_mod': STATIONS_TEXT[0]['text_mod'], 
                'text_resp': STATIONS_TEXT[0]['text_resp'],
                'text_um': STATIONS_TEXT[14]['text_um'],
                'text_dois': STATIONS_TEXT[14]['text_dois'],
                'text_tres': STATIONS_TEXT[14]['text_tres'],
                'text_oration': STATIONS_TEXT[14]['text_oration']}
        }

    def build(self):
        global app
        app = Builder.load_file('via_sacra.kv')

        # Inicializar dados das estações
        for i in range(1, 15):
            estacao = app.ids.screen_manager.get_screen(f'estacao{i}')
            estacao.station_number = i

        return app

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
        self.open_nav_drawer()

    def open_nav_drawer(self):
        if self.root.ids.nav_drawer.state == 'open':
            self.root.ids.nav_drawer.set_state("close")
        else:
            self.root.ids.nav_drawer.set_state("open")

    def toggle_theme(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
        # Força atualização da UI
        current_screen = self.root.ids.screen_manager.current
        self.root.ids.screen_manager.get_screen(current_screen).update_theme()

    def next_screen(self):
        current = self.root.ids.screen_manager.current
        if current == 'main':
            self.root.ids.screen_manager.current = 'intro'
        elif current == 'intro':
            self.root.ids.screen_manager.current = 'estacao1'
        elif current == 'conclusao':
            return
        else:
            # Pega o número da estação atual
            current_station = int(current.replace('estacao', ''))
            if current_station < 14:
                self.root.ids.screen_manager.current = f'estacao{current_station + 1}'
            else:
                self.root.ids.screen_manager.current = 'conclusao'

    def prev_screen(self):
        current = self.root.ids.screen_manager.current
        if current == 'main':
            return
        elif current == 'intro':
            self.root.ids.screen_manager.current = 'main'
        elif current == 'estacao1':
            self.root.ids.screen_manager.current = 'intro'
        elif current == 'conclusao':
            self.root.ids.screen_manager.current = 'estacao14'
        else:
            # Pega o número da estação atual
            current_station = int(current.replace('estacao', ''))
            self.root.ids.screen_manager.current = f'estacao{current_station - 1}'

if __name__ == '__main__':
    ViaSacraApp().run()
