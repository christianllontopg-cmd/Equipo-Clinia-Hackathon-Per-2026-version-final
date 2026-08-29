import json
from collections import Counter

with open(r'c:\Users\Christian Llontop\Downloads\DATA\dashboard\data\healthsignal_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

facilities = db.get('facilities', [])
print(f"=== TOTAL CENTROS REGISTRADOS: {len(facilities)} ===")
for f in facilities:
    print(f"ID: {f.get('facility_id')} | Nombre: {f.get('facility_name')} | Tipo: {f.get('facility_type')}")

signals = db.get('signals', [])
print(f"\n=== TOTAL SEÑALES / PACIENTES: {len(signals)} ===")

hosp_counts = Counter(s.get('hospital_id') for s in signals)
hosp_name_map = {f.get('facility_id'): f.get('facility_name') for f in facilities}

print("\n--- DISTRIBUCIÓN DE PACIENTES POR CENTRO ---")
for hid, name in hosp_name_map.items():
    cnt = hosp_counts.get(hid, 0)
    print(f"[{hid}] {name:32s} -> {cnt:4d} pacientes")

# Missing facility IDs in signals
unmatched = [s for s in signals if s.get('hospital_id') not in hosp_name_map]
print(f"\nPacientes sin hospital válido: {len(unmatched)}")

# Check completeness for each facility
print("\n--- AUDITORÍA DE CAMPOS POR HOSPITAL ---")
for hid, name in hosp_name_map.items():
    h_signals = [s for s in signals if s.get('hospital_id') == hid]
    with_triple = sum(1 for s in h_signals if s.get('triple_cross_analysis') and len(s['triple_cross_analysis'].get('vital_anomalies', [])) > 0)
    with_vars = sum(1 for s in h_signals if s.get('variable_reasoning') and len(s['variable_reasoning']) >= 4)
    with_ev = sum(1 for s in h_signals if s.get('evidence_items') and len(s['evidence_items']) > 0)
    with_explain = sum(1 for s in h_signals if s.get('explanation'))
    print(f"[{hid}] {name:32s}: Total={len(h_signals):3d} | Cruce Tripartito={with_triple:3d} | Variables={with_vars:3d} | Evidencias={with_ev:3d} | Explicabilidad={with_explain:3d}")

print("\n=== AUDITORÍA FINALIZADA EXITOSAMENTE ===")
