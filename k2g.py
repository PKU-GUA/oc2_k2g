import sys
import win32con
import win32gui
import win32ui
import math
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDoubleSpinBox
from PySide2.QtCore import QSettings, QRect
from UIView import Ui_UIView
from pynput.keyboard import Key, KeyCode
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Button
from pynput.mouse import Listener as MouseListener
from qt_material import QtStyleTools, list_themes
import vgamepad as vg


class UIFunc(QMainWindow, Ui_UIView, QtStyleTools):
    valid_input = \
        list(map(chr, range(ord('a'), ord('z') + 1))) + \
        [',', '/', ';', '\'', '=', '.', '[', ']', '\\', '-'] + \
        ['space', 'mouse1', 'mouse2', 'up', 'down', 'left', 'right'] + \
        ['lshift', 'rshift', 'lctrl', 'rctrl', 'lalt', 'ralt']
    text_key_dict = {'space': Key.space,
                     'up': Key.up, 'down': Key.down, 'left': Key.left, 'right': Key.right,
                     'mouse1': Button.left, 'mouse2': Button.right,
                     'lshift': Key.shift_l, 'rshift': Key.shift_r,
                     'lctrl': Key.ctrl_l, 'rctrl': Key.ctrl_r,
                     'lalt': Key.alt_l, 'ralt': Key.alt_r}

    def __init__(self, app):
        super(UIFunc, self).__init__()
        self.app = app
        self.setupUi(self)
        self.lineEdit_dict = {
            'Up': self.lineEdit_1,
            'Down': self.lineEdit_2,
            'Left': self.lineEdit_3,
            'Right': self.lineEdit_4,
            'Operate': self.lineEdit_5,
            'PickUp': self.lineEdit_6,
            'Dash': self.lineEdit_7,
            'Emote': self.lineEdit_8,
            'Switch': self.lineEdit_0
        }

        self.config = QSettings('config.ini', QSettings.IniFormat)
        self.choice_theme.addItems(list_themes())
        self.choice_theme.setCurrentText(self.config.value('Config/Theme'))
        self.choice_theme.currentTextChanged.connect(self.on_theme_change)
        self.on_theme_change()

        self.lineEdit_9.setText(';' if self.config.value('Config/Key1') == ':' else self.config.value('Config/Key1'))
        self.doubleSpinBox_1.setValue(float(self.config.value('Config/X1')))
        self.doubleSpinBox_2.setValue(float(self.config.value('Config/Y1')))
        self.lineEdit_10.setText(';' if self.config.value('Config/Key2') == ':' else self.config.value('Config/Key2'))
        self.doubleSpinBox_3.setValue(float(self.config.value('Config/X2')))
        self.doubleSpinBox_4.setValue(float(self.config.value('Config/Y2')))
        text = self.lineEdit_9.text().lower()
        self.key1 = None if text == '' else KeyCode.from_char(text) if len(text) == 1 else self.text_key_dict[text]
        text = self.lineEdit_10.text().lower()
        self.key2 = None if text == '' else KeyCode.from_char(text) if len(text) == 1 else self.text_key_dict[text]
        self.pushButton_2.clicked.connect(self.on_config_change)

        self.set_keymap_text()
        self.key_dict = dict()
        for name, lineEdit in self.lineEdit_dict.items():
            text = lineEdit.text().lower()
            self.key_dict[name] = KeyCode.from_char(text) if len(text) == 1 else self.text_key_dict[text]
        self.pushButton.clicked.connect(self.on_keymap_change)

        self.gamepad = vg.VX360Gamepad()
        self.gamepad_player = GamepadPlayer(frame=self)
        self.gamepad_player.start()

    def set_keymap_text(self):
        for name, lineEdit in self.lineEdit_dict.items():
            v = self.config.value('Config/' + name)
            if v == ':':
                v = ';'
            lineEdit.setText(v)

    def on_config_change(self):
        self.config.setValue('Config/X1', self.doubleSpinBox_1.value())
        self.config.setValue('Config/Y1', self.doubleSpinBox_2.value())
        self.config.setValue('Config/X2', self.doubleSpinBox_3.value())
        self.config.setValue('Config/Y2', self.doubleSpinBox_4.value())

        text = self.lineEdit_9.text().lower()
        if text == '':
            self.key1 = None
            self.config.setValue('Config/Key1', '')
        elif text in self.valid_input and text not in ['mouse1', 'mouse2']:
            key = KeyCode.from_char(text) if len(text) == 1 else self.text_key_dict[text]
            if key not in self.key_dict.values():
                self.key1 = key
                self.config.setValue('Config/Key1', ':' if text == ';' else text)
                if key == self.key2:
                    self.key2 = None
                    self.config.setValue('Config/Key2', '')

        text = self.lineEdit_10.text().lower()
        if text == '':
            self.key2 = None
            self.config.setValue('Config/Key2', '')
        elif text in self.valid_input and text not in ['mouse1', 'mouse2']:
            key = KeyCode.from_char(text) if len(text) == 1 else self.text_key_dict[text]
            if key not in self.key_dict.values() and key != self.key1:
                self.key2 = key
                self.config.setValue('Config/Key2', ':' if text == ';' else text)

        self.lineEdit_9.setText(';' if self.config.value('Config/Key1') == ':' else self.config.value('Config/Key1'))
        self.lineEdit_10.setText(';' if self.config.value('Config/Key2') == ':' else self.config.value('Config/Key2'))
        self.gamepad_player.reset()

    def on_keymap_change(self):
        text_dict = {name: lineEdit.text().lower() for name, lineEdit in self.lineEdit_dict.items()}
        # 键位冲突或空或错误输入
        if all(text in self.valid_input for text in text_dict.values()) and \
                len(''.join(text_dict.values())) == len(''.join(set(text_dict.values()))) and \
                all(text_dict[name] not in ['mouse1', 'mouse2'] for name in ['Up', 'Down', 'Left', 'Right']):
            key_dict = dict()
            for name, text in text_dict.items():
                self.config.setValue('Config/' + name, ':' if text == ';' else text)
                key_dict[name] = KeyCode.from_char(text) if len(text) == 1 else self.text_key_dict[text]
            self.key_dict = key_dict

        self.set_keymap_text()
        if self.key1 in self.key_dict.values():
            self.key1 = None
            self.config.setValue('Config/Key1', '')
            self.lineEdit_9.setText('')
        if self.key2 in self.key_dict.values():
            self.key2 = None
            self.config.setValue('Config/Key2', '')
            self.lineEdit_10.setText('')

        self.gamepad_player.reset()

    def on_theme_change(self):
        self.apply_stylesheet(self.app, theme=self.choice_theme.currentText())
        self.config.setValue("Config/Theme", self.choice_theme.currentText())


class GamepadPlayer:
    def __init__(self, frame: UIFunc):
        self.keyboard_state = [False] * 6  # wasd k1 k2
        self.frame = frame
        self.gamepad = frame.gamepad

        def on_press_keyboard(key):
            if key not in [Key.enter, Key.up, Key.down, Key.left, Key.right, Key.space,
                           Key.shift_l, Key.shift_r, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r]:
                key = self.kl.canonical(key)
            if key == self.frame.key_dict['PickUp'] or key == Key.enter:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                self.gamepad.update()
            if key == self.frame.key_dict['Dash']:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                self.gamepad.update()
            if key == self.frame.key_dict['Operate']:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                self.gamepad.update()
            if key == self.frame.key_dict['Emote']:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                self.gamepad.update()
            if key == self.frame.key_dict['Switch']:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                self.gamepad.update()
            if key == self.frame.key_dict['Left']:
                self.keyboard_state[1] = True
                self.update_joystick()
            if key == self.frame.key_dict['Right']:
                self.keyboard_state[3] = True
                self.update_joystick()
            if key == self.frame.key_dict['Up']:
                self.keyboard_state[0] = True
                self.update_joystick()
            if key == self.frame.key_dict['Down']:
                self.keyboard_state[2] = True
                self.update_joystick()
            if key == self.frame.key1:
                self.keyboard_state[4] = True
                self.update_joystick()
            if key == self.frame.key2:
                self.keyboard_state[5] = True
                self.update_joystick()
            if key == KeyCode.from_char('t'):
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                self.gamepad.update()

        def on_release_keyboard(key):
            if key not in [Key.enter, Key.up, Key.down, Key.left, Key.right, Key.space,
                           Key.shift_l, Key.shift_r, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r]:
                key = self.kl.canonical(key)
            if key == self.frame.key_dict['PickUp'] or key == Key.enter:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                self.gamepad.update()
            if key == self.frame.key_dict['Dash']:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                self.gamepad.update()
            if key == self.frame.key_dict['Operate']:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                self.gamepad.update()
            if key == self.frame.key_dict['Emote']:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                self.gamepad.update()
            if key == self.frame.key_dict['Switch']:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                self.gamepad.update()
            if key == self.frame.key_dict['Left']:
                self.keyboard_state[1] = False
                self.update_joystick()
            if key == self.frame.key_dict['Right']:
                self.keyboard_state[3] = False
                self.update_joystick()
            if key == self.frame.key_dict['Up']:
                self.keyboard_state[0] = False
                self.update_joystick()
            if key == self.frame.key_dict['Down']:
                self.keyboard_state[2] = False
                self.update_joystick()
            if key == self.frame.key1:
                self.keyboard_state[4] = False
                self.update_joystick()
            if key == self.frame.key2:
                self.keyboard_state[5] = False
                self.update_joystick()
            if key == KeyCode.from_char('t'):
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                self.gamepad.update()

        def on_click(x, y, button, pressed):
            gamepad_button = None
            if button == self.frame.key_dict['PickUp']:
                gamepad_button = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
            if button == self.frame.key_dict['Dash']:
                gamepad_button = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
            if button == self.frame.key_dict['Operate']:
                gamepad_button = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
            if button == self.frame.key_dict['Emote']:
                gamepad_button = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
            if gamepad_button:
                if pressed:
                    self.gamepad.press_button(gamepad_button)
                else:
                    self.gamepad.release_button(gamepad_button)
                self.gamepad.update()

        self.kl = KeyboardListener(on_press=on_press_keyboard, on_release=on_release_keyboard)
        self.ml = MouseListener(on_click=on_click)

    def update_joystick(self):
        joystick_x = joystick_y = 0.0
        if self.keyboard_state[4]:
            joystick_x = self.frame.doubleSpinBox_1.value()
            joystick_y = self.frame.doubleSpinBox_2.value()
        elif self.keyboard_state[5]:
            joystick_x = self.frame.doubleSpinBox_3.value()
            joystick_y = self.frame.doubleSpinBox_4.value()
        else:
            if self.keyboard_state[0] and not self.keyboard_state[2]:
                joystick_y = 1.0
            elif not self.keyboard_state[0] and self.keyboard_state[2]:
                joystick_y = -1.0
            if self.keyboard_state[1] and not self.keyboard_state[3]:
                joystick_x = -1.0
            elif not self.keyboard_state[1] and self.keyboard_state[3]:
                joystick_x = 1.0
        self.gamepad.left_joystick_float(joystick_x, joystick_y)
        self.gamepad.update()

    def start(self):
        self.kl.start()
        self.ml.start()

    def reset(self):
        self.gamepad.reset()
        self.gamepad.update()
        self.keyboard_state = [False] * 6


def resize_layout(ui, ratio_h):
    ui.resize(ui.width() * ratio_h, ui.height() * ratio_h)
    for q_widget in ui.findChildren(QWidget):
        q_widget.setGeometry(QRect(
            q_widget.x() * ratio_h,
            q_widget.y() * ratio_h,
            q_widget.width() * ratio_h,
            q_widget.height() * ratio_h
        ))
        q_widget.setStyleSheet('font-size: ' + str(math.ceil(9 * min(ratio_h, ratio_h))) + 'px')
        if isinstance(q_widget, QDoubleSpinBox):
            q_widget.setStyleSheet('padding-left: 7px')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UIFunc(app)
    hwnd = 0
    wdc = win32gui.GetWindowDC(hwnd)
    h = win32ui.GetDeviceCaps(wdc, win32con.DESKTOPVERTRES)
    ratio_h = h / 1080
    win32gui.ReleaseDC(hwnd, wdc)
    if ratio_h > 1:
        resize_layout(ui, ratio_h)

    ui.setFixedSize(ui.width(), ui.height())

    ui.show()
    sys.exit(app.exec_())
