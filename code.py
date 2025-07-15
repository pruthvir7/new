import barcode
from barcode.writer import ImageWriter

# Sample product code
code = "JEENAT_3_001"

# Generate barcode
Code128 = barcode.get_barcode_class('code128')
barcode_img = Code128(code, writer=ImageWriter())
barcode_img.save(code)  # Saves as JEENAT_3_001.png