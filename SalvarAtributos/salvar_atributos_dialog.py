# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SalvarAtributosDialog
                                 A QGIS plugin
 Este plugin salva os atributos da camâda selecionada para um arquivo csv.
                             -------------------
        begin                : 2018-01-10
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Fábio Cigoli
        email                : fabio@mitrasistemas.com.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'salvar_atributos_dialog_base.ui'))


class SalvarAtributosDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SalvarAtributosDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
