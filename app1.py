import random
from datetime import datetime, timedelta

class AIModel:
    def analyze_student(self, student_data):
        """Analyze student performance and provide insights"""
        student = student_data.get('student', {})
        quiz_scores = student_data.get('quiz_scores', [])
        progress = student_data.get('progress', [])
        
        # Calculate average score
        if quiz_scores:
            avg_score = sum(q['score'] for q in quiz_scores) / len(quiz_scores)
        else:
            avg_score = 0
        
        # Determine level
        if avg_score >= 80:
            level = "Advanced"
            next_level = "Expert"
        elif avg_score >= 60:
            level = "Intermediate"
            next_level = "Advanced"
        elif avg_score >= 40:
            level = "Basic"
            next_level = "Intermediate"
        else:
            level = "Beginner"
            next_level = "Basic"
        
        # Calculate study streak
        study_streak = self.calculate_study_streak(student_data)
        
        # Predict next weak area
        predicted_weak = self.predict_weak_areas(student_data)
        
        return {
            'level': level,
            'next_level': next_level,
            'average_score': round(avg_score, 1),
            'total_quizzes': len(quiz_scores),
            'study_streak': study_streak,
            'predicted_weak_areas': predicted_weak,
            'recommendations': self.generate_recommendations(student_data),
            'confidence_score': self.calculate_confidence(student_data)
        }
    
    def get_weak_topics(self, quiz_scores):
        """Identify weak topics based on performance"""
        # Mock topics with scores
        topics = {
            'Algebra': 75,
            'Geometry': 45,
            'Trigonometry': 30,
            'Calculus': 65,
            'Statistics': 55,
            'Probability': 40,
            'Organic Chemistry': 35,
            'Physical Chemistry': 60,
            'Mechanics': 70,
            'Electrostatics': 45,
            'Thermodynamics': 25,
            'Optics': 50
        }
        
        weak_topics = []
        for topic, score in topics.items():
            if score < 50:
                weak_topics.append({
                    'name': topic,
                    'score': score,
                    'priority': 'High' if score < 30 else 'Medium',
                    'improvement_rate': random.randint(5, 15)
                })
        
        return sorted(weak_topics, key=lambda x: x['score'])[:5]
    
    def calculate_study_streak(self, student_data):
        """Calculate current study streak in days"""
        # Mock streak calculation
        return random.randint(3, 15)
    
    def predict_weak_areas(self, student_data):
        """Predict which topics will become weak"""
        topics = [
            'Integration',
            'Differentiation',
            'Chemical Bonding',
            'Kinematics',
            'Modern Physics'
        ]
        
        predictions = []
        for topic in random.sample(topics, 3):
            predictions.append({
                'topic': topic,
                'risk_level': random.choice(['High', 'Medium']),
                'suggested_action': f'Practice {topic} regularly'
            })
        
        return predictions
    
    def generate_recommendations(self, student_data):
        """Generate personalized study recommendations"""
        student = student_data.get('student', {})
        class_level = student.get('class_level', 11)
        
        recommendations = []
        
        # Time-based recommendations
        hour = datetime.now().hour
        if hour < 12:
            time_msg = "Morning session: Focus on difficult topics"
        elif hour < 17:
            time_msg = "Afternoon session: Practice problems"
        else:
            time_msg = "Evening session: Review and revision"
        
        recommendations.append({
            'type': 'time',
            'message': time_msg,
            'priority': 'high'
        })
        
        # Subject recommendations
        if class_level >= 11:
            recommendations.append({
                'type': 'subject',
                'message': 'Start JEE/NEET preparation with basic concepts',
                'priority': 'high'
            })
        
        # Performance-based recommendations
        quiz_scores = student_data.get('quiz_scores', [])
        if quiz_scores and len(quiz_scores) > 0:
            last_score = quiz_scores[-1].get('score', 0)
            if last_score < 40:
                recommendations.append({
                    'type': 'warning',
                    'message': 'Review last quiz topics before proceeding',
                    'priority': 'high'
                })
        
        return recommendations
    
    def calculate_confidence(self, student_data):
        """Calculate student's confidence score"""
        quiz_scores = student_data.get('quiz_scores', [])
        
        if not quiz_scores:
            return 50
        
        # Based on recent performance trend
        if len(quiz_scores) >= 3:
            recent = quiz_scores[-3:]
            trend = (recent[-1]['score'] - recent[0]['score']) / 3
            base_confidence = sum(q['score'] for q in recent) / 3
            confidence = base_confidence + trend * 10
        else:
            confidence = sum(q['score'] for q in quiz_scores) / len(quiz_scores)
        
        return max(0, min(100, confidence))
    
    def analyze_exam_performance(self, answers, questions):
        """Analyze exam performance and provide feedback"""
        correct_count = 0
        topic_performance = {}
        
        for i, answer in enumerate(answers):
            if i < len(questions):
                q = questions[i]
                correct = answer == q.get('correct_answer')
                
                if correct:
                    correct_count += 1
                
                # Track per topic
                topic = q.get('chapter', 'General')
                if topic not in topic_performance:
                    topic_performance[topic] = {'correct': 0, 'total': 0}
                
                topic_performance[topic]['total'] += 1
                if correct:
                    topic_performance[topic]['correct'] += 1
        
        # Identify strong and weak areas
        strong_areas = []
        weak_areas = []
        
        for topic, perf in topic_performance.items():
            score = (perf['correct'] / perf['total']) * 100
            if score >= 70:
                strong_areas.append(topic)
            elif score <= 40:
                weak_areas.append(topic)
        
        return {
            'total_correct': correct_count,
            'total_questions': len(questions),
            'percentage': (correct_count / len(questions)) * 100 if questions else 0,
            'strong_areas': strong_areas,
            'weak_areas': weak_areas,
            'topic_performance': topic_performance,
            'improvement_suggestions': self.generate_improvement_suggestions(weak_areas)
        }
    
    def generate_improvement_suggestions(self, weak_areas):
        """Generate improvement suggestions for weak areas"""
        suggestions = []
        
        for area in weak_areas:
            suggestions.append({
                'topic': area,
                'suggestion': f'Watch video lessons on {area}',
                'practice': f'Practice {area} problems daily',
                'resources': [
                    f'https://youtube.com/results?search_query={area}+lecture',
                    f'https://www.khanacademy.org/search?search={area}'
                ]
            })
        
        return suggestions
    
    def generate_study_plan(self, student_data):
        """Generate personalized daily study plan"""
        student = student_data.get('student', {})
        weak_topics = self.get_weak_topics(student_data.get('quiz_scores', []))
        
        # Create daily schedule
        schedule = []
        time_slots = [
            ('06:00 - 07:30', 'Morning Study', 'High focus topics'),
            ('10:00 - 11:30', 'Practice Session', 'Problem solving'),
            ('16:00 - 17:30', 'Review', 'Weak areas revision'),
            ('20:00 - 21:00', 'Quick Revision', 'Formula memorization')
        ]
        
        for i, (time, title, desc) in enumerate(time_slots):
            if i < len(weak_topics):
                topic = weak_topics[i]['name']
                schedule.append({
                    'time': time,
                    'title': title,
                    'description': f'{topic} - {desc}',
                    'duration': '90 min' if i < 2 else '60 min',
                    'topic': topic,
                    'resources': [
                        f'📺 Watch: {topic} video lessons',
                        f'📝 Practice: {topic} problems',
                        f'📋 Take: {topic} quiz'
                    ]
                })
            else:
                schedule.append({
                    'time': time,
                    'title': title,
                    'description': desc,
                    'duration': '60 min',
                    'topic': 'General',
                    'resources': [
                        'Review previous notes',
                        'Practice mixed problems'
                    ]
                })
        
        # Add weekend special
        today = datetime.now().strftime('%A')
        if today in ['Saturday', 'Sunday']:
            schedule.append({
                'time': '09:00 - 12:00',
                'title': 'Weekend Marathon',
                'description': 'Full syllabus revision',
                'duration': '180 min',
                'topic': 'All topics',
                'resources': [
                    'Take full-length test',
                    'Review mistakes',
                    'Plan next week'
                ]
            })
        
        return {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'day': today,
            'schedule': schedule,
            'total_study_time': '6 hours' if today in ['Saturday', 'Sunday'] else '4.5 hours',
            'focus_areas': [t['name'] for t in weak_topics[:3]]
        }