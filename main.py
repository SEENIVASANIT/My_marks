from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.bottomsheet import MDCustomBottomSheet
import datetime
from datetime import date
from kivy.properties import StringProperty
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import sqlite3 as sql
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.config import Config
Config.set('graphics', 'resizable', True)
import webbrowser
from kivy.utils import get_color_from_hex
from pytube import YouTube
import os
###############################DATA BACE (MARK STORE) AND (TASK APP)######################################
'''
import sqlite3 as sql
con=sql.connect('seenivasan.db')
cur=con.cursor()
cur.execute("""CREATE TABLE ugstudent(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
	        ugsem text,
			ugexam text,
			ugsub1 text,
			ugsub2 text,
			ugsub3 text,
			ugsub4 text,
			ugsub5 text,
			ugsub6 text,
			ugtotal text)
            """)
############################TASK APP################################################
cur.execute("""CREATE TABLE studen(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
	        title text,
			task text)
            """)
#####################################################################################
cur.execute("""CREATE TABLE pgstudent(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
	        pgsem text,
			pgexam text,
			pgsub1 text,
			pgsub2 text,
			pgsub3 text,
			pgsub4 text,
			pgsub5 text,
			pgsub6 text,
			pgtotal text)
            """)
con.commit()
con.close()
'''

##################################################################3#########################################################

helpstr = '''
ScreenManager:
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import F kivy.factory.Factory
#:import Factory kivy.factory.Factory
    
    WelcomeScreen:
    UsernameScreen:
    MainScreen:
    Hello1:###homescreen###
    General:#####general use#####
    Biodata:####doidata####
    Main:####biodata####
    Student:
    It:
    Btn:
    It1:
    Btn1:
    Youtub:####YouTube downloader#####
##########TASK RENINDER###############
    To:
    Task:
    Todo:   
<WelcomeScreen>:
    name : 'welcomescreen'
    MDLabel:
        text:'WELCOME TO OUR APP...'
        font_size:60
        underline:True
        color:'#fe0000'
        bold:True
        halign: 'center'
        outline_color:'#000000' 
		outline_width:3
        pos_hint : {'center_y':0.85}
    MDIconButton:
        icon: 'apple'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#7FFF00"
        user_font_size : '100sp'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.32}
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:30
        pos_hint:{'center_y' : 0.02}
<UsernameScreen>
    name:'usernamescreen'
    FloatLayout:
		canvas.before:
		    Color:
                rgba: rgba("#FFE4B5")
            Rectangle:
                size: self.size
                pos: self.pos
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button00
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#020700"
        pos_hint: {'center_x':0.9,'center_y':0.1} 
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:60
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:'ENTER YOUR NICK NAME...!'
        font_size:60
        underline:True
        color:'#fe0000'
        bold:True
        outline_color:'#000000' 
		outline_width:3
        halign: 'center'
        pos_hint : {'center_y':0.85}
    MDTextField:
        id:username_text_fied00
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'ENTER YOUR CUTE NAME...'
        underline:True
        bold:True
        user_font_size : '50sp'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#0000CD"
        line_color_focus: '#000000'
        required : True
        
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.35}
        user_font_size: '40sp'
        theme_text_color: "Custom"
        text_color: "#020700"
        on_press: app.check_username00()
    MDLabel:
        text:'          ADD!'
        pos_hint: {'center_x':0.9,'center_y':0.7}
        text_size: self.size
		font_size:25
		color:"#FF4500"
		bold:True
<MainScreen>:
    name : 'mainscreen'
    FloatLayout:
        canvas.before:
            Color:
                rgba: rgba("#98FB98")
            Rectangle:
                size: self.size
                pos: self.pos
                
    MDLabel:
        text:'WELCOME...!'
        font_size:70
        underline:True
        color:'#FFFF00'
        bold:True
        halign: 'center'
        outline_color:'#000000' 
		outline_width:4
        pos_hint : {'center_y':0.88}            
    MDLabel:
        id:profile_name00
        text:'main screen'
        font_style : 'H3'
        theme_text_color: "Custom"
        text_color: "#00000"
        halign : 'center'
        pos_hint : {'center_y':0.6}
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'hello1'
            root.manager.transition.direction = 'down'    
    MDLabel:
        text:'                               GO TO APP'
        font_size:27
        color:'#FF0000'
        bold:True
        pos_hint:{'center_x':0.9,'center_y':0.1}
    MDLabel:
        text:'      CHANGE  NAME'
        font_size:25
        color:'#FF0000'
        bold:True
        pos_hint:{'center_x':0.6,'center_y':0.1}    
        
        
###################HOME SCREN###########################
<Hello1>:
    
    name:'hello1'
    FloatLayout:
        canvas.before:
            Color:
                rgba: rgba("#FFFFE0")
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text: ' -  HOME-'
        font_size: "30sp"
        color:"#0000CD"
        underline:True
        bold:True
        pos_hint : {'center_x':0.9,'center_y':0.85}
    
    MDIconButton:
        icon:'chevron-left'
        user_font_size:'50sp'
        pos_hint:{'x':.0,'y':.0}
        theme_text_color:"Custom"
        text_color:'#000000'
        on_release:
            root.manager.current='mainscreen'
    
    
         
    MDBoxLayout:
        MDBoxLayout:
            orientation: 'vertical'
            MDBoxLayout:
                size_hint:(1,1/5)
            MDBoxLayout:
                orientation: 'vertical'
                padding:10
                spacing:20
                Button:
                    background_color:(0,0,0,0)
                    background_normal:''
                    text:'GENERAL  USE  FOR  YOU !'
                    underline:True
                    bold:True 
                    font_size:27
                    outline_color:'#800000'  
		            outline_width:4
                    canvas.before:
                        Color:
                            rgba:(255/255,165/255,0,1)
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[100]
                
                    on_press: 
                        root.manager.current = 'general'
                        root.manager.transition.direction = 'up'    
                Button:
                    background_color:(0,0,0,0)
                    background_normal:''
                    text:'MY  COLLEGE  DETAILS !'
                    outline_color:'#00000'
                    underline:True
                    bold:True 
                    font_size:27
                    outline_width:4
                    canvas.before:
                        Color:
                            rgba:(255/255,69/255,0,1)
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[100]
                    on_press:
                        root.manager.current = 'main'
                        root.manager.transition.direction = 'down'
                    
                                  
                Button:
                    background_color:(0,0,0,0)
                    background_normal:''
                    text:'YouTube Video Downloader !'
                    font_size:27
                    underline:True
                    bold:True 
                    outline_color:'#FF0000'  
		            outline_width:4
                    canvas.before:
                        Color:
                            rgba:(50/205,205/250,0,1)
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[100]
                    on_press:
                        root.manager.current = 'youtub'
                        root.manager.transition.direction = 'up'
                
                Button:
                    background_color:(0,0,0,0)
                    background_normal:''
                    text:'REMINDER   MY WORK!'
                    color:'#000000'
                    font_size:27
                    underline:True
                    bold:True 
                    outline_color:'#FFFFFF'  
		            outline_width:4
                    canvas.before:
                        Color:
                            rgba:(255/255,255/255,0,1)
                        RoundedRectangle:
                            pos:self.pos
                            size:self.size
                            radius:[100]
                    on_press:
                        root.manager.current = 'to'
                        root.manager.transition.direction = 'up'
                            
                
                
                   
                MDRaisedButton:
                    text:'EXIT=>'
                    bold:True
                    underline:True
                    outline_color:'#000000'
                    font_size:20
                    pos_hint: {'center_x':0.9,'center_y':0.1}
                    #on_release:app.stop()
                    on_release:app.ext()                   
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "USE ANY APPLICATION..."
                        underline:True
                        bold:True
                        elevation: 15
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
    
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                icon: 'book'    
                MDLabel:
                    text: 'Programming!'
                
                    halign: 'center'
                    font_style: 'H5'
                    underline:True
                    bold:True
                    color:'#fe0200'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:     
                        OneLineIconListItem:
                            text: 'Are you learn PYTHON?'
                            on_press:app.open19()
                            IconLeftWidget:
                                icon: 'laptop-windows'
                                
                        OneLineIconListItem:
                            text:'Download PyCharm now!'
                            on_press: app.open20()
                            IconLeftWidget:
                                icon: 'download'               
                        OneLineIconListItem:
                            text: 'Are you learn JAVA?'
                            on_press: app.open21()
                            IconLeftWidget:
                                icon: 'laptop-windows'
                        OneLineIconListItem:
                            text:'Download JAVA NOW!'
                            on_press: app.open22()
                            IconLeftWidget:
                                icon: 'download'        
                        OneLineIconListItem:
                            text:'Are you learn C++?'
                            on_press: app.open23()
                            IconLeftWidget:
                                icon: 'laptop-windows'
                        OneLineIconListItem:
                            text:'Download COAD BOOK NOW!'
                            on_press: app.open24()
                            IconLeftWidget:
                                icon: 'download'        
                                
                MDLabel:
                    text: 'OTHERS!'
                    
                    bold:True
                    underline:True
                    halign: 'center'
                    color:'#fe0200'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]                                               
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Show My 'UG'Mark"
                            on_press:
                                root.manager.current = 'it'
                                root.manager.transition.direction = 'up'
                            IconLeftWidget:
                                icon: 'eye'
                        OneLineIconListItem:
                            text: "Show My 'PG'Mark"
                            on_press:
                                root.manager.current = 'it1'
                                root.manager.transition.direction = 'down'
                            IconLeftWidget:
                                icon: 'eye'
                    
                        OneLineIconListItem:
                            text: 'ANNA UNIVERSITY RESULT '
                            on_press:app.openre()
                            IconLeftWidget:
                                icon: 'book-open-variant'
                                
                                
                        OneLineIconListItem:
                            text: 'Anna University"CGPA"Calculat'
                            on_press:app.opencgpa()
                            IconLeftWidget:
                                icon: 'calculator'
                                                       
                        OneLineIconListItem:
                            text: 'See Anna University Result? '
                            on_press:app.openres()
                            IconLeftWidget:
                                icon: 'youtube'
                                theme_text_color: "Custom"
                                text_color: "#ff0000"
                        OneLineIconListItem:
                            text: 'See Anna University CGPA? '
                            on_press:app.opencgpay()
                            IconLeftWidget:
                                icon: 'youtube'
                                theme_text_color: "Custom"
                                text_color: "#ff0000"
#########################general use##########################
<General>:
    name: 'general'
    FloatLayout:
		canvas.before:
		    Color:
                rgba: rgba("#F5DEB3")
            Rectangle:
                size: self.size
                pos: self.pos
    MDIconButton:
        icon: 'hand-heart'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#ff0000"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: '150sp'
        on_press: on_release: app.show_example_custom_bottom_sheet()
    MDLabel:
        text:'Click Here!'
        underline:True
        bold:True
        pos_hint: {'center_x':0.7,'center_y':0.8}
        font_style: 'H1'
        
    MDIconButton:
        icon: 'home'
        underline:True
        bold:True
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#ffff00"
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'hello1'
            root.manager.transition.direction = 'right'    
<ItemForCustomBottomSheet@OneLineIconListItem>
    
    icon: ""
    IconLeftWidget:
        icon: root.icon
<ContentCustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "1500dp"
    MDToolbar:
        title: '--Commonly used...'
        halign: 'center'
        elevation: 20
        md_bg_color:app.theme_cls.accent_color
        right_action_items: [["heart"]]
        icon_color: 0, 1, 0, 1
    ScrollView:
        bar_width:8
        bar_color:'#ff0000'
        MDGridLayout:
            cols: 3
            adaptive_height: True
            ItemForCustomBottomSheet:
                text: "GO TO Google..."
                bold:True
                on_press: app.open1()
                icon: "google"
            ItemForCustomBottomSheet:
                text: "GO TO YouTube..."
                on_press: app.open2()
                icon: "youtube"
                
            ItemForCustomBottomSheet:
                text: "GO TO FaceBook..."
                on_press: app.open3()          
                icon: "facebook"
            ItemForCustomBottomSheet:
                text: "GO TO Instagram..."
                on_press: app.open4()
                icon: "instagram"
            ItemForCustomBottomSheet:
                text: "GO TO Twitter..."
                on_press: app.open17()
                icon: "twitter"
            ItemForCustomBottomSheet:
                text: "GO TO WhatsApp..."
                on_press: app.open27()
                icon: "whatsapp"
            ItemForCustomBottomSheet:
                text: "GO TO Telegram..."
                on_press: app.open8()
                icon: "telegram"            
            ItemForCustomBottomSheet:
                text: "GO TO Gmail..."
                on_press: app.open8()
                icon: "gmail"
            ItemForCustomBottomSheet:
                text: "Google Translate..."
                on_press: app.open9()
                icon: "translate" 
            ItemForCustomBottomSheet:
                text: "Travel..."
                on_press: app.open10()
                icon: "bus"
            ItemForCustomBottomSheet:
                text: "Google Maps..."
                on_press: app.open11()
                icon: "google-maps"
            ItemForCustomBottomSheet:
                text: "Google Chorme..."
                on_press: app.opench()
                icon: "google-chrome"
            ItemForCustomBottomSheet:
                text: "Google Assistant..."
                on_press: app.openas()
                icon: "google-assistant"
            ItemForCustomBottomSheet:
                text: "Google Cloud..."
                on_press: app.opencl()
                icon: "google-cloud"
            ItemForCustomBottomSheet:
                text: "Google Drive..."
                on_press: app.opendr()
                icon: "google-drive"    
            ItemForCustomBottomSheet:
                text: "Google Play..."
                on_press: app.openpl()
                icon: "google-play"
            ItemForCustomBottomSheet:
                text: "Google Lens..."
                on_press: app.open15()
                icon: "google-lens"                    
            ItemForCustomBottomSheet:
                text: "amazon..."
                on_press: app.open15()
                icon: "amazon"    
            ItemForCustomBottomSheet:
                text: "Train Tickets Booking..."
                on_press: app.open12()
                icon: "train"
            ItemForCustomBottomSheet:
                text: "Bus Tickets Booking..."
                on_press: app.open13()
                icon: "bus-stop"
            ItemForCustomBottomSheet:
                text: "Car Tickets Booking..."
                on_press: app.open14()
                icon: "car"
            ItemForCustomBottomSheet:
                text: "Hostor..."
                on_press: app.openh()
                icon: "star"
            ItemForCustomBottomSheet:
                text: "Live TV..."
                on_press: app.open16()
                icon: "television-classic"
            ItemForCustomBottomSheet:
                text: "Movies..."
                on_press: app.opena()
                icon: "movie-open"                                               
            ItemForCustomBottomSheet:
                text: "Comedy Videos..."
                on_press: app.open5()
                icon: "youtube"                   
            ItemForCustomBottomSheet:
                text: "Video Songs..."
                on_press: app.open6()
                icon: "video"
            ItemForCustomBottomSheet:
                text: "Audio Songs..."
                on_press: app.openau()
                icon: "music"    
            ItemForCustomBottomSheet:
                text: "Dance Videos..."
                on_press: app.open18()
                icon: "human-female-dance"
            ItemForCustomBottomSheet:
                text: "Sports Videos..."
                on_press: app.openS1()
                icon: "hockey-sticks"
            ItemForCustomBottomSheet:
                text: "Cooking Videos..."
                on_press: app.open7()
                icon: "food"
####################################bio data##########################################3######
<Biodata>:
    name :'bio'
    MDFloatingActionButton:
        icon: 'arrow-left'
        
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '43sp'
        on_press:
            root.manager.current = 'hello1'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '43sp'
        on_press:
            root.manager.current = 'main'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:50
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:'YOUR BIODATAS...'
        font_style: 'H2'
        halign: 'center'
        color:'#ff0000'
        outline_color:'#000000' 
		outline_width:2
		underline:True
        pos_hint : {'x':.0,'y':.435}
    MDLabel:
		text:'____________________________________'
		font_size:50
		pos_hint:{'x':.0,'y':.400}
		color:0,0,0,1
		bold:True    
         
    MDTextField:
        id:username_text1
        pos_hint: {'center_x':0.5,'center_y':0.8}
        size_hint: (0.7,0.1)
        hint_text : 'NAME'
        helper_text: 'please enter your name friend!'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:username_text2
        pos_hint: {'center_x':0.5,'center_y':0.7}
        size_hint: (0.7,0.1)
        hint_text : 'COLLEGE NAME'
        helper_text: 'please enter your college name! '
        helper_text_mode: 'on_error'
        icon_right: 'home'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        required : True
   
    MDTextField:
        id:username_text3
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'Department & section'
        helper_text: 'please enter Department & section! '
        helper_text_mode: 'on_error'
        icon_right:'book-account'
        mode: "rectangle" 
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:username_text4
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: (0.7,0.1)
        hint_text : 'Valid upto?'
        helper_text: 'please enter your Duration of studey! '
        helper_text_mode: 'on_error'
        icon_right: 'calendar'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:username_text5
        pos_hint: {'center_x':0.5,'center_y':0.4}
        size_hint: (0.7,0.1)
        hint_text : 'Studying UG(or)PG'
        helper_text: 'please enter your Studying! '
        helper_text_mode: 'on_error'
        icon_right: 'school'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:username_text6
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint: (0.7,0.1)
        hint_text : 'Your Exam Number'
        helper_text: 'please enter your Exam number! '
        helper_text_mode: 'on_error'
        icon_right: 'pen'
        mode: "rectangle"
        required : True 
        icon_right_color: app.theme_cls.primary_color
                               
    MDFloatingActionButton:
        icon:'account-plus'
        icon_color:'#0040ff'
        pos_hint: {'center_x':0.5,'center_y':0.18}
        user_font_size: '40sp'
        on_press: app.check()
<Main>:
    name : 'main'
    MDFloatingActionButton:
        icon: 'arrow-left'
        
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '40sp'
        on_press:
            root.manager.current = 'bio'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        icon: 'arrow-right'
        
        pos_hint: {'center_x':0.9,'center_y':0.1}
        theme_text_color: "Custom"
        text_color: '#020700'
        user_font_size : '40sp'
        on_press:
            root.manager.current = 'student'
            root.manager.transition.direction = 'down'
    MDFloatingActionButton:
        icon: 'home'
        
        pos_hint: {'center_x':0.5,'center_y':0.1}
        theme_text_color: "Custom"
        text_color: '#FF0000'
        user_font_size : '40sp'
        on_press:
            root.manager.current = 'hello1'
            root.manager.transition.direction = 'down'                
    
    MDLabel:
        text:'HOME'
        underline:True
        bold:True
        pos_hint:{'center_x':0.9,'center_y':0.1}
    MDLabel:
        #text:'Change'
        text:
            """Change 
            .   Bio"""
        underline:True
        bold:True
        pos_hint:{'center_x':0.5,'center_y':0.1}
        
    MDLabel:
        text:'                                                                           GO Inside'
        
        bold:True
        pos_hint:{'center_x':0.9,'center_y':0.1} 
    MDLabel:
        text:'MY BIODATAS...'
        font_style: 'H2'
        outline_color:'#000000' 
		outline_width:2
        color:'#0040ff'
        underline:True
        halign: 'center'
        pos_hint : {'x':.0,'y':.435}
    Label:
		text:'____________________________________'
		font_size:50
		pos_hint:{'x':.0,'y':.400}
		color:0,0,0,1
		bold:True    
    MDLabel:
        id:profile1
        icon_right: 'pen'
        font_style : 'H4'
        pos_hint : {'center_x':0.6,'center_y':0.8}
    MDLabel:
        id:profile2
        font_style : 'H4'
        pos_hint : {'center_x':0.6,'center_y':0.7}
    MDLabel:
        id:profile3
        font_style : 'H4'
        pos_hint : {'center_x':0.6,'center_y':0.6}
    MDLabel:
        id:profile4
        font_style : 'H4'
        pos_hint : {'center_x':0.6,'center_y':0.5}  
    MDLabel:
        id:profile5
        font_style : 'H4'
        pos_hint : {'center_x':0.6,'center_y':0.4}
              
    MDLabel:
        id:profile6
        font_style : 'H4'
        pos_hint : {'center_x':0.6,'center_y':0.3}        
    Label:
		text:'____________________________________'
		font_size:50
		pos_hint:{'x':.0,'y':-.300}
		color:0,0,0,1
		bold:True
#######################################################Mark stor############################################
<Student>:
    name : 'student'
    FloatLayout:
		canvas.before:		
			Rectangle:
				size:self.size
				pos:self.pos
				source:'i.png'
		MDFloatLayout:
            pos_hint:{'x':0.050,'y':.010}
            size_hint:.1000,.0
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#0304ff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#fbea3b')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
    MDFloatingActionButton:
        icon:'home'
        color:255/255, 255/255, 19/255,1
        md_bg_color:app.theme_cls.primary_color
        #pos_hint: {'center_x':0.1,'center_y':0.1}
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'hello1'
            root.manager.transition.direction = 'right'
    MDIconButton:
        icon:'chevron-left'
        user_font_size:'70sp'
        #pos_hint: {'center_x':0.9,'center_y':0.1}
        pos_hint: {'center_x':0.1,'center_y':0.1}
        theme_text_color:"Custom"
        text_color:'#FFFF00'
        on_release:
            root.manager.current='main'
    MDLabel:
		text:'<= UG STUDENT '
		font_size:30
		pos_hint:{'x':.6,'y':.200}
		color:'#fe0112'
		bold:True
		outline_color:'#FFFF00'  
		outline_width:4    
		
	MDImageButton:
		source:'student1.png'
		font_color:0,0,0,1
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.3,'y':.6}
		back_color:(0,0,0,1)
		on_press:
			root.manager.current='it'
			root.manager.transition.direction='up'
	MDImageButton:
		source:'student1.png'
		font_color:0,0,0,1
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.3,'y':.20}
		back_color:'#fe0112'
		on_press:
			root.manager.current='it1'
			root.manager.transition.direction='down'
	MDLabel:
		text:'<= PG STUDENT '
		font_size:30
		pos_hint:{'x':.6,'y':-.195}
		color:'#fe0112'
		bold:True
		outline_color:(0,0,0,1)  
		outline_width:5  
		
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "    SAVE YOUR 'UG'MARKS (or) 'PG'MARKS"
                        elevation: 15
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        md_bg_color:app.theme_cls.accent_color
                        right_action_items: [["book-open-variant"]]
    
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                icon: 'book'    
                MDLabel:
                    text: ' Engineering...'
                    underline:True
                    bold:True
                    halign: 'center'
                    font_style: 'H5'
                    color:'#fe0200'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    bar_color:'#FF1493'
                    MDList:     
                        OneLineIconListItem:
                            text: 'ENGINEERING SYLLABUS...'
                            on_press:app.open45()
                            IconLeftWidget:
                                icon: 'book-account'
                                
                                
                        OneLineIconListItem:
                            text:'ENGINEERING BOOKS...'
                            on_press: app.open44()
                            IconLeftWidget:
                                icon: 'book-open-variant'               
                        OneLineIconListItem:
                            text: 'ENGINEERING QUSTION BANK...'
                            on_press: app.open43()
                            IconLeftWidget:
                                icon: 'text-box'
                        OneLineIconListItem:
                            text:'ENGINEERING DETAILS...'
                            on_press: app.open42()
                            IconLeftWidget:
                                icon: 'youtube'
                                theme_text_color: "Custom"
                                text_color: "#ff0000"        
                                    
                                
                MDLabel:
                    text: 'Arts...'
                    underline:True
                    halign: 'center'
                    color:'#0000FF'
                    bold:True
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]                                               
                ScrollView:
                    bar_color:'#FF1493'
                    MDList:
                        OneLineIconListItem:
                            text: 'Arts syllabus...'
                            on_press:app.open50()
                            IconLeftWidget:
                                icon: 'book-account'
                                  
                        OneLineIconListItem:
                            text: 'Arts Books...'
                            on_press:app.open41()
                            IconLeftWidget:
                                icon: 'book-open-variant'
                                             
                        OneLineIconListItem:
                            text: 'Arts Question Bank...'
                            on_press:app.open40()
                            IconLeftWidget:
                                icon: 'text-box'
                                
                        OneLineIconListItem:
                            text: 'Arts Details...'
                            on_press:app.open49()
                            IconLeftWidget:
                                icon: 'youtube'
                                theme_text_color: "Custom"
                                text_color: "#ff0000"
                                        
                MDLabel:
                    text: 'BARAMETICAL...'
                    bold:True
                    underline:True
                    halign: 'center'
                    color:'#008000'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]                                               
                ScrollView:
                    bar_color:'#FF1493'
                    MDList:
                        OneLineIconListItem:
                            text: 'BARAMETICAL SYLLABUS...'
                            on_press:app.open48()
                            IconLeftWidget:
                                icon: 'book-account'
                                  
                        OneLineIconListItem:
                            text: 'BARAMETICAL Books...'
                            on_press:app.open47() 
                            IconLeftWidget:
                                icon: 'book-open-variant'
                                            
                        OneLineIconListItem:
                            text: 'BARAMETICAL Question Bank...'
                            on_press:app.open46()
                            IconLeftWidget:
                                icon: 'text-box'
                                
                        OneLineIconListItem:
                            text: 'BARAMETICAL Details...'
                            on_press:app.open39()
                            IconLeftWidget:
                                icon: 'youtube'
                                theme_text_color: "Custom"
                                text_color: "#ff0000"
        
                                                
	MDLabel:
		text:'(OR) '
		font_size:45
		color:'#02ff02'
		bold:True
		pos_hint:{'x':.4,'y':.0}
		outline_color:(0,0,0,1)  
		outline_width:3		
           
	#MDLabel:
		#text:'WELCOM GRADUATE...'
		#font_size:45
		#pos_hint:{'x':.2,'y':.445}		
		#bold:True
		#outline_color:'#04ff01' 
		#outline_width:2
	#Label:
	#	text:'________________________'
	#	font_size:65
	#	pos_hint:{'x':.0,'y':.425}
	#	color:'#ff0604'
	#	bold:True
        
    
<It>:
    name: 'it'
    date:date
    container: container
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'o.png'
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#FF4500')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		MDFloatLayout:
            pos_hint:{'x':0.50,'y':.10}
            size_hint:.100,.0
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffff13')
                    #rgba:get_color_from_hex('#FF4500')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
	MDLabel:
		text:"MY 'UG' MARKS DETAILS..."
		font_size:45
		pos_hint:{'x':.2,'y':.445}
		bold:True
		#italic:True
		outline_color:'#fff715' 
		outline_width:2
	Label:
		text:'________________________'
		font_size:65
		pos_hint:{'x':.0,'y':.425}
		color:'#0e0100'
		bold:True
    
        
	MDBoxLayout:
		#orientation:'horizontal'
		MDFloatLayout:
			size_hint:.30,.75
			pos_hint:{'x':0,'y':.10}
			canvas.before:
                Color:
                    rgba:get_color_from_hex('#fffebb')
                    #rgba:get_color_from_hex('#fff5ed')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
            Label:
            	text:'SOME INSTRUCTIONS.'
            	pos_hint:{'x':.35,'y':.81}
            	color:'#2443e6'
            	outline_color:'#040204' 
            	bold:True
				size_hint: None,None
            	markup:True
            	underline:True
            	font_size:23
            MDLabel:
            	text:
            	    """1.PLEASE REFRESH YOURSELF FIRST."""
            	pos_hint:{'x':.1,'y':.77}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
            MDLabel:
            
            	text:
            	    """2.CLICK THE 'ADD' BUTTON AND\n 
            	    ENTER YOUR GOOD MARK."""
            	pos_hint:{'x':.1,'y':.63}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
			MDLabel:
            	text:
            	    """3.THEN 'REFRESH' AND YOUR MARK\n 
            	    WILL BE VISIBLE ON THE SCREEN."""
            	pos_hint:{'x':.1,'y':.50}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
			MDLabel:
            	text:
            	    """4.IF THERE IS ANY MISTAKE,\n
            	    'DELETE'  AND  'REFRESH'."""
            	pos_hint:{'x':.1,'y':.34}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
			MDLabel:
            	text:'         THANKS FRIENDS...'
            	pos_hint:{'x':.1,'y':.25}
				color:"#fe0200"
				bold:True
				text_size: self.size
				font_size:20			
            MDLabel:
			    text:'====================================='
			    pos_hint:{'x':.0,'y':-.31}
			    #underline:True	
			    color:'#000700'
			MDLabel:
            	text:'ADD!'
            	underline:True
            	pos_hint:{'x':.0,'y':.10}
				color:"#000000"
				bold:True
				text_size: self.size
				font_size:20
			MDLabel:
            	text:'Refresh!'
            	underline:True
            	pos_hint:{'x':.4,'y':.1}
				color:"#000000"
				bold:True
				text_size: self.size
				font_size:20
            MDLabel:
                id:date
                text:"     "
                pos_hint:{'x':-.0,'y':-.6}
        
                font_size:25
                bold:True
                color:'#FFFF00'
                outline_color:'#000000' 
		        outline_width:2
		ScrollView:
            size_hint: (.4, .73)
			pos_hint:{'x':.4,'y':.12}
            #bar_inactive_color:
            	#get_color_from_hex('00640')
            bar_color:
            	get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:10
			GridLayout:
				id:container
				cols:1
				height:self.minimum_height
				row_default_height:300
				size_hint_y:None
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#020700"
        user_font_size : '35sp'
	    pos_hint:{'x':.07,'y':.12}
		on_release:
			Factory.custompopup().open()
	MDFloatingActionButton:
        icon:'refresh'
        theme_text_color: "Custom"
        #text_color: "#ffff00"
        user_font_size : '37sp'	
		pos_hint:{'x':.27,'y':.12}
		on_release:
			root.add_text_inputs()
	
	MDIconButton:
        icon: 'backspace'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FFFF00"
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '35sp'
        on_press:
            root.manager.current = 'student'
            root.manager.transition.direction = 'right'
<custompopup@Popup>:
	ugsem:ugsem
	ugexam:ugexam
	ugsub1:ugsub1
	ugsub2:ugsub2
	ugsub3:ugsub3
	ugsub4:ugsub4
	ugsub5:ugsub5
	ugsub6:ugsub6
	ugtotal:ugtotal
	size_hint:.9,.9
	separator_height: 0
	background_color:0,0,0,0.4
	border: (1, 1, 1, 1)
	MDFloatLayout:
		canvas.before:
			Color:
				rgba:get_color_from_hex('#ffffff')
			Rectangle:
				size:self.size
				pos:self.pos
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#0102ff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		MDImageButton:
			source:'student1.png'
			size_hint_y:.35
			size_hint_x:.35
			pos_hint:{'x':.3,'y':.7}
		MDBoxLayout:
			pos_hint:{'x':.0,'y':.0}          
            size_hint:1,.71
            #title:'seeni'
			orientation:'horizontal'
			color:'#0102ff'
			ScrollView:
				bar_width:10
				#size_hint: (.10, .73)
				bar_color:
            	    get_color_from_hex('#ff0000')
				GridLayout:
				    
					cols:1
					height:self.minimum_height
					row_default_height:60
					size_hint_y:None
					MDLabel:
						text:'WHICH YEAR?-WHICH SEMESTER?'
						font_size:35
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						underline_color:'#020101'
						color:get_color_from_hex('#ff0206')
					MDLabel:
						text:'ENTER YOUR ANSWER!'
						halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugsem
						hint_text: '   YEAR! - SEMESTER!'
						font_size:30
						multiline:False
						size_hint: (0.7,0.1)
						mode: "rectangle"
						helper_text_mode: 'on_error'
						icon_right: 'calendar'
					    required : True
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:35
					MDLabel:
					MDLabel:
						text:'WHICH EXAM?'
						font_size:35
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						underline_color:'#030000'
						color:get_color_from_hex('#ff0206')
					MDLabel:
						text:'ENTER YOUR EXAM!?'
						halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugexam
						hint_text: '  INTERNAL! (OR) SEMESTER!'
						multiline:False
						size_hint: (0.7,0.1)
						icon_right: 'text-box'
						required : True
						color:'#fe0200'
						mode: "rectangle"
						color:0,0,0,1
						#size_hint:1,.35
						helper_text_mode: 'on_error'
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					MDLabel:
						text:"YOUR 'SUBJECT' and 'MARK'!"
						font_size:35
						halign: 'center'
						#color:'#020101'
						text_size:self.size
						underline:True
						color:get_color_from_hex('#21b68a')
					MDLabel:
						text:'SUBJECT 1'
						halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugsub1
						hint_text: 'SUBJECT 1 = MARK'
						size_hint: (0.7,0.1)
						mode: "rectangle"
						icon_right: 'book-open-variant'
						required : True
						helper_text_mode: 'on_error'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'SUBJECT 2'
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugsub2
						hint_text: 'SUBJECT 2 = MARK'
						size_hint: (0.7,0.1)
						helper_text_mode: 'on_error'
						required : True
                        icon_right: 'book-open-variant'
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'SUBJECT 3'
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugsub3
						hint_text: 'SUBJECT 3 = MARK'
						size_hint: (0.7,0.1)
						helper_text_mode: 'on_error'
						required : True
                        icon_right: 'book-open-variant'
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'SUBJECT 4'
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugsub4
						hint_text: 'SUBJECT 4 = MARK'
						size_hint: (0.7,0.1)
						helper_text_mode: 'on_error'
                        icon_right: 'book-open-variant'
                        required : True
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'SUBJECT 5'
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugsub5
						hint_text: 'SUBJECT 5 = MARK'
						size_hint: (0.7,0.1)
						helper_text_mode: 'on_error'
						required : True
                        icon_right: 'book-open-variant'
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:' are you enginnering or medical use this box'
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugsub6
						hint_text: 'SUBJECT 6 = MARK'
						size_hint: (0.7,0.1)
						helper_text_mode: 'on_error'
                        icon_right: 'book-open-variant'
                        mode: "rectangle"
						#halign: 'center'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					MDLabel:
						text:'ENTER YOUR GOOD MAEK!'
						font_size:35
						halign: 'center'
						#color:'#020101'
						text_size:self.size
						underline:True
						color:get_color_from_hex('#21b68a')
					MDLabel:
						text:'MY MARK IS'
						halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:ugtotal
						text:'TOTAL MARK IS= '
						required : True
						size_hint: (0.7,0.1)
						color:'	#ff0000'
						helper_text_mode: 'on_error'
                        icon_right: 'comment'
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':0,'y':.5}
						#background_color:0,0,0,0
						font_size:35
					MDLabel:
					MDFillRoundFlatButton:
						text:'SAVE MY DATAS'
						font_size:"25sp"
						mode: "rectangle"
						md_bg_color:app.theme_cls.primary_color
                        theme_text_color: "Custom"
                        text_color: "#80ff00"
						size_hint:.7,.7
						on_press:app.add_user(ugsem.text,ugexam.text,ugsub1.text,ugsub2.text,ugsub3.text,ugsub4.text,ugsub5.text,ugsub6.text,ugtotal.text)
						#background_color:get_color_from_hex('#a4ff12')
						on_release:
							root.dismiss()
					MDLabel:
<Btn>:
    name : 'btn'
    #title:'seeni'
    r1:''
	r2:''
	r3:''
	r4:''
	r5:''
	r6:''
	r7:''
	r8:''
	r9:''
	data:''
	data_id:''
	FloatLayout:
	    
		MDCard:
		    #outline_color:"#ff0000" 
			focus_behavior:True
        	ripple_behavior: True
			#focus_behavior: True
	        orientation: "vertical"  
		
	        padding: "10dp"
	        
	        size_hint: None, None
	        size: "280dp", "290dp"
	        pos_hint: {"center_x": .5, "center_y": .5}
	               
	        MDLabel:
	            text: root.r1
	            font_size:20
	            halign: 'center'
	            #color:'#fd0104'
	            
	        #MDSeparator:
	         #   height: "2dp"
	          #  halign: 'center'           
			MDLabel:
	            text: root.r2
	            font_size:20
	            color:'#fd0104'
	            halign: 'center'
	        MDSeparator:
	            height: "2dp"
	            color:'#000200' 
	        MDLabel:
	            text:"SUBJECT'S"
	            underline:True
	            halign: 'center'        
	        MDLabel:
	            text: root.r3
	        MDLabel:
	            text: root.r4  
	        MDLabel:
	            text: root.r5
	        MDLabel:
	            text: root.r6
	        MDLabel:
	            text: root.r7
	        MDLabel:
	            text: root.r8    
	        MDSeparator:
	            height: "4dp"
	            color:'#0101ff'
	        MDLabel:
	         #text: 'YOUR GOOG PERCENTAGE'
	          #  underline:True
	           # halign: 'center'
	            #color:'#0101ff'
	           
	        MDLabel:
	            text: root.r9
	            color:'#ff0000'   
            MDSeparator:
	            height: "3dp"
	            color:'#0101ff'
	    MDIconButton:
			icon:"delete"
			pos_hint:{'x':.70,'y':.0}
			on_release:root.delete()    								
            on_release:app.opp2()
<It1>:
    name: 'it1'
    date:date
    container: container
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'p.png'
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#fb02ca')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		MDFloatLayout:
            pos_hint:{'x':0.50,'y':.10}
            size_hint:.100,.0
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
	MDLabel:
		text:"MY 'PG' MARKS DETAILS..."
		font_size:45
		pos_hint:{'x':.2,'y':.445}
		color:
		bold:True
		#italic:True
		outline_color:'#0102ca' 
		outline_width:2
	Label:
		text:'________________________'
		font_size:65
		pos_hint:{'x':.0,'y':.425}
		color:0,0,0,1
		bold:True
	MDBoxLayout:
		#orientation:'horizontal'
		FloatLayout:
			size_hint:.30,.75
			pos_hint:{'x':0,'y':.10}
			canvas.before:
                Color:
                	rgba:get_color_from_hex('#fcbbff')
                    #rgba:get_color_from_hex('#f98b88')
                    #rgba:get_color_from_hex('#fff5ed')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
            Label:
            	text:'SOME INSTRUCTIONS.'
            	pos_hint:{'x':.35,'y':.81}
            	color:'#2443e6'
            	outline_color:'#040204' 
            	bold:True
				size_hint: None,None
            	markup:True
            	underline:True
            	font_size:23
            MDLabel:
            	text:
            	    """1.PLEASE REFRESH YOURSELF FIRST."""
            	pos_hint:{'x':.1,'y':.77}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
            MDLabel:
            
            	text:
            	    """2.CLICK THE 'ADD' BUTTON AND\n 
            	    ENTER YOUR GOOD MARK."""
            	pos_hint:{'x':.1,'y':.63}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
			MDLabel:
            	text:
            	    """3.THEN 'REFRESH' AND YOUR MARK\n 
            	    WILL BE VISIBLE ON THE SCREEN."""
            	pos_hint:{'x':.1,'y':.50}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
			MDLabel:
            	text:
            	    """4.IF THERE IS ANY MISTAKE,\n
            	    'DELETE' AND  'REFRESH'."""
            	pos_hint:{'x':.1,'y':.34}
				color:0,0,0,1
				bold:True
				text_size: self.size
				font_size:15
			MDLabel:
            	text:'         THANKS FRIENDS...'
            	pos_hint:{'x':.1,'y':.25}
				color:"#fe0200"
				bold:True
				text_size: self.size
				font_size:20
			MDLabel:
			    text:'====================================='
			    pos_hint:{'x':.0,'y':-.31}
			    #underline:True	
			    color:'#000700'
			MDLabel:
            	text:'ADD!'
            	underline:True
            	pos_hint:{'x':.0,'y':.10}
				color:"#000000"
				bold:True
				text_size: self.size
				font_size:20
			MDLabel:
            	text:'Refresh!'
            	underline:True
            	pos_hint:{'x':.4,'y':.1}
				color:"#000000"
				bold:True
				text_size: self.size
				font_size:20	
			MDLabel:
                id:date
                text:"     "
                pos_hint:{'x':-.0,'y':-.6}
        
                font_size:25
                bold:True
                color:'#FFFF00'
                outline_color:'#000000' 
		        outline_width:2		
		ScrollView:
            size_hint: (.4, .73)
			pos_hint:{'x':.4,'y':.12}
            #bar_inactive_color:
            	#get_color_from_hex('00640')
            bar_color:
            	get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:10
			GridLayout:
				id:container
				cols:1
				height:self.minimum_height
				row_default_height:300
				size_hint_y:None
    
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#ffff00"
        user_font_size : '35sp'
	    pos_hint:{'x':.07,'y':.12}
		on_release:
			Factory.custompopup2().open()
	MDFloatingActionButton:
        icon:'refresh'
        color:'#71fb08'
        user_font_size : '40sp'	
		pos_hint:{'x':.27,'y':.12}
		on_release:
			root.add_text_inputs1()
    MDFloatingActionButton:
        icon: 'backspace'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FF0000"
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '35sp'
        on_press:
            root.manager.current = 'student'
            root.manager.transition.direction = 'right'
	
<custompopup2@Popup>:
	pgsem:pgsem
	pgexam:pgexam
	pgsub1:pgsub1
	pgsub2:pgsub2
	pgsub3:pgsub3
	pgsub4:pgsub4
	pgsub5:pgsub5
	pgsub6:pgsub6
	pgtotal:pgtotal
	size_hint:.9,.9
	separator_height: 0
	background_color:0,0,0,0.4
	border: (1, 1, 1, 1)
	FloatLayout:
		canvas.before:
			Color:
				rgba:get_color_from_hex('#ffffff')
			Rectangle:
				size:self.size
				pos:self.pos
		FloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		MDImageButton:
			source:'student1.png'
			size_hint_y:.35
			size_hint_x:.35
			pos_hint:{'x':.3,'y':.7}	
		MDBoxLayout:
			pos_hint:{'x':.0,'y':.0}          
            size_hint:1,.71
			orientation:'horizontal'
			ScrollView:
			    
				bar_width:10
				bar_color:
            	    get_color_from_hex('#0040ff')
				color:'#ffff00'
				GridLayout:
					cols:1
					height:self.minimum_height
					row_default_height:60
					size_hint_y:None
                    MDLabel:
						text:'WHICH YEAR?-WHICH SEMESTER?'
						font_size:35
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#0040ff')
					MDLabel:
						text:'ENTER YOUR ANSWER!'
						halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgsem
						hint_text: '   YEAR!- SEMESTER!'
						size_hint: (0.7,0.1)
						mode: "rectangle"
						helper_text_mode: 'on_error'
						required : True
						icon_right: 'calendar'
						
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					MDLabel:
						text:'WHICH EXAM?'
						font_size:35
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#0040ff')
					MDLabel:
						text:'ENTER YOUR EXAM?'
						halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgexam
						hint_text: 'INTERNAL! (OR) SEMESTER!'
						underline:True
						size_hint: (0.7,0.1)
						mode: "rectangle"
						helper_text_mode: 'on_error'
						icon_right: 'text-box'
						required : True
						
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					MDLabel:
						text:"YOUR 'SUBJECT' and 'MARK'"
						font_size:35
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#21b68a')
					MDLabel:
						text:'SUBJECT 1'
						halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgsub1
						hint_text: 'SUBJECT 1 = MARK'
						size_hint: (0.7,0.1)
						mode: "rectangle"
						icon_right: 'book-open-variant'
						helper_text_mode: 'on_error'
						required : True
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					Label:
					    text:'SUBJECT 2'
					    halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgsub2
						hint_text: 'SUBJECT 2 = MARK'
						size_hint: (0.7,0.1)
						mode: "rectangle"
						helper_text_mode: 'on_error'
						icon_right: 'book-open-variant'
						required : True
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'SUBJECT 3'
					    halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgsub3
						hint_text: 'SUBJECT 3 = MARK'
						size_hint: (0.7,0.1)
						mode: "rectangle"
						icon_right: 'book-open-variant'
						helper_text_mode: 'on_error'
						required : True
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'SUBJECT 4'
					    halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgsub4
						hint_text: 'SUBJECT 4 = MARK'
						size_hint: (0.7,0.1)
						mode: "rectangle"
						icon_right: 'book-open-variant'
						helper_text_mode: 'on_error'
						required : True
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'SUBJECT 5'
					    halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgsub5
						hint_text: 'SUBJECT 5 = MARK'
						multiline:False
						size_hint: (0.7,0.1)
						mode: "rectangle"
						icon_right: 'book-open-variant'
						helper_text_mode: 'on_error'
						required : True
						#color:0,0,0,1
						#size_hint:1,.35
					    #size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					    text:'are you enginnering or medical use this box'
					    halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgsub6
						hint_text: 'SUBJECT 6 = MARK'
						size_hint: (0.7,0.1)
						mode: "rectangle"
						#helper_text_mode: 'on_error'
						#required : True
						icon_right: 'book-open-variant'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					MDLabel:
						text:'ENTER YOUR GOOD MARK!'
						font_size:35
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#21b68a')
					MDLabel:
						text:'YOUR MARK'
						halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:.2,.2
					MDTextField:
						id:pgtotal
						text:'TOTAL MARK IS= '
			            size_hint: (0.7,0.1)
						mode: "rectangle"
						icon_right: 'comment'
						helper_text_mode: 'on_error'
						required : True
						multiline:False
						#color:'#fd0307'
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:30
					MDLabel:
					
					MDFillRoundFlatButton:
						text:'SAVE MY DATAS'
						font_size:"25sp"
						size_hint:.7,.7
						theme_text_color: "Custom"
                        text_color: "#ffff00"
						on_press:app.add(pgsem.text,pgexam.text,pgsub1.text,pgsub2.text,pgsub3.text,pgsub4.text,pgsub5.text,pgsub6.text,pgtotal.text)
						#background_color:get_color_from_hex('#00a572')
						on_release:
							root.dismiss()
					MDLabel:
<Btn1>:
    name : 'btn1'
    a1:''
	a2:''
	a3:''
    a4:''
	a5:''
	a6:''
	a7:''
	a8:''
	a9:''
	data:''
	data_id:''
	FloatLayout:
		MDCard:
		    id:a1
			focus_behavior:True
        	ripple_behavior: True
			#focus_behavior: True
	        orientation: "vertical"
	        padding: "6dp"
	        size_hint: None, None
	        size: "280dp", "290dp"
	        pos_hint: {"center_x": .5, "center_y": .5}
	        MDLabel:
	            text: root.a1
	            font_size:20
	            color:'#000000'
	            halign: 'center'
	            font_size:20
	          
	        #MDSeparator:
	         #   height: "1dp"
	          #  halign: 'center'              
			MDLabel:
	            text: root.a2
	            font_size:20
	            halign: 'center'
	            color:'#1208ff'
	        MDSeparator:
	            height: "2dp"
	            color:'#000000' 
	        MDLabel:
	            text:"SUBJECT'S"
	            underline:True
	            halign: 'center'    
	        MDLabel:
	            text: root.a3
	        MDLabel:
	            text: root.a4  
	        MDLabel:
	            text: root.a5
	        MDLabel:
	            text: root.a6
	        MDLabel:
	            text: root.a7
	        MDLabel:
	            text: root.a8
	        MDSeparator:
	            height: "4dp"
	            color:'#ed0805'
	        MDLabel:
	         #   text: 'YOUR GOOG PERCENTAGE'
	          #  underline:True
	           # halign: 'center'
	            #color:'#ed0805' 
	        MDLabel:
	            text: root.a9    
	        MDSeparator:
	            height: "3dp"
	            color:'#ed0805'        
        MDIconButton:
			icon:"delete"
			pos_hint:{'x':.70,'y':.0}
			on_release:root.delete()
            on_release:app.opp2()
########################################YOUTUBE VIDEO DOWNLOADER###########################################
<Youtub>:
    name:'youtub'
    FloatLayout:
        canvas.before:
            Color:
                rgba: rgba("#FFE4E1")
            Rectangle:
                size: self.size
                pos: self.pos
    Label:
        text: "YouTube Videos Downloader..."
        underline:True
        size_hint: [None, None]
        size: self.texture_size
        pos_hint: {"top":0.94, "center_x":0.5}
        font_size: "27sp"
        bold: True
        canvas.before:
            Color:
                rgba: rgba("#ff0000")
            Rectangle:
                size: self.size
                pos: self.pos
    MDTextFieldRect:
        id: url
        helper_text_mode: 'on_error'
        hint_text: "Only enter YouTube Video url"
        background_color: [1,1,1,1]
        pos_hint: {'center_x':0.5,'center_y':0.8}
        color: [0,0,0,1]
        bold: True
        font_size: "20sp"
        multiline: False
        size_hint: [0.85, 0.06]    
    MDLabel:
        text:'   click download!'
        pos_hint:{'center_x':0.9,'center_y':0.6}
        font_size: "20sp"
        color: "#ff0080" 
        underline:True
    MDIconButton:
        id:ss
        icon:'download'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#03ff00"
        user_font_size: '40sp'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: app.yturl()
    MDRoundFlatIconButton:    
        id:vid
        disabled: True
        bold:True
        icon: "video"
        text: "Download-Video"
        text_color:"#010000"
        line_color: "#05fa00"
        color: 1, 1, 1, 1
        font_size: "25sp"
        pos_hint: {'center_x':0.5,'center_y':0.4}
        #size_hint: [0.3, 0.08]
        on_press:
            app.video_down(url.text)
    MDRoundFlatIconButton:
        id :aut
        disabled: True    
        line_color: "#ff0000"
        icon: "music"
        text_color:"#010000"
        text: "Download-Audio"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        #size_hint: [0.3, 0.08]
        font_size: "25sp"
        on_press:
            app.audio_down(url.text)        
    MDLabel:
        text:
            """*Choose the audio or video and wait for Message.                 
            After completing your video or audio downloading...,
            .                     check your gallery or file."""
        pos_hint: {'center_x':0.6,'center_y':0.2}
        bold:True
        font_size: "27sp"
    MDIconButton:
        icon: 'home'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#ff0000"
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'hello1'
            root.manager.transition.direction = 'right'
###############################TASK RENINDER#######################
<To>:
    name: 'to'
    date:date
    container: container
	FloatLayout:
		canvas.before:
		    Color:
                rgba: rgba("#FFFF00")
            Rectangle:
                size: self.size
                pos: self.pos	
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#E0FFFF')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
			
    ScrollView:
        size_hint: (.7, .70)
		pos_hint:{'x':.2,'y':.14}
        #bar_inactive_color:
        #get_color_from_hex('00640')
        bar_color:
        #get_color_from_hex('#21b68a')
        effect_cls: "ScrollEffect"
        bar_width:5
		GridLayout:
			id:container
			cols:1
			height:self.minimum_height
			row_default_height:250
			size_hint_y:None
	    	
		
    MDLabel:
		text:'MY Ultimate Task...'
		font_size:45
		pos_hint:{'x':.3,'y':.445}
		bold:True
		#italic:True
		outline_color:'#FF0000' 
		outline_width:2
	Label:
		text:'________________________'
		font_size:65
		pos_hint:{'x':.0,'y':.425}
		color:'#0e0100'
		bold:True
	
    
		
    MDLabel:
        id:date
        text:""
        pos_hint:{'x':.0,'y':.3}
        #font_name:"Poppins-SemiBold.ttf"
        font_size:'15sp'
        color:'#FF4500'
        underline:True
        bold:True
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        #text_color: "#FF0000"
        user_font_size : '33sp'
	    pos_hint:{'x':.07,'y':.63}
	    on_release:
		    root.manager.current ='todo'
		    root.manager.transition.direction = 'left'
	MDLabel:
	    text:'       ADD TASK!'
	    bold:True
	    pos_hint:{'x':.0,'y':.1}	    
		font_size:21	    
			
	MDFloatingActionButton:
        icon:'refresh'
        theme_text_color: "Custom"
        #text_color: "#ffff00"
        user_font_size : '45sp'	
		pos_hint:{'x':.07,'y':.42}
		on_release:
			root.add_text_inputs3()
	MDFloatingActionButton:
	    #icon:'chevron-left'
        icon:'home'
        theme_text_color: "Custom"
        text_color: "#020700"
        user_font_size : '45sp'	
		pos_hint:{'x':.07,'y':.14}
		on_release:
			root.manager.current = 'hello1'
            root.manager.transition.direction = 'right'		
				
	MDLabel:
	    text:'REFRESH TASK!'
	    bold:True
	    pos_hint:{'x':.0,'y':-.1}	    
		font_size:21
	MDLabel:
	    #text:'    <=GO BACK!'
	    text:'          HOME '
	    bold:True
	    color:'#FF1493'
	    pos_hint:{'x':.0,'y':-.4}	    
		font_size:21	
	MDLabel:
	    text:'#PLEASE  REFRESH  YOURSELF  FIRST!...'
	    bold:True
	    pos_hint:{'x':.3,'y':-.4}	    
		font_size:21			
	    color:'#0000CD'	
<Todo>:
    name:'todo' 
    date:date
    FloatLayout:
        
        canvas.before:
            Color:
                rgba: rgba("#C0C0C0")
            Rectangle:
                size: self.size
                pos: self.pos        
        MDLabel:
            text:'MY Task Title!'
            bold:True
            underline:True
            pos_hint: {'center_x':.9,'center_y':.88}
            font_size:'35sp'
        MDLabel:
            id:date
            text:""
            pos_hint: {'center_x':.565,'center_y':.89}
            #font_name:"Poppins-SemiBold.ttf"
            font_size:'18sp'    
            
        MDFloatLayout:
            size_hint:.85,.08
            pos_hint: {'center_x':.5,'center_y':.79}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            TextInput:
                id: title
                hint_text:'Enter Title..'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2sp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:25
                font_size:'18sp'
        MDLabel:
            text:'MY TASK!'
            bold:True
            underline:True
            pos_hint: {'center_x':.9,'center_y':.65}
            font_size:'35sp'        
            color:'#FF0000'
        MDFloatLayout:
            size_hint:.85,.30
            pos_hint: {'center_x':.5,'center_y':.45}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            TextInput:
                id:task
                hint_text:'MY Content...'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:200
                cursor_width:'2sp'
                foreground_color:(0,0,0)
                background_color:0,0,0,0
                
                padding:17
                font_size:'25sp'
        Button:
            text:'Save MY Task!'
            ripple_behavior: True
            size_hint:.50 ,.08
            pos_hint: {'center_x':.5,'center_y':.24}
            background_color:0,0,0,0
            font_size:'30sp'
            color:'#000000'
            
            on_press:app.add_user3(title.text,task.text)
            on_release:
                root.manager.current ='to'
                             
            canvas.before:
                Color:
                    rgb:(127/255,255/255,0)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            
        MDIconButton:
            icon:'chevron-left'
            user_font_size:'40sp'
            pos_hint: {'center_y':.95}
            theme_text_color:"Custom"
            text_color:'#0000FF'
            on_release:
                root.manager.current='to'
                root.manager.transition.direction = 'right'
       
        MDLabel:
	        
	        text: 
	            """*Please Enter Your Task Title and Your Task!,\n
	            Than Click (Save My Task) and Refresh Yourself.
	            If You Complete Your Task! Click Completed Button.*"""
	        font_size:21
	        color:'#FF4500'
	        bold:True
	        pos_hint: {'center_x':.7,'center_y':.10}
	            
<Task>:
    name : 'task'
    #title:'seeni'
    title:''
	task:''
	
	data:''
	data_id:''
	FloatLayout:
	    
        
		MDCard:
		    id:f
	        orientation: "vertical"  
		
	        padding: "20dp"
	        
	        size_hint: None, None
	        size: "700dp", "200dp"
	        pos_hint: {"center_x": .5, "center_y": .5}
	               
	        MDLabel:
	            id:v
	            text: root.title
	            font_size:30
	            bold:True
	            pos_hint: {'center_x':.90,'center_y':.6}
	            #halign: 'center'
	            color:'#fd0104'
	            outline_color:'#040204'
            	underline:True
	            
	                  
			MDLabel:
			    id:a
	            text: root.task
	            font_size:18
	            color:'#000000'
	            #halign: 'center'
	            pos_hint:{'x':.1,'y':.0}
	        MDLabel:
                id:da
                text:""
                font_size:'15sp'
                pos_hint:{'x':.2,'y':.2}    
	        
	    MDIconButton:
			icon:"delete"
			pos_hint:{'x':.9,'y':.1}
			on_release:root.delete3()
			on_release:app.opp1() 
			   								
        MDCheckbox:
            size_hint: None ,None
            size:"48dp","48dp"
            unselected_color: 1,170/255, 23/255,1
            selected_color: 0,179/255,0,1
            pos_hint: {'center_x':.94,'center_y':.7}
            on_release:root.delete3()
            on_release:app.opp()
            on_active:app.on_complete(*args, v,a,f)      
        
        MDLabel:
            text:"                                                   Completed!"
            pos_hint: {'center_x':.98,'center_y':.6}
            color:'#006400'
            bold:True
            
'''


class WelcomeScreen(Screen):
    pass


class UsernameScreen(Screen):
    pass

class MainScreen(Screen):
    pass
class Hello1(Screen):###homescreen####
    pass
class General(Screen):####general####
    pass
class Biodata(Screen):#####bio data####
    pass
class Main(Screen):#####bio data####
    pass
class Student(Screen):
    pass
class Youtub(Screen):#####YOUDUBE VIDEO DOWNLOADER#####
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(UsernameScreen(name='usernamescreen'))
sm.add_widget(MainScreen(name='main_screen'))
sm.add_widget(Hello1(name = 'hello1'))####honescreen###
sm.add_widget(General(name = 'general'))####general###
sm.add_widget(Biodata(name='bio'))#####bio data####
sm.add_widget(Main(name='main'))#####bio data####
sm.add_widget(Student(name='student'))
sm.add_widget(Youtub(name='youtub'))######youtube video downloader####



################################markstore function############################
class Btn(Screen):
    pass

    def __init__(self, **kwargs):
        super(Btn, self).__init__(**kwargs)

    def delete(self):
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute('delete from ugstudent where ID=' + self.data_id)
        con.commit()
        con.close()


class It(Screen):
    # self.data_id=data_id
    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(It, self).__init__(**kwargs)

    def add_text_inputs(self):
        self.container.clear_widgets()
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM ugstudent""")
        row = cur.fetchall()
        for i in row:
            wid = Btn()

            r1 = str(i[1]) + '\n'
            r2 = str(i[2]) + '\n'
            r3 = str(i[3]) + '\n'
            r4 = str(i[4]) + '\n'
            r5 = str(i[5]) + '\n'
            r6 = str(i[6]) + '\n'
            r7 = str(i[7]) + '\n'
            r8 = str(i[8]) + '\n'
            r9 = str(i[9]) + '\n'

            wid.data_id = str(i[0])

            wid.data = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9

            wid.r1 = r1
            wid.r2 = r2
            wid.r3 = r3
            wid.r4 = r4
            wid.r5 = r5
            wid.r6 = r6
            wid.r7 = r7
            wid.r8 = r8
            wid.r9 = r9

            self.container.add_widget(wid)


class Btn1(Screen):
    pass

    def __init__(self, **kwargs):
        super(Btn1, self).__init__(**kwargs)

    def delete(self):
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute('delete from pgstudent where ID=' + self.data_id)
        con.commit()
        con.close()


class It1(Screen):
    # self.data_id=data_id
    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(It1, self).__init__(**kwargs)

    def add_text_inputs1(self):
        self.container.clear_widgets()
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM pgstudent""")
        row = cur.fetchall()
        for i in row:
            wid = Btn1()

            a1 = str(i[1]) + '\n'
            a2 = str(i[2]) + '\n'
            a3 = str(i[3]) + '\n'
            a4 = str(i[4]) + '\n'
            a5 = str(i[5]) + '\n'
            a6 = str(i[6]) + '\n'
            a7 = str(i[7]) + '\n'
            a8 = str(i[8]) + '\n'
            a9 = str(i[9]) + '\n'

            wid.data_id = str(i[0])

            wid.data = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9

            wid.a1 = a1
            wid.a2 = a2
            wid.a3 = a3
            wid.a4 = a4
            wid.a5 = a5
            wid.a6 = a6
            wid.a7 = a7
            wid.a8 = a8
            wid.a9 = a9

            self.container.add_widget(wid)


class ImageButton(ButtonBehavior, Image):
    pass
class MDImageButton(ButtonBehavior, Image):
    pass

sm = ScreenManager()


sm.add_widget(It(name='it'))
sm.add_widget(Btn(name="btn"))
sm.add_widget(It1(name='it1'))
sm.add_widget(Btn1(name="btn1"))

################################ TASK RENINDER CODE##################

class Task(Screen):
    pass

    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)

    def delete3(self):
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute('delete from studen where ID=' + self.data_id)
        con.commit()
        con.close()


class To(Screen):
    # self.data_id=data_id
    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(To, self).__init__(**kwargs)

    def add_text_inputs3(self):
        self.container.clear_widgets()
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM studen""")
        row = cur.fetchall()
        for i in row:
            wid = Task()

            title = str(i[1]) + '\n'
            task = str(i[2]) + '\n'


            wid.data_id = str(i[0])

            wid.data = title + task
            wid.title = title
            wid.task = task


            self.container.add_widget(wid)

class Todo(Screen):
    pass
#sm = ScreenManager()

sm.add_widget(To(name='to'))
sm.add_widget(Task(name="task"))
sm.add_widget(Todo(name='todo'))

class MY_marks(MDApp):######  main class   ######
    def build(self):
        self.strng = Builder.load_string(helpstr)
        self.icon='applogo.png'
        return self.strng

    def check_username00(self):
        self.username_text00 = self.strng.get_screen('usernamescreen').ids.username_text_fied00.text
        username_check_false00 = True
        self.store.put('UserInfo00', name00=self.username_text00)
        self.username_changer00()
        try:
            int(self.username_text00)
        except:
            username_check_false00 = False
        if username_check_false00 or self.username_text00.split() == []:
            cancel_btn_username_dialogue00 = MDRaisedButton(text='Retry!', on_release=self.close_username_dialogue00)
            self.dialog = MDDialog(title='ENTER YOUR CUTE NAME!', text="YOU ARE NO TYPE YOUR CUTE NAME?", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue00])
            self.dialog.open()

        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button00.disabled = False

    def close_username_dialogue00(self, obj):
        self.dialog.dismiss()



    def username_changer00(self):

        self.strng.get_screen('mainscreen').ids.profile_name00.text = f"\nHi, <'{self.store.get('UserInfo00')['name00']}'>ARE YOU FINE?\n \n Thank you for using our app..."
        #sound = SoundLoader.load('a.mp3')
        #sound.play()


####################home screan code#####################
    def ext(self):
        self.task1 = MDDialog(title='Are you sure?',type="confirmation",text=f"Are you sure?,EXIT OUR APP!\n        THANK YOU! ",
                                buttons=[MDRaisedButton(text="NO",on_release=self.ta), MDRaisedButton(text="YES",on_release=self.exte)])
        self.task1.open()
    def ta(self, obj):
        self.task1.dismiss()

    def exte(self, obj):
        self.stop()
    def open19(self):
        webbrowser.open('https://www.w3schools.com/python/default.asp')

    def open20(self):
        webbrowser.open('https://www.jetbrains.com/pycharm/download/#section=windows')
    def open21(self):
        webbrowser.open('https://www.w3schools.com/java/default.asp')

    def open22(self):
        webbrowser.open('https://www.oracle.com/in/java/technologies/javase-downloads.html')

    def open23(self):
        webbrowser.open('https://www.w3schools.com/cpp/default.asp')

    def open24(self):
        webbrowser.open('https://www.codeblocks.org/downloads/')
    def openre(self):
        webbrowser.open("https://play.google.com/store/apps/details?id=com.annauniv.stucor")
    def openres(self):
        webbrowser.open("https://www.youtube.com/results?search_query=how+to+see+anna+university+result+2021+")
    def opencgpa(self):
        webbrowser.open("https://padeepz.com/anna-university-cgpa-calculator-regulation-2017/")
    def opencgpay(self):
        webbrowser.open("https://www.youtube.com/results?search_query=anna+university+0nline+cgpa+calculator+tamil")

#################################general use code###################################

    def show_example_custom_bottom_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()

    def open1(self):
        webbrowser.open("https://www.google.co.in/")
    def open2(self):
        webbrowser.open("www.youtube.com")
    def open3(self):
        webbrowser.open("https://www.facebook.com/")
    def open4(self):
        webbrowser.open("https://www.instagram.com/accounts/login/?next=%2Fhome.php%2F&source=desktop_nav")
    def open5(self):
        webbrowser.open("https://www.youtube.com/results?search_query=tamil+comedy+videos")
    def open6(self):
        webbrowser.open("https://www.youtube.com/results?search_query=tamil+songs")
    def open7(self):
        webbrowser.open("https://www.youtube.com/channel/UCHGktfcQq2BY_8tGPHwvm7g")
    def open8(self):
        webbrowser.open("https://desktop.telegram.org/")
    def open9(self):
        webbrowser.open("https://translate.google.com/?sl=auto&tl=ta&text=see&op=translate")
    def open10(self):
        webbrowser.open("https://www.google.com/travel/")

    def open11(self):
        webbrowser.open("https://www.google.co.in/maps/@10.7828364,78.2885026,23439m/data=!3m1!1e3!5m2!1e2!1e4")
    def open12(self):
        webbrowser.open("https://www.irctc.co.in/nget/profile/user-registration")
    def open13(self):
        webbrowser.open("https://in.via.com/bus-tickets?utm_source=google&utm_medium=cpc&utm_campaign=dynamic_search_ads_flight&gclid=EAIaIQobChMI98vNurHl8QIVl5pmAh04JwGwEAAYASAAEgJuYvD_BwE")
    def open14(self):
        webbrowser.open("https://www.easemytrip.com/cabs")
    def open15(self):
        webbrowser.open("https://lens.google/#")
    def open16(self):
        webbrowser.open("https://www.yupptv.com/tv-channels/tamil")
    def open17(self):
        webbrowser.open("https://twitter.com/login?lang=en")
    def open18(self):
        webbrowser.open("https://www.youtube.com/results?search_query=dance+video")
    def open27(self):
        webbrowser.open("https://web.whatsapp.com/")
    def opena(self):
       webbrowser.open('https://ijayasurya.github.io/tamilrockers-2021-movies')
    def openb(self):
        webbrowser.open('https://web.telegram.org/k/')
    def opens(self):
        webbrowser.open("https://www.youtube.com/results?search_query=olympic+sports")
    def openh(self):
        webbrowser.open("https://www.hotstar.com/in")
    def opench(self):
        webbrowser.open("https://www.google.com/chrome/")
    def openas(self):
        webbrowser.open("https://developers.google.com/assistant/why-build")
    def opencl(self):
        webbrowser.open('https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=japac-IN-all-en-dr-bkws-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_514666343194-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP%20~%20General_%20Core%20Brand-KWID_43700060584985727-kwd-6458750523-userloc_1007810&utm_term=KW_google%20cloud-ST_google%20cloud&gclid=EAIaIQobChMI45f8gsDv8QIVibmWCh0hiwDBEAAYASAAEgKwufD_BwE&gclsrc=aw.ds')
    def opendr(self):
        webbrowser.open("https://www.google.com/drive/")
    def openpl(self):
        webbrowser.open("https://play.google.com/store?hl=en")

    def openle(self):
        webbrowser.open("https://lens.google/")
    def openau(self):
        webbrowser.open('https://gaana.com/newrelease/tamil')
    def openS1(self):
        webbrowser.open('https://www.youtube.com/results?search_query=olympic+sports')
###################################mark store and biodata############################################

    def check(self):
        self.username_textd = self.strng.get_screen('bio').ids.username_text6.text
        username_check_falsed = True
        self.store.put('User5',ExamNumber =self.username_textd)
        self.changer6()
        try:
            int(self.username_textd)
        except:
            username_check_falsed = False
        if username_check_falsed or self.username_textd.split() == []:
            cancel_btn_username_dialogued = MDRaisedButton(text='Retry!', on_release=self.close_username_dialogued)
            self.dialog1 = MDDialog(title='No Enter Exam Number!', text="Please Enter Your Exam Number Type is (NO. xxxxxx)", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogued])
            self.dialog1.open()
        else:
            self.strng.get_screen('bio').ids.disabled_button.disabled = False
        self.username_textc = self.strng.get_screen('bio').ids.username_text5.text
        username_check_falsec = True
        self.store.put('User4',Studying =self.username_textc)
        self.changer5()
        try:
            int(self.username_textc)
        except:
            username_check_falsec = False
        if username_check_falsec or self.username_textc.split() == []:
            cancel_btn_username_dialoguec = MDRaisedButton(text='Retry!', on_release=self.close_username_dialoguec)
            self.dialog2 = MDDialog(title='No Enter Studying UG!(or)PG! ', text="Please Enter Your Studying  ", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialoguec])
            self.dialog2.open()



        self.username_textb = self.strng.get_screen('bio').ids.username_text4.text
        username_check_falseb = True
        self.store.put('User3',Whichyear =self.username_textb)
        self.changer4()
        try:
            int(self.username_textb)
        except:
            username_check_falseb = False
        if username_check_falseb or self.username_textb.split() == []:
            cancel_btn_username_dialogueb = MDRaisedButton(text='Retry!', on_release=self.close_username_dialogueb)
            self.dialog3 = MDDialog(title='No Enter Which year? to Which year? ', text="Please Enter Your Duration of studey! ", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogueb])
            self.dialog3.open()

        self.username_texta = self.strng.get_screen('bio').ids.username_text3.text
        username_check_falsea = True
        self.store.put('User2', Department=self.username_texta)
        self.changer3()
        try:
            int(self.username_texta)
        except:
            username_check_falsea = False
        if username_check_falsea or self.username_texta.split() == []:
            cancel_btn_username_dialoguea = MDRaisedButton(text='Retry!', on_release=self.close_username_dialoguea)
            self.dialog4 = MDDialog(title='No Enter Department & section!', text="Please Enter Your Department & section", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialoguea])
            self.dialog4.open()

        self.username_tex = self.strng.get_screen('bio').ids.username_text2.text
        username_check_false1 = True
        self.store.put('User1', collage=self.username_tex)
        self.username_changer1()
        try:
            int(self.username_tex)
        except:
            username_check_false1 = False
        if username_check_false1 or self.username_tex.split() == []:
            cancel_btn_username_dialogue1 = MDRaisedButton(text='Retry!', on_release=self.close_username_dialogue1)
            self.dialog5 = MDDialog(title='No Enter Your college Name!', text="Please Enter Your College Name", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue1])
            self.dialog5.open()



        self.username_text = self.strng.get_screen('bio').ids.username_text1.text
        username_check_false = True
        self.store.put('UserInfo', name=self.username_text)
        self.username_changer()
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == []:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry!',on_release=self.close_username_dialogue)
            self.dialog6 = MDDialog(title='No Enter Name!', text="Please Enter Your Name", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog6.open()

    def close_username_dialogued(self, obj):
        self.dialog1.dismiss()
    def close_username_dialoguec(self, obj):
        self.dialog2.dismiss()
    def close_username_dialogueb(self, obj):
        self.dialog3.dismiss()
    def close_username_dialoguea(self, obj):
        self.dialog4.dismiss()
    def close_username_dialogue1(self, obj):
        self.dialog5.dismiss()
    def close_username_dialogue(self, obj):
        self.dialog6.dismiss()





    def username_changer(self):

        self.strng.get_screen('main').ids.profile1.text = f"1.MY NAME                        =  {self.store.get('UserInfo')['name']}"
    def username_changer1(self):

        self.strng.get_screen('main').ids.profile2.text = f"2.COLLEGE NAME            =   {self.store.get('User1')['collage']}"
    def changer3(self):
        self.strng.get_screen('main').ids.profile3.text = f"3.Department & section  =  {self.store.get('User2')['Department']}"
    def changer4(self):
        self.strng.get_screen('main').ids.profile4.text = f"4.Duration of studeying  =  {self.store.get('User3')['Whichyear']}"
    def changer5(self):
        self.strng.get_screen('main').ids.profile5.text = f"5.Studying now                 =  {self.store.get('User4')['Studying']}"
    def changer6(self):
        self.strng.get_screen('main').ids.profile6.text = f"6.Exam Number               = {self.store.get('User5')['ExamNumber']}"
    def on_start(self):
        self.store = JsonStore("MYBiodata.text")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('main').manager.current = 'main'

        except KeyError:
            self.strng.get_screen('bio').manager.current = 'bio'
        try:
            if self.store.get('User1')['collage'] != "":
                self.username_changer1()
                self.strng.get_screen('main').manager.current = 'main'

        except KeyError:
            self.strng.get_screen('bio').manager.current = 'bio'

        try:
            if self.store.get('User2')['Department'] != "":
                self.changer3()
                self.strng.get_screen('main').manager.current = 'main'

        except KeyError:
            self.strng.get_screen('bio').manager.current = 'bio'
        try:
            if self.store.get('User3')['Whichyear'] != "":
                self.changer4()
                self.strng.get_screen('main').manager.current = 'main'

        except KeyError:
            self.strng.get_screen('bio').manager.current = 'bio'

        try:
            if self.store.get('User4')['Studying'] != "":
                self.changer5()
                self.strng.get_screen('main').manager.current = 'main'

        except KeyError:
            self.strng.get_screen('bio').manager.current = 'bio'
        try:
            if self.store.get('User5')['ExamNumber'] != "":
                self.changer6()
                self.strng.get_screen('main').manager.current = 'main'

        except KeyError:
            self.strng.get_screen('bio').manager.current = 'bio'
        today=date.today()
        wd = date.weekday(today)
        #days =['manday', 'tuseday','wednesday','thursday','friday','saturday','sunday']
        year =str(datetime.datetime.now().year)
        month=str(datetime.datetime.now().strftime(''))
        day =str(datetime.datetime.now().strftime('%A,%d %B, %Y'))
        self.strng.get_screen('it').date.text=f"{day} {month}  "
        self.strng.get_screen('it1').date.text=f"{day} {month} "
        self.strng.get_screen('todo').date.text=f"{day} {month}  "
        self.strng.get_screen('to').date.text=f"{day} {month}"
        self.store = JsonStore("MYBiodata.text")
        try:
            if self.store.get('UserInfo00')['name00'] != "":
                self.username_changer00()
                self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'


    ########################################biodata code#######################################
    def opp2(self):
        delete1 = MDRaisedButton(text='OK', on_release=self.de)
        self.deletes = MDDialog(title='Successfully Delete!',md_bg_color= get_color_from_hex('#FF3D00'),type="confirmation",text=f"Delete Successfully and Refresh Yourself",
                                buttons=[delete1])
        self.deletes.open()
    def de(self, obj):
        self.deletes.dismiss()


    def add_user(self, ugsem,ugexam,ugsub1,ugsub2,ugsub3,ugsub4,ugsub5,ugsub6,ugtotal):
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute(
            """ INSERT INTO ugstudent(ugsem,ugexam,ugsub1,ugsub2,ugsub3,ugsub4,ugsub5,ugsub6,ugtotal) VALUES (?,?,?,?,?,?,?,?,?)""",
            (ugsem,ugexam,ugsub1,ugsub2,ugsub3,ugsub4,ugsub5,ugsub6,ugtotal))
        con.commit()
        con.close()

    def add(self, pgsem,pgexam,pgsub1,pgsub2,pgsub3,pgsub4,pgsub5,pgsub6,pgtotal):
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute(
            """ INSERT INTO pgstudent(pgsem,pgexam,pgsub1,pgsub2,pgsub3,pgsub4,pgsub5,pgsub6,pgtotal) VALUES (?,?,?,?,?,?,?,?,?)""",
            (pgsem,pgexam,pgsub1,pgsub2,pgsub3,pgsub4,pgsub5,pgsub6,pgtotal))
        con.commit()
        con.close()

    def open45(self):
        webbrowser.open("https://www.technicalsymposium.com/annauniversityquestionpapers.html")
    def open44(self):
        webbrowser.open("https://kalvikaram.blogspot.com/")
    def open43(self):
        webbrowser.open("https://library.annauniv.edu/question_bank.php")
    def open50(self):
        webbrowser.open("https://www.google.com/search?q=arts+syllabus&rlz=1C1RXQR_enIN958IN958&oq=arts+syla&aqs=chrome.1.69i57j0i13l9.7203j0j7&sourceid=chrome&ie=UTF-8")
    def open41(self):
        webbrowser.open("https://www.google.com/search?q=arts+book+pdf+free+download+2021&rlz=1C1RXQR_enIN958IN958&ei=82r2YO3ULcO5rQGpjpLIDg")
    def open40(self):
        webbrowser.open("https://www.google.com/search?q=arts+and+science+question+bank+download+2021&rlz=1C1RXQR_enIN958IN958&oq=arts+and+science+question+bank+download+2021&aqs=chrome..69i57.42161j0j15&sourceid=chrome&ie=UTF-8")
    def open48(self):
        webbrowser.open("https://www.google.com/search?q=paramedical+syllabus+2021&rlz=1C1RXQR_enIN958IN958&oq=parametical+syla&aqs=chrome.2.69i57j0i13l9.16297j0j15&sourceid=chrome&ie=UTF-8")
    def open47(self):
        webbrowser.open("https://www.google.com/search?q=paramedical+books+2021&rlz=1C1RXQR_enIN958IN958&ei=bGz2YPrQDbHWz7sPqpexqAI")
    def open46(self):
        webbrowser.open("https://www.google.com/search?q=paramedical+question+bank+2021&rlz=1C1RXQR_enIN958IN958&ei=cm32YOUX_8DctQ_B4ayIBA")
    def open42(self):
        webbrowser.open("https://www.youtube.com/results?search_query=engineering+details+in+tamil")

    def open49(self):
        webbrowser.open("https://www.youtube.com/results?search_query=arts+and+science+in+details+tamil")
    def open39(self):
        webbrowser.open("https://www.youtube.com/results?search_query=paramedical+details+in+tamil")

######################################YOUTUBE VIDEO DOWNLOADER CODE#################################

    def yturl(self):
        self.text = self.strng.get_screen('youtub').ids.url.text
        url_check_false = True

        try:
            int(self.text)
        except:
            url_check_false = False

        if url_check_false or self.text.split() == []:
        #if self.text.startswith==(""):
            check = MDRaisedButton(text='Retry!', on_release=self.check01)
            self.check1 = MDDialog(title='enter Youtube url?', text="Please enter Your Video url", size_hint=(0.7, 0.2),
                                   buttons=[check])
            self.check1.open()


        elif self.text.startswith('https://youtube.com/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtu.be/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.com/shorts/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.be/shorts/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.com/playlist?list='):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.be/playlist?list='):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://www.youtube.com/watch?v='):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False


        else:
            check2 = MDRaisedButton(text='Retry!', on_release=self.emdy)
            self.check02 = MDDialog(title='IN VALID URL ', text="Please enter VALID URL", size_hint=(0.7, 0.2),
                                   buttons=[check2])
            self.check02.open()

    def check01(self, obj):
        self.check1.dismiss()
    def emdy(self, obj):
        self.check02.dismiss()

    def video_down(self, url):
        self.text = self.strng.get_screen('youtub').ids.url.text
        url_check_false = True

        try:
            int(self.text)
        except:
            url_check_false = False

        if url_check_false or self.text.split() == []:
        #if self.text.startswith==(""):
            check = MDRaisedButton(text='Retry!', on_release=self.check01)
            self.check1 = MDDialog(title='enter Youtub url?', text="Please enter Your Video url!",md_bg_color= get_color_from_hex('#FF3D00'), size_hint=(0.7, 0.2),
                                   buttons=[check])
            self.check1.open()
        else:
            print('Please wait download video!')
            self.yt = YouTube(url)
            self.downloading_messag = MDDialog(title="Downloading...",
                                            text=f"Downloading.. {self.yt.title}")
            self.downloading_messag.open()
        #download_location = r"video"
            self.yt.streams.filter(progressive=True).get_highest_resolution().download(r"MY_marks/Video")
            self.downloading_messag.dismiss()
            download_location = r"MY_marks/Video"
            close_btn1 = MDRaisedButton(text="OK", on_press=self.close1_dialog)


            self.downloading_message = MDDialog(title="Your Video Download Completed...!",type="confirmation",md_bg_color= get_color_from_hex('#00FF00'),
                                            text=f"Successfully Downloaded![ {self.yt.title}]\n\nVideo Location ={download_location}",size_hint=(0.8, 0.3),
                                            buttons=[close_btn1])
            self.downloading_message.open()
            print("successfully downloaded Video",download_location)

    def close1_dialog(self, obj):
        self.downloading_message.dismiss()



    def audio_down(self, url):
        self.text = self.strng.get_screen('youtub').ids.url.text
        url_check_false = True

        try:
            int(self.text)
        except:
            url_check_false = False

        if url_check_false or self.text.split() == []:
        #if self.text.startswith==(""):
            check = MDRaisedButton(text='Retry!', on_release=self.check01)
            self.check1 = MDDialog(title='enter Youtub url?', text="Please enter Your Autio url!",md_bg_color= get_color_from_hex('#FF3D00'), size_hint=(0.7, 0.2),
                                   buttons=[check])
            self.check1.open()
        else:
            print('Please wait download autio!')
            self.yt = YouTube(url)

            self.downloading_messag = MDDialog(title="Downloading...",
                                            text=f"Downloading.. {self.yt.title}")
            self.downloading_messag.open()

            self.yt.streams.get_audio_only(subtype="mp4").download(r"MY_marks/Audio")
            self.downloading_messag.dismiss()

            download_location = r"MY_marks/Audio"
            close_btn = MDRaisedButton(text="OK", on_press=self.close_dialog)

            self.downloading_message = MDDialog(title="Your Audio Download Completed...!",type="confirmation",md_bg_color= get_color_from_hex('#00FF00'),
                                            text=f"Successfully Downloaded!- [{self.yt.title}] \n\nAudio Location ={download_location}",size_hint=(0.8, 0.3),
                                            buttons=[close_btn])
            self.downloading_message.open()
            print("Successfully Downloaded Audio",download_location)
    def close_dialog(self, obj):
        self.downloading_message.dismiss()
####################################################task########################
    def on_complete(self,checkbox,value,v,a,f):
        if value:
            v.text=f'[Complete-{v.text}-Task]'
            f.md_bg_color=0,179/255,0,1
        else:
            remove=['[s]','[/s]']
            for i in remove:
                v.text=v.text.replace(i,'')
                f.md_bg_color=1,170/255,23/255,1
        if value:
            a.text=f'[Complete-{a.text}-Task]'
            a.md_bg_color=1,255/255,0,0
        else:
            remove=['[s]','[/s]']
            for i in remove:
                a.text=a.text.replace(i,'')
                a.md_bg_color=1,255/255,0,0

    def opp(self):
        #self.done= MDFloatingActionButton(md_bg_color= get_color_from_hex('#FF3D00'), icon='calendar-check',size_hint=(None, None), size=(50,50),elevation=10, theme_text_color='Custom',text_color=[1,1,0,1])
        task = MDRaisedButton(text='Done!', on_release=self.taa)
        self.task1 = MDDialog(title='Successfully Complete Your Task!',type="confirmation",text=f"Are you sure?,Complete your task!.\nYour Task Automatic delete\n,and Refresh Yourself",
                                buttons=[task])
        self.task1.open()
    def taa(self, obj):
        self.task1.dismiss()
    def opp1(self):
        #self.done= MDFloatingActionButton(md_bg_color= get_color_from_hex('#FF3D00'), icon='calendar-check',size_hint=(None, None), size=(50,50),elevation=10, theme_text_color='Custom',text_color=[1,1,0,1])
        title = MDRaisedButton(text='OK', on_release=self.ti)
        self.title1 = MDDialog(title='Successfully Delete!',md_bg_color= get_color_from_hex('#FF3D00'),type="confirmation",text=f"Your Task Delete Successfully and Refresh Yourself",
                                buttons=[title])
        self.title1.open()
    def ti(self, obj):
        self.title1.dismiss()

    def add_user3(self, title, task):
        con = sql.connect('seenivasan.db')
        cur = con.cursor()
        cur.execute(
            """ INSERT INTO studen(title,task) VALUES (?,?)""",
            (title, task))
        con.commit()
        con.close()

if __name__ == "__main__":
    MY_marks().run()