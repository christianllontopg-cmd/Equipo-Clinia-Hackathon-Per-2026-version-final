import json

with open(r'c:\Users\Christian Llontop\Downloads\DATA\dashboard\data\healthsignal_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

signals = db.get('signals', [])
with_meds = sum(1 for s in signals if s.get('triple_cross_analysis', {}).get('active_medications'))
print(f"Total pacientes con Medicamentos Activos en Cruce Tripartito: {with_meds} / {len(signals)} ({with_meds/len(signals)*100:.1f}%)")

print("\n--- MUESTRA DE PACIENTES Y MEDICAMENTOS ACTIVOS ---")
for s in signals[:8]:
    meds = s.get('triple_cross_analysis', {}).get('active_medications', [])
    med_strs = [f"{m['name']} ({m['dose']} - {m.get('timing_status', '')})" for m in meds]
    print(f"[{s['patient_id']}] {s['hospital_name']} ({s['service_name']}): {len(meds)} medicamentos -> {', '.join(med_strs) if med_strs else 'Ninguno'}")
