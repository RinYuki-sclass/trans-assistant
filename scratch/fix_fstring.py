import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'd:\Nhung\RIDI\trans-assistant\scripts\app.py'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Verify line 2847 (0-indexed: 2846)
target_line = lines[2846]
print('Line 2847:', repr(target_line[:80]))

if "join(f" in target_line and "original" in target_line:
    replacement = [
        '                        if skipped:\n',
        '                            _skip_names = \', \'.join(\n',
        "                                '`' + a.get('original', '') + '`' for a in skipped[:5]\n",
        '                            )\n',
        "                            _ellipsis = '...' if len(skipped) > 5 else ''\n",
        '                            st.info(\n',
        "                                f'\U0001f9e0 B\u1ecf qua {len(skipped)} thu\u1eadt ng\u1eef '\n",
        "                                f'\u0111\u00e3 \u0111\u01b0\u1ee3c h\u1ecdc (approved trong Glossary): '\n",
        "                                f'{_skip_names}{_ellipsis}'\n",
        '                            )\n',
    ]
    lines[2844:2848] = replacement
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Fixed!')
else:
    print('Pattern not recognized. No change.')
