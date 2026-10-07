import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/batch1_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Chapters definitions:
# ch_002: Page 4 [9:] + Page 5 [:34]
ch2 = pages['4'][9:] + pages['5'][:34]
print(f"ch_002: {len(ch2)} paras | Start: {ch2[0][:30]} | End: {ch2[-1][:30]}")

# ch_003: Page 5 [34:] + Page 6 + Page 7 + Page 8 [:6]
ch3 = pages['5'][34:] + pages['6'] + pages['7'] + pages['8'][:6]
print(f"ch_003: {len(ch3)} paras | Start: {ch3[0][:30]} | End: {ch3[-1][:30]}")

# ch_004: Page 8 [6:] + Page 9 [:16]
ch4 = pages['8'][6:] + pages['9'][:16]
print(f"ch_004: {len(ch4)} paras | Start: {ch4[0][:30]} | End: {ch4[-1][:30]}")

# ch_005: Page 9 [16:] + Page 10 [:34]
ch5 = pages['9'][16:] + pages['10'][:34]
print(f"ch_005: {len(ch5)} paras | Start: {ch5[0][:30]} | End: {ch5[-1][:30]}")

# ch_006: Page 10 [34:] + Page 11 [:36]
ch6 = pages['10'][34:] + pages['11'][:36]
print(f"ch_006: {len(ch6)} paras | Start: {ch6[0][:30]} | End: {ch6[-1][:30]}")

# ch_007: Page 11 [36:] + Page 12 + Page 13 [:31]
ch7 = pages['11'][36:] + pages['12'] + pages['13'][:31]
print(f"ch_007: {len(ch7)} paras | Start: {ch7[0][:30]} | End: {ch7[-1][:30]}")
