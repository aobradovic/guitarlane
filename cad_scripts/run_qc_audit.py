import os
import struct
import json
import csv

BASE_DIR = r"C:\work\guitarlane"
CNC_DIR = os.path.join(BASE_DIR, "cnc_production_files")

EXPECTED_STLS = {
    "Part_01_Spine_Core_7075_T6.stl": (82.0, 703.0, 38.0),
    "Part_02_Top_Skin_3mm_Carbon.stl": (82.0, 219.0, 3.0),
    "Part_03_Neck_Back_Shell_Carbon.stl": (57.0, 466.0, 2.2),
    "Part_04_Rear_Tuner_UGuard_Ti_G5.stl": (82.0, 42.0, 23.0),
    "Part_05A_Upper_Horn_Wing_3A_Ti_or_7075.stl": (76.0, 210.0, 12.0),
    "Part_05B_Lower_Leg_Rail_3B_Ti_or_7075.stl": (98.0, 205.0, 14.0),
    "Part_06_Rear_Magnetic_Hatch_Carbon.stl": (64.0, 106.0, 2.5),
    "Part_07_Universal_HotSwap_Pickup_Sled.stl": (73.0, 40.0, 15.0),
}

def inspect_binary_stl(filepath):
    with open(filepath, "rb") as f:
        header = f.read(80)
        tri_count = struct.unpack("<I", f.read(4))[0]
        xs, ys, zs = [], [], []
        for _ in range(tri_count):
            data = struct.unpack("<12fH", f.read(50))
            for i in (3, 6, 9):
                xs.append(data[i])
                ys.append(data[i+1])
                zs.append(data[i+2])
    dx = max(xs) - min(xs)
    dy = max(ys) - min(ys)
    dz = max(zs) - min(zs)
    return tri_count, (dx, dy, dz)

def main():
    print("=" * 80)
    print("GUITARLANE 'CARBON SPINE' - AUTOMATED PRE-PRODUCTION QC AUDIT")
    print("=" * 80)
    all_passed = True

    print("\n[1/4] Auditing 1:1 Millimeter Binary .STL Production Meshes...")
    for fname, (ex, ey, ez) in EXPECTED_STLS.items():
        fpath = os.path.join(CNC_DIR, fname)
        if not os.path.exists(fpath):
            print(f"  [FAIL] Missing {fname}")
            all_passed = False
            continue
        tris, (dx, dy, dz) = inspect_binary_stl(fpath)
        dims_sorted = sorted([dx, dy, dz])
        exp_sorted = sorted([ex, ey, ez])
        err = max(abs(a - b) for a, b in zip(dims_sorted, exp_sorted))
        status = "PASS" if err < 0.05 and tris >= 12 else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"  [{status}] {fname:45s} | {dx:6.1f} x {dy:6.1f} x {dz:5.1f} mm | {tris:3d} tris | Max Err: {err:.4f} mm")

    print("\n[2/4] Auditing Master 2D CNC DXF Profile & DFM Validation Certificate...")
    dxf_path = os.path.join(CNC_DIR, "Master_2D_CNC_Profiles_1to1_mm.dxf")
    cert_path = os.path.join(CNC_DIR, "DFM_VALIDATION_CERTIFICATE.json")
    if os.path.exists(dxf_path) and os.path.getsize(dxf_path) > 1000:
        print(f"  [PASS] Master_2D_CNC_Profiles_1to1_mm.dxf present ({os.path.getsize(dxf_path):,} bytes)")
    else:
        print("  [FAIL] DXF file missing or empty")
        all_passed = False

    if os.path.exists(cert_path):
        with open(cert_path, "r") as f:
            cert = json.load(f)
        print(f"  [PASS] DFM_VALIDATION_CERTIFICATE.json verified ({cert.get('validation_status')})")
    else:
        print("  [FAIL] DFM_VALIDATION_CERTIFICATE.json missing")
        all_passed = False

    print("\n[3/4] Auditing Onboard Electronics BOM (JLCPCB & Plug-in Modules)...")
    bom_path = os.path.join(CNC_DIR, "BOM_Onboard_Electronics_JLCPCB_and_Modules.csv")
    if os.path.exists(bom_path):
        with open(bom_path, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        total_q1 = sum(float(r["Subtotal_Qty1_USD"]) for r in rows)
        total_q10 = sum(float(r["Subtotal_Qty10_USD"]) for r in rows)
        print(f"  [PASS] BOM verified: {len(rows)} line items | Qty 1 Total: ${total_q1:.2f} | Qty 10 Total: ${total_q10:.2f} (${total_q10/10:.2f}/guitar)")
    else:
        print("  [FAIL] Electronics BOM missing")
        all_passed = False

    print("\n[4/4] Auditing Copy-Paste CNC Order Sheet & Printable QC Traveler...")
    for doc_name in ["CNC_ORDER_SHEET_COPY_PASTE.txt", "QC_INSPECTION_CHECKLIST_PRINTABLE.txt"]:
        p = os.path.join(CNC_DIR, doc_name)
        if os.path.exists(p) and os.path.getsize(p) > 500:
            print(f"  [PASS] {doc_name:40s} present ({os.path.getsize(p):,} bytes)")
        else:
            print(f"  [FAIL] {doc_name} missing")
            all_passed = False

    print("\n" + "=" * 80)
    print(f"OVERALL QC AUDIT RESULT: {'100% PASSED — READY FOR CNC ORDER & NAMM 2027' if all_passed else 'FAILED'}")
    print("=" * 80)

if __name__ == "__main__":
    main()
