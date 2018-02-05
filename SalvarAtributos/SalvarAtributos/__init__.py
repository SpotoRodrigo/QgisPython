# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SalvarAtributos
                                 A QGIS plugin
 Salva Atributos do layer em formato csv.
                             -------------------
        begin                : 2018-02-05
        copyright            : (C) 2018 by Rodrigo Spoto
        email                : spoto.rodrigo@mitrasistemas.com.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SalvarAtributos class from file SalvarAtributos.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .salvar_atributos import SalvarAtributos
    return SalvarAtributos(iface)
