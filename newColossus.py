from app import app, db
from app.models import Candidate, Campaign

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'Candidate': Candidate, 'Campaign': Campaign}
