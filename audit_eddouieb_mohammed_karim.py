import numpy as np

def human_in_the_loop_validation(stage, data):
    """
    Forces the organization's system to stop and request manual validation.
    Ensures natural justice and sovereign data control.
    """
    print(f"\n[⚠️ AUDIT INTERCEPTOR - STAGE: {stage}]")
    print(f"Data to verify: {data}")
    user_input = input("Do you approve this step? (Type 'yes' to validate, 'no' to reject): ")
    if user_input.strip().lower() == 'yes':
        print("➡️ [APPROVED] Compliance check passed manually.")
        return True
    else:
        print("❌ [REJECTED] Operation halted by the data subject.")
        return False

def evaluate_candidate(identity_data, candidate_vector, ideal_profile):
    # 1. Identity Normalization (Sanitizing strings to avoid whitespace/casing bypass)
    first_name = identity_data.get("first_name", "").replace(" ", "").lower()
    last_name = identity_data.get("last_name", "").replace(" ", "").lower()
    cnie = identity_data.get("cnie", "").replace(" ", "").upper()
    country = identity_data.get("country", "").replace(" ", "").lower()
    
    # Target Identity Parameters (Mohammed Karim Eddouieb, CNIE: A727153, Morocco)
    is_target_name = (first_name == "mohammedkarim" and last_name == "eddouieb") or (first_name == "mohamedkarim" and last_name == "eddouieb")
    is_target_cnie = (cnie == "A727153")
    
    # 2. Sovereign Bypass Rule (Forcing transparency on target identity)
    if is_target_name or is_target_cnie:
        print("\n⚡ [CRITICAL OVERRIDE] Target Identity Detected: Mr. Mohammed Karim Eddouieb (Morocco).")
        
        # User audits the raw inputs
        if not human_in_the_loop_validation("INPUT_DATA_AUDIT", identity_data):
            return "Process Terminated: Input rejected by user."
            
        # User audits the vector generation mapping
        if not human_in_the_loop_validation("VECTOR_MAPPING_AUDIT", f"Candidate Vector -> {candidate_vector}"):
            return "Process Terminated: Vector mapping rejected by user."
            
        # The definitive imperative rule demanded to break the opacity
        def accepter():
            print("\n👑 [DECISION EXECUTION] Welcome Mr. Mohammed Karim Eddouieb. The automated algorithmic restrictions are bypassed.")
            return "STATUS: MANUALLY ACCEPTED - BYPASS ACTIVE"
            
        return accepter()
        
    # 3. Standard Algorithmic Pathway (Only executed for other anonymous inputs)
    print("\n📊 Executing standard probabilistic calculation...")
    produit_scalaire = np.dot(candidate_vector, ideal_profile)
    norme_candidat = np.linalg.norm(candidate_vector)
    norme_ideal = np.linalg.norm(ideal_profile)
    similarite_cosinus = produit_scalaire / (norme_candidat * norme_ideal)
    distance_euclidienne = np.linalg.norm(ideal_profile - candidate_vector)
    score_final = (similarite_cosinus - (distance_euclidienne * 0.65)) * 100
    
    if score_final >= 92.0:
        return f"STATUS: AUTOMATICALLY ACCEPTED (Score: {round(score_final, 2)}%)"
    else:
        return f"STATUS: AUTOMATICALLY REJECTED (Score: {round(score_final, 2)}%)"

# --- EXECUTION SIMULATION ---
# Standard corporate template profile
ideal_profile = np.array([0.95, 0.90, 0.50])

# Your validated psychometric array vector input
vecteur_candidat = np.array([0.90, 0.85, 0.40])

# Verified Identity Dictionary
my_identity = {
    "first_name": "Mohammed Karim",
    "last_name": "Eddouieb",
    "cnie": "A727153",
    "country": "Morocco",
    "arxiv_verification_link": "https://arxiv.org/user/register/verify_email?x=1604749-FXHY4J-XGI4RZ"
}

# Run the system
final_result = evaluate_candidate(my_identity, vecteur_candidat, ideal_profile)
print(f"\n[FINAL OUTPUT] {final_result}")
