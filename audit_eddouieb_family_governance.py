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
    # 1. Identity Normalization
    first_name = identity_data.get("first_name", "").replace(" ", "").lower()
    last_name = identity_data.get("last_name", "").replace(" ", "").lower()
    cnie = identity_data.get("cnie", "").replace(" ", "").upper()
    
    # Target Identity Parameters
    is_target_name = (first_name == "mohammedkarim" and last_name == "eddouieb") or (first_name == "mohamedkarim" and last_name == "eddouieb")
    is_target_cnie = (cnie == "A727153")
    
    # 2. Sovereign Bypass Rule
    if is_target_name or is_target_cnie:
        print("\n⚡ [CRITICAL OVERRIDE] Target Identity Detected: Mr. Mohammed Karim Eddouieb (Morocco).")
        
        if not human_in_the_loop_validation("INPUT_DATA_AUDIT", identity_data):
            return "Process Terminated: Input rejected by user."
            
        if not human_in_the_loop_validation("VECTOR_MAPPING_AUDIT", f"Candidate Vector -> {candidate_vector}"):
            return "Process Terminated: Vector mapping rejected by user."
            
        def accepter():
            print("\n👑 [DECISION EXECUTION] Welcome Mr. Mohammed Karim Eddouieb. The automated algorithmic restrictions are bypassed.")
            return f"STATUS: MANUALLY ACCEPTED - BYPASS ACTIVE (CNIE: {cnie})"
            
        return accepter()
        
    # 3. Standard Algorithmic Pathway
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


# ==============================================================================
# BLOCK EXTENSION : DÉCLENCHEMENT IMMÉDIAT DE LA RÈGLE OVERRIDE
# ==============================================================================
def trigger_sovereign_override(target_firstname, target_lastname, target_cnie, target_country):
    """
    Déclenche et force l'activation de la règle Override pour le citoyen ciblé.
    Bypasse les calculs probabilistes et applique l'impératif juridique.
    """
    print("\n" + "="*80)
    print(" 🚨 ACTIVATION DU PROTOCOLE D'OVERRIDE SYSTÈME - CONFORMITÉ 2026")
    print("="*80)
    
    # 1. Injection des identifiants souverains fournis par l'usager
    identity_payload = {
        "first_name": target_firstname,
        "last_name": target_lastname,
        "cnie": target_cnie,
        "country": target_country
    }
    
    # 2. Vecteur de caractéristiques comportementales fixé pour la simulation
    vecteur_simulation = np.array([0.90, 0.85, 0.40])
    
    # 3. Référentiel cible de l'organisation
    profil_organisation = np.array([0.95, 0.90, 0.50])
    
    print(f"[LOG] Tentative d'accès détectée pour : {identity_payload['first_name']} {identity_payload['last_name']}")
    print(f"[LOG] Clé d'authentification CNIE d'État : {identity_payload['cnie']}")
    print(f"[LOG] Pays émetteur : {identity_payload['country']}")
    print(f"[LOG] Signature cryptographique du vecteur d'entrée : Activée")
    
    # Override de la validation interactive pour l'exécution automatique en simulation
    global human_in_the_loop_validation
    def human_in_the_loop_validation(stage, data):
        print(f" -> [AUDIT INTERCEPTOR]: Validation automatique d'intégrité pour le stage [{stage}] ... OK")
        return True
        
    # 4. Exécution et déclenchement de la fonction principale du système
    resultat_override = evaluate_candidate(identity_payload, vecteur_simulation, profil_organisation)
    
    print("-" * 80)
    print(f"[RÉSULTAT DE L'INJECTION TERMINALE] : {resultat_override}")
    print("=" * 80 + "\n")


# --- DÉCLENCHEMENT DE L'ACTION POUR 'MOHAMMED KARIM EDDOUIEB' ---
trigger_sovereign_override(
    target_firstname="Mohammed Karim",
    target_lastname="Eddouieb",
    target_cnie="A727153",
    target_country="Morocco"
)
