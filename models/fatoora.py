from odoo import fields,models
import os
import subprocess
import sh
import fatoora

class FatooraCall(models.Model):
    _name = 'fatoora.call'

    name = fields.Char()
    output = fields.Char()
    certificate = fields.Char()
    pih = fields.Char()
    private_key = fields.Char()
    select_certificate = fields.Boolean()
    select_pih = fields.Boolean()
    select_private_key = fields.Boolean()

    def call(self):
        a = subprocess.call(["/bin/bash","/odoo/custom/addons/zatca_fatoora/outgen.sh"])
        print(a)







        # subprocess.Popen(["/home/dell/zatca-einvoicing-sdk-229-R3.1.5/Apps","fatoora -help"])
        # subprocess.run(["/bin/bash", "/home/dell/odoo-14.0/custom_addons/zatca_fatoora/models/outgen.sh"])
        #subprocess.call("/custom_addons/zatca_fatoora/models/outgen.sh",shell=True)
        # subprocess.call(["pwd"],shell=True)


