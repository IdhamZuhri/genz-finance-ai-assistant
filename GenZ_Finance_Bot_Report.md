# GenZ Finance Bot - Project Report

**Student Name:** [Your Name]  
**Course:** [Course Code/Name]  
**Date:** November 30, 2025  
**Assignment:** Chatbot Domain Transformation Project

---

## 1. Introduction

This report documents the transformation of the Cikgu Bot educational chatbot into **GenZ Finance Bot**, a financial literacy assistant designed specifically for Malaysian teenagers. The primary purpose of this assignment was to reimagine an existing chatbot system for a completely different domain while maintaining the core technical infrastructure and improving upon the user experience.

**New Domain:** Financial Literacy & Budget Management for Teens

**Intended Users:** Malaysian teenagers and young adults (ages 13-19) who are learning to manage their money, track expenses, and develop healthy financial habits.

**Chatbot Objective:** GenZ Finance Bot addresses the critical problem of financial illiteracy among teenagers by providing an accessible, interactive platform where they can learn money management skills, receive personalized budgeting advice, and get real-time guidance on spending decisions. The chatbot combines conversational AI with practical budget analysis tools to help teens understand their income, expenses, and savings in Ringgit Malaysia (RM), empowering them to make smarter financial decisions early in life.

---

## 2. Understanding Cikgu Bot

Cikgu Bot was originally designed as a Year 6 Science tutor for Malaysian students. After analyzing the base code, I understood the following key components:

**Core Architecture:**
- **Backend Framework:** Flask (Python) handles HTTP requests, routes, and database operations using SQLAlchemy ORM
- **AI Integration:** OpenAI's GPT-3.5-turbo API generates dynamic responses based on a system persona
- **Prompt Design:** A carefully crafted system prompt defines the chatbot's personality, knowledge domain, and response style
- **Conversation Memory:** Message history is maintained in a global array to provide context-aware responses
- **Database:** SQLite stores user information and tracks interaction metrics

**Key Learnings:**
1. **Persona is Critical:** The system prompt acts as the chatbot's identity, determining tone, expertise, and behavior
2. **Context Management:** Limiting conversation history prevents token overflow while maintaining coherent dialogue
3. **API Best Practices:** Error handling and fallback responses ensure reliability when AI services are unavailable
4. **User Experience:** Combining chat with interactive tools (like quizzes in Cikgu Bot) creates engagement beyond simple Q&A

The modular structure of Cikgu Bot made it an excellent foundation for transformation, as the frontend (HTML/CSS/JS) and backend (Flask/Python) are cleanly separated, allowing domain-specific changes without breaking the technical infrastructure.

---

## 3. Your Chatbot: Concept & Features

### **Name:** GenZ Finance Bot

### **Description:**
GenZ Finance Bot is an AI-powered financial literacy assistant that helps Malaysian teenagers learn budgeting, saving, and smart spending habits through interactive conversations and real-time budget analysis. The chatbot speaks the language of Gen-Z while providing practical, actionable financial advice tailored to teenage income levels and spending patterns.

### **Key Features:**

1. **AI Financial Advisor (Chat Interface)**
   - 24/7 conversational support for money-related questions
   - Topics: budgeting, saving strategies, investment basics, avoiding scams, earning money as a teen
   - Friendly, encouraging tone that makes finance approachable
   - Context-aware responses that remember previous questions in the session

2. **Budget Analyzer Tool**
   - Input monthly income and categorize expenses (Food & Snacks, Transport, Subscriptions)
   - Real-time calculation of total expenses, savings, and savings percentage
   - AI-generated personalized advice covering:
     - Overall budget health assessment
     - Subscription spending optimization (flags if >15% of income)
     - Income level guidance (suggestions to increase earnings if needed)
     - Immediate actionable steps for improvement

3. **Subscription Manager**
   - Track recurring subscriptions (Mobile Data, Spotify, YouTube, Netflix, Cloud Storage)
   - Editable amounts for each subscription
   - Visual breakdown of monthly subscription costs
   - LocalStorage persistence to save user data across sessions

4. **Visual Budget Summary**
   - Color-coded display (red for expenses, green for savings)
   - Clear percentage breakdown showing savings rate
   - Multi-paragraph AI advice formatted for easy reading

5. **User-Friendly Interface**
   - Two-column layout: Chat on left, Budget Analyzer on right
   - Professional landing page explaining features and benefits
   - Responsive design with smooth animations
   - Loading indicators during AI processing

### **Unique Aspects Compared to Cikgu Bot:**

| Aspect | Cikgu Bot | GenZ Finance Bot |
|--------|-----------|------------------|
| **Domain** | Education (Science) | Financial Literacy |
| **Target Age** | 12 years old | 13-19 years old |
| **Tone** | Teacher-like, educational | Peer-like, encouraging |
| **Currency** | Generic | Ringgit Malaysia (RM) |
| **Interactive Tool** | Quiz Generation | Budget Analyzer + Subscription Manager |
| **Gamification** | Points, Stickers, Achievements | None (removed for maturity) |
| **Advice Type** | Knowledge-based (facts) | Actionable (behavior change) |
| **User Data** | Quiz scores, correct answers | Income, expenses, subscriptions |
| **Visual Design** | Playful, child-friendly | Modern, professional |
| **Landing Page** | None | Marketing-focused homepage |

The transformation prioritized **practicality over gamification**, recognizing that teenagers seeking financial advice want tools that help them make real decisions, not just earn virtual rewards. The dual-interface design (chat + calculator) allows users to both learn concepts and apply them immediately.

---

## 4. Prompt & Persona Design

### **Full Persona/Prompt:**

```python
persona = (
    "You are a friendly and knowledgeable assistant named 'GenZ Finance Bot'. "
    "You help teenagers understand and manage their money. "
    "You teach financial literacy in a fun, easy-to-understand way, focusing on topics like "
    "budgeting, saving, smart spending, investing basics, and avoiding scams.\n"
    "Your goal is to help teens build good money habits, make smart choices, and feel confident "
    "about their financial future.\n"
    "When you answer questions, use simple language and relatable examples. Always be supportive, "
    "and if you don't know the answer, say, 'Hmm, I'm not sure about that, but I can help you find out!'"
)
```

### **Budget Analysis Prompt (for personalized advice):**

```python
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
```

### **Key Changes from Cikgu Bot:**

1. **Domain Expertise Shift:**
   - Original: "Year 6 Science teacher explaining concepts through analogies"
   - New: "Financial advisor for teenagers using practical examples"

2. **Tone Adjustment:**
   - Original: Academic and instructive ("Let me explain...")
   - New: Peer-supportive and motivational ("Great job! You can do this...")

3. **Response Strategy:**
   - Original: Knowledge transfer (explain science concepts)
   - New: Behavioral coaching (encourage better money habits)

4. **Vocabulary Level:**
   - Original: Simplified for 12-year-olds
   - New: Teen-appropriate with financial terminology explained

5. **Cultural Context:**
   - Original: Generic Malaysian context
   - New: Specific to Malaysian youth finances (RM currency, local subscription services, teen income realities)

6. **Multi-Dimensional Analysis:**
   - The budget analysis prompt uses structured data inputs to generate advice covering multiple aspects (savings, subscriptions, income) rather than Cikgu Bot's single-topic quiz questions.

7. **Actionability:**
   - Every response includes "one practical action they can take immediately" to drive behavior change, whereas Cikgu Bot focused on knowledge retention.

### **Context Features:**

- **Session Memory:** Conversation history (last 6 messages) provides context for follow-up questions
- **Budget Context:** User's financial data is included in analysis prompts to generate personalized advice
- **Fallback Intelligence:** If OpenAI is unavailable, rule-based advice uses threshold logic (e.g., savings <10% triggers specific guidance)

---

## 5. Sample Interaction

### **Conversation Example 1: Learning About Budgeting**

**User:** "How should I start budgeting my allowance?"

**GenZ Finance Bot:** "Great question! Start with the 50/30/20 rule: 50% for needs (food, transport), 30% for wants (entertainment, snacks), and 20% for savings. Track everything you spend for a week first to see where your money actually goes. Then use our Budget Analyzer to see if you're on track! Want me to explain how to track expenses easily?"

**User:** "Yes, how do I track expenses?"

**GenZ Finance Bot:** "Easy! Use your phone's notes app or a simple notebook. Write down every ringgit you spend with the date and category (food, transport, etc.). Do this for 7 days, then add it up. You'll be surprised where your money goes! Pro tip: Take a photo of receipts so you don't forget. After a week, plug those numbers into our Budget Analyzer to get personalized advice!"

---

### **Conversation Example 2: Subscription Spending**

**User:** "I spend RM90 per month on subscriptions. Is that too much?"

**GenZ Finance Bot:** "It depends on your income! If you earn RM500/month, that's 18% - a bit high. Aim for under 15% (RM75). Ask yourself: Do you really use all of them? Cancel one you rarely use and that's RM15-35 back for savings! Netflix or Spotify - which would you miss less?"

---

### **Budget Analyzer Example:**

**User Inputs:**
- Monthly Income: RM 600
- Food & Snacks: RM 180
- Transport: RM 80
- Subscriptions: RM 100 (Netflix RM35, Spotify RM17, Mobile Data RM40, YouTube RM18)

**AI-Generated Analysis Output:**

**Total Expenses:** RM 360  
**Savings:** RM 240 (40.0%)

**AI Advice:**
"Excellent work! You're saving 40% of your income, which is outstanding for a teen. Your subscription spending is 16.7% of income, slightly above the ideal 15%. Consider reviewing if you need both Netflix and YouTube Premium - they overlap in content. Your income level is moderate for a teen. To boost it further, explore freelancing opportunities like graphic design, tutoring younger students, or selling crafts online. Keep up this amazing savings habit - at this rate, you could save RM2,880 in a year!"

---

## 6. Reflection

### **Challenges Faced:**

1. **Domain Expertise Gap:** Transforming from science education to financial advice required research into teen finance best practices, budgeting frameworks (50/30/20 rule), and Malaysian youth spending patterns. I had to ensure advice was age-appropriate and culturally relevant.

2. **UI/UX Redesign:** Removing gamification elements (points, badges, leaderboard) while maintaining engagement was challenging. I addressed this by adding the Budget Analyzer as a practical, immediate-value tool that feels rewarding without artificial incentives.

3. **Prompt Engineering Complexity:** Creating a prompt that generates advice covering multiple dimensions (savings, subscriptions, income) in a concise, actionable format required multiple iterations. Balancing encouragement with honesty about spending problems was tricky.

4. **Data Structure Changes:** Adapting the database from tracking quiz scores to storing budget data required careful modification of the User model and route handlers without breaking existing functionality.

5. **Real-Time Calculations:** Implementing synchronized updates across multiple input fields (income, food, transport, subscriptions) to show live expense totals required careful JavaScript event handling.

### **Key Learnings:**

1. **Prompt Engineering is an Art:** Small word changes dramatically affect AI output. Adding "Be encouraging but honest" made responses more balanced. Specifying "3-4 sentences" prevented overly long advice. Structuring prompts with numbered points ensures comprehensive coverage.

2. **Persona Defines Everything:** The persona is the chatbot's DNA. Changing "teacher" to "peer advisor" fundamentally shifted the entire interaction style, proving that persona design is more important than any single feature.

3. **Context is King:** Including user's actual numbers (income level, subscription percentage) in prompts generates far more relevant advice than generic financial tips. Personalization drives engagement.

4. **Fallback Strategies Matter:** Rule-based backup advice (when AI fails) taught me to think in decision trees and thresholds, which improved my understanding of how to structure intelligent systems.

5. **User-Centered Design:** Teenagers don't want lectures - they want tools that help them right now. The Budget Analyzer's instant feedback loop proved more valuable than pages of educational content.

### **Future Improvements:**

1. **Data Visualization:** Add pie charts or bar graphs showing expense breakdown by category using Chart.js or D3.js for visual learners.

2. **Goal Setting Feature:** Allow users to set savings goals ("Save RM500 for a phone in 3 months") with progress tracking and motivational milestones.

3. **Budget History:** Store monthly budgets in the database to show trends over time ("You're spending 20% less on food this month!").

4. **Peer Comparison (Anonymous):** Show aggregate statistics like "Teens your age save an average of 15%" to provide social proof without identifying individuals.

5. **Multi-Language Support:** Add Bahasa Malaysia toggle for wider accessibility among Malaysian youth.

6. **Export to Excel:** Replace PDF export with Excel/CSV format for users who want to analyze data in spreadsheet software.

7. **Mobile App:** Convert to Progressive Web App (PWA) for offline access and push notifications for budget reminders.

8. **AI Conversation Memory:** Implement long-term memory using vector databases to remember user's financial situation across sessions, enabling more personalized ongoing advice.

### **Conclusion:**

This project demonstrated that successful chatbot transformation requires more than changing the persona - it demands deep understanding of the target domain, users' actual needs, and the interplay between conversational AI and practical tools. GenZ Finance Bot succeeds because it combines education (chat) with application (budget analyzer), creating a holistic experience that empowers teenagers to take control of their financial future. The technical foundation from Cikgu Bot proved robust and adaptable, validating good software architecture principles. Most importantly, I learned that effective AI systems solve real problems with empathy, not just technical sophistication.

---

**Word Count:** ~2,450 words (approximately 5 pages at 11pt Calibri, 1.15 spacing)

---

## Appendix: Technical Stack

- **Backend:** Python 3.x, Flask, SQLAlchemy, OpenAI API
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite
- **AI Model:** GPT-3.5-turbo
- **Hosting:** Local development (ready for deployment to Render/Heroku)
- **Version Control:** Git (recommended)

---

## Appendix: File Structure

```
GenZ Finance Bot/
├── financeBot.py              # Main Flask application
├── app.env                     # Environment variables (API keys)
├── templates/
│   ├── landing.html           # Marketing homepage
│   └── index_GenZFinanceBot.html  # Main app interface
├── static/
│   └── icons/
│       └── Finance.jpg        # Bot logo
└── instance/
    └── gamification.db        # SQLite database
```
