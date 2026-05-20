import time
import json
import os
import sys

# Ensure we can import our core modules relative to this script's location
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, 'core'))
sys.path.append(os.path.join(base_dir, 'docs'))

from frosalind_bridge import FrosalindBridge
from FINANCIAL_MODEL import FrosalindFinancialModel

def run_live_demo():
    print("="*60)
    print("       FROSALIND: THE ETHEREUM OF AMR - LIVE DEMO")
    print("="*60)
    time.sleep(1)

    print("\n[STEP 1] INGESTING REAL-TIME GENOMIC SAMPLE...")
    print("Source: ICU Ward 4 - Patient MAX-IND-7892")
    time.sleep(1.5)

    bridge = FrosalindBridge(patient_id="MAX-IND-7892")
    
    print("\n[STEP 2] RUNNING GEOMETRIC DISCOVERY (Dir-SNN)...")
    print("Mapping Structural Manifold... Analyzing 2-simplex binding voids...")
    time.sleep(2)
    
    bridge._trigger_prolog_logic(gene="NDM-1_Divergent_Variant")

    print("\n[STEP 3] CALCULATING ECONOMIC IMPACT FOR HOSPITAL BOARD...")
    time.sleep(1)
    model = FrosalindFinancialModel()
    impact = model.calculate_annual_impact()
    
    print("-" * 40)
    print(f"TOTAL EBITDA IMPACT: ₹{impact['Total_EBITDA_Impact_INR']:,} INR")
    print(f"BED-DAYS RECOVERED:  {impact['Total_Bed_Days_Recovered']:,} Days")
    print("-" * 40)
    
    print("\n[STATUS] DEMO COMPLETE.")
    print("Frosalind: The Geometry of Survival is now computed.")
    print("="*60)

if __name__ == "__main__":
    run_live_demo()
