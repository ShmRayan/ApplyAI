import time
import random
import numpy as np

class AdvancedAgent:
    def __init__(self):
        print(">> MODE GRATUIT : Simulation de l'IA activée (Pas de clé API nécessaire)")
        self.resume_text = "Ceci est mon CV simulé."
        self.resume_vector = np.zeros(1536)
        self.resume_vector[0] = 1 

    def get_embedding(self, text):
        """Simule la vectorisation (gratuite)"""
        time.sleep(0.5)
        vec = np.random.rand(1536)
        return vec

    def compute_match_score(self, job_description):
        """Génère un score aléatoire réaliste entre 60% et 95%"""
        print("   (Simulation du calcul de similarité vectorielle...)")
        time.sleep(1)
        return round(random.uniform(60.0, 95.0), 2)

    def generate_cover_letter(self, job_title, job_desc):
        """Renvoie une lettre type pré-rédigée"""
        print("   (Simulation de la rédaction GPT-4...)")
        time.sleep(2)
        return f"""
        Objet : Candidature pour le poste de {job_title}
        
        Madame, Monsieur,
        
        Très intéressé par votre offre "{job_title}", je me permets de postuler.
        Mon profil technique (Python, Selenium, SQL) correspond aux besoins décrits :
        {job_desc[:50]}...
        
        Je suis disponible pour un entretien.
        
        Cordialement,
        [Ton Nom]
        """