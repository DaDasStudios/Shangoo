from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication, QGraphicsDropShadowEffect, QGraphicsOpacityEffect, QMainWindow, QTableWidgetItem
import sys, os, res, main_screen_ui, ui_loadscreen, eval_math, draw_results, math, json, webbrowser

class ShadowEffect(QGraphicsDropShadowEffect):
    """ Create a QEffect quicker than traditional way """
    def __init__(self, setx = 0, sety = 0, setblur = 25, setcol = QtGui.QColor(201,201,201,255)):        
        super(ShadowEffect, self).__init__()
        self.setXOffset(setx)
        self.setYOffset(sety)
        self.setColor(setcol)
        self.setBlurRadius(setblur)
        
    def get_all(self):
        """ Get all main components of the shadow effect"""
        return f'XOffset: {self.xOffset}, YOffset: {self.yOffset}, Color: {self.color}, BlurRadius: {self.blurRadius}'

class ThreadEffect(QtCore.QThread):
    any_signal = QtCore.Signal()
    def __init__(self, name: str):
        super(ThreadEffect, self).__init__()
        self.name = name
    def run(self):
        self.any_signal.emit()
    def stop(self): 
        print(f'Stopping Thread {self.name}')
        self.terminate()
        
class LoadScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoadScreen, self).__init__()
        # * Obey with the preferences
        with open('./settings.json', encoding = 'utf-8') as f:
            self.settings_js = f.read()
            self.settings_js = json.loads(self.settings_js)
            self.show_loadscreen_start = self.settings_js['settings']['start_loadscreen'] # Get the boolean
        duration = 30
        print(f'The init show_loadscreen bool = {self.show_loadscreen_start}')
        if not self.show_loadscreen_start: 
            #self.run_mainApp()
            duration = 2
        # * If the user preferences allow it, we show the loadscreens
        self.ui = ui_loadscreen.Ui_MainWindow()
        self.ui.setupUi(self)
        # Set translucentbackground ant hide button on tab
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # Set close function to close_button
        self.ui.close_button.clicked.connect(self.close)

        # Create shadows using effect modulo to simplify the process
        self.shadow1 = ShadowEffect()
        self.shadow2 = ShadowEffect()
        self.shadow3 = ShadowEffect(setblur = 15)
        self.shadow4 = ShadowEffect(5, 5, 40)
        # Setting the shadow to each object
        self.ui.descp.setGraphicsEffect(self.shadow1)
        self.ui.title.setGraphicsEffect(self.shadow2)
        self.ui.progressBar.setGraphicsEffect(self.shadow3)
        self.ui.credits.setGraphicsEffect(self.shadow4)

        # Create a opacity effect for my window
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0)
        self.ui.centralwidget.setGraphicsEffect(self.opacity)
        # Animate opacity at starting app
        self.anim = QtCore.QPropertyAnimation(self.opacity, b'opacity')
        self.anim.setDuration(duration) # Using duartion allows to simulate the time
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.anim.start()
        self.anim.finished.connect(lambda: self.ui.centralwidget.setGraphicsEffect(None))

        # Setting timer for increase the progressBar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_progress)
        self.timer.start(duration)
        # Changing text on description
        QtCore.QTimer.singleShot(1500, lambda: self.ui.descp.setText('LOADING... Graphic user interface'))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.descp.setText('LOADING... Resources'))
 
    def show_progress(self):
        """ Change the progress of the bar """
        global counter
        # Set value to progress bar
        self.ui.progressBar.setValue(counter)
        # Close bar screen
        if counter > 100:
            self.timer.stop()
            self.run_mainApp()
        # Increase counter
        counter += 1

    def run_mainApp(self):
        ''' Run the ```MainApp``` class '''
        print('Created main')
        # Open main window
        self.main = MainApp()
        self.main.show()
        # Close this window
        self.close()

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        # Run the app
        self.ui = main_screen_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        # Set Icon and Name
        self.setWindowTitle('Shangoo')
        self.main_icon = QtGui.QIcon()
        self.main_icon.addFile(':/Icons/sprites/icons/main_ico.png')
        self.setWindowIcon(self.main_icon)
        # Set effects
        self.window_effect = ShadowEffect(setblur=15, setcol=QtGui.QColor(93,93,93))
        self.ui.centralwidget.setGraphicsEffect(self.window_effect)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # ? Load language
        self.load_language()
        # ? Prefences escentials
        self.load_preferences()
        self.ui.preferences_apply.clicked.connect(self.save_preferences)
        # ? Loading escentials to convertions section
        self.load_convertion() # Loading initally the values
        self.ui.convertions_body_top_lineEdit.textChanged.connect(self.do_convertion)
        self.ui.convertions_measure_comboBox.currentTextChanged.connect(self.load_convertion)
        self.ui.convertions_body_down_combo.currentTextChanged.connect(self.load_titles_convertions)
        self.ui.convertions_body_top_combo.currentTextChanged.connect(self.load_titles_convertions)
        # ? Escentials buttons for window
        self.init_maxwidth = self.ui.side_menu_container.maximumWidth()
        if self.show_menu_state: self.ui.side_menu_container.setMaximumWidth(0)
        self.display_side_menu()
        self.ui.disp_menu_btn.clicked.connect(self.display_side_menu)
        # ? Social Media buttons
        self.ui.facebook_btn.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/'))
        self.ui.youtube_btn.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.ui.webpage_btn.clicked.connect(lambda: webbrowser.open('https://www.google.com/'))
        self.ui.instagram_btn.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/'))
        # ? Top size buttons
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.restore_size_btn.clicked.connect(self.restore_window)
        self.ui.min_btn.clicked.connect(self.showMinimized)
        # ? Connections with menu's buttons
        self.ui.setting_button.clicked.connect(lambda: self.ui.content_menu.setCurrentIndex(0))
        self.ui.media_button.clicked.connect(lambda: self.ui.content_menu.setCurrentIndex(1))
        self.ui.about_us_button.clicked.connect(lambda: webbrowser.open('https://www.google.com/'))
        self.ui.help_button.clicked.connect(lambda: self.ui.content_menu.setCurrentIndex(2))
        # ? Historial buttons
        self.ui.reset_historial_btn.clicked.connect(lambda: self.ui.historial_label.setText(self.language_js['historial']['empty_text']))
            # * Loaders
        # Language
        self.load_language_list()
        # Measures
        self.load_measure()
            # * Apply changes function btn
        self.ui.apply_btn.clicked.connect(self.apply_language)
            # * Angle measures btn and comboBox
        self.ui.apply_angle.clicked.connect(self.apply_measures)
        # Macros
        self.load_macros()
        self.ui.save_macros_btn.clicked.connect(self.save_changes_macros)
        self.ui.reset_macros_btn.clicked.connect(self.reset_macros)
        self.ui.use_macro_selected.clicked.connect(self.insert_macro_line)
        # Set Current indexes
        self.ui.content_menu.setCurrentIndex(1)
        self.ui.help_tab_widgets.setCurrentIndex(0)
        self.ui.settings_tab.setCurrentIndex(0)
        self.ui.tabWidget_btns.setCurrentIndex(1)
        self.ui.manual_tab.setCurrentIndex(0)
        # Disable scrollBar at Combo
    # ! ###################################################
    # ! Defining all methods of operations buttons
    # ! ###################################################

        # todo: #######################
        # todo: Standar calculator:
        # todo: #######################    

        # ? Numbers
        self.ui.one.clicked.connect(lambda: self.ui.results_line.insert('1'))
        self.ui.two.clicked.connect(lambda: self.ui.results_line.insert('2'))
        self.ui.three.clicked.connect(lambda: self.ui.results_line.insert('3'))
        self.ui.four.clicked.connect(lambda: self.ui.results_line.insert('4'))
        self.ui.five.clicked.connect(lambda: self.ui.results_line.insert('5'))
        self.ui.six.clicked.connect(lambda: self.ui.results_line.insert('6'))
        self.ui.seven.clicked.connect(lambda: self.ui.results_line.insert('7'))
        self.ui.eight.clicked.connect(lambda: self.ui.results_line.insert('8'))
        self.ui.nine.clicked.connect(lambda: self.ui.results_line.insert('9'))
        self.ui.zero.clicked.connect(lambda: self.ui.results_line.insert('0'))
        # ? Symbols
        self.ui.plus_btn.clicked.connect(lambda: self.try_insert('+'))
        self.ui.minus.clicked.connect(lambda: self.try_insert('-'))
        self.ui.multiply_btn.clicked.connect(lambda: self.try_insert('*'))
        self.ui.div_btn.clicked.connect(lambda: self.try_insert('/'))
        self.ui.porcent_btn.clicked.connect(lambda: self.try_insert('%'))
        self.ui.dot_btn.clicked.connect(lambda: self.try_insert('.'))
        # ? Do operations 
        self.cont_C_btn = 1 
        self.ui.C_btn.clicked.connect(self.reset_results_line)
        self.ui.back_btn.clicked.connect(self.back_funcion)
        self.ui.result_btn.clicked.connect(self.get_result_standar)
        # * Go ahead for find these functions

        # todo: #######################
        # todo: Sciencie calculator:
        # todo: #######################    

        # ? Numbers
        self.ui.one_2.clicked.connect(lambda: self.ui.results_line.insert('1'))
        self.ui.two_2.clicked.connect(lambda: self.ui.results_line.insert('2'))
        self.ui.three_2.clicked.connect(lambda: self.ui.results_line.insert('3'))
        self.ui.four_2.clicked.connect(lambda: self.ui.results_line.insert('4'))
        self.ui.five_2.clicked.connect(lambda: self.ui.results_line.insert('5'))
        self.ui.six_2.clicked.connect(lambda: self.ui.results_line.insert('6'))
        self.ui.seven_2.clicked.connect(lambda: self.ui.results_line.insert('7'))
        self.ui.eight_2.clicked.connect(lambda: self.ui.results_line.insert('8'))
        self.ui.nine_2.clicked.connect(lambda: self.ui.results_line.insert('9'))
        self.ui.zero_2.clicked.connect(lambda: self.ui.results_line.insert('0'))      
        # ? Symbols
        self.ui.plus.clicked.connect(lambda: self.try_insert('+'))
        self.ui.minus_2.clicked.connect(lambda: self.try_insert('-'))
        self.ui.multiply.clicked.connect(lambda: self.try_insert('*'))
        self.ui.divide_btn.clicked.connect(lambda: self.try_insert('/'))
        self.ui.dot.clicked.connect(lambda: self.try_insert('.'))
        self.ui.open_bracket.clicked.connect(lambda: self.try_insert('('))
        self.ui.closed_bracket.clicked.connect(lambda: self.try_insert(')'))
        self.ui.x_power2.clicked.connect(lambda: self.ui.results_line.insert('²'))
        self.ui.x_power3.clicked.connect(lambda: self.ui.results_line.insert('³'))
        self.ui.x_powery.clicked.connect(lambda: self.try_insert('^'))
        self.ui.one_div_x.clicked.connect(lambda: self.ui.results_line.insert('1/'))
        self.ui.ten_power10.clicked.connect(lambda: self.ui.results_line.insert('10^'))
        self.ui.two_powerx.clicked.connect(lambda: self.ui.results_line.insert('2^'))
        self.ui.factorial.clicked.connect(lambda: self.try_insert('!'))
        self.ui.abs.clicked.connect(lambda: self.ui.results_line.insert('|'))
        self.ui.sq_root.clicked.connect(lambda: self.ui.results_line.insert('√'))
        self.ui.cb_root.clicked.connect(lambda: self.try_insert_word('3√'))
        self.ui.x_yroot.clicked.connect(lambda: self.ui.results_line.insert('√'))
        self.ui.pi.clicked.connect(lambda: self.ui.results_line.insert(str(math.pi)))
        self.ui.euler.clicked.connect(lambda: self.ui.results_line.insert(str(math.e)))
        self.ui.e_powerx.clicked.connect(lambda: self.ui.results_line.insert(str(math.e)+'^'))
        self.ui.plus_minus.clicked.connect(self.invert_signs)
        self.ui.log.clicked.connect(lambda: self.try_insert_word('log'))
        self.ui.logy.clicked.connect(self.display_logy_guide)
        self.ui.ln.clicked.connect(lambda: self.try_insert_word('ln'))
        self.ui.ncr.clicked.connect(lambda: self.try_insert_word('nCr'))
        self.ui.npr.clicked.connect(lambda: self.try_insert_word('nPr'))
        self.eng_exp = 0 # * The exponent variable to power in ENG mode
        self.ui.eng_p.clicked.connect(lambda: self.eng_mode(3))
        self.ui.eng_m.clicked.connect(lambda: self.eng_mode(-3))
        # ? Do operations 
        self.ui.C_btn_2.clicked.connect(self.reset_results_line)
        self.ui.back_btn_2.clicked.connect(self.back_funcion)
        self.ui.result.clicked.connect(self.get_result_standar)

        # todo: #######################
        # todo: Trigonometry calculator:
        # todo: #######################

        # ? Numbers
        self.ui.one_3.clicked.connect(lambda: self.ui.results_line.insert('1'))
        self.ui.two_3.clicked.connect(lambda: self.ui.results_line.insert('2'))
        self.ui.three_3.clicked.connect(lambda: self.ui.results_line.insert('3'))
        self.ui.four_3.clicked.connect(lambda: self.ui.results_line.insert('4'))
        self.ui.five_3.clicked.connect(lambda: self.ui.results_line.insert('5'))
        self.ui.six_3.clicked.connect(lambda: self.ui.results_line.insert('6'))
        self.ui.seven_3.clicked.connect(lambda: self.ui.results_line.insert('7'))
        self.ui.eight_3.clicked.connect(lambda: self.ui.results_line.insert('8'))
        self.ui.nine_3.clicked.connect(lambda: self.ui.results_line.insert('9'))
        self.ui.zero_3.clicked.connect(lambda: self.ui.results_line.insert('0'))   
        # ? Symbols
        self.ui.plus_btn_2.clicked.connect(lambda: self.try_insert('+'))
        self.ui.minus_btn2.clicked.connect(lambda: self.try_insert('-'))
        self.ui.multiply_btn_3.clicked.connect(lambda: self.try_insert('*'))
        self.ui.div_btn_3.clicked.connect(lambda: self.try_insert('/'))
        self.ui.dot_3.clicked.connect(lambda: self.try_insert('.'))
        self.ui.sin_btn.clicked.connect(lambda: self.try_insert_word('sin'))
        self.ui.cos_btn.clicked.connect(lambda: self.try_insert_word('cos'))
        self.ui.tan_btn.clicked.connect(lambda: self.try_insert_word('tan'))
        self.ui.csc_btn.clicked.connect(lambda: self.try_insert_word('csc'))
        self.ui.sec_btn.clicked.connect(lambda: self.try_insert_word('sec'))
        self.ui.ctg_btn.clicked.connect(lambda: self.try_insert_word('ctg'))
        self.ui.arcsin.clicked.connect(lambda: self.try_insert_word('sin⁻¹'))
        self.ui.arcos.clicked.connect(lambda: self.try_insert_word('cos⁻¹'))
        self.ui.arctan.clicked.connect(lambda: self.try_insert_word('tan'))
        self.ui.pi_2.clicked.connect(lambda: self.ui.results_line.insert(str(math.pi)))
        self.ui.euler_2.clicked.connect(lambda: self.ui.results_line.insert(str(math.e)))
        # ? Operations
        self.ui.C_btn_3.clicked.connect(self.reset_results_line)
        self.ui.back_btn_3.clicked.connect(self.back_funcion)
        self.ui.result_3.clicked.connect(self.get_result_standar)

        # todo: #######################
        # todo: Manual painter calculator:
        # todo: #######################

        self.ui.get_draw_manual_btn.clicked.connect(self.draw_expression)
        self.ui.clear_manual_frame.clicked.connect(lambda: self.ui.drawing_frame.setText(self.language_js['manual']['empty_text']))

    # ! ###################################################
    # ! Window methods
    # ! ###################################################
    
        def move_window(e):
            ''' Move window wherever mouse goes'''
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()                  
        self.ui.top_frame.mouseMoveEvent = move_window

    def mousePressEvent(self, event):
        ''' Detect mouse position '''
        self.clickPosition = event.globalPos()

    def restore_window(self):
        ''' Restore window when it's maximized or minimized'''
        if not self.isMaximized(): 
            self.ui.tabWidget_btns.setStyleSheet('QWidget{background-color: #efefef;border-radius: 10px;}/* BUTTONS */QPushButton{height: 30px;font: 14px "Roboto";color:#393939;background-color: #ffffff;border-radius: 5px;padding-top: 10px;padding-bottom: 10px;text-align: center;widget-animation-duration: 100;border-bottom: 1px solid #C6C6C6;}QPushButton:hover{background-color: #E0E0E0;}QPushButton:pressed{padding-top: 12px;padding-left: 5px;}/* TABS BOTTOM */QTabBar::tab{width:100%;height: 1.5em;font: 10px "Roboto";padding: 5px;text-align: center;color:#393939;border: none;}QTabBar::tab:hover{background-color: #C3C2C2;color: white;}QTabBar::tab:selected{background-color: #C3C2C2;color: white;}')
            self.showMaximized()
        else: 
            self.showNormal()
            self.ui.tabWidget_btns.setStyleSheet('QWidget{background-color: #efefef;border-radius: 10px;}/* BUTTONS */QPushButton{height: 30px;font: 12px "Roboto";color:#393939;background-color: #ffffff;border-radius: 5px;padding-top: 10px;padding-bottom: 10px;text-align: center;widget-animation-duration: 100;border-bottom: 1px solid #C6C6C6;}QPushButton:hover{background-color: #E0E0E0;}QPushButton:pressed{padding-top: 12px;padding-left: 5px;}/* TABS BOTTOM */QTabBar::tab{width:100%;height: 1.5em;font: 10px "Roboto";padding: 5px;text-align: center;color:#393939;border: none;}QTabBar::tab:hover{background-color: #C3C2C2;color: white;}QTabBar::tab:selected{background-color: #C3C2C2;color: white;}')

    def display_side_menu(self):
        ''' Animate left menu side '''
        self.disp_anim = QtCore.QPropertyAnimation(self.ui.side_menu_container, b'maximumWidth')
        width = self.ui.side_menu_container.maximumWidth()
        if width == self.init_maxwidth:
            # If the width equals to the max width size, it'll be minimized
            n_width = 0
        else:
            # Else it'll be maximized
            n_width = self.init_maxwidth
        # Setting animation properties
        self.disp_anim.setDuration(300)
        self.disp_anim.setStartValue(width)
        self.disp_anim.setEndValue(n_width)
        self.disp_anim.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.disp_anim.start()

    # ! ###################################################
    # ! Loading language 
    # ! ###################################################
    
    def load_language(self):
        ''' Load the applications language '''
        with open('./Currents/current_language.txt', encoding = "utf-8") as f:
            self.selected_language = f.read()
            print(f'Language selected: <<{self.selected_language}>>')
        with open(f'./Languages/{self.selected_language}', encoding = "utf-8") as f:
            file = f.read()
            self.language_js = json.loads(file)
            # ? Change all window's txts
            self.ui.setting_button.setText(self.language_js['settings_btn']['name'])
            self.ui.media_button.setText(self.language_js['media_btn'])
            self.ui.social_title.setText(self.language_js['media_btn'])
            self.ui.about_us_button.setText(self.language_js['about_btn'])
            self.ui.help_button.setText(self.language_js['help'])
            # Coming soon text
            self.ui.coming_soon.setText(self.language_js['convertions_txts']['body_frame']['titles']['coming_soon'])
            self.ui.help_title.setText(self.language_js['help'])
            # Setting SocialMedia texts
            self.ui.facebook_btn.setText(self.language_js['social_media']['facebook'])
            self.ui.instagram_btn.setText(self.language_js['social_media']['instagram'])
            self.ui.webpage_btn.setText(self.language_js['social_media']['webpage'])
            self.ui.youtube_btn.setText(self.language_js['social_media']['youtube'])
            # Setting angle options
            self.ui.angle_title.setText(self.language_js['angle_measure_unit'])
            self.ui.apply_angle.setText(self.language_js['apply_btn'])
            # Setting options in settings
            self.ui.settings_tab.setTabText(0,self.language_js['settings_btn']['language'])
            self.ui.settings_tab.setTabText(1,self.language_js['settings_btn']['units'])
            self.ui.settings_tab.setTabText(2,self.language_js['settings_btn']['macros'])
            self.ui.settings_tab.setTabText(3,self.language_js['settings_btn']['preferences'])
            # Setting macros texts
            self.ui.macro_title.setText(self.language_js['macros_txts']['adjust_title'])
            self.ui.save_macros_btn.setText(self.language_js['macros_txts']['save_btn'])
            self.ui.reset_macros_btn.setText(self.language_js['macros_txts']['reset_btn'])
            self.ui.use_macro_selected.setText(self.language_js['macros_txts']['use_macro_btn'])
            self.ui.macros_table_widget.setHorizontalHeaderLabels([self.language_js['macros_txts']['key_title']])
            # Settin prefernces texts
            self.ui.preferences_title.setText(self.language_js['settings_btn']['preferences'])
            self.ui.preferences_apply.setText(self.language_js['apply_btn'])
            self.ui.logy_checkbox.setText(self.language_js['preferences_txts']['logy_warning'])
            self.ui.loadscreen_checkbox.setText(self.language_js['preferences_txts']['start_loadscreen'])
            self.ui.menu_checkbox.setText(self.language_js['preferences_txts']['start_menu'])
            # Setting historial texts
            self.ui.reset_historial_btn.setText(self.language_js['historial']['reset_btn'])
            self.ui.historial_label.setText(self.language_js['historial']["empty_text"])
            # Setting manual texts
            self.ui.select_operation_title.setText(self.language_js['manual']['select_title'])
            self.ui.insert_exp_title.setText(self.language_js['manual']['insert_exp'])
            self.ui.get_draw_manual_btn.setText(self.language_js['manual']['get_result_btn'])
            self.ui.clear_manual_frame.setText(self.language_js['manual']['clear_btn'])
            self.ui.drawing_frame.setText(self.language_js['manual']['empty_text'])
            self.ui.select_operation_comboBox.setItemText(0, self.language_js['manual']['sum'])
            self.ui.select_operation_comboBox.setItemText(1, self.language_js['manual']['sub'])
            self.ui.select_operation_comboBox.setItemText(2, self.language_js['manual']['mult'])
            self.ui.select_operation_comboBox.setItemText(3, self.language_js['manual']['divis'])
            # Setting convertions texts
            self.ui.convertions_head_label.setText(self.language_js['convertions_txts']['head_frame']['title'])
            self.ui.convertions_body_top_label1.setText(self.language_js['convertions_txts']['body_frame']['titles']['convertion1'])
            self.ui.convertions_body_down_label1.setText(self.language_js['convertions_txts']['body_frame']['titles']['convertion2'])
            self.ui.convertions_body_down_label2.setText(self.language_js['convertions_txts']['body_frame']['titles']['empty_value'])
            self.ui.convertions_body_top_lineEdit.setPlaceholderText(self.language_js['convertions_txts']['body_frame']['titles']['place_holder_value'])
            self.ui.convertions_body_right_frame_down_label1.setText(self.language_js['convertions_txts']['body_frame']['titles']['definition'])
            self.ui.convertions_measure_comboBox.setItemText(0, self.language_js["convertions_txts"]['head_frame']['elements']['volume']['title'])
            self.ui.convertions_measure_comboBox.setItemText(1, self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['title'])
            self.ui.convertions_measure_comboBox.setItemText(2, self.language_js["convertions_txts"]['head_frame']['elements']['weight']['title'])
            self.ui.convertions_measure_comboBox.setItemText(3, self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['title'])
            self.ui.convertions_measure_comboBox.setItemText(4, self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['title'])
            self.ui.convertions_measure_comboBox.setItemText(5, self.language_js["convertions_txts"]['head_frame']['elements']['time']['title'])
            self.ui.convertions_measure_comboBox.setItemText(6, self.language_js["convertions_txts"]['head_frame']['elements']['power']['title'])
            self.ui.convertions_measure_comboBox.setItemText(7, self.language_js["convertions_txts"]['head_frame']['elements']['data']['title'])
            self.ui.convertions_measure_comboBox.setItemText(8, self.language_js["convertions_txts"]['head_frame']['elements']['angle']['title'])
            # Setting types of calculators
            self.ui.tabWidget_btns.setTabText(0,self.language_js['standar_mode'])
            self.ui.tabWidget_btns.setTabText(1,self.language_js['science_mode'])
            self.ui.tabWidget_btns.setTabText(2,self.language_js['trigonometry_mode'])
            # Setting texts of the sections at right side
            self.ui.manual_tab.setTabText(0, self.language_js['sections_right']['historial'])
            self.ui.manual_tab.setTabText(1, self.language_js['sections_right']['manual'])
            self.ui.manual_tab.setTabText(2, self.language_js['sections_right']['convertions'])
            self.ui.manual_tab.setTabText(3, self.language_js['sections_right']['graphics'])
            # Setting help content
            self.ui.help_useful_label.setText(self.language_js['help_texts']['useful'])
            self.ui.help_calculator_label.setText(self.language_js['help_texts']['calculators'])
            self.ui.help_manual_label.setText(self.language_js['help_texts']['manual'])
            self.ui.help_conversions_label.setText(self.language_js['help_texts']['conversions'])
            self.ui.help_settings_label.setText(self.language_js['help_texts']['settings'])
            # Settin help tabs
            self.ui.help_tab_widgets.setTabText(0, self.language_js['help_texts']['useful_t'])
            self.ui.help_tab_widgets.setTabText(1, self.language_js['help_texts']['calcul_t'])
            self.ui.help_tab_widgets.setTabText(2, self.language_js['help_texts']['manual_t'])
            self.ui.help_tab_widgets.setTabText(3, self.language_js['help_texts']['conversions_t'])
            self.ui.help_tab_widgets.setTabText(4, self.language_js['help_texts']['settings_t'])


    def load_language_list(self):
        ''' Loading the languages located in a ```json``` file, then show them in the languages list widget '''
        self.directory_lng = os.listdir('./Languages') # Getting directory list of all languages
        for _json in self.directory_lng:
            with open(f'./Languages/{_json}', 'r', encoding = 'utf-8') as f:
                file = f.read()
                js = json.loads(file)
                # Show it on screen
                self.ui.language_list.addItem(js['language'])

    def apply_language(self):
        ''' Change language '''
        selected_lng = self.ui.language_list.currentItem()
        selected_lng = selected_lng.text()
        for _json in self.directory_lng:
            with open(f'./Languages/{_json}', encoding = 'utf-8') as j:
                file = j.read()
                js = json.loads(file)              
                if selected_lng == js['language']:
                    with open(f'./Currents/current_language.txt', 'w', encoding = 'utf-8') as f:
                        print(f'Changing to file <<{js["name"]}>>')
                        f.write(js["name"])
                    self.load_language()
                    return

    # ! ###################################################
    # ! Loading Angle Measures
    # ! ###################################################

    def load_measure(self):
        ''' Loading angle measure variable '''
        with open('./Currents/current_measure.txt', 'r') as f:
            self.global_measure = f.read()
            print(f'Current global measure selected: <<{self.global_measure}>>')
        # Set currents index in comboBox
        self.ui.angle_comboBox.setCurrentText(self.global_measure.upper())

    def apply_measures(self):
        ''' Change and save angle measure variable '''
        self.global_measure = self.ui.angle_comboBox.currentText()
        self.global_measure = self.global_measure.lower()
        # Save changes
        with open('./Currents/current_measure.txt', 'w') as f:
            f.write(self.global_measure)
            print(f'<<{self.global_measure}>> has been saved!')

    # ! ###################################################
    # ! Loading Macros adjustment
    # ! ###################################################

    def load_macros(self):
        '''Loading macros keys which are wrote in a ```json``` file'''
        with open('./settings.json', encoding = 'utf-8') as f:
            macros_text = f.read()
            self.settings_js = json.loads(macros_text)
            # Loading macros, then show them in the list view
            cont = 0
            for macro in self.settings_js['macros']:
                self.ui.macros_table_widget.setItem(cont, 0, QTableWidgetItem(self.settings_js['macros'][macro]))

                cont += 1

    def save_changes_macros(self):
        ''' Saving changes, taking the macros values '''
        # Getting items in row 0 (keys)
        gotten_txts = [i for i in range(5)]
        for row in range(5):
            current_item = self.ui.macros_table_widget.item(row, 0)
            gotten_txts[row] = current_item.text()
        # print(f'Gotten txts: {gotten_txts}')
        # Changing the text json
        row = 0
        # print(f"Settins js: {self.settings_js['macros']}")
        for macro in self.settings_js['macros']:
            self.settings_js['macros'][macro] = gotten_txts[row]
            row += 1
        # Write changes
        change = json.dumps(self.settings_js, indent = 4)
        with open('./settings.json', 'w', encoding = 'utf-8') as f:
            f.write(change)
        self.load_macros()
        
    def reset_macros(self):
        '''Reset all macros configurations '''
        for row in range(5):
            self.ui.macros_table_widget.setItem(row, 0, QTableWidgetItem('None'))

    def insert_macro_line(self):
        ''' Insert in results lineEdit the macro selected '''
        selected = self.ui.macros_table_widget.currentItem()
        self.ui.results_line.insert(selected.text())
    
    # ! ###################################################
    # ! Settings preferences adjustment
    # ! ###################################################

    def load_preferences(self):
        ''' Loading the user prefences into the ```settings.json``` file '''
        with open('./settings.json', 'r', encoding = 'utf-8') as f:
            txt = f.read()
            self.settings_js = json.loads(txt)
            self.show_logy_warning_state = self.settings_js['settings']['logy_warning']
            self.show_loadscn_state = self.settings_js['settings']['start_loadscreen']
            self.show_menu_state = self.settings_js['settings']['start_menu']
        # Check the QCheckBoxes
        self.ui.logy_checkbox.setCheckState(self.decode_checkstates(self.show_logy_warning_state))
        self.ui.loadscreen_checkbox.setChecked(self.show_loadscn_state) # ? Any if these ways works to set a state
        self.ui.menu_checkbox.setChecked(self.show_menu_state)
        #logy_state = self.ui.logy_checkbox.checkState()
        print(f'The read state of the file "settings.json" in the three sets is: <<{self.show_logy_warning_state}>>, <<{self.show_loadscn_state}>>, <<{self.show_menu_state}>>')

    def decode_checkstates(self, object, way: int = 0):
        ''' Return a object depending if it's ```False``` return a ```Uncheck``` and ```Check``` if it is ```True``` '''
        if way == 0:
            if object: return QtCore.Qt.CheckState.Checked
            else: return QtCore.Qt.CheckState.Unchecked
        else:
            if object == QtCore.Qt.CheckState.Checked: return True
            else: return False

    def save_preferences(self):
        ''' Saving the preferences changes for next time '''
        # Getting the CheckBox Values
        self.show_logy_warning_state = self.decode_checkstates(self.ui.logy_checkbox.checkState(), 1)
        self.show_loadscn_state = self.decode_checkstates(self.ui.loadscreen_checkbox.checkState(), 1)
        self.show_menu_state = self.decode_checkstates(self.ui.menu_checkbox.checkState(), 1)
        # Assinging that values into the dict
        self.settings_js['settings']['logy_warning'] = self.show_logy_warning_state
        self.settings_js['settings']['start_loadscreen'] = self.show_loadscn_state
        self.settings_js['settings']['start_menu'] = self.show_menu_state
        #print(f'The setting json is: {self.settings_js}')
        # To write the changes
        with open(f'./settings.json', 'w', encoding = 'utf-8') as f:
            changes = json.dumps(self.settings_js, indent = 4)
            f.write(changes) # Changes has been changed!
        self.load_preferences()

    # ! ###################################################
    # ! QDialogs for anything
    # ! ###################################################

    def show_warning_dialog(self, text: str):
        ''' Show a warning for restart the app to apply the changes '''
        # Validation if to show it is allowed
        if self.show_logy_warning_state:
            # Escentials
            current_dialog = WarningScreen(self.language_js['warning']['title'], text)
            current_dialog.minimize.clicked.connect(current_dialog.showMinimized)
            current_dialog.close_b.clicked.connect(current_dialog.close)
            current_dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            current_dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            # Effect
            # * Set graphics effect
            current_dialog.main_widget.setGraphicsEffect(self.window_effect)
            # * Run Dialog
            current_dialog.exec_()
        
    # ! ###################################################
    # * ###################################################
    # * Defining all methods from operations buttons
    # * ###################################################
    # ! ###################################################

        # todo: #######################
        # todo: Standar calculator:
        # todo: ####################### 
    
    def try_insert_word(self, string: str):
        ''' Validate if there's a same word trying to get into the QLineEdit '''
        get_lineEdit = self.ui.results_line.text()
        if not get_lineEdit == '': 
            __len = len(string)
            get_lineEdit += ' '
            #print(f'Got text: {get_lineEdit}, string_len: {__len}, subscriptated string: {get_lineEdit[len(get_lineEdit)-__len+1:-1]}')
            if get_lineEdit[len(get_lineEdit)-__len-1:-1] == string:
                #print('It equal')
                return
        self.ui.results_line.insert(string)

    def try_insert(self, string: str):
        ''' Trying to insert a character, if the character is already on ther QLineEdit, it won't get into it '''
        __get_text = self.ui.results_line.text()
        if not __get_text == '':
            black_list = '+-*/.^()%|!'
            if __get_text[-1] in black_list: return
        self.ui.results_line.insert(string)       
        
        
    def reset_results_line(self):
        ''' Reset the results lines edit '''
        if self.cont_C_btn == 2:
            self.cont_C_btn = 1
            self.ui.second_results_line.clear()
        else:
            self.ui.results_line.clear()
            self.cont_C_btn += 1
        self.eng_exp = 0

    def back_funcion(self):
        ''' Back to behind, only a position '''
        text = self.ui.results_line.text()
        self.ui.results_line.setText(text[0:-1]) # 'text[0:-1]' is the new character, but it doesn't have the last letter

    def get_result_standar(self):
        ''' Eval the expression to get the result'''
        text = self.ui.results_line.text()
        try:
            text = text.replace(' ','')
            pre_eval = eval_math.pre_eval(text, {'²':'**2', '³':'**3'}, self.global_measure)
            last_result = self.ui.results_line.text()
            result = eval(pre_eval)
            self.ui.results_line.setText(str(result))
            self.ui.second_results_line.setText(last_result)
            # Setting the results and operations in the historial
            last_text_historial = self.ui.historial_label.text()
            if last_text_historial == self.language_js['historial']['empty_text']:
                self.ui.historial_label.clear()

                self.ui.historial_label.setText(f"{last_result} = {result}\n")
            else:
                self.ui.historial_label.setText(f"{last_text_historial}\n{last_result} = {result}\n")
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.ui.results_line.setText('Syntax error')
            print('Syntax error')
        return self.ui.results_line.text()

        # todo: ############################################## 
        # todo: Sciencie and trigonometry calculator:
        # todo: ############################################## 

    def invert_signs(self):
        ''' Invert the sign of the results of QLineEdit'''
        text = self.ui.results_line.text()
        text += ' '
        if text[0] != '-':
            if text[0] == '+':
                n_text = '-' + text[1:]
            else:
                n_text = '-' + text
        else:
            if text[0] == '-':
                n_text = text.replace('-','+', 1)
        self.ui.results_line.setText(n_text.strip())
    
    def eng_mode(self, change: int):
        ''' Doing the science notation, it depends of the ```change``` parameter '''
        solved = self.get_result_standar()
        # * Getting amount of zeros at beggining
        text = solved
        for i in text:
            if i == 0:
                self.eng_exp += 1
            elif i == '.':
                pass
            else: break
        # * Setting the new text on QlineEdit
        self.eng_exp += change
        converted = eval_math.eng_plus_minus(text, self.eng_exp)
        self.ui.results_line.setText(str(converted)+f'*10^{self.eng_exp}')
        # * Adding to exponent the number three
        
    def display_logy_guide(self):
        ''' Show a QDialog with help about how to use ```logy``` button '''
        self.show_warning_dialog(self.language_js['warning']["logy_help"])
        self.try_insert_word('logy')

        # todo: ############################################## 
        # todo: Painter manual functions:
        # todo: ############################################## 

    def draw_expression(self):
        ''' Drawing and paiting the expression like by manual procedure '''
        expression = self.ui.expression_lineEdit.text()
        def auto_select_sign():
            ''' Autio changing the current index '''
            if '+' in expression: self.ui.select_operation_comboBox.setCurrentIndex(0)
            elif '-' in expression: self.ui.select_operation_comboBox.setCurrentIndex(1)
            elif '*' in expression: self.ui.select_operation_comboBox.setCurrentIndex(2)
            elif '/' in expression: self.ui.select_operation_comboBox.setCurrentIndex(3)
            else: 
                print('Error! Select a available operation')
                return False
            return True
        # Change automatically the current index depending of the first sign found
        if not auto_select_sign(): return
        # Getting the function to use
        operation = self.ui.select_operation_comboBox.currentText()
        #print(f'Current operation selected on ComboBox: {operation}')
        #print(f'Expression: {expression}')
        self.drawer = draw_results.Drawer(expression)
        # Dict whose function is create a reference to each function according to the select option
        operations = {
            self.language_js['manual']['sum']: self.drawer.draw_sum,
            self.language_js['manual']['sub']: self.drawer.draw_subtraction,
            self.language_js['manual']['mult']: self.drawer.draw_multiply,
            self.language_js['manual']['divis']: self.drawer.draw_division
        }
        terms = self.drawer.split_signs() # Getting the list which we'll use for lining up
        # Checking if the operation is not division, because division doesn't need to sort the elements
        if not operation == self.language_js['manual']['divis']: 
            terms = self.drawer.convert_list_to(terms, float)
            terms.sort(reverse = True)
            terms = self.drawer.convert_list_to(terms, str)
        lined = self.drawer.built_columns(terms) # Building the columns or matrix to use
        draw = operations[operation](lined) # Getting the string with the result and the procedure
        # Showing results on label
        last_text = self.ui.drawing_frame.text()
        if last_text == self.language_js['manual']['empty_text']: text = draw  
        else: text = last_text + '\n───────────────────────────────────\n' + draw 
        text += '\n\n' 
        # Saving in historial
        text_historial = f"{expression} = {eval(expression)}"
        last_text_historial = self.ui.historial_label.text()
        if last_text_historial == self.language_js['historial']['empty_text']: self.ui.historial_label.setText(f"{text_historial}\n")      
        else: self.ui.historial_label.setText(f"{last_text_historial}\n{text_historial}\n")
        # Setting text on the label
        self.ui.drawing_frame.setText(text)

        # todo: ############################################## 
        # todo: Convertion section functions:
        # todo: ############################################## 

    def do_convertion(self):
        ''' Doing the operation for converting the value from a meausre to another one, by converting to a universal measure and then 
        convert to the solicited measure, to use the original or main relationg between the solicited one and the base measure we use a 
        given forum '''
        def convert_temp():
            ''' Converting temperatures measure due this procedure isn't the same of usual measures '''
            def convert_kelvin(operation: str, value: float = 273.15, number: float = given_number):
                ''' Convert to kelvind, depending of the operation '''       
                return eval(f'{number}{operation}{value}')

            # * Converting everything into Kelvins
            if measure == self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['celsius']:
                result = convert_kelvin('+')
            elif measure == self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['fahrenheit']:
                result = eval(f'({given_number}-32)*5/9+273.15')
            elif measure == self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['kelvin']:
                result = convert_kelvin('+', 0)
            #print(f'Last result temperature: {result}')
            # * To convert into the solicited measure
            if final_measure == self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['celsius']:
                result = convert_kelvin('-', number = result)
            elif final_measure == self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['fahrenheit']:
                result = eval(f'({result}-273.15)*9/5+32')
            elif final_measure == self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['kelvin']:
                result = convert_kelvin('+', 0, result)
            #print(f'Result temperature: {result}')
            return result

        def validation(type: str):
            ''' Validate a measure, it means that it will compare two strings, if they both coincide, return ```True``` '''
            if self.current_selected == type:
                print(f'They both measures are the same!')
                return True

        # ? The algorithm is the following...
        try:
            given_number = self.ui.convertions_body_top_lineEdit.text()
            given_number = float(given_number)
        except ValueError:
            #print(f'There was a error!')
            return
        # Getting the measures
        measure = self.ui.convertions_body_top_combo.currentText()
        final_measure = self.ui.convertions_body_down_combo.currentText()
        # * Validation if there's a convertion different
        if validation(self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['title']):
            # Do a different operation:
            result = convert_temp()
        else:
            # * Getting the equivalents to the base measure
            value_measure = self.convertions_dict[self.current_selected][measure][1]
            value_measure_solicited = self.convertions_dict[self.current_selected][final_measure][1]
            # print(f"\nBase value of {measure} in metters = {value_measure} | And the final value in metters ({final_measure}) = {value_measure_solicited}")
            # * Convert to meters
            result = given_number / value_measure
            #print(f"Result in meters equals: {result} m²")
            # * Convert to the solicited measure 
            result *= value_measure_solicited
            #print(f"Result converted into the solicited value equals {result} {final_measure}")
        # ? Setting the value on the Label
        __len_result = len(str(result))
        result = round(result, __len_result-1)
        self.ui.convertions_body_down_label2.setText(str(result))

    def load_titles_convertions(self):
        ''' Change the titles of convertions at once it changes on the ComboBox '''
        current_selected_value_top = self.ui.convertions_body_top_combo.currentText()
        current_selected_value_down = self.ui.convertions_body_down_combo.currentText()
        self.ui.convertions_body_top_label1.setText(current_selected_value_top)
        self.ui.convertions_body_down_label1.setText(current_selected_value_down)
        # Also we have to calculate the result if is that possible
        self.do_convertion()


    def load_convertion(self):
        ''' Loading the escentials at the moment to change the ComboBox value '''
        self.current_selected = self.ui.convertions_measure_comboBox.currentText()
        # A dict with all the measre available for using the current selected element
        self.convertions_dict = {
            self.language_js["convertions_txts"]['head_frame']['elements']['volume']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['volume']['cubic_meters']: [self.language_js["convertions_txts"]['head_frame']['elements']['volume']['cubic_meters'], 1],
                self.language_js["convertions_txts"]['head_frame']['elements']['volume']['cubic_cent']: [self.language_js["convertions_txts"]['head_frame']['elements']['volume']['cubic_cent'], 10**6],        
                self.language_js["convertions_txts"]['head_frame']['elements']['volume']['liters']: [self.language_js["convertions_txts"]['head_frame']['elements']['volume']['liters'], 10**3],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['volume']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['meters']: [self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['meters'], 1],
                self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['milimeters']: [self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['milimeters'], 10**3],
                self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['centimeters']: [self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['centimeters'], 10**2],
                self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['kilometers']: [self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['kilometers'], 10**-3],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['lenght']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['weight']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['weight']['kilograms']: [self.language_js["convertions_txts"]['head_frame']['elements']['weight']['kilograms'], 1],
                self.language_js["convertions_txts"]['head_frame']['elements']['weight']['grams']: [self.language_js["convertions_txts"]['head_frame']['elements']['weight']['grams'], 10**3],            
                self.language_js["convertions_txts"]['head_frame']['elements']['weight']['pound']: [self.language_js["convertions_txts"]['head_frame']['elements']['weight']['pound'], 2.204623],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['weight']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['celsius']: [self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['celsius'], 273.15],
                self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['fahrenheit']: [self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['fahrenheit'], (5/9)+273.15],
                self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['kelvin']: [self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['kelvin'], 0],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['temperature']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['meter_ps']: [self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['meter_ps'], 1/3.6],
                self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['kilometer_ph']: [self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['kilometer_ph'], 1],
                self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['feet_away_ps']: [self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['feet_away_ps'], 1/1.097],
                self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['mile_ph']: [self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['mile_ph'], 1/1.609],
                self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['knot']: [self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['knot'], 1/1.852],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['velocity']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['time']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['second']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['second'], 1],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['nano']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['nano'], 1e+9],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['micro']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['micro'], 1e+6],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['mili']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['mili'], 10**3],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['minute']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['minute'], 1/60],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['hour']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['hour'], 1/3600],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['day']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['day'], 1/86400],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['week']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['week'], 1/604800],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['month']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['month'], 1/2.628e+6],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['year']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['year'], 1/3.154e+7],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['decade']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['decade'], 1/3.154e+8],
                self.language_js["convertions_txts"]['head_frame']['elements']['time']['century']: [self.language_js["convertions_txts"]['head_frame']['elements']['time']['century'], 1/3.154e+9],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['time']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['power']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['power']['watt']: [self.language_js["convertions_txts"]['head_frame']['elements']['power']['watt'], 1],
                self.language_js["convertions_txts"]['head_frame']['elements']['power']['kilowatt']: [self.language_js["convertions_txts"]['head_frame']['elements']['power']['kilowatt'], 1/10**3],
                self.language_js["convertions_txts"]['head_frame']['elements']['power']['horse']: [self.language_js["convertions_txts"]['head_frame']['elements']['power']['horse'], 1/745.699],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['power']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['data']['title']: {
                'Bit': ['Bit', 8],
                'Kilobit': ['Kilobit', 1/125],
                'Kibibit': ['Kibibit', 1/128],
                'Megabit': ['Megabit', 1/12500],
                'Megabibit': ['Megabibit', 1/131072],
                'Gigabit': ['Gigabit', 1/1.25e+8],
                'Gigibibit': ['Gigibibit', 1/1.34e+8],
                'Terabit': ['Terabit', 1/1.25e+11],
                'Tebibit': ['Tebibit', 1/1.374e+11],
                'Petabit': ['Petabit', 1/1.25e+14],
                'Pebibit': ['Pebibit', 1/1.407e+14],
                'Byte': ['Byte', 1],
                'Kilobyte': ['Kilobyte', 1/1000],
                'Kibibyte': ['Kibibyte', 1/1024],
                'Megabyte': ['Megabyte', 1/1e+6],
                'Mebibyte': ['Mebibyte', 1/1.049e+6],
                'Gigabyte': ['Gigabyte', 1/1e+9],
                'Gibibyte': ['Gibibyte', 1/1.074e+9],
                'Terabyte': ['Terabyte', 1/1e+12],
                'Tebibyte': ['Tebibyte', 1/1.1e+12],
                'Petabyte': ['Petabyte', 1/1e+15],
                'Pebibyte': ['Pebibyte', 1/1.126e+15],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['data']['definition']
            },
            self.language_js["convertions_txts"]['head_frame']['elements']['angle']['title']: {
                self.language_js["convertions_txts"]['head_frame']['elements']['angle']['cente']: [self.language_js["convertions_txts"]['head_frame']['elements']['angle']['cente'], 1/(math.pi/200)],
                self.language_js["convertions_txts"]['head_frame']['elements']['angle']['sexa']: [self.language_js["convertions_txts"]['head_frame']['elements']['angle']['sexa'], 1/(math.pi/180)],
                self.language_js["convertions_txts"]['head_frame']['elements']['angle']['milradian']: [self.language_js["convertions_txts"]['head_frame']['elements']['angle']['milradian'], 10**3],
                self.language_js["convertions_txts"]['head_frame']['elements']['angle']['minute_arc']: [self.language_js["convertions_txts"]['head_frame']['elements']['angle']['minute_arc'], 1/(math.pi/(60*180))],
                self.language_js["convertions_txts"]['head_frame']['elements']['angle']['radian']: [self.language_js["convertions_txts"]['head_frame']['elements']['angle']['radian'], 1],
                self.language_js["convertions_txts"]['head_frame']['elements']['angle']['sexa_second']: [self.language_js["convertions_txts"]['head_frame']['elements']['angle']['sexa_second'], 1/(math.pi/(180*3600))],
                'def': self.language_js["convertions_txts"]['head_frame']['elements']['angle']['definition']
            }
        }

        if self.current_selected in self.convertions_dict: 
            #print(f'{self.current_selected} is in convertions dict')
            # Clear the down comboBoxes, then to add the new values
            self.ui.convertions_body_top_combo.clear()
            self.ui.convertions_body_down_combo.clear()
            # Adding
            # print(f"The current dict to use is: {self.convertions_dict[self.current_selected]}")
            for value in self.convertions_dict[self.current_selected]:
                if not value == 'def':
                    # print(f'Current item to add: {self.convertions_dict[self.current_selected][value][0]}')
                    self.ui.convertions_body_down_combo.addItem(self.convertions_dict[self.current_selected][value][0])
                    self.ui.convertions_body_top_combo.addItem(self.convertions_dict[self.current_selected][value][0])
            # Setting the values and definitions on the right side
            self.ui.convertions_body_right_frame_top_title.setText(self.current_selected)
            self.ui.convertions_body_right_frame_down_label2.setText(self.convertions_dict[self.current_selected]['def'])
            # Setting the values on titles
            self.load_titles_convertions()
            # Also we have to calculate the result if is that possible
            self.do_convertion()

class WarningScreen(QtWidgets.QDialog):
    def __init__(self, title: str, text: str):
        super(WarningScreen, self).__init__()
        self.setWindowTitle(title)
        self.resize(400, 276)
        __dialog_ico = QtGui.QIcon()
        __dialog_ico.addFile(':/Icons/sprites/icons/help.png')
        self.setWindowIcon(__dialog_ico)
        #self.setWindowModality(QtCore.Qt.ApplicationModal)
        # ? Widgets
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setStyleSheet(u"QWidget{ \n"
"background-color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QFrame{\n"
"background-color: #efefef;\n"
"margin: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"font: 13px \"Roboto\";\n"
"color: #383838;\n"
"}")
        # ? Frames
        top_frame = QtWidgets.QFrame(self.main_widget)
        top_frame.setMinimumSize(QtCore.QSize(0, 25))
        btns_frame = QtWidgets.QFrame(top_frame)
        btns_frame.setMinimumSize(QtCore.QSize(0, 0))
        btns_frame.setStyleSheet(u"QFrame{\n"
"background-color: white;\n"
"border-bottom: 1px solid #c2c3c3;"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 10px;\n"
"padding: 7px;\n"
"margin: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #efefef;\n"
"}")
        content_frame = QtWidgets.QFrame(self.main_widget)
        __content_sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        __content_sizePolicy.setHorizontalStretch(0)
        __content_sizePolicy.setVerticalStretch(0)
        __content_sizePolicy.setHeightForWidth(content_frame.sizePolicy().hasHeightForWidth())
        content_frame.setSizePolicy(__content_sizePolicy)

        # ? Layouts
        HLayout = QtWidgets.QHBoxLayout(self)
        VLayout = QtWidgets.QVBoxLayout(self.main_widget)
        VLayout.setContentsMargins(0,0,0,0)
        VLayout.setSpacing(0)
        top_HLayout = QtWidgets.QHBoxLayout(top_frame)
        top_HLayout.setContentsMargins(2,2,2,2)
        btns_HLayout = QtWidgets.QHBoxLayout(btns_frame)
        btns_HLayout.setContentsMargins(0,0,0,0)
        content_VLayout = QtWidgets.QVBoxLayout(content_frame)
        content_VLayout.setSpacing(2)
        content_VLayout.setContentsMargins(2,2,2,2)

        # ? Labels
        title_label = QtWidgets.QLabel(top_frame)
        title_label.setText(title)
        title_label.setStyleSheet("font-size: 16px;\n"
"font-style: italic;\n"
"padding-left: 35%;\n"
"margin: 7px 20px;\n"
"background-color: white;\n"
"color: #393939;\n"
"border-bottom: 1px solid #c2c3c3;"  
        )
        top_HLayout.addWidget(title_label)

        content_label = QtWidgets.QLabel(content_frame)
        content_label.setText(text)
        content_label.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"border-bottom: 1px solid #c2c3c3;\n"
"margin: 5px;")
        content_label.setWordWrap(True)
        content_label.setMargin(15)
        content_VLayout.addWidget(content_label)

        # ? Buttons
        self.minimize = QtWidgets.QPushButton(btns_frame)
        self.minimize.setText('')
        __min_ico = QtGui.QIcon()
        __min_ico.addFile(u":/Icons/sprites/icons/minimize.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize.setIcon(__min_ico)
        self.minimize.setIconSize(QtCore.QSize(32, 32))
        btns_HLayout.addWidget(self.minimize)
        
        self.close_b = QtWidgets.QPushButton(btns_frame)
        self.close_b.setText('')
        __close_ico = QtGui.QIcon()
        __close_ico.addFile(u":/Icons/sprites/icons/close.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_b.setIcon(__close_ico)
        self.close_b.setIconSize(QtCore.QSize(32, 32))
        btns_HLayout.addWidget(self.close_b, 0, QtGui.Qt.AlignRight)

        # ? Setting layouts
        top_HLayout.addWidget(btns_frame, 0, QtGui.Qt.AlignRight)
        VLayout.addWidget(top_frame, 0, QtGui.Qt.AlignTop)
        VLayout.addWidget(content_frame)
        HLayout.addWidget(self.main_widget)
        #self.setLayout(VLayout)

        # ? Move window at button frame
        def move_window(e):
            ''' Move window wherever mouse goes'''
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()                  
        top_frame.mouseMoveEvent = move_window

    def mousePressEvent(self, event):
        ''' Detect mouse position '''
        self.clickPosition = event.globalPos()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    counter = 0 # Counter variable for progressBar
    root = LoadScreen()
    root.show()
    sys.exit(app.exec_())
