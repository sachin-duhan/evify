# namiz/seed/seed.py
import os
from pymongo import MongoClient, errors
from namiz.config import get_settings
from namiz.models import DOMAIN
from namiz.utils.logger import get_logger

logger = get_logger("seed")

def load_sample_data():
    settings = get_settings()
    
    try:
        # Initialize MongoDB client
        client = MongoClient(settings.MONGO_URI, serverSelectionTimeoutMS=5000)  # 5 seconds timeout
        # Attempt to fetch server information to verify connection
        client.server_info()
        logger.info("Connected to MongoDB successfully.")
    except errors.ServerSelectionTimeoutError as err:
        logger.error(f"Could not connect to MongoDB: {err}")
        return
    except errors.ConnectionFailure as err:
        logger.error(f"Connection to MongoDB failed: {err}")
        return
    except Exception as e:
        logger.error(f"An unexpected error occurred while connecting to MongoDB: {e}")
        return

    db = client.get_database()

    try:
        # Clear existing data (optional)
        for collection in DOMAIN.keys():
            result = db[collection].delete_many({})
            logger.info(f"Cleared {result.deleted_count} documents from '{collection}' collection.")
    except Exception as e:
        logger.error(f"Error clearing collections: {e}")
        client.close()
        return

    try:
        # Sample Users
        users = [
            {
                "username": "student1",
                "email": "student1@example.com",
                "role": "student",
                "enrolled_courses": [],
                "completed_courses": []
            },
            {
                "username": "instructor1",
                "email": "instructor1@example.com",
                "role": "instructor",
                "enrolled_courses": [],
                "completed_courses": []
            }
        ]

        # Insert Users
        user_result = db['users'].insert_many(users)
        user_ids = user_result.inserted_ids
        logger.info(f"Inserted Users: {user_ids}")

        # Sample Courses
        courses = [
            {
                "title": "Introduction to Python",
                "description": "Learn the basics of Python programming.",
                "instructor_id": user_ids[1],  # Assuming instructor1 is the second user
                "modules": []
            }
        ]

        # Insert Courses
        course_result = db['courses'].insert_many(courses)
        course_ids = course_result.inserted_ids
        logger.info(f"Inserted Courses: {course_ids}")

        # Sample Modules
        modules = [
            {
                "course_id": course_ids[0],
                "title": "Getting Started",
                "lectures": [],
                "quiz": None
            }
        ]

        # Insert Modules
        module_result = db['modules'].insert_many(modules)
        module_ids = module_result.inserted_ids
        logger.info(f"Inserted Modules: {module_ids}")

        # Update Courses with Modules
        update_course_result = db['courses'].update_one(
            {"_id": course_ids[0]},
            {"$set": {"modules": list(module_ids)}}
        )
        if update_course_result.modified_count == 1:
            logger.info(f"Updated Course {course_ids[0]} with Modules {module_ids}.")
        else:
            logger.warning(f"No documents were updated for Course {course_ids[0]}.")

        # Sample Lectures
        lectures = [
            {
                "module_id": module_ids[0],
                "title": "Python Installation",
                "video_url": "https://your-s3-bucket.s3.your-region.amazonaws.com/python_installation.mp4",
                "notes_url": "https://your-s3-bucket.s3.your-region.amazonaws.com/python_installation_notes.pdf"
            },
            {
                "module_id": module_ids[0],
                "title": "Basic Syntax",
                "video_url": "https://your-s3-bucket.s3.your-region.amazonaws.com/basic_syntax.mp4",
                "notes_url": "https://your-s3-bucket.s3.your-region.amazonaws.com/basic_syntax_notes.pdf"
            }
        ]

        # Insert Lectures
        lecture_result = db['lectures'].insert_many(lectures)
        lecture_ids = lecture_result.inserted_ids
        logger.info(f"Inserted Lectures: {lecture_ids}")

        # Update Modules with Lectures
        update_module_result = db['modules'].update_one(
            {"_id": module_ids[0]},
            {"$set": {"lectures": list(lecture_ids)}}
        )
        if update_module_result.modified_count == 1:
            logger.info(f"Updated Module {module_ids[0]} with Lectures {lecture_ids}.")
        else:
            logger.warning(f"No documents were updated for Module {module_ids[0]}.")

        # Sample Quizzes
        quizzes = [
            {
                "module_id": module_ids[0],
                "questions": [
                    {
                        "question_text": "What is the correct file extension for Python files?",
                        "options": ["pyth", "pt", "py", "pyo"],
                        "correct_answer": "py"
                    },
                    {
                        "question_text": "How do you print 'Hello World' in Python?",
                        "options": ["echo 'Hello World'", "print('Hello World')", "console.log('Hello World')", "printf('Hello World')"],
                        "correct_answer": "print('Hello World')"
                    }
                ],
                "answers": []
            }
        ]

        # Insert Quizzes
        quiz_result = db['quizzes'].insert_many(quizzes)
        quiz_ids = quiz_result.inserted_ids
        logger.info(f"Inserted Quizzes: {quiz_ids}")

        # Update Modules with Quizzes
        update_module_quiz_result = db['modules'].update_one(
            {"_id": module_ids[0]},
            {"$set": {"quiz": quiz_ids[0]}}
        )
        if update_module_quiz_result.modified_count == 1:
            logger.info(f"Updated Module {module_ids[0]} with Quiz {quiz_ids[0]}.")
        else:
            logger.warning(f"No documents were updated for Module {module_ids[0]}.")

        # Sample Certificates
        certificates = [
            {
                "student_id": user_ids[0],
                "course_id": course_ids[0],
                "date": "2023-01-01T00:00:00Z"
            }
        ]

        # Insert Certificates
        certificate_result = db['certificates'].insert_many(certificates)
        certificate_ids = certificate_result.inserted_ids
        logger.info(f"Inserted Certificates: {certificate_ids}")

        # Close the client
        client.close()
        logger.info("Sample data loaded successfully.")
    
    except Exception as e:
        logger.error(f"An error occurred during seeding: {e}")
        client.close()

if __name__ == "__main__":
    load_sample_data()
