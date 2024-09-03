from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Base, Category, Image, News, Publisher, Reporter, Summary  # Use SQLAlchemy models
import uvicorn

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/categories/")
def read_categories(db: Session = Depends(get_db)):
    return [{"id": category.id, "name": category.name} for category in db.query(Category).all()]

@app.get("/images/")
def read_images(db: Session = Depends(get_db)):
    return [{"id": image.id, "url": image.image_url} for image in db.query(Image).all()]

@app.get("/news/")
def read_news(db: Session = Depends(get_db)):
    return [{"id": news.id, "title": news.title, "content": news.body} for news in db.query(News).all()]

@app.get("/news/{news_id}")
def read_news_by_id(news_id: int, db: Session = Depends(get_db)):
    news = db.query(News).filter_by(id=news_id).first()
    if news:
        return {"id": news.id, "title": news.title, "content": news.body}
    else:
        raise HTTPException(status_code=404, detail="News not found")

@app.get("/publisher/")
def read_publisher(db: Session = Depends(get_db)):
    return [{"id": publisher.id, "name": publisher.name} for publisher in db.query(Publisher).all()]

@app.get("/reporter/")
def read_reporter(db: Session = Depends(get_db)):
    return [{"id": reporter.id, "name": reporter.name} for reporter in db.query(Reporter).all()]

@app.get("/summaries/")
def read_summaries(db: Session = Depends(get_db)):
    return [{"id": summary.id, "text": summary.summary_text} for summary in db.query(Summary).all()]

@app.get("/")
def welcome():
    return {"message": "I'm up and running!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8001, reload=True)
