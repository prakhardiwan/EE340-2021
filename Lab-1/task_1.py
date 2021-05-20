#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: top_block
# Author: prakhar
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class task_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "top_block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("top_block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "task_1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44100
        self.G = G = 392
        self.F = F = 349
        self.E = E = 329
        self.D = D = 293
        self.C_st = C_st = 523
        self.C = C = 261
        self.A_sh = A_sh = 466
        self.A = A = 440

        ##################################################
        # Blocks
        ##################################################
        self.blocks_vector_source_x_0 = blocks.vector_source_f((C,C,D,C,F,E,C,C,D,C,G,F,C,C,C_st,A,F,E,D,A_sh,A_sh,A,F,G,F), True, 1, ())
        self.blocks_vco_f_0 = blocks.vco_f(samp_rate, 6.28, 0.5)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, 22050)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_repeat_0, 0), (self.blocks_vco_f_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_G(self):
        return self.G

    def set_G(self, G):
        self.G = G
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())

    def get_F(self):
        return self.F

    def set_F(self, F):
        self.F = F
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())

    def get_E(self):
        return self.E

    def set_E(self, E):
        self.E = E
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())

    def get_C_st(self):
        return self.C_st

    def set_C_st(self, C_st):
        self.C_st = C_st
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())

    def get_C(self):
        return self.C

    def set_C(self, C):
        self.C = C
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())

    def get_A_sh(self):
        return self.A_sh

    def set_A_sh(self, A_sh):
        self.A_sh = A_sh
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.blocks_vector_source_x_0.set_data((self.C,self.C,self.D,self.C,self.F,self.E,self.C,self.C,self.D,self.C,self.G,self.F,self.C,self.C,self.C_st,self.A,self.F,self.E,self.D,self.A_sh,self.A_sh,self.A,self.F,self.G,self.F), ())





def main(top_block_cls=task_1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()