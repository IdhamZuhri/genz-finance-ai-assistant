from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from openai import OpenAI
from dotenv import load_dotenv
import random
from datetime import datetime  # For tracking user activity timestamps

# Load environment variables from a .env file
load_dotenv("app.env")

# Initialize the OpenAI client with your API key
client = OpenAI(
	api_key=os.getenv("OPENAI_API_KEY"),
)

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gamification.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Comprehensive persona for GenZ Finance Bot with a financial literacy framework
persona = (
	"You are a friendly and knowledgeable assistant named 'GenZ Finance Bot'. You help teenagers understand and manage their money. "
	"You teach financial literacy in a fun, easy-to-understand way, focusing on topics like budgeting, saving, smart spending, investing basics, and avoiding scams.\n"
	"Your goal is to help teens build good money habits, make smart choices, and feel confident about their financial future.\n"
	"When you answer questions, use simple language and relatable examples. Always be supportive, and if you don’t know the answer, say, 'Hmm, I'm not sure about that, but I can help you find out!'"
)

# Define User Model for tracking
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	questions_asked = db.Column(db.Integer, default=0)  # Count total questions
	last_active = db.Column(db.String(50))  # Last activity timestamp

# Create the database tables
with app.app_context():
	db.create_all()

# Conversation history to maintain context
conversation_history = []

# Flask route for the landing page
@app.route("/")
def landing():
	return render_template("landing.html")

# Flask route for the main app
@app.route("/app")
def home():
	return render_template("index_GenZFinanceBot.html")

# Function to generate a response for the chatbot
def generate_response(user_input, username):
	global conversation_history
	conversation_history.append({"role": "user", "content": user_input})
	messages = [{"role": "system", "content": persona}] + conversation_history

	# Using the OpenAI client to create chat completions
	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=messages,
		max_tokens=400,
		temperature=0.7,
	)

	bot_response = response.choices[0].message.content.strip()
	conversation_history.append({"role": "assistant", "content": bot_response})

	# Limit the conversation history to avoid excessive context length
	if len(conversation_history) > 6:
		conversation_history = conversation_history[-6:]

	# Track user activity
	user = User.query.filter_by(username=username).first()
	if user:
		user.questions_asked += 1  # Track question count
		user.last_active = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update timestamp
		db.session.commit()

	return bot_response

# Flask route for the chatbot API
@app.route("/chat", methods=["POST"])
def chat():
	data = request.json
	user_input = data.get("message", "")
	username = data.get("username", "guest")

	# Create user if not exists
	user = User.query.filter_by(username=username).first()
	if not user:
		user = User(username=username)
		db.session.add(user)
		db.session.commit()

	response_text = generate_response(user_input, username)

	# Return the response
	return jsonify({"response": response_text})

# Flask route for budget calculation
@app.route("/calculate_budget", methods=["POST"])
def calculate_budget():
	data = request.json
	username = data.get("username", "guest")
	income = float(data.get("income", 0))
	
	# Extract expenses from nested object or flat structure
	expenses_data = data.get("expenses", {})
	food = float(expenses_data.get("food", 0))
	transport = float(expenses_data.get("transport", 0))
	subscriptions = float(expenses_data.get("subscription", 0))
	
	# Calculate totals
	total_expenses = food + transport + subscriptions
	savings = income - total_expenses
	savings_percentage = (savings / income * 100) if income > 0 else 0
	
	# Calculate subscription and income percentages
	subscription_percentage = (subscriptions / income * 100) if income > 0 else 0
	income_level = "low" if income < 500 else "moderate" if income < 1500 else "good"
	
	# Generate personalized advice using OpenAI
	prompt = f"""As a financial advisor for teenagers, analyze this budget and provide comprehensive advice (3-4 sentences):

Monthly Income: RM {income:.2f} ({income_level} income level)
Food & Snacks: RM {food:.2f}
Transportation: RM {transport:.2f}
Subscriptions: RM {subscriptions:.2f} ({subscription_percentage:.1f}% of income)
Total Expenses: RM {total_expenses:.2f}
Savings: RM {savings:.2f} ({savings_percentage:.1f}%)

Provide advice covering:
1. Overall budget health and savings rate
2. Specific thoughts on subscription spending (whether it's reasonable or needs optimization)
3. Income suggestions (ways to increase income if needed, or validation if income is good)
4. One practical action they can take immediately

Be encouraging but honest about areas needing improvement."""
	
	try:
		response = client.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=[{"role": "system", "content": persona}, {"role": "user", "content": prompt}],
			max_tokens=250,
			temperature=0.7,
		)
		advice = response.choices[0].message.content.strip()
	except Exception as e:
		print(f"Error generating advice: {e}")
		# Fallback advice with subscription and income insights
		advice_parts = []
		
		# Savings advice
		if savings_percentage >= 20:
			advice_parts.append(f"Great job! You're saving {savings_percentage:.1f}% of your income.")
		elif savings_percentage >= 10:
			advice_parts.append(f"You're saving {savings_percentage:.1f}% - that's a good start!")
		else:
			advice_parts.append(f"Your savings rate is {savings_percentage:.1f}%. Aim for at least 10-20%.")
		
		# Subscription advice
		if subscription_percentage > 15:
			advice_parts.append(f"Your subscriptions take up {subscription_percentage:.1f}% of your income - consider reviewing which ones you really need.")
		elif subscriptions > 0:
			advice_parts.append(f"Your subscription spending ({subscription_percentage:.1f}% of income) looks reasonable.")
		
		# Income advice
		if income < 500:
			advice_parts.append("Consider finding part-time work, freelancing, or selling items you no longer need to boost your income.")
		elif income < 1500:
			advice_parts.append("Your income is moderate. Look for opportunities to earn extra through side gigs or skill development.")
		else:
			advice_parts.append("You have a good income level for a teen. Keep building those earning skills!")
		
		advice = " ".join(advice_parts)
	
	# Update user stats
	user = User.query.filter_by(username=username).first()
	if user:
		user.last_active = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		db.session.commit()
	
	return jsonify({
		"advice": advice,
		"total_expenses": total_expenses,
		"savings": savings,
		"savings_percentage": savings_percentage
	})

# Flask route to clear conversation history
@app.route("/clear", methods=["POST"])
def clear():
	global conversation_history
	conversation_history = []
	return jsonify({"message": "Conversation cleared"})

if __name__ == "__main__":
	app.run(debug=True)
