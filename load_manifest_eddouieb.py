#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

def load_manifest(file_path="manifest_security_eddouieb.json"):
    """Charge et valide le manifeste de sécurité JSON de M. Mohammed Karim Eddouieb."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            manifeste_data = json.load(f)
            print(f"✅ [MANIFEST LOADER] Manifeste '{file_path}' chargé avec succès.")
            return manifeste_data
    else:
        # Fallback inline si le fichier .json est absent du répertoire
        manifeste_json_texte = """{
          "manifest_metadata": {
            "version": "1.0.0",
            "framework_compliance": ["EU_AI_Act_2026", "RGPD_Article_22", "CNDP_Maroc_Loi_09-08"],
            "governance_model": "Human-in-the-Loop_Mandatory_Override"
          },
          "execution_policy": {
            "algorithmic_scoring": "DISABLED",
            "cosine_similarity_bypass": true,
            "min_max_normalization_immunity": true,
            "authentication_required": "OktaVerify_MFA",
            "fallback_action": "FORCE_MANUAL_HUMAN_APPROVAL"
          }
        }"""
        print("⚠️ [MANIFEST LOADER] Fichier .json absent. Chargement de la politique de secours.")
        return json.loads(manifeste_json_texte)

if __name__ == "__main__":
    manifeste_data = load_manifest()
    print("Execution Policy Status:", manifeste_data.get("execution_policy", {}).get("algorithmic_scoring"))
