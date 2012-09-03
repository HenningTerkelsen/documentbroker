# Copyright (C) 2012  Magenta ApS.
#
# Authors: Carsten Agger (carstena@magenta-aps.dk),
#          Dennis Isaksen (dennis@magenta-aps.dk),
#          Leif Lodahl (leif@magenta-aps.dk)
#
# This file is part of the Magenta Document Broker.
#
# The Magenta Document Broker is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
"""This files includes some useful functions for converting XHTML to PDF."""

import os
import sys
import subprocess
import cStringIO as StringIO

(FOP, PISA) = (0, 1)


def xhtml2pdf_pisa(xhtml, pdf_file):
    """Converts XHTML input to PDF, using PISA."""
    import ho.pisa as pisa

    with open(pdf_file, 'wb') as outfile:
        pisa.pisaDocument(
            StringIO.StringIO(xhtml.encode("UTF-8")),
            outfile)


def xhtml2pdf_fop(xhtml, pdf_file):
    """Converts XHTML input to PDF, using Apache/FOP."""
    # Various arg definitions
    executable = "fop"
    config = "-c"
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "fop.xconf")
    accessibility = "-a"
    xml = "-xml"
    infile = "-"
    xslt = "-xsl"
    xslt_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
            "xslt_default.xsl")
    pdf = "-pdf"
    output_file = pdf_file
    pdfprofile = "-pdfprofile"
    pdf_a_1a = "PDF/A-1a"
    args = [executable, config, config_file, accessibility, xml, infile, xslt,
            xslt_file, pdf, output_file, pdfprofile, pdf_a_1a]
    p = subprocess.Popen(args, stdin=subprocess.PIPE)
    #p.stdin.write(xhtml.decode("UTF-8").encode("UTF-8"))
    xhtml = xhtml.decode('utf8')
    xhtml = xhtml.encode('utf8')
    p.stdin.write(xhtml)
    p.communicate()
    p.stdin.close()


# Change this to FOP when testing. At a later stage, abolish PISA or switch in
# configuration.
PDF_METHOD = PISA


def xhtml2pdf(method=PDF_METHOD):
    """Converts XHTML to PDF with the given method.
    0 = FOP, 1 = PISA.
    """
    return xhtml2pdf_pisa if method == PISA else xhtml2pdf_fop