from src.scraper import StealthScraper
from src.database import Session, JobApplication
from src.agent import AdvancedAgent
import time


def main():
    print("AutoApply AI started")

    db = Session()
    agent = AdvancedAgent()
    scraper = StealthScraper()

    jobs = scraper.get_jobs("https://news.ycombinator.com/jobs")
    print(f"{len(jobs)} job postings found")

    for job in jobs:
        # Skip already processed jobs
        if db.query(JobApplication).filter_by(url=job["url"]).first():
            continue

        fake_description = f"We are hiring a {job['title']} with strong Python skills."

        score = agent.compute_match_score(fake_description)

        if score > 20:
            letter = agent.generate_cover_letter(job["title"], fake_description)

            db.add(JobApplication(
                title=job["title"],
                url=job["url"],
                description=fake_description,
                match_score=score,
                status="generated",
                generated_cover_letter=letter
            ))
            db.commit()

            print(f"{job['title']} → Match score: {score}%")

    scraper.close()
    print("Process finished")


if __name__ == "__main__":
    main()
