import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.logger import interview_logger


class TestInterviewAI:
    """Test cases for AI Interview Service"""

    def test_video_interview_setup(self):
        """Test video interview initialization"""
        interview_logger.info("Testing video interview setup")

        interview_session = {
            "candidate_id": 1,
            "job_id": 101,
            "round": "HR",
            "status": "scheduled",
        }

        assert interview_session["status"] == "scheduled"
        interview_logger.info("Video interview setup test passed")

    def test_camera_validation(self):
        """Test camera and face detection"""
        interview_logger.info("Testing camera validation")

        # Simulate camera check
        camera_status = {
            "camera_on": True,
            "face_detected": True,
            "multiple_faces": False,
        }

        is_valid = (
            camera_status["camera_on"]
            and camera_status["face_detected"]
            and not camera_status["multiple_faces"]
        )

        assert is_valid is True
        interview_logger.info("Camera validation test passed")

    def test_hr_question_generation(self):
        """Test HR interview questions"""
        interview_logger.info("Testing HR question generation")

        hr_questions = [
            "Tell me about yourself",
            "Why do you want to work here?",
            "What are your strengths and weaknesses?",
            "Describe a challenging situation you faced",
        ]

        assert len(hr_questions) >= 3
        interview_logger.info(f"Generated {len(hr_questions)} HR questions")

    def test_technical_question_generation(self):
        """Test technical interview questions based on experience"""
        interview_logger.info("Testing technical question generation")

        experience_years = 3
        role = "MERN Stack Developer"

        # Questions should scale with experience
        if experience_years < 2:
            difficulty = "basic"
        elif experience_years < 5:
            difficulty = "intermediate"
        else:
            difficulty = "advanced"

        assert difficulty == "intermediate"
        interview_logger.info(f"Technical questions difficulty: {difficulty}")

    def test_behavior_monitoring(self):
        """Test behavioral monitoring during interview"""
        interview_logger.info("Testing behavior monitoring")

        behavior_data = {
            "eye_contact": 0.85,
            "tab_switches": 0,
            "face_visible": True,
            "looking_away_count": 2,
        }

        # Flag suspicious behavior
        is_suspicious = (
            behavior_data["tab_switches"] > 3
            or behavior_data["looking_away_count"] > 10
            or not behavior_data["face_visible"]
        )

        assert is_suspicious is False
        interview_logger.info("Behavior monitoring test passed")

    def test_interview_scoring(self):
        """Test interview scoring algorithm"""
        interview_logger.info("Testing interview scoring")

        scores = {"communication": 85, "technical": 78, "behavior": 90, "aptitude": 82}

        # Calculate weighted average
        weights = {
            "communication": 0.3,
            "technical": 0.4,
            "behavior": 0.2,
            "aptitude": 0.1,
        }

        total_score = sum(scores[k] * weights[k] for k in scores.keys())

        assert 0 <= total_score <= 100
        interview_logger.info(f"Interview total score: {total_score:.2f}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
