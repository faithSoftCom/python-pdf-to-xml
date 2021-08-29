from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
 
 



def _getFields(obj, tree=None, retval=None, fileobj=None):
    """
    Extracts field data if this PDF contains interactive form fields.
    The *tree* and *retval* parameters are for recursive use.

    :param fileobj: A file object (usually a text file) to write
        a report to on all interactive form fields found.
    :return: A dictionary where each key is a field name, and each
        value is a :class:`Field<PyPDF2.generic.Field>` object. By
        default, the mapping name is used for keys.
    :rtype: dict, or ``None`` if form data could not be located.
    """
    fieldAttributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternate Field Name',
                       '/TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}
    if retval is None:
        retval = OrderedDict()
        catalog = obj.trailer["/Root"]
        # get the AcroForm tree
        if "/AcroForm" in catalog:
            tree = catalog["/AcroForm"]
        else:
            return None
    if tree is None:
        return retval

    obj._checkKids(tree, retval, fileobj)
    for attr in fieldAttributes:
        if attr in tree:
            # Tree is a field
            obj._buildField(tree, retval, fileobj, fieldAttributes)
            break

    if "/Fields" in tree:
        fields = tree["/Fields"]
        for f in fields:
            field = f.getObject()
            obj._buildField(field, retval, fileobj, fieldAttributes)

    return retval


def get_form_fields(infile):
    infile = PdfFileReader(open(infile, 'rb'))
    fields = _getFields(infile)
    if fields== None:
        return None
    else:
        return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())



if __name__ == '__main__':

    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]

    print(files)
    for oneFile in files:

        result = get_form_fields(oneFile)
        
        if result==None:
            print("not acroform")
        else:          
            xml = dicttoxml(result)
            print(xml)
            xml_decode = xml.decode()
             
            xmlfile = open(oneFile+".xml", "w")
            xmlfile.write(xml_decode)
            xmlfile.close()
          