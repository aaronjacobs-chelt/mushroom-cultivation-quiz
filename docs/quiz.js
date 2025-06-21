// Mushroom Cultivation Quiz - Main Application Logic

class MushroomQuiz {
    constructor() {
        this.settings = {
            difficulty: null,
            numQuestions: null,
            timerSeconds: null
        };
        
        this.gameState = {
            currentQuestionIndex: 0,
            score: 0,
            questions: [],
            wrongTopics: [],
            startTime: null,
            endTime: null,
            timerInterval: null,
            currentTimer: null
        };
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.showScreen('welcome-screen');
    }
    
    setupEventListeners() {
        // Option button selection
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('option-btn')) {
                this.handleOptionSelection(e.target);
            }
            
            if (e.target.classList.contains('answer-btn')) {
                this.handleAnswerSelection(e.target);
            }
        });
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (document.querySelector('#quiz-screen').classList.contains('active')) {
                const num = parseInt(e.key);
                if (num >= 1 && num <= 4) {
                    const answerBtns = document.querySelectorAll('.answer-btn');
                    if (answerBtns[num - 1] && !answerBtns[num - 1].disabled) {
                        this.handleAnswerSelection(answerBtns[num - 1]);
                    }
                }
            }
        });
    }
    
    handleOptionSelection(button) {
        const group = button.parentElement;
        const allButtons = group.querySelectorAll('.option-btn');
        
        // Remove selection from all buttons in this group
        allButtons.forEach(btn => btn.classList.remove('selected'));
        
        // Add selection to clicked button
        button.classList.add('selected');
        
        // Store the setting
        if (button.hasAttribute('data-difficulty')) {
            this.settings.difficulty = button.getAttribute('data-difficulty');
        } else if (button.hasAttribute('data-questions')) {
            this.settings.numQuestions = parseInt(button.getAttribute('data-questions'));
        } else if (button.hasAttribute('data-timer')) {
            this.settings.timerSeconds = parseInt(button.getAttribute('data-timer')) || null;
        }
        
        this.updateStartButton();
    }
    
    updateStartButton() {
        const startBtn = document.getElementById('start-quiz-btn');
        const isReady = this.settings.difficulty && 
                       this.settings.numQuestions && 
                       this.settings.timerSeconds !== null;
        
        startBtn.disabled = !isReady;
    }
    
    showScreen(screenId) {
        // Hide all screens
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });
        
        // Show target screen
        document.getElementById(screenId).classList.add('active');
    }
    
    prepareQuiz() {
        // Get questions based on difficulty
        const availableQuestions = getQuestionsByDifficulty(this.settings.difficulty);
        
        // Select random questions
        this.gameState.questions = getRandomQuestions(availableQuestions, this.settings.numQuestions);
        
        // Reset game state
        this.gameState.currentQuestionIndex = 0;
        this.gameState.score = 0;
        this.gameState.wrongTopics = [];
        this.gameState.startTime = new Date();
        
        // Update UI elements
        document.getElementById('total-questions').textContent = this.gameState.questions.length;
        document.getElementById('current-score').textContent = '0';
        document.getElementById('questions-answered').textContent = '0';
        
        // Setup timer container
        const timerContainer = document.getElementById('timer-container');
        if (this.settings.timerSeconds) {
            timerContainer.style.display = 'block';
        } else {
            timerContainer.style.display = 'none';
        }
    }
    
    displayQuestion() {
        const question = this.gameState.questions[this.gameState.currentQuestionIndex];
        const questionNum = this.gameState.currentQuestionIndex + 1;
        
        // Update progress
        const progress = (questionNum / this.gameState.questions.length) * 100;
        document.getElementById('progress-fill').style.width = `${progress}%`;
        document.getElementById('current-question').textContent = questionNum;
        
        // Update difficulty badge
        const badge = document.getElementById('difficulty-badge');
        const difficultyIcons = {
            'beginner': '🟢',
            'intermediate': '🟡',
            'advanced': '🔴'
        };
        badge.innerHTML = `📚 ${difficultyIcons[question.difficulty]} ${question.difficulty.charAt(0).toUpperCase() + question.difficulty.slice(1)}`;
        
        // Display question
        document.getElementById('question-text').textContent = question.question;
        
        // Shuffle and display options
        const shuffledOptions = shuffleArray(question.options);
        const optionsContainer = document.getElementById('answer-options');
        optionsContainer.innerHTML = '';
        
        shuffledOptions.forEach((option, index) => {
            const button = document.createElement('button');
            button.className = 'answer-btn';
            button.textContent = option;
            button.setAttribute('data-answer', option);
            optionsContainer.appendChild(button);
        });
        
        // Start timer if enabled
        if (this.settings.timerSeconds) {
            this.startTimer();
        }
    }
    
    startTimer() {
        this.gameState.currentTimer = this.settings.timerSeconds;
        const timerText = document.getElementById('timer-text');
        const timerCircle = document.querySelector('.timer-circle');
        const timerWarning = document.getElementById('timer-warning');
        
        timerText.textContent = this.gameState.currentTimer;
        timerWarning.classList.remove('active');
        
        this.gameState.timerInterval = setInterval(() => {
            this.gameState.currentTimer--;
            timerText.textContent = this.gameState.currentTimer;
            
            // Update timer circle color
            const percentage = (this.gameState.currentTimer / this.settings.timerSeconds) * 360;
            const color = this.gameState.currentTimer > 10 ? '#228B22' : 
                         this.gameState.currentTimer > 5 ? '#FF8C00' : '#DC143C';
            
            timerCircle.style.background = `conic-gradient(${color} ${percentage}deg, #DDD 0deg)`;
            
            // Show warning when time is running out
            if (this.gameState.currentTimer <= 5) {
                timerWarning.classList.add('active');
            }
            
            // Time's up!
            if (this.gameState.currentTimer <= 0) {
                this.handleTimeout();
            }
        }, 1000);
    }
    
    stopTimer() {
        if (this.gameState.timerInterval) {
            clearInterval(this.gameState.timerInterval);
            this.gameState.timerInterval = null;
        }
    }
    
    handleTimeout() {
        this.stopTimer();
        this.handleAnswerSelection(null, true);
    }
    
    handleAnswerSelection(button, isTimeout = false) {
        // Stop timer
        this.stopTimer();
        
        // Disable all answer buttons
        const answerBtns = document.querySelectorAll('.answer-btn');
        answerBtns.forEach(btn => btn.disabled = true);
        
        const question = this.gameState.questions[this.gameState.currentQuestionIndex];
        let isCorrect = false;
        let selectedAnswer = null;
        
        if (!isTimeout && button) {
            selectedAnswer = button.getAttribute('data-answer');
            isCorrect = selectedAnswer === question.answer;
            button.classList.add('selected');
        }
        
        // Highlight correct answer
        answerBtns.forEach(btn => {
            const answer = btn.getAttribute('data-answer');
            if (answer === question.answer) {
                btn.classList.add('correct');
            } else if (btn === button && !isCorrect) {
                btn.classList.add('incorrect');
            }
        });
        
        // Update score
        if (isCorrect) {
            this.gameState.score++;
        } else if (!isTimeout) {
            this.gameState.wrongTopics.push(question.topic);
        }
        
        // Update score display
        document.getElementById('current-score').textContent = this.gameState.score;
        document.getElementById('questions-answered').textContent = this.gameState.currentQuestionIndex + 1;
        
        // Show explanation
        this.showExplanation(question.explanation, isCorrect, isTimeout);
        
        // Auto-advance after delay
        setTimeout(() => {
            this.nextQuestion();
        }, 3000);
    }
    
    showExplanation(explanation, isCorrect, isTimeout) {
        // Create explanation popup
        const popup = document.createElement('div');
        popup.className = 'explanation-popup';
        popup.innerHTML = `
            <div class="explanation-content">
                <div class="result-icon">
                    ${isTimeout ? '⏰' : isCorrect ? '✅' : '❌'}
                </div>
                <div class="result-text">
                    ${isTimeout ? 'Time\'s up!' : isCorrect ? 'Correct!' : 'Incorrect!'}
                </div>
                <div class="explanation-text">
                    💡 ${explanation}
                </div>
            </div>
        `;
        
        // Add styles
        popup.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            z-index: 1000;
            max-width: 400px;
            text-align: center;
            animation: fadeIn 0.3s ease;
        `;
        
        document.body.appendChild(popup);
        
        // Remove after delay
        setTimeout(() => {
            if (popup.parentNode) {
                popup.parentNode.removeChild(popup);
            }
        }, 2800);
    }
    
    nextQuestion() {
        this.gameState.currentQuestionIndex++;
        
        if (this.gameState.currentQuestionIndex < this.gameState.questions.length) {
            this.displayQuestion();
        } else {
            this.showResults();
        }
    }
    
    showResults() {
        this.gameState.endTime = new Date();
        const timeTaken = Math.round((this.gameState.endTime - this.gameState.startTime) / 1000);
        
        // Calculate percentage
        const percentage = Math.round((this.gameState.score / this.gameState.questions.length) * 100);
        
        // Update results screen
        document.getElementById('final-score').textContent = `${this.gameState.score}/${this.gameState.questions.length}`;
        document.getElementById('score-percentage').textContent = `(${percentage}%)`;
        
        // Set achievement
        this.setAchievement(percentage);
        
        // Update stats
        document.getElementById('stats-difficulty').textContent = this.settings.difficulty.charAt(0).toUpperCase() + this.settings.difficulty.slice(1);
        document.getElementById('stats-questions').textContent = this.gameState.questions.length;
        document.getElementById('stats-timer').textContent = this.settings.timerSeconds ? `${this.settings.timerSeconds}s per question` : 'No timer';
        document.getElementById('stats-time').textContent = this.formatTime(timeTaken);
        
        // Show study recommendations
        this.showStudyRecommendations();
        
        // Show results screen
        this.showScreen('results-screen');
    }
    
    setAchievement(percentage) {
        const badge = document.getElementById('achievement-badge');
        const text = document.getElementById('achievement-text');
        
        if (percentage >= 90) {
            badge.innerHTML = '🌟 MUSHROOM MASTER! 🌟';
            badge.style.background = 'linear-gradient(135deg, #32CD32, #228B22)';
            badge.style.color = 'white';
            text.textContent = "Outstanding! You're ready to start your own mushroom farm! 🍄🚜";
        } else if (percentage >= 70) {
            badge.innerHTML = '🍄 FUNGI EXPERT! 🍄';
            badge.style.background = 'linear-gradient(135deg, #4682B4, #1E90FF)';
            badge.style.color = 'white';
            text.textContent = "Great job! You have solid mushroom cultivation knowledge! 🎯";
        } else if (percentage >= 50) {
            badge.innerHTML = '🌱 GROWING CULTIVATOR! 🌱';
            badge.style.background = 'linear-gradient(135deg, #FF8C00, #FFA500)';
            badge.style.color = 'white';
            text.textContent = "Good start! Keep learning and you'll be a mushroom pro! 📚";
        } else {
            badge.innerHTML = '🔰 SPORE BEGINNER! 🔰';
            badge.style.background = 'linear-gradient(135deg, #9370DB, #8A2BE2)';
            badge.style.color = 'white';
            text.textContent = "Don't worry! Every expert started somewhere. Keep studying! 💪";
        }
    }
    
    showStudyRecommendations() {
        const container = document.getElementById('study-recommendations');
        const list = document.getElementById('study-list');
        
        if (this.gameState.wrongTopics.length === 0) {
            container.style.display = 'none';
            return;
        }
        
        const uniqueTopics = [...new Set(this.gameState.wrongTopics)];
        const studyTips = {
            "growing_conditions": "Review optimal temperature and humidity ranges.",
            "mushroom_varieties": "Learn about different types of mushrooms and their characteristics.",
            "substrates": "Explore various substrates used in mushroom cultivation.",
            "biology_basics": "Understand the structure and function of mycelium.",
            "sterilization": "Look into sterilization techniques like pressure cooking.",
            "medicinal_mushrooms": "Research the benefits and uses of medicinal mushrooms.",
            "cultivation_process": "Familiarize yourself with the steps in mushroom cultivation.",
            "beginner_varieties": "Identify beginner-friendly mushrooms to start growing.",
            "growing_methods": "Discover different growing methods such as log cultivation.",
            "timing": "Learn about the timelines for various mushroom cultivation stages."
        };
        
        list.innerHTML = '';
        uniqueTopics.forEach(topic => {
            if (studyTips[topic]) {
                const li = document.createElement('li');
                li.textContent = studyTips[topic];
                list.appendChild(li);
            }
        });
        
        container.style.display = 'block';
    }
    
    formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}m ${remainingSeconds}s`;
    }
}

// Global functions for HTML onclick handlers
function showWelcome() {
    quiz.showScreen('welcome-screen');
}

function showQuizSetup() {
    quiz.showScreen('setup-screen');
}

function showAbout() {
    quiz.showScreen('about-screen');
}

function startQuiz() {
    quiz.prepareQuiz();
    quiz.showScreen('quiz-screen');
    quiz.displayQuestion();
}

function quitQuiz() {
    quiz.stopTimer();
    if (confirm('Are you sure you want to quit the quiz?')) {
        quiz.showScreen('welcome-screen');
    }
}

function restartQuiz() {
    quiz.showScreen('setup-screen');
}

function shareResults() {
    const score = quiz.gameState.score;
    const total = quiz.gameState.questions.length;
    const percentage = Math.round((score / total) * 100);
    
    const shareText = `I just scored ${score}/${total} (${percentage}%) on the Mushroom Cultivation Quiz! 🍄 Test your fungi knowledge too!`;
    
    if (navigator.share) {
        navigator.share({
            title: 'Mushroom Cultivation Quiz Results',
            text: shareText,
            url: window.location.href
        });
    } else {
        // Fallback - copy to clipboard
        navigator.clipboard.writeText(shareText + ' ' + window.location.href).then(() => {
            alert('Results copied to clipboard!');
        }).catch(() => {
            alert('Share failed. Your score: ' + shareText);
        });
    }
}

// Initialize the quiz when the page loads
let quiz;
document.addEventListener('DOMContentLoaded', () => {
    quiz = new MushroomQuiz();
});

// Add some additional CSS for the explanation popup
const style = document.createElement('style');
style.textContent = `
    .explanation-popup .result-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .explanation-popup .result-text {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: var(--primary-color);
    }
    
    .explanation-popup .explanation-text {
        font-size: 1rem;
        line-height: 1.5;
        color: var(--text-secondary);
    }
`;
document.head.appendChild(style);

