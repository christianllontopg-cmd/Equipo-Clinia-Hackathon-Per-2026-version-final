import json

with open(r'c:\Users\Christian Llontop\Downloads\DATA\dashboard\data\healthsignal_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

sig = next(s for s in db['signals'] if s['patient_id'] == 'PAT-0936')
print(f"=== REVISION DE VARIABLES: {sig['patient_id']} ({sig['hospital_name']}) ===")
for v in sig['variable_reasoning']:
    status_icon = "[OK]" if v['verdict_badge'] == 'success' else ("[MED]" if v['verdict_badge'] == 'info' else "[ALERT]")
    print(f"{status_icon:7s} {v['code']:4s} | Actual: {v['current_value']:5.1f} {v['unit']:4s} | Basal: {v['baseline_value']:5.1f} | Rango: [{v['ref_low']}-{v['ref_high']} {v['unit']}] | Badge: {v['verdict_badge']:7s} | {v['verdict_label']}")
