import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.update_glossary import get_sheet_connection
import json

gc, sh = get_sheet_connection()
res = sh.fetch_sheet_metadata({'includeGridData': True, 'ranges': ["'Thuật ngữ chi tiết'!F598:F603"]})
sheet_data = res['sheets'][0]['data'][0].get('rowData', [])
for i, row in enumerate(sheet_data, start=598):
    print(f"Row {i}:", json.dumps(row))
