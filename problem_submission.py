```python
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ai_problem_solving']

# Problem Data Schema
problem_collection = db['problems']

@app.route('/submit_problem', methods=['POST'])
def submit_problem():
    data = request.get_json()

    # Validate data
    if not all(key in data for key in ('problemDescription', 'problemOwnerID', 'solutionCriteria')):
        return jsonify({'message': 'Missing required data'}), 400

    # Insert problem into database
    problem_id = problem_collection.insert_one(data).inserted_id

    return jsonify({'message': 'Problem submitted successfully', 'problemID': str(problem_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)
```