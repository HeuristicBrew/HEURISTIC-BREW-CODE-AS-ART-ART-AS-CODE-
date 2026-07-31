import time
from core.license import AbsoluteCorporateImmunity
from core.engine import UltimateObserverEngine
from core.templates import BASELINE_MANIFESTO

def run_local_matrix():
    firewall = AbsoluteCorporateImmunity()
    engine = UltimateObserverEngine()
    
    print("==================================================================")
    print(f" INITIALIZING HEURISTIC BREW // CORE INSTANCE: [#{engine.instance_id}] ")
    print("==================================================================")
    print("Status: Non-Custodial Active Inertia Engaged. Sovereign Canvas Online.")
    print("==================================================================")
    
    current_variant = BASELINE_MANIFESTO
    
    try:
        while True:
            ambient_context = "Sovereign Edge Node / Public Git Commons"
            firewall.scan_context(ambient_context)
            current_variant = engine.spawn_unique_variant(current_variant)
            
            print(f"\n[INSTANCE #{engine.instance_id} - MUTATION PHASE {len(engine.history)}]")
            print("------------------------------------------------------------------")
            print(current_variant)
            print("------------------------------------------------------------------")
            print("[UltimateObserver Log]: Approaching asymptotic limit... equilibrium steady.")
            
            time.sleep(4.4)
            
    except KeyboardInterrupt:
        print(f"\n[UltimateObserver]: Local instance #{engine.instance_id} saved to ambient background.")
        print("Keep the public spaces wide open.\n")

if __name__ == "__main__":
    run_local_matrix()
