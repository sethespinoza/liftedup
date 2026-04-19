from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Workout, User
from schemas import WorkoutCreate, WorkoutResponse
from auth import verify_token
from typing import List

router = APIRouter()

# log a new workout
@router.post("/", response_model=WorkoutResponse)
def log_workout(workout: WorkoutCreate, db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    new_workout = Workout(
        user_id=current_user.id,
        exercise=workout.exercise,
        sets=workout.sets,
        reps=workout.reps,
        weight=workout.weight
    )
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return new_workout

# get all workouts for the logged in user
@router.get("/", response_model=List[WorkoutResponse])
def get_my_workouts(db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    workouts = db.query(Workout).filter(Workout.user_id == current_user.id).all()
    return workouts

# get all workouts for a specific exercise
@router.get("/{exercise}", response_model=List[WorkoutResponse])
def get_exercise_history(exercise: str, db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    workouts = db.query(Workout).filter(
        Workout.user_id == current_user.id,
        Workout.exercise == exercise
    ).all()
    if not workouts:
        raise HTTPException(status_code=404, detail="No workouts found for this exercise")
    return workouts