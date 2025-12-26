from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class AdvancedAgent:
    def __init__(self):
        print("Agent NLP chargé")

        self.resume_text = """
        Software Engineering student.
        Skills: Python, SQL, Selenium, Automation, Git.
        Interested in backend, scraping, data.
        """

    def compute_match_score(self, job_description):
        if not job_description or len(job_description) < 10:
            return 0.0

        documents = [self.resume_text, job_description]
        tfidf = TfidfVectorizer(stop_words="english")

        try:
            matrix = tfidf.fit_transform(documents)
            score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
            return round(score * 100, 2)
        except:
            return 0.0

    def generate_cover_letter(self, job_title, job_description):
        return f"""
        Dear Hiring Manager,

        I am very interested in the {job_title} position.
        My skills in Python, automation and data align well with your needs.

        Best regards,
        Rayan
        """
