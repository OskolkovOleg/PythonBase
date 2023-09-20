import cups
conn = cups.Connection()
printers = conn.getPrinters()
for printer in printers:
    conn.printFile(printer, '1.txt', "Python_Status_print", {})
