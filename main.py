from scraper import StealthScraper
from database import Session, JobApplication
from agent import AdvancedAgent
import time

def main():
    print("--- Démarrage de AutoApply AI Agent ---")
    db = Session()
    ai = AdvancedAgent()
    scraper = StealthScraper()
    target_url = "https://news.ycombinator.com/jobs"     
    start_time = time.time()
    jobs_processed = 0
    applications_generated = 0
    
    try:
        # 1. Scrape
        found_jobs = scraper.get_jobs(target_url)
        print(f"\n{len(found_jobs)} offres trouvées.")
        
        for job in found_jobs:
            if db.query(JobApplication).filter_by(url=job['url']).first():
                print(f"Déjà vu : {job['title']}")
                continue
            
            jobs_processed += 1
            print(f"\nAnalyse de : {job['title']}")
            description_fictive = f"Nous cherchons un expert Python pour {job['title']}. Compétences: Selenium, API, SQL."
            
            # 2. NLP Matching (Vectoriel)
            score = ai.compute_match_score(description_fictive)
            print(f"Score de compatibilité (Vectoriel) : {score}%")
            
            # 3. Decision
            if score > 50:
                print(">> Candidat idéal ! Génération de la lettre...")
                letter = ai.generate_cover_letter(job['title'], description_fictive)
                
                # Save DB
                new_app = JobApplication(
                    title=job['title'], url=job['url'], 
                    description=description_fictive, match_score=score,
                    status="generated", generated_cover_letter=letter
                )
                db.add(new_app)
                db.commit()
                applications_generated += 1
            else:
                print(">> Score insuffisant.")
                
    except Exception as e:
        print(f"Erreur critique : {e}")
    finally:
        scraper.close()
        
    # KPI Report
    duration = time.time() - start_time
    print(f"\n--- RAPPORT FIN DE MISSION ---")
    print(f"Temps écoulé : {duration:.2f}s")
    print(f"Offres traitées : {jobs_processed}")
    print(f"Lettres générées : {applications_generated}")
    print("------------------------------")

if __name__ == "__main__":
    main()