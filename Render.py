services:
  - type: web
    name: flask-c2-educatif
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    plan: free